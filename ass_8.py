import requests
import json
response=requests.get(" https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?")
print(response.content)
