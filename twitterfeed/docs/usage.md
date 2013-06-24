Usage
=====

## Template integration

In your template, load the twitter template tags:

	{% load twitter_tags %}

Place the following tag anywhere in your template:

	{% twitter_user_timeline "username" limit %}

`username` must be in quote

`limit` must be an integer

The tag will push variable to your template context, in the same key name as `TWITTER_CONTEXT_STATUS_KEY`.

So it is then up to you how you display your statuses. Here's a simple example:

	{% for status in twitter_statuses %}
		<p>{{status.text|safe}} - {{status.created_at|safe}}</p>
	{% endfor %}
	
And a more advanced one:

	{% for status in twitter_statuses %}
		<a href="http://twitter.com/{{status.user.screen_name}}" target="_blank"><img src="{{status.user.profile_image_url}}" alt="{{status.user.name}}" title="{{status.user.name}}"></a>
		<p><strong>{{status.user.name}}</strong><br> {{status.text|safe}}<br> {{status.created_at|safe}}</p>
	{% endfor %}
	
## Variables

`status.text`: the tweet message

`status.created_at`: the formatted date of the tweet

###Complete JSON status

	status = {
		'contributors': s.contributors,
		'coordinates':s.coordinates, 
		'created_at':twitter_date_format(s.created_at),
		'created_at_in_seconds':s.created_at_in_seconds, 
		'favorited':s.favorited, 
		'geo':s.geo, 
		'hashtags':[], 
		'id':s.id, 
		'in_reply_to_screen_name':s.in_reply_to_screen_name, 
		'in_reply_to_status_id':s.in_reply_to_status_id, 
		'in_reply_to_user_id':s.in_reply_to_user_id, 
		'location':s.location, 
		'media':s.media, 
		'now':s.now, 
		'place':s.place, 
		'relative_created_at':s.relative_created_at, 
		'retweet_count':s.retweet_count, 
		'retweeted':s.retweeted, 
		'retweeted_status':s.retweeted_status, 
		'source':s.source, 
		'text':replace_url_to_link(s.text),
		'truncated':s.truncated, 
		'urls':s.urls, 
		'user':{
			'description':s.user.description, 
			'followers_count':s.user.followers_count, 
			'id':s.user.id, 
			'listed_count':s.user.listed_count, 
			'location':s.user.location, 
			'name':s.user.name, 
			'profile_image_url':s.user.profile_image_url, 
			'screen_name':s.user.screen_name, 
			'status':s.user.status, 
			'statuses_count':s.user.statuses_count, 
			'url':s.user.url,
		}, 
		'user_mentions':s.user_mentions,
		}