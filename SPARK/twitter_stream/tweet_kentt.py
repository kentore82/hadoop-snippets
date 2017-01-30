import json
import tweepy
import socket
import sys

def initialize():
    with open("/home/kentt/pems/twitter/config.json") as config_data:
        config = json.load(config_data)

    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)

    stream = TwitterStreamListener()
    twitter_stream = tweepy.Stream(auth = api.auth, listener=stream)
    twitter_stream.filter(track=['python'], async=True)


class TwitterStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        
        data_dict=json.loads(data)
        
        try:
            text = str(data_dict["lang"])+' : '+str(data_dict["text"].decode('utf_8'))
        except:
            text = "Cannot_encode"

        print text

        #except KeyboardInterrupt:
        #    print('Aborting on Ctrl-c, goodbye!')
        #    pass


    #def on_error(self, status_code):
    #    try:
    #        if status_code == 420:
    #            return False
    #    except KeyboardInterrupt:
    #        print('Aborting on Ctrl-c, goodbye!')
    #        pass

        

if __name__ == "__main__":
    initialize()
    
