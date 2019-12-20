from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from ast import literal_eval
import json

from src.splitter import split

app = Flask(__name__)

@app.route("/split", methods=['GET', 'POST'])
def rawdata():
    if request.method == 'POST':
        raw_data = request.form.getlist("words")
        raw_data = json.loads(raw_data[0])

        text = split(raw_data)
        
        return jsonify({'text': text})

    if request.method == 'GET':
        return "try a POST"

app.run(port=8080, debug=True)