import json, re
from twitterfeed import twitter
from twitterfeed import settings as twitter_settings

def replace_url_to_link(value):
    # Replace url to link
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    # Replace email to mailto
    urls = re.compile(r"([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="mailto:\1">\1</a>', value)
    return value

def twitter_date_format(datestring):
	d = datestring.split(' ')
	return u"%s %s %s" % (d[2], d[1], d[5])

def user_timeline(username, limit=10):

	api = twitter.Api(consumer_key=twitter_settings.TWITTER_CONSUMER_KEY, consumer_secret=twitter_settings.TWITTER_CONSUMER_SECRET, access_token_key=twitter_settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=twitter_settings.TWITTER_ACCESS_TOKEN_SECRET)
	statuses = api.GetUserTimeline(screen_name=username, count=limit)
	status_json = []
	for s in statuses:
		status_json.append({'text':replace_url_to_link(s.text), 'created_at':twitter_date_format(s.created_at)})
	return json.dumps(status_json)

def twitter_search(term, limit=3):
	api = twitter.Api(consumer_key=twitter_settings.TWITTER_CONSUMER_KEY, consumer_secret=twitter_settings.TWITTER_CONSUMER_SECRET, access_token_key=twitter_settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=twitter_settings.TWITTER_ACCESS_TOKEN_SECRET)
	statuses = api.GetSearch(term=term, per_page=50, page=1, include_entities=True)
	status_json = []
	i=0
	for s in statuses:
		if i < limit:
			if s.entities.get('media', False):
				status_json.append({'text':replace_url_to_link(s.text), 'created_at':twitter_date_format(s.created_at), 'media':s.entities['media']})
				i=i+1
	return json.dumps(status_json)

#['contributors', 'coordinates', 'created_at', 'created_at_in_seconds', 'favorited', 'geo', 'hashtags', 'id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 
# 'in_reply_to_user_id', 'location', 'now', 'place', 'relative_created_at', 'retweet_count', 'retweeted', 'retweeted_status', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']