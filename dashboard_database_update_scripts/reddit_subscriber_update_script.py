import praw

import psycopg2

reddit = praw.Reddit(client_id='zSxaKfFzfoasnQ',
                     client_secret='ftGyUfQqeLnxFylbqkC2MX_DOHA',
                     user_agent='Python subscriber count checker v1.0 (by /u/Varauk )')

subreddit = reddit.subreddit('iotex')

print(subreddit.subscribers)


conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE REDDIT_SUBSCRIBERS
      (SUBSCRIBERS INT PRIMARY KEY     NOT NULL);''')

print("Table created successfully")

cur.execute("INSERT INTO REDDIT_SUBSCRIBERS (SUBSCRIBERS) VALUES (%s)", [subreddit.subscribers])

conn.commit()
print("Records created successfully")
conn.close()

