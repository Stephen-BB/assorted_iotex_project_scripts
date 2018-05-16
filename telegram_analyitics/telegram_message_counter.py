import time
import calendar

from pyrogram import Client
from pyrogram.api import functions
from pyrogram.api.errors import FloodWait

client = Client("example")
client.start()

target = "IoTeXGroup"  # "me" refers to your own chat (Saved Messages)
history = []  # List that will contain all the messages of the target chat
limit = 100  # Amount of messages to retrieve for each API call
offset = 0  # Offset starts at 0

while True:
    try:
        messages = client.send(
            functions.messages.GetHistory(
                client.resolve_peer(target),
                0, 0, offset, limit, 0, 0, 0
            )
        )
    except FloodWait as e:
        # For very large chats the method call can raise a FloodWait
        time.sleep(e.x)  # Sleep X seconds before continuing
        continue

    if not messages.messages:
        break  # No more messages left

    history.extend(messages.messages)
    offset += limit

client.stop()
from_ids = []
for item in history:
    from_ids.append(item.from_id)

unique_ids = set(from_ids)
print(len(unique_ids))

print(len(history))
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0
day6 = 0
day7 = 0
day8 = 0
day9 = 0
day10 = 0
day11 = 0
day12 = 0
day13 = 0
day14 = 0
day15 = 0
day16 = 0
day17 = 0
day18 = 0
day19 = 0
day20 = 0
day21 = 0
day22 = 0
day23 = 0
day24 = 0
day25 = 0
day26 = 0
day27 = 0
day28 = 0
day29 = 0
day30 = 0
longer_ago = 0

for item in history:
    if item.date > calendar.timegm(time.gmtime()) - 86400:
        day1 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 2):
        day2 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 3):
        day3 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 4):
        day4 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 5):
        day5 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 6):
        day6 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 7):
        day7 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 8):
        day8 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 9):
        day9 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 10):
        day10 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 11):
        day11 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 12):
        day12 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 13):
        day13 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 14):
        day14 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 15):
        day15 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 16):
        day16 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 17):
        day17 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 18):
        day18 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 19):
        day19 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 20):
        day20 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 21):
        day21 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 22):
        day22 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 23):
        day23 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 24):
        day24 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 25):
        day25 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 26):
        day26 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 27):
        day27 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 28):
        day28 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 29):
        day29 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 30):
        day30 += 1
    elif item.date > calendar.timegm(time.gmtime()) - (86400 * 30):
        day30 += 1
    else:
        longer_ago += 1


print(day1)
print(day2)
print(day3)
print(day4)
print(day5)
print(day6)
print(day7)
print(day8)
print(day9)
print(day10)
print(day11)
print(day12)
print(day13)
print(day14)
print(day15)
print(day16)
print(day17)
print(day18)
print(day19)
print(day20)
print(day21)
print(day22)
print(day23)
print(day24)
print(day25)
print(day26)
print(day27)
print(day28)
print(day29)
print(day30)

print(longer_ago)
# Now the "history" list contains all the messages sorted by date in
# descending order (from the most recent to the oldest one)
