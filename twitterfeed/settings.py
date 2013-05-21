from django.conf import settings

# How long to cache for in seconds
TWITTER_CACHE_TIMEOUT = getattr(settings, 'TWITTER_CACHE_TIMEOUT', 1800)
# The cache key name for twitter statuses
TWITTER_CACHE_STATUS_KEY = getattr(settings, 'TWITTER_CACHE_STATUS_KEY', 'twitter_statuses')
# The context key name for twitter statuses
TWITTER_CONTEXT_STATUS_KEY = getattr(settings, 'TWITTER_CONTEXT_STATUS_KEY', 'twitter_statuses')

# Twitter credentials
TWITTER_CONSUMER_KEY = getattr(settings, 'TWITTER_CONSUMER_KEY', False)
TWITTER_CONSUMER_SECRET = getattr(settings, 'TWITTER_CONSUMER_SECRET', False)
TWITTER_ACCESS_TOKEN_KEY = getattr(settings, 'TWITTER_ACCESS_TOKEN_KEY', False)
TWITTER_ACCESS_TOKEN_SECRET = getattr(settings, 'TWITTER_ACCESS_TOKEN_SECRET', False)


