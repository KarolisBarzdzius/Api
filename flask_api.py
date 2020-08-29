from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json})
    else:
        return jsonify({'about': 'Hello World'})

@app.route("/keliamieji/<int:metai>", methods=['GET'])
def keliamieji(metai):
    if isleap(metai):
        return jsonify({'result': "Keliamieji"})
    else:
        return jsonify({'result': "NE Keliamieji"})

if __name__ == '__main__':
    app.run()