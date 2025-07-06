from flask import Flask, jsonify, request

# create a Flask app
app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
  query = request.get_json()
  return query


app.run(debug=True)
# testing :
# $ curl -X POST  http://127.0.0.1:5000/search -H 'Content-Type: application/json' -d '{"freq":"[34.55,5.55]","power":"[123.33,23.33]"}'