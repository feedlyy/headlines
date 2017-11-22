# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:47:28 2017

@author: Feedlyy
"""

from flask import render_template


#app = Flask(__name__)
#@app.route("/")
#def get_news():
#    return "no news is good news"

#if __name__ == '__main__':
#    app.run(port=5001, debug=True)
    


#app2 = Flask(__name__)

import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEED = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest'}


@app.route("/")
@app.route("/<publication>")





def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return render_template("home.html", articles = feed['entries'])
    
if __name__ == "__main__":
    app.run(port=5010, debug=True)
    