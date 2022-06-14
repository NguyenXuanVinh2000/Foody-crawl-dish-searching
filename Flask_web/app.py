from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': '172.17.0.1', 'port': 9200}])


@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data =[]
        drink_names = request.form['search']
        sort = request.form['drinks']
        resp = es.search(index="store", size=50 ,
        body=
{
  "query": {    
    "match": {
      "drink_names": {
        "query": drink_names,
        "max_expansions": 3

      }
    }
  }
}
                    )
        for hit in resp['hits']['hits']:
           data.append(hit["_source"])
        if sort == "price":
            data = sorted(data, key=lambda i: float(i["prices"]), reverse=False)
        elif sort == "Rating":
            data = sorted(data, key=lambda i: float(i["ratings"]), reverse=True)
        if not data:    
            return render_template('no_results.html')
        return render_template('search.html', datas = data)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
