import psycopg2
import json

con = psycopg2.connect(
    database="pss",
    user="postgres",
    password="1234567",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")

cur = con.cursor()
# cur.execute('''CREATE TABLE STUDENT
#      (ADMISSION INT PRIMARY KEY NOT NULL,
#      NAME TEXT NOT NULL,
#      AGE INT NOT NULL,     апрапрапрапрапрар
#      COURSE CHAR(50),
#      DEPARTMENT CHAR(50));''')


cur.execute('''CREATE TABLE PushKar
      (session_event_id INT PRIMARY KEY NOT NULL,
      barcode int not null,
      payment_rrn text not null,
      visitor_full_name text not null,
      uuid text not null,
      visitor_last_name int not null,
      visitor_first_name int not null,
      update_date int not null,
      create_date int not null ,
      session_organization_id text not null,
      refund_date text null,
      comment text null,
      refund_reason text null,
      status TEXT not null,
      payment_date text not null,
      visit_date text null,
      payment_ticket_price text not null,
      bucket_id text not null,
      payment_amount text not null,
      payment_id text not null,
      session_params text not null,
      buyer_mobile_phone int not null,
      session_date text not null,
      visitor_middle_name text null,
      owner text not null);''')

print("Table created successfully")
con.commit()
con.close()






# # import psycopg2
# # connection = psycopg2.connect(con)
# cursor = con.cursor()
# cursor.execute("set search_path to public")
# #
# #
# with open('example.json') as file:
#     # change json.load(file) to file.read()
#     data = file.read()
#
# # Just put a placeholder %s instead of using {} and .format().
# query_sql = """
# insert into PushKar select * from
# (PushKar %s);
# """
#
# # change .execute(query_sql) to .execute(query_sql, (data,))
# cursor.execute(query_sql, (data,))
# # Add a commit on the connection.
# con.commit()



#
# data = []
# with open('example.json') as f:
#     for line in f:
#         data.append(json.loads(line))
#
# fields = [
#       'session_event_id' ,
#       'barcode',
#       'payment_rrn' ,
#       'visitor_full_name' ,
#       'uuid' ,
#       'visitor_last_name' ,
#       'visitor_first_name',
#       'update_date' ,
#       'create_date' ,
#       'session_organization_id',
#       'refund_date',
#       'comment',
#       'refund_reason',''
#       'status' ,
#       'payment_date' ,
#       'visit_date',
#       'payment_ticket_price',
#       'bucket_id',
#       'payment_amount',
#       'payment_id',
#       'session_params',
#       'buyer_mobile_phone',
#       'session_date',
#       'visitor_middle_name'
#       'owner'
# ]
#
# for item in data:
#     my_data = [item[field] for field in fields]
#     insert_query = "INSERT INTO PushKar VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
#     cursor.execute(insert_query, tuple(my_data))