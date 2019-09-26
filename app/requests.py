import urllib.request,json
from config import Config
from .models import Quotes

quote_url = None

def configureRequest(app):
  global quote_url
  quote_url = app.config['QUTES_URL']

def fetchQuotes():
  '''
  function that gets random quotes
  '''
  quote_url = "http://quotes.stormconsultancy.co.uk/random.json"
  with urllib.request.urlopen(quote_url) as url:
    get_quotes_data = url.read()
    quote_response = json.loads(get_quotes_data)

    quote = None
    if quote_response:
      author = quote_response.get('author')
      randomquote = quote_response.get('quote')
      quote = Quotes(author,randomquote)
  return quote