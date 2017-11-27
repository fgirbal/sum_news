from flask import Flask, render_template, redirect, url_for, request, Response
from flask import make_response
import os.path
import requests as r
import gensim
import re, string, math
import nltk
import random as rand

app = Flask(__name__)
NEWS_API_KEY = '--'
DIFFBOT_TOKEN = '--'
connectors = [' Additionally, ', ' In addition, ', ' Also, ', ' Besides, ', ' Furthermore, ', ' Moreover, '];
test = False

def summarise(url):
    diff_bot_url = 'https://api.diffbot.com/v3/article?url=' + url + '&token='+ DIFFBOT_TOKEN
    resp = r.get(diff_bot_url)
    text = resp.json()['objects'][0]['text']
    return summarise_text(text)

def summarise_text(text):
    num_sentences = len(nltk.sent_tokenize(text))
    #while num_sentences > 10:
    #    ratio = 10 / num_sentences
    #    text = gensim.summarization.summarizer.summarize(text, ratio=ratio)
    #   num_sentences = len(nltk.sent_tokenize(text))

    #return str(num_sentences)
    if num_sentences == 0:
    	return ""

    return gensim.summarization.summarizer.summarize(text, ratio=2.0/num_sentences)

#if test == True:
	#	resp1 = make_response('{"text" : "test", "url" : "test", "keywords" : "test1,test2"}')
    #	resp1.headers['Content-Type'] = "application/json"
    #	return resp1

@app.route("/")
def home():
    return "hi"

@app.route("/index")
def index():
    return render_template("index.html", title = 'Projects')

@app.route('/requestnews', methods=['GET', 'POST'])
def login():
   	message = None
   	if request.method == 'POST':
   		num = request.form['num']
        news_sources = request.form['news_sources']

        news_api_url = 'https://newsapi.org/v2/everything?sources=' + news_sources + '&page=' + str(math.ceil(int(num)/20.0)) + '&apiKey=a8f94a7888994470b4df89155e9ab084'
        result = r.get(news_api_url)
        rjson = result.json()
        url_text = rjson['articles'][int(num)%20]['url']
        description_text = rjson['articles'][int(num)%20]['description']
        print description_text

        to_send = summarise(url_text)
        C = nltk.sent_tokenize(to_send)
        for i in xrange(1,len(C)):
        	val = rand.randint(0,len(connectors)-1)
        	C[i] = connectors[val] + C[i][:1].lower() + C[i][1:]

        to_send = ""
        for i in xrange(0,len(C)):
        	to_send += C[i]

       	to_send = filter(lambda x: x in string.printable, to_send)

        to_send = to_send.replace('"', "'")

        if len(description_text) > 200:
        	keywords = gensim.summarization.keywords(description_text, words=8)
        else:
        	keywords = gensim.summarization.keywords(to_send, words=8)

        resp = make_response('{"text" : "' + to_send.replace("\n", " ") + '", "url" : "' + url_text + '", "keywords" : "' + keywords.replace("\n", ",") + '"}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        #return render_template('index.html', message='')

if __name__ == "__main__":
	app.run(debug = True)