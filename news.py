import requests
from forms import NewPost

API_KEY = "421ce3a588544ae193f3492f77956d73"
# country = input('Country: ')
country = 'ca'
# query = input('What are you searching for?')

top_headlines_endpoint = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
# everything_endpoint = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'

top_headlines_endpoint_response = requests.get(f'{top_headlines_endpoint}').json()


# everything_endpoint_response = requests.get(f'{everything_endpoint}')

class News:
    # ------------------ ARTICLE TITLES ------------------ #
    article_titles = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_titles.append(top_headlines_endpoint_response['articles'][i]['title'])

    # ------------------ ARTICLE DESCRIPTIONS ------------------ #

    article_descriptions = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_descriptions.append(top_headlines_endpoint_response['articles'][i]['description'])

    # ------------------ ARTICLE AUTHORS ------------------ #

    article_authors = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_authors.append(top_headlines_endpoint_response['articles'][i]['author'])

    # ------------------ ARTICLE URLS ------------------ #

    article_urls = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_urls.append(top_headlines_endpoint_response['articles'][i]['url'])

    # ------------------ ARTICLE IMG URLS ------------------ #

    article_img_urls = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_img_urls.append(top_headlines_endpoint_response['articles'][i]['urlToImage'])

    # ------------------ ARTICLE CONTENT ------------------ #
    article_content = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_content.append(top_headlines_endpoint_response['articles'][i]['content'])

    # ------------------ ARTICLE PUBLISHED AT ------------------ #
    article_published_at = []
    for i in range(len(top_headlines_endpoint_response['articles'])):
        article_published_at.append(top_headlines_endpoint_response['articles'][i]['publishedAt'])
