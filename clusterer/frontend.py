from flask import Flask, render_template, request
from flask_googlecharts import GoogleCharts, BarChart
from backend import *
import json

from src.inOut import getData
import src.config as conf
from src.logger import logger

app = Flask(__name__)
backend = Backend()

@app.route("/")
def index():
    return render_template('start.html')

@app.route("/rawdata", methods=['GET', 'POST'])
def rawdata():
    if request.method == 'POST':
        path = request.form["path"]
        depth = request.form["depth"]
        calc_sw = 'true' == request.form["cal_stopwords"]

        if not path:
            backend.loadRawData(depth)
        else:
            backend.loadRawData(path=path)
        logger.info("raw Data loadad, next loading stopwords")
        backend.loadStopWords(calc_sw)

        return "sucsessfully loaded the data"

    if request.method == 'GET':
        return "try a POST"

@app.route("/preprocess", methods=['GET', 'POST'])
def preprocess():
    if request.method == 'POST':
        no_ppo = 'true' == request.form["no_ppo"]
        only_noun = 'true' == request.form["only_nouns"]
        lem = 'true' == request.form["lemmatization"]
        split = 'true' == request.form["split"]
        stem = 'true' == request.form["stemming"]

        backend.getProcessedData(no_ppo = no_ppo, only_noun = only_noun, lem = lem, stem = stem, split = split)

        return "succsessfully processed the data"

    if request.method == 'GET':
        return "try a POST"

@app.route("/res", methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        repr = request.form["representation"]
        algo = request.form["algorithm"]
        similarity_measure = request.form["similarity"]
        min_ngrams = int(request.form["min_ngram"]) if request.form["min_ngram"].isdigit() else 1
        max_ngrams = int(request.form["max_ngram"]) if request.form["max_ngram"].isdigit() else 1
        n_cluster = int(request.form["n_cluster"])
        n_dim = request.form["n_dim"]

        if n_dim.isdigit():
            n_dim = int(n_dim)
            res = backend.runAlgorithm(repr, algo, similarity_measure, n_cluster, min_ngrams, max_ngrams, n_dim = n_dim)
        else:
            res = backend.runAlgorithm(repr, algo, similarity_measure, n_cluster, min_ngrams, max_ngrams)

        return res

    if request.method == 'GET':
        return "no data"

app.run(debug=True)