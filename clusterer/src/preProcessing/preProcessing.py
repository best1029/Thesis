from nltk.corpus import stopwords
from nltk.stem.cistem import Cistem
from nltk.tokenize import word_tokenize
import re
import json
from germalemma import GermaLemma
import spacy
import json
import requests

from src.inOut import dict2file
from src.inOut import getData, file2list
import src.config as conf
from src.logger import logger

class PreProcessor:
    def __init__(self, customStopWords = True):

        # create stemmer
        self.stemmer = Cistem()

        # create lemmatizer
        self.lemmatizer = GermaLemma()

        # create nlp for pos_tagging
        self.nlp = spacy.load('de_core_news_sm')

    def getCleanDocs(self, data):
        pages = self.agg_pages(data)
        logger.info("Data aggrigated to Docs")

        docs = {}
        for domain in pages:
            words = word_tokenize(pages[domain], language = "german")
            if len(words) > 10000:
                words = words[:10000]
            
            # words smaller 2 out
            words = [word for word in words if len(word) > 1]

            # exclude "words" without letters 
            words = [word for word in words if re.search('[a-zA-Z]', word)]

            # exclude special characters 
            words = [re.sub('[^\w|-|.|\"|\s]', '', word) for word in words]

            docs[domain] = ' '.join(words)
        logger.info("removed tokens with length < 2 or no letters from docs")
        return docs

    def agg_pages(self, raw_data):
        res = dict()
        logger.info("aggrigation started")
        for k in raw_data:
            big_string_list = []
            data = json.loads(raw_data[k])
            for page in data:
                if not (page["title"] is None or page["content"] is None):
                    big_string_list.append(page["title"])
                    big_string_list.append(page["content"])    
            res[k] = "\n".join(big_string_list)

        return res

    def text_preprocess(self, docs, stopwords, no_ppo = True, only_nouns = True, lemmatize = True, stemming = True, split = True):
        res = {}
    
        for domain in docs:
            words = word_tokenize(docs[domain], language = "german")
            # reduction of words (in case of big websites) -> should only be necessary, if crawler uses a certain depth
            if len(words) > 1000000:
                words = words[:1000000]
            words = ' '.join(words)
            words = self.nlp(words)

            # exclude persons, places and organisations (optional)
            if no_ppo:
                words = [wort for wort in words if wort.ent_type_ not in ["PER", "ORG", "LOC"]]

            # only nouns (optional)
            if only_nouns:
                words = [wort for wort in words if wort.pos_ == 'NOUN']

            # lemmatization
            if lemmatize:
                worte_lem = []
                for wort in words:
                    if wort.pos_ in ["NOUN", "VERB", "ADJ", "ADV"]:
                        try:
                            wort_lem = self.lemmatizer.find_lemma(wort.orth_, wort.pos_)
                            worte_lem.append(wort_lem)
                        except:
                            print("error " + wort.pos_ + " " + wort.orth_)
                            worte_lem.append(wort.orth_)
                    else:
                        worte_lem.append(wort.orth_)
                words = worte_lem
            else:
                words = [wort.orth_ for wort in words]

            # split compund words
            if split:
                myobj = {'words': json.dumps(words)}
                x = requests.post(conf.url_split, data = myobj)
                res_req = json.loads(x.text) 
                words = res_req['text']
            
            # all lower
            words = [wort.lower() for wort in words]

            # exclude stopwords 
            words = [wort for wort in words if wort.lower() not in stopwords]

            # stemming
            word2stem = {}
            stem2word = {}
            if stemming:
                worte_stemmed = []
                for wort in words:
                    w_stem = self.stemmer.stem(wort)

                    # hier gehen informationen verloren, da ein wort z.b bau (aus baum) im dict abgespeichert wird
                    # und später von dem wort bau (aus bauer) überschrieben wird -> bau ist dann immer bauer (auch wenn es ursprünglich baum war)

                    word2stem[wort] = w_stem
                    stem2word[w_stem] = wort
                    worte_stemmed.append(w_stem)
        
                res[domain] = " ".join(worte_stemmed) 

                dict2file(word2stem, ".\\src\\Data\\PreProcessing", "word2stem.json")
                dict2file(stem2word, ".\\src\\Data\\PreProcessing", "stem2word.json")

            else:
                res[domain] = " ".join(words)
  
        dict2file(res, ".\\src\\Data\\PreProcessing", "aufbereiteteDaten.json")
    
        return res