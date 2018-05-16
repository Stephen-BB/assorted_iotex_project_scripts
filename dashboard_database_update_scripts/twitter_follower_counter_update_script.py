import tweepy

import psycopg2

# Variables that contains the user credentials to access Twitter API
access_token = "2963554943-LIKwxG0O3RDVvkBqcsTkvWgtiaQYzGt9RSyzcb1"
access_token_secret = "IHbAcMrox4rFU3T5ccy6TMRpIG5qXG33A8kpH7mn0V1EA"
consumer_key = "F22pmwM7h4c7B3qaTwjFAmFbL"
consumer_secret = "HSzk8wwRlWHEoXlvrInAUeUz85zqMRbU15u8SDvxLc6ve2pegg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


iotex_twitter = api.get_user('iotex_io')

twitter_followers = iotex_twitter.followers_count

print(iotex_twitter.followers_count)

conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

cur.execute("UPDATE TWITTER_FOLLOWER_COUNT set NUM_FOLLOWERS = (%s)", [iotex_twitter.followers_count])


conn.commit()
print("Records created successfully")
conn.close()
