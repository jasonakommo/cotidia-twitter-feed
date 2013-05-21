import json

from django.core.cache import cache
from django import template

from twitterfeed.utils import user_timeline, twitter_search
from twitterfeed import settings as twitter_settings

register = template.Library()

class UserTimelineNode(template.Node):
    def __init__(self, username, limit):
        self.username = username
        self.limit = limit
    def render(self, context):

        # if cache.get(twitter_settings.TWITTER_CACHE_STATUS_KEY):
        #     statuses = cache.get(twitter_settings.TWITTER_CACHE_STATUS_KEY)
        # else:
        #     statuses = user_timeline(self.username, self.limit)
        #     cache.set(twitter_settings.TWITTER_CACHE_STATUS_KEY, statuses, twitter_settings.TWITTER_CACHE_TIMEOUT)
        statuses = user_timeline(self.username, self.limit)
        context[twitter_settings.TWITTER_CONTEXT_STATUS_KEY] = json.loads(statuses)

        print json.loads(statuses)

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