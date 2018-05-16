import psycopg2

conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE TWITTER_FOLLOWERS
      (ID INT PRIMARY KEY     NOT NULL,
      DATE           TEXT    NOT NULL,
      FOLLOWERS            INT     NOT NULL);''')
print("Table created successfully")


cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (2, '1/22', 58)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (3, '1/23', 72)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (4, '1/24', 91)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (5, '1/25', 100)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (6, '1/26', 138)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (7, '1/27', 177)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (8, '1/28', 220)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (9, '1/29', 242)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (10, '1/30', 282)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (11, '1/31', 296)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (12, '2/1', 322)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (13, '2/2', 379)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (14, '2/3', 420)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (15, '2/4', 443)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (16, '2/5', 449)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (17, '2/6', 452)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (18, '2/7', 458)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (19, '2/8', 473)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (20, '2/9', 489)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (21, '2/10', 511)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (22, '2/11', 525)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (23, '2/12', 543)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (24, '2/13', 556)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (25, '2/14', 596)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (26, '2/15', 615)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (27, '2/16', 643)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (28, '2/17', 653)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (29, '2/18', 672)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (30, '2/19', 702)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (31, '2/20', 731)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (32, '2/21', 1590)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (33, '2/22', 1660)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (34, '2/23', 1800)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (35, '2/24', 1920)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (36, '2/25', 2000)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (37, '2/26', 2030)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (38, '2/27', 2050)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (39, '2/28', 2110)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (40, '3/1', 2200)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (41, '3/2', 2250)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (42, '3/3', 2280)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (43, '3/4', 2290)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (44, '3/5', 2330)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (45, '3/6', 2350)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (46, '3/7', 2380)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (47, '3/8', 2390)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (48, '3/9', 2370)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (49, '3/10', 2440)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (50, '3/11', 2460)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (51, '3/12', 2490)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (52, '3/13', 2520)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (53, '3/14', 2540)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (54, '3/15', 2550)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (55, '3/16', 2570)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (56, '3/17', 2570)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (57, '3/18', 2580)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (58, '3/19', 2590)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (59, '3/20', 2580)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (60, '3/21', 2600)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (61, '3/22', 2600)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (62, '3/23', 2600)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (63, '3/24', 2620)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (64, '3/25', 2620)");

cur.execute("INSERT INTO Twitter_Followers (ID, DATE, FOLLOWERS) \
      VALUES (65, '3/26', 2620)");




conn.commit()
print("Records created successfully")
conn.close()


