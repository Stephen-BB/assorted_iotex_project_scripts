from pyrogram import Client
from pyrogram.api import functions

import psycopg2

client = Client("example")
client.start()

full_channel = client.send(
    functions.channels.GetFullChannel(
        channel=client.resolve_peer("IoTexGroup")
    )
)

num_mems = full_channel.full_chat.participants_count

print(full_channel.full_chat.participants_count)
client.stop()
conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

# commented out code was used to make the initial db entry
# cur.execute('''CREATE TABLE TELEGRAM_NUM_MEMS
#       (NUM_MEMS INT PRIMARY KEY     NOT NULL);''')
# print("Table created successfully")
#
# cur.execute("INSERT INTO TELEGRAM_NUM_MEMS (NUM_MEMS) VALUES (%s)", [num_mems])

cur.execute("UPDATE TELEGRAM_NUM_MEMS set NUM_MEMS = (%s)", [num_mems])


conn.commit()
print("Records created successfully")
conn.close()
