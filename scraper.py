from bs4 import BeautifulSoup as bs
import requests
import discogs_client

def setupAPI():
    d = discogs_client.Client("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                            consumer_key = "oDYvRJhHcCDEZufnvWGF",
                            consumer_secret = "UqukPkVujumXwUAWNLtoYxmxHNQzFMzR")
    url = d.get_authorize_url()
    return url[2]

def getUserCollection(s):
    profileUrl ="https://www.discogs.com/my"
    soup = bs(s.get(profileUrl).text, 'html.parser')
    print(soup.text)
