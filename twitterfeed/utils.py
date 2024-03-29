import json, re, twitter
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

	api = twitter.Api(consumer_key=twitter_settings.TWITTER_CONSUMER_KEY, consumer_secret=twitter_settings.TWITTER_CONSUMER_SECRET, access_token_key=twitter_settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=twitter_settings.TWITTER_ACCESS_TOKEN_SECRET, base_url=twitter_settings.TWITTER_BASE_URL, cache=False)
	statuses = api.GetUserTimeline(screen_name=username, count=limit, include_rts=True)
	status_json = render_statuses(statuses)

	return json.dumps(status_json)

def twitter_search(term, limit=3):
	api = twitter.Api(consumer_key=twitter_settings.TWITTER_CONSUMER_KEY, consumer_secret=twitter_settings.TWITTER_CONSUMER_SECRET, access_token_key=twitter_settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=twitter_settings.TWITTER_ACCESS_TOKEN_SECRET, base_url=twitter_settings.TWITTER_BASE_URL)
	statuses = api.GetSearch(term=term, count=limit, include_entities=True)
	status_json = render_statuses(statuses)
	# i=0
	# for s in statuses:
	# 	if i < limit:
	# 		if s.entities.get('media', False):
	# 			status_json.append({'text':replace_url_to_link(s.text), 'created_at':twitter_date_format(s.created_at), 'media':s.entities['media']})
	# 			i=i+1

	return json.dumps(status_json)

#['contributors', 'coordinates', 'created_at', 'created_at_in_seconds', 'favorited', 'geo', 'hashtags', 'id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 
# 'in_reply_to_user_id', 'location', 'now', 'place', 'relative_created_at', 'retweet_count', 'retweeted', 'retweeted_status', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']

def render_statuses(statuses):
	status_json = []
	for s in statuses:
		user = {
			'description':s.user.description, 
			'followers_count':s.user.followers_count, 
			'id':s.user.id, 
			'listed_count':s.user.listed_count, 
			'location':s.user.location, 
			'name':s.user.name, 
			'profile_image_url':s.user.profile_image_url, 
			'screen_name':s.user.screen_name, 
			'statuses_count':s.user.statuses_count, 
			'url':s.user.url,
		}

		hashtags = [hashtag.text for hashtag in s.hashtags]
		media = []
		for m in s.media:
			media.append({
				"display_url": m.display_url, 
				"expanded_url": m.expanded_url, 
				"id": m.id, 
				"media_url": m.media_url, 
				"media_url_https": m.media_url_https, 
				"type": m.type, 
				"url": m.url
				})
		status = {
		'contributors': s.contributors,
		'coordinates':s.coordinates, 
		'created_at':twitter_date_format(s.created_at),
		'favorited':s.favorited, 
		'geo':s.geo, 
		'hashtags':hashtags, 
		'id':s.id, 
		'in_reply_to_screen_name':s.in_reply_to_screen_name, 
		'in_reply_to_status_id':s.in_reply_to_status_id, 
		'in_reply_to_user_id':s.in_reply_to_user_id, 
		'location':s.location, 
		'media':media, 
		'now':s.now, 
		'place':s.place, 
		'retweet_count':s.retweet_count, 
		'retweeted':s.retweeted, 
		'source':s.source, 
		'text':replace_url_to_link(s.text),
		'truncated':s.truncated, 
		'user':user,
		}

		status_json.append(status)

	return status_json
