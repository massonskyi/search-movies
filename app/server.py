import configparser

from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from utils.search_movie import search_movies
app = Flask(__name__)
CORS(app)  

config = configparser.ConfigParser()
config.read(config)

@app.route("/search_movies", methods=["POST"])
def search_movie():
    title = request.args.get('title')
    # imdb_id = request.args.get('imdb_id')
    year = request.args.get('year')
    # r_type = request.args.get('r_type', 'movie')
    # plot = request.args.get('plot', 'short')

    result = search_movies(title, None, year, None, None, '31bb8dfa')
    
    if not result:
        return jsonify({'error': 'No movies found.'}), 404
    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

