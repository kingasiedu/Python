import tweepy
import time 


#Api Access Key and Secret
auth = tweepy.OAuthHandler('Wpv7ZIerx7RufsGw04WHtemgW','N30NUF7xoOH5RXcEhBv5Et4fAr6UKYHJAN7clutqNAw4SBrYri')

#Api access token and access secret key
auth.set_access_token('1324903634904215552-eCgLacyFAtS6e2Medel16kZ7UMpXbN','4gQhoZW5PSqxe61T6o6xXFCYXVoCNsMH4pdFMdFeZhbQ4')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True) #Notify you if you've reached the rate limit 

FILE = "id.txt"

def retrieve_id(file):
    f_read = open(file, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_id(id, file):
    f_write = open(file, 'w')
    f_write.write(str(id))
    f.write.close()
    return


def reply():
    print("Replying tweeta")
    last_seen_id = retrieve_id(FILE)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id)) + '-' + mention.full_text, flush=True)
        last_seen_id = mentions.id
        store_id(last_seen_id, FILE)
        if "#John" in mention.fullz-text.lower():
            print("Responding #John" flush=True)

            api.update_status("@" + mention.user.screen_name + "#John this is me", mention.id)
while True:
    reply()
    time.sleep(15)


