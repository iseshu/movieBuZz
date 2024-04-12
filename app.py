from flask import Flask, render_template,request,jsonify
from pymongo import MongoClient
import re,os


uri = os.environ.get('URI')
client = MongoClient(uri)
db = client['database']
collection = db['data']
app = Flask(__name__,template_folder='templates')
dwn_url = os.environ.get('STREAM_URL')


@app.get('/')
def index ():
    items = list(collection.find())
    return render_template('index.html',items=items[::-1])
@app.get('/<id>/<movie>')
def page(id,movie):
    item= collection.find_one({"_id":int(id)})
    return render_template('page.html',item=item,dwn_url=dwn_url)

@app.get('/search')
def search():
    query= request.args.get('query')
    regex_query = {'title': {'$regex': re.escape(query), '$options': 'i'}}
    items = list(collection.find(regex_query))
    if query =="":
        return jsonify(items[::-1])
    else:
        return jsonify(items)


@app.route('/stream')
def stream():
    id = request.args.get('id')
    item = collection.find_one({"_id":int(id)})
    return render_template('stream.html',dwn_url=dwn_url,item=item,size_format=size_format)

def size_format(b):
    if b < 1000:
              return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b/1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b/1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b/1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b/1000000000000) + 'TB'

if __name__ == '__main__':
    app.run()

