import requests
from bs4 import BeautifulSoup


def get_qiita_trend_data():
    url = 'https://qiita.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    data = soup.find(class_="css-81mxb5")
    data = a.find('h2')
    data = a.find('a')
    #記事のタイトル取得
    title = data.string
    #記事のurlを取得
    url = data['href']
    return title,url