from flask import Flask, render_template, url_for
from news import News

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    rass = News()
    return render_template('news.html', news=rass)


if __name__ == '__main__':
    app.run(debug=True)
