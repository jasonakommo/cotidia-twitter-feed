Installation
============

Download the package:

	$ pip install -e 

Add it to the installed apps in setting:

	INSTALLED_APPS = (
		...
	    'twitterfeed',
	)
	
Make sure you have a cache backend in place, as the twitter feed will be cached. If you use database cache, you will need to create the table:

	python manage.py createcachetable [cache_table_name]


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