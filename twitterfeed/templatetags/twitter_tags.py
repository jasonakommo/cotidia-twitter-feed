import json, re

from django.core.cache import cache
from django import template

from twitterfeed.utils import user_timeline, twitter_search
from twitterfeed import settings as twitter_settings

register = template.Library()


# Timeline

class UserTimelineNode(template.Node):
    def __init__(self, username, limit):
        self.username = template.Variable(username)
        self.limit = limit
    def render(self, context):

        try:
            self.username = self.username.resolve(context)
        except template.VariableDoesNotExist:
            pass

        if twitter_settings.TWITTER_ENABLE_CACHE:
            cache_key = twitter_settings.TWITTER_CACHE_STATUS_KEY + 'user_timeline' + re.sub('\W+', ' ', str(self.username)).strip()
            if cache.get(cache_key):
                statuses = cache.get(cache_key)
            else:
                statuses = user_timeline(str(self.username), self.limit)
                cache.set(cache_key, statuses, twitter_settings.TWITTER_CACHE_TIMEOUT)
        else:
            statuses = user_timeline(str(self.username), self.limit)

        context[twitter_settings.TWITTER_CONTEXT_STATUS_KEY] = json.loads(statuses)

        return ''

@register.tag(name="twitter_user_timeline")
def do_user_timeline(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, username, limit = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires some arguments: username, limit" % token.contents.split()[0])
    if not (username[0] == username[-1] and username[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return UserTimelineNode(username[1:-1], limit)

# Search

class SearchNode(template.Node):
    def __init__(self, query, limit):
        self.query = template.Variable(query)
        self.limit = limit
    def render(self, context):
        try:
            self.query = self.query.resolve(context)
        except template.VariableDoesNotExist:
            pass

        if twitter_settings.TWITTER_ENABLE_CACHE:
            cache_key = twitter_settings.TWITTER_CACHE_STATUS_KEY + 'search' + re.sub('\W+', ' ', self.query).strip()

            if cache.get(cache_key):
                statuses = cache.get(cache_key)
            else:
                statuses = twitter_search(self.query, self.limit)
                cache.set(cache_key, statuses, twitter_settings.TWITTER_CACHE_TIMEOUT)
        else:
            statuses = twitter_search(self.query, self.limit)

        context[twitter_settings.TWITTER_CONTEXT_STATUS_KEY] = json.loads(statuses)

        return ''

@register.tag(name="twitter_search")
def do_twitter_search(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, query, limit = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires some arguments: username, limit" % token.contents.split()[0])
    if not (query[0] == query[-1] and query[0] in ('"', "'")):
        #raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
        return SearchNode(query, limit)
    #if has quotes around
    else:
        return SearchNode(query[1:-1], limit)






