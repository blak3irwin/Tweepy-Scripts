import tweepy
import sys

#This is a first take at a script to provide all tweets in past 30 days within specified distance around a set of coordinates.
#My plan is to expand this script and add additional scripts or combine into a more robust scripts.  


tweepy.certfile="/root/Downloads/certnew2.cer"
tweepy.cert_reqs='NONE'
#define Twitter Keys and ACCESS_TOKEN_SECRET
CONSUMER_KEY = 'tT57SvQtwUkDFpiAPrTrvDIk0'
CONSUMER_SECRET = 'jYrO5gj6TJmueB1W9yCMtv4USGRhR1s6CBUBgYWDiIw4b9TxrV'
ACCESS_TOKEN = '2224289669-8v6p9QHQju3TYmXuRJR18uu8hpQlQjoKvvyuBgA'
ACCESS_TOKEN_SECRET = 'V3Iby0OFqRnJcTMLtd5QdqhgGLuKF3V4khJ5tlhfXjUQF'

#session authentication
def authenticate():
    #sets keys/tokens
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    #authenticate
    api = tweepy.API(auth)
    #print username to validate auth was successful
    print (api.me().name)
    print 'authentication successful'
    return api

#geolocation function for tweets near a location
def geolocate(geocode,dist,api):
    #print variables
    print 'geocode = '+geocode
    print 'dist = '+dist
    #query of twitter by lat,lon,digest
    results = api.search(show_user="true",geocode=geocode+','+dist)

    #parse status
    #parsed_results = [s.text.encode('utf8') for s in results]
    #print status
    print 'status from location\n\n'
    for line in results:
        print 'Username = @'+line.user.screen_name
        print 'Tweet - '+line.text,'\n'

#listing of who a user follows by username
def friendslist(friends,api):
    print 'list of friends for '+friends
    results = api.friends_ids(friends)
    for i in results:
        user = api.get_user(i)
        print '@'+user.screen_name

args = sys.argv[1:]

if not args:
    print 'usage: [--geocode 12.1234567,98.7654321 5km]'
    sys.exit(1)
geocode = ''
dist = ''
if args:
    if args[0] == '--geocode':
        geocode = args[1]
        dist = args[2]
        del args[0:2]
        api = authenticate()
        geolocate(geocode,dist,api)
    elif args[0] == '--friends':
        friends = args[1]
        del args[0:2]
        api = authenticate()
        friendslist(friends,api)
    else:
        print 'usage: [--geocode 12.1234567,98.7654321 5km or --friends <username>]'
        sys.exit(1)
