from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('source.html',id = source_id )

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_sources('popular')
    print(popular_news)
    title = 'NewsApp - Informative channel to catch your daily news'
    return render_template('index.html', title = title,popular = popular_news)
