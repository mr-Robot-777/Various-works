import json
import pandas as pd
import psycopg2


con = psycopg2.connect(
    database="pss",
    user="postgres",
    password="1234567",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")





with open('rec_imp_test.json', 'r') as j:
    json_data1 = json.load(j)
    # print(json_data)
#
# data = pd.read_json("rec_imp_test.json")
# df = pd.DataFrame(data)
#
#
# print(df)

#
# Frozenset=frozenset(json_data1)
# print(Frozenset)
print(json_data1['0001ad0041738ac671fe52a5f887742e'])



# json_data = dict({ggg})
# sorted_values = sorted(json_data.values()) # Sort the values
# sorted_dict = {}
#
# for i in sorted_values:
#     for k in json_data.keys():
#         if json_data[k] == i:
#             sorted_dict[k] = json_data[k]
#             break
#
# print(sorted_dict)