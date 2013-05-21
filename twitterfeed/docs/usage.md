Usage
=====

In your template, load the twitter template tags:

	{% load twitter_tags %}

Place the following tag anywhere in your template:

	{% twitter_user_timeline "username" limit %}

`username` must be in quote

`limit` must be an integer

The tag will push variable to your template context, in the same key name as `TWITTER_CONTEXT_STATUS_KEY`.

So it is then up to you how you display your statuses. Here's an example:

	{% for status in twitter_statuses %}
		<p>{{status.text|safe}} - {{status.created_at|safe}}</p>
	{% endfor %}
	
Available status variables are:

`status.text`: the tweet message
`status.created_at`: the formatted date of the tweet