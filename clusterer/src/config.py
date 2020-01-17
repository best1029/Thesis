import os
dirname = os.path.dirname(__file__)

#path_bereinigtesCrawlErgebnis_Startseiten = os.path.join(dirname, r'data/technischBereinigt/TeilC.json')
path_bereinigtesCrawlErgebnis_Startseiten = os.path.join(dirname, r'data/technischBereinigt/bereinigtesCrawlergebnis_Startseiten.json')
path_bereinigtesCrawlErgebnis_Startseiten_Evaluation = os.path.join(dirname, r'data/technischBereinigt/bereinigtesCrawlergebnis_Startseiten_Evaluation.json')
path_bereinigtesCrawlErgebnis_16 = os.path.join(dirname, r'data/technischBereinigt/bereinigtesCrawlergebnis_16.json')
path_bereinigtesCrawlErgebnis_16_Evaluation = os.path.join(dirname, r'data/technischBereinigt/bereinigtesCrawlergebnis_Evaluation.json')
path_goldstandard = os.path.join(dirname, r'data/goldstandard/goldstandard.json')
path_goldstandard_evaluation = os.path.join(dirname, r'data/goldstandard/goldstandard_evaluation.json')

path_aufbereitet = os.path.join(dirname, r'data/preProcessing/aufbereiteteDaten.json')
path_model_wiki = os.path.join(dirname, r'data/models/wiki_model.bin')
path_model_extended = os.path.join(dirname, r'data/models/model_extended.bin')
path_stopwords_ger = os.path.join(dirname, r'data/preProcessing/stopwords.txt')

#path_rohdaten = "C:\\cygwin64\\home\\solr-import-export-json-master\\out\\Goldstandard_V3_16Tief.json"
#path_urls = "C:\\cygwin64\\home\\apache-nutch-1.15-binary\\urls\\Goldstandard.txt"

url_split = 'http://localhost:8080/split'

default_idf_limit_min = 2.1
default_idf_limi_max = 3.85