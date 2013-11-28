Installation
============

Download the package:

	$ pip install -e git+https://guillaumepiot@bitbucket.org/guillaumepiot/cotidia-twitter-feed.git#egg=twitterfeed

Add it to the installed apps in setting:

	INSTALLED_APPS = (
		...
	    'twitterfeed',
	)
	
Make sure you have a cache backend in place, as the twitter feed will be cached. If you use database cache, you will need to create the table:

	python manage.py createcachetable [cache_table_name]

And add the following cache settings:

	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
	        'LOCATION': 'cache_table_name',
	    }
	}


Twitter settings
----------------


### MANDATORY

Must be set in your project settings

	# Twitter credentials
	`TWITTER_CONSUMER_KEY = ''`
	`TWITTER_CONSUMER_SECRET = ''`
	`TWITTER_ACCESS_TOKEN_KEY = ''`
	`TWITTER_ACCESS_TOKEN_SECRET = ''`

### OPTIONAL

	# How long to cache for in seconds
	`TWITTER_CACHE_TIMEOUT = 1800`

	# The cache key name for twitter statuses
	`TWITTER_CACHE_STATUS_NAME = 'twitter_statuses'`

	# The context key name for twitter statuses
	`TWITTER_CONTEXT_STATUS_KEY = 'twitter_statuses'`
	
	# The base API url
	`TWITTER_BASE_URL` = 'https://api.twitter.com/1.1'
	
	# Caching (Recommended)
	TWITTER_ENABLE_CACHE = getattr(settings, 'TWITTER_ENABLE_CACHE', True)

### NON UNIQUE CACHE KEY

You may have more than one Twitter query to cache, let's say if you a different twitter search result on each page. The cache key specified in settings will automatically add the type of feed (usere timeline or search) and the username or query. That way you can have more than one query cached at any given time.

Bear in mind that you could run into a rate limit over 150 hits per hour, so with a timeout of 30 mins, you may only be able to have 75 different twitter queries cached at any given time.