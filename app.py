from flask import Flask, render_template,request,jsonify
from pymongo import MongoClient
from bot import telegram
import re,os


uri = os.environ.get('URI')
client = MongoClient(uri)
db = client['database']
collection = db['data']
app = Flask(__name__)
dwn_url = os.environ.get('STREAM_URL')


@app.get('/')
def index ():
    items = list(collection.find())
    return render_template('index.html',items=items[::-1])
@app.get('/<id>/<movie>')
def page(id,movie):
    item= collection.find_one({"_id":int(id)})
    return render_template('page.html',item=item,username=os.environ.get('BOT_USERNAME'),dwn_url=dwn_url)

@app.get('/search')
def search():
    query= request.args.get('query')
    regex_query = {'title': {'$regex': re.escape(query), '$options': 'i'}}
    items = list(collection.find(regex_query))
    if query =="":
        return jsonify(items[::-1])
    else:
        return jsonify(items)

@app.post('/telegram')
def tg():
    data = request.get_json()
    if data.get('message'):
        telegram(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run()

