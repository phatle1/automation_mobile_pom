import data_access_object_db.data_connect as data_connect
from data_access_object_db.load_db_config import load_db_config


class feeds_queries:
    @staticmethod
    def q_get_stores_by_internal_store_number(yum_id, content):
        return f"""select * from t_feeds f where f.created_by = '{yum_id}' 
                    and f."content" like '%{content}%';"""


class feeds_queries_execute:
    cursor = data_connect.connect(load_db_config(section='feeds_dev'))

    @staticmethod
    def get_feed_by_yum_id_and_content(yum_id, content):
        query = feeds_queries.q_get_stores_by_internal_store_number(yum_id.lower(), content.lower())
        feeds_queries_execute.cursor.execute(query)
        rows = feeds_queries_execute.cursor.fetchall()
        return rows


abc = feeds_queries_execute()
test = abc.get_feed_by_yum_id_and_content(yum_id='gcv2701', content='fgympm')
print(test)

# print(next(test))
# x = [tup[0] for tup in test]
# print(x)
# while True:
#     try:
#         print("Received on next(): ", next(test))
#     except StopIteration:
#         break
