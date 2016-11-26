import twitter
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def fetch_tweets():
    api = twitter.Api(consumer_key=settings.CONSUMER_KEY,
                      consumer_secret=settings.CONSUMER_SECRET,
                      access_token_key=settings.ACCESS_TOKEN,
                      access_token_secret=settings.ACCESS_TOKEN_SECRET)
    print settings.TWITTER_SEARCH_QUERY
    return api.GetSearch(raw_query=settings.TWITTER_SEARCH_QUERY)
