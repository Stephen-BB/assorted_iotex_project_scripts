import psycopg2

conn = psycopg2.connect(host="ec2-54-197-250-121.compute-1.amazonaws.com", database="dfgsrc4s6pvsg1",
                        user="pwmseqpabtftve", password="29aafbd1f8fba41fefdd9415b38687294bad376c867161208537e8a8a64f2505")

print("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE TELEGRAM_MESSAGES
      (ID INT PRIMARY KEY     NOT NULL,
      DATE           TEXT    NOT NULL,
      MESSAGES            INT     NOT NULL);''')
print("Table created successfully")

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (1, '2/12', 1183)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (2, '2/13', 772)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (3, '2/14', 558)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (4, '2/15', 342)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (5, '2/16', 190)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (6, '2/17', 99)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (7, '2/18', 90)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (8, '2/19', 209)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (9, '2/20', 307)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (10, '2/21', 394)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (11, '2/22', 5436)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (12, '2/23', 45885)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (13, '2/24', 25532)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (14, '2/25', 3955)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (15, '2/26', 2137)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (16, '2/27', 2176)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (17, '2/28', 1906)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (18, '3/3', 1465)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (19, '3/2', 1222)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (20, '3/3', 982)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (21, '3/4', 862)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (22, '3/5', 875)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (23, '3/6', 956)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (24, '3/7', 814)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (25, '3/8', 694)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (26, '3/9', 2501)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (27, '3/10', 1675)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (28, '3/11', 808)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (29, '3/12', 800)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (30, '3/13', 3353)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (31, '3/14', 2092)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (32, '3/15', 472)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (33, '3/16', 408)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (34, '3/17', 336)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (35, '3/18', 268)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (36, '3/19', 532)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (37, '3/20', 586)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (38, '3/21', 1447)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (39, '3/22', 550)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (40, '3/23', 304)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (41, '3/24', 267)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (42, '3/25', 213)");

cur.execute("INSERT INTO TELEGRAM_MESSAGES (ID, DATE, MESSAGES) \
      VALUES (43, '3/26', 199)");

conn.commit()
print("Records created successfully")
conn.close()


