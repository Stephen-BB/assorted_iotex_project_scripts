from pytrends.request import TrendReq

import psycopg2



pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["iotex"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')

interest_over_time_df = pytrends.interest_over_time()


interest_dict = interest_over_time_df['iotex'].to_dict()

timestamps = []
values = []
for item in interest_dict:
    values.append(interest_dict[item])  # engagement value
    timestamps.append(item.to_pydatetime().strftime('%m/%d/%Y'))  # panda timestamp can add .date to just get date btw

print(timestamps[0].strftime('%m/%d/%Y'))

conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE GOOGLE_TRENDS
      (TREND_VALUE INT PRIMARY KEY     NOT NULL,
      TREND_DATE    TEXT    NOT NULL);''')

print("Table created successfully")

i = 0
while i < len(values):
    cur.execute("INSERT GOOGLE_TRENDS (TREND_VALUE, ) = (%s)", [values[i]])
    i += 1

cur.execute("INSERT INTO REDDIT_SUBSCRIBERS (SUBSCRIBERS) VALUES (%s)", [subreddit.subscribers])

conn.commit()
print("Records created successfully")
conn.close()
