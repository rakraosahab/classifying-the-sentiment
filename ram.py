
from flask import Flask, request, jsonify
from inshorts import getNews
from flask_cors import CORS

ram = Flask(__name__)
ram.secret_key = "This code for Indegenous Company"
CORS(ram)

@ram.route('/')
def home():
    return 'News API is UP!<br><br>A part of <a href="https://github.com/rakraosahab">Rakesh Projects</a>'

@ram.route('/news')
def news():
    if request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))

if __name__ == '__main__':
    ram.debug = True
    ram.run(host='0.0.0.0',port=5000,use_reloader=True)
