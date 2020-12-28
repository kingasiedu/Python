import tweepy
import time

#Api Access Key and Secret
auth = tweepy.OAuthHandler('Wpv7ZIerx7RufsGw04WHtemgW','N30NUF7xoOH5RXcEhBv5Et4fAr6UKYHJAN7clutqNAw4SBrYri')

#Api access token and access secret key
auth.set_access_token('1324903634904215552-eCgLacyFAtS6e2Medel16kZ7UMpXbN','4gQhoZW5PSqxe61T6o6xXFCYXVoCNsMH4pdFMdFeZhbQ4')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


user = api.me()


#Prints the information of the user
#print(user)

#Prints the name of the user
#print(user.screen_name)




def retweet():
    
    search = "#Jon1"
    for tweet in tweepy.Cursor(api.search, search).items(number_of_tweet):
        try:
            #Searches and retweets tweet that are found 
            print("About to retweet")
            tweet.retweet()
            print("Your tweet has been retweeted")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
       
    

while True:
    retweet()
    time.sleep(5)
    


            


