from flask import Flask, render_template, url_for
from news import News
from weather import Weather

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    rass = News()
    titles = rass.article_titles
    descriptions = rass.article_descriptions
    content = rass.article_content
    authors = rass.article_authors
    return render_template('news.html', news=rass, titles=titles, descriptions=descriptions, content=content, authors=authors)


@app.route('/weather')
def weather():
    w = Weather()
    report = w.report
    return render_template('weather.html', weather=report)


if __name__ == '__main__':
    app.run(debug=True)
