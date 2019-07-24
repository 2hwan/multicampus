"""View Instagram user follower count from Instagram public api"""
import requests

def getfollowedby(url):
	"""View Instagram user follower count"""
	link = 'https://www.instagram.com/%s/?__a=1'
	tag = link % (url)
	user = requests.get(tag)
	print(user.json())
	follower = (user.json()['graphql']['user']['edge_followed_by']['count'])
	#return (user.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['thumbnail_src'])
	lst_thumbnail = []
	for i in range(10):
		lst_thumbnail.append(user.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['thumbnail_src'])
	return (follower, lst_thumbnail)

def getname(url):
	"""Split the URL from the username"""
	return url.replace("https://", "").replace("www.", "").replace("instagram.com/", "").replace("/", "")

