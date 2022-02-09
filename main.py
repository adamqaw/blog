from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import requests
from weather import Weather
from forms import NewPost
from news import News
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd2376qudyafcgab81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NewsArticles(db.Model):
    __tablename__ = "news_articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    author = db.Column(db.String(100))
    url = db.Column(db.String(300))
    img_url = db.Column(db.String(300))
    content = db.Column(db.String(6000))
    date = db.Column(db.String(10))


# db.create_all()

# ------------------- NEWS API------------------- # 
API_KEY = "421ce3a588544ae193f3492f77956d73"
# country = input('Country: ')
country = 'ca'
# query = input('What are you searching for?')

top_headlines_endpoint = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
# everything_endpoint = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'

top_headlines_endpoint_response = requests.get(f'{top_headlines_endpoint}').json()


# everything_endpoint_response = requests.get(f'{everything_endpoint}')

@app.route('/', methods=['GET', 'POST'])
def home():
    # Configure forms and post to db
    if not dt.datetime.today():
        for i in range(len(News.article_titles)):
            new_post = NewPost(
                title=News.article_titles[i],
                description=News.article_descriptions[i],
                content=News.article_content[i],
                author=News.article_authors[i],
                date=News.article_published_at[i],
                url=News.article_urls[i],
                img_url=News.article_img_urls[i]
            )

            n = NewsArticles(
                title=new_post.title.data,
                description=new_post.description.data,
                content=new_post.content.data,
                author=new_post.author.data,
                date=new_post.date.data,
                url=new_post.url.data,
                img_url=new_post.img_url.data,
            )

            db.session.add(n)
            db.session.commit()
        else:
            pass
    return render_template('index.html')


@app.route('/news', methods=['GET', 'POST'])
def news():
    # Fetch items from DB
    articles = NewsArticles.query.all()

    return render_template('news.html', articles=articles)


@app.route('/weather')
def weather():
    w = Weather()
    report = w.report
    return render_template('weather.html', weather=report)


if __name__ == '__main__':
    app.run(debug=True)
