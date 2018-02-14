import tweepy
import sys

#This is a first take at a script to provide all tweets in past 30 days within specified distance around a set of coordinates.
#My plan is to expand this script and add additional scripts or combine into a more robust scripts.  


#define Twitter Keys and ACCESS_TOKEN_SECRET
#Get KEYS and ACCESS TOKENS for you account from here https://apps.twitter.com
CONSUMER_KEY = ‘INPUT CONSUMER KEY HERE’
CONSUMER_SECRET = ‘INPUT CONSUMER SECRET HERE’
ACCESS_TOKEN = ‘INPUT ACCESS TOKEN HERE’
ACCESS_TOKEN_SECRET = ‘INPUT ACCESS TOKEN SECRET HERE’


#sets keys/tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#authenticate
api = tweepy.API(auth)

#print username to validate auth was successful
print(api.me().name)
print ‘If name prints, authentication is successful’
#need to enhance code

args = sys.argv[1:]

if not args:
    print 'usage: [--geocode 12.1234567,98.7654321 --dist 5km]'
    sys.exit(1)
geocode = ''
dist = ''

if args[0] == '--geocode':
    geocode = args[1]
    del args[0:2]
if args[0] == '--dist':
    dist = args[1]
    del args[0:2]
print 'geocode = '+geocode
print 'dist = '+dist
#query of twitter by lat,lon,digest
results = api.search(show_user="true",geocode=geocode+','+dist)


#print tweet username and status
print 'status from location\n\n'
for line in results:
    print 'Username: @'+line.user.screen_name
    print ’Status: '+line.text,'\n'
