
# coding: utf-8

# In[9]:


import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# In[ ]:


from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('Oct20trends.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#23YearsOfTimelessDDLJ',"#INDvPAK","#2CroreJobs","The BJP","Huddersfield","#CHEMUN","HUDLIV","Sumit Malik"],stall_warnings=True)

