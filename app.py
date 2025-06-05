from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/health-news')
def health_news():
    url = "https://www.youm7.com/Section/%D8%B5%D8%AD%D8%A9-%D9%88%D8%B7%D8%A8/245/1"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.select('.sectionList .newsList li')
    news = []

    for article in articles:
        title_tag = article.select_one('a')
        if title_tag:
            title = title_tag.get('title', '').strip()
            link = "https://www.youm7.com" + title_tag['href']
            news.append({"title": title, "link": link})

    return jsonify(news)

if __name__ == '__main__':
    app.run()
