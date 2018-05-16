import time
import calendar
import xlsxwriter

from pyrogram import Client
from pyrogram.api import functions, types
from pyrogram.api.errors import FloodWait

from zombie_detector_functions import bool_converter, make_list

client = Client("example")
client.start()
target = "TestGrouppppp"  # Target channel/supergroup


def filtered_user_list(filter_string):
    user_list = []  # List that will contain all the users of the target chat
    limit = 200  # Amount of users to retrieve for each API call
    offset = 0  # Offset starts at 0

    while True:
        try:
            participants = client.send(
                functions.channels.GetParticipants(
                    channel=client.resolve_peer(target),
                    filter=types.ChannelParticipantsSearch(filter_string),
                    offset=offset,
                    limit=limit,
                    hash=0
                )
            )
        except FloodWait as e:
            # Very large channels will trigger FloodWait.
            # When happens, wait X seconds before continuing
            time.sleep(e.x)
            continue

        if not participants.participants:
            break  # No more participants left

        user_list.extend(participants.users)
        offset += limit
    return user_list


users = filtered_user_list("")

for item in users:
    print(item)
one_day = 0
three_days = 0
one_week = 0
one_month = 0
longer = 0
right_now = 0
timestamps = []
was_online_list = []
iternum = 0
while iternum < len(users):
    if isinstance(users[iternum].status, types.UserStatusOnline):
        timestamps.append(calendar.timegm(time.gmtime()))
        one_day += 1
        right_now += 1
    elif isinstance(users[iternum].status, types.UserStatusRecently):
        timestamps.append(calendar.timegm(time.gmtime()))
        one_day += 1
    elif isinstance(users[iternum].status, types.UserStatusLastWeek):
        timestamps.append(calendar.timegm(time.gmtime()) - 604800)
        one_week += 1
    elif isinstance(users[iternum].status, types.UserStatusLastMonth):
        timestamps.append(calendar.timegm(time.gmtime()) - 2592000)
        one_month += 1
    elif isinstance(users[iternum].status, types.UserStatusOffline):
        timestamps.append(users[iternum].status.was_online)
        was_online_list.append(users[iternum].status.was_online)
    iternum += 1


for item in was_online_list:
    if item > calendar.timegm(time.gmtime()) - 86400:
        one_day += 1
    elif item > calendar.timegm(time.gmtime()) - 259200:
        three_days += 1
    elif item > calendar.timegm(time.gmtime()) - 604800:
        one_week += 1
    elif item > calendar.timegm(time.gmtime()) - 2592000:
        one_month += 1
    else:
        longer += 1


print(one_day)
print(three_days)
print(one_week)
print(one_month)
print(longer)
print(right_now)


a_users = filtered_user_list("a")
b_users = filtered_user_list("b")
c_users = filtered_user_list("c")
d_users = filtered_user_list("d")
e_users = filtered_user_list("e")
f_users = filtered_user_list("f")
g_users = filtered_user_list("g")
h_users = filtered_user_list("h")
i_users = filtered_user_list("i")
j_users = filtered_user_list("j")
k_users = filtered_user_list("k")
l_users = filtered_user_list("l")
m_users = filtered_user_list("m")
n_users = filtered_user_list("n")
o_users = filtered_user_list("o")
p_users = filtered_user_list("p")
q_users = filtered_user_list("q")
r_users = filtered_user_list("r")
s_users = filtered_user_list("s")
t_users = filtered_user_list("t")
u_users = filtered_user_list("u")
v_users = filtered_user_list("v")
w_users = filtered_user_list("w")
x_users = filtered_user_list("x")
y_users = filtered_user_list("y")
z_users = filtered_user_list("z")


def list_extractor(input_list, field):
    output_list = []
    for items in input_list:
        output_list.append(getattr(items, field))
    return output_list


a_users_id = list_extractor(a_users, "id")
b_users_id = list_extractor(b_users, "id")
c_users_id = list_extractor(c_users, "id")
d_users_id = list_extractor(d_users, "id")
e_users_id = list_extractor(e_users, "id")
f_users_id = list_extractor(f_users, "id")
g_users_id = list_extractor(g_users, "id")
h_users_id = list_extractor(h_users, "id")
i_users_id = list_extractor(i_users, "id")
j_users_id = list_extractor(j_users, "id")
k_users_id = list_extractor(k_users, "id")
l_users_id = list_extractor(l_users, "id")
m_users_id = list_extractor(m_users, "id")
n_users_id = list_extractor(n_users, "id")
o_users_id = list_extractor(o_users, "id")
p_users_id = list_extractor(p_users, "id")
q_users_id = list_extractor(q_users, "id")
r_users_id = list_extractor(r_users, "id")
s_users_id = list_extractor(s_users, "id")
t_users_id = list_extractor(t_users, "id")
u_users_id = list_extractor(u_users, "id")
v_users_id = list_extractor(v_users, "id")
w_users_id = list_extractor(w_users, "id")
x_users_id = list_extractor(x_users, "id")
y_users_id = list_extractor(y_users, "id")
z_users_id = list_extractor(z_users, "id")

unique_user_ids = set(a_users_id + b_users_id + c_users_id + d_users_id + e_users_id + f_users_id + g_users_id +
                      h_users_id + i_users_id + j_users_id + k_users_id + l_users_id + m_users_id + n_users_id +
                      o_users_id + p_users_id + q_users_id + r_users_id + s_users_id + t_users_id + u_users_id +
                      v_users_id + w_users_id + x_users_id + y_users_id + z_users_id)

print(len(unique_user_ids))


id_list = []
mutual_contact_bool_list = []
deleted_bool_list = []
bot_bool_list = []
verified_bool_list = []
first_name_list = []
last_name_list = []
username_list = []
phone_list = []
photo_list = []
for item in users:
    id_list.append(item.id)
    mutual_contact_bool_list.append(item.mutual_contact)
    deleted_bool_list.append(item.deleted)
    bot_bool_list.append(item.bot)
    verified_bool_list.append(item.verified)
    first_name_list.append(item.first_name)
    last_name_list.append(item.last_name)
    username_list.append(item.username)
    phone_list.append(item.phone)
    photo_list.append(item.photo)

photo_bool_list = bool_converter(photo_list)
phone_bool_list = bool_converter(phone_list)

number = 0
real_or_fake_list = []
while number < len(users):
    if photo_bool_list[number] & ~bot_bool_list[number] & ~deleted_bool_list[number] & phone_bool_list[number]:
        real_or_fake_list.append(1)
    else:
        real_or_fake_list.append(0)
    number = number + 1

real_or_fake_list_photo = make_list(photo_bool_list)

workbook = xlsxwriter.Workbook('TelegramUserInfo.xlsx')
worksheet = workbook.add_worksheet()

# Iterate over the data and write it out row by row.
worksheet.write(0, 0, "ID")
worksheet.write(0, 1, "First Name")
worksheet.write(0, 2, "Last Name")
worksheet.write(0, 3, "Username")
worksheet.write(0, 4, "Photo")


def make_col(input_list, col_offset):
    col = 0
    row = 1
    for thing in input_list:
        worksheet.write(row, col + col_offset, thing)
        row += 1


make_col(id_list, 0)
make_col(first_name_list, 1)
make_col(last_name_list, 2)
make_col(username_list, 3)
make_col(photo_bool_list, 4)

workbook.close()
client.stop()

