import psycopg2
import data_connect
from load_db_config import load_db_config


class stores_queries:
    @staticmethod
    def q_stores_by_internal_store_number(internal_store_number):
        query = f"""select * from t_store where internal_store_number in ('{internal_store_number}');"""
        return query

    @staticmethod
    def q_stores_by_store_id(store_id):
        query = f"""select * from t_store where id = '{store_id}';"""
        return query


class stores_queries_execute:
    def __init__(self):
        self.cursor = data_connect.connect(load_db_config(section='stores_dev'))

    def get_stores_by_internal_store_number(self, internal_id):
        query = stores_queries.q_stores_by_internal_store_number(internal_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_stores_by_store_id(self, store_id):
        query = stores_queries.q_stores_by_store_id(store_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    # queries_execute.get_user_by_yum_id('gcv2701')


abc = stores_queries_execute()
test = abc.get_stores_by_store_id(store_id='19016')
print(test)

# print(next(test))
# x = [tup[0] for tup in test]
# print(x)
# while True:
#     try:
#         print("Received on next(): ", next(test))
#     except StopIteration:
#         break
