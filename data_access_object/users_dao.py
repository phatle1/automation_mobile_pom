import psycopg2
import data_connect
from load_db_config import load_db_config


class users_queries:
    @staticmethod
    def get_user_by_yum_id(yum_id):
        query = f"select * from t_user where yum_id = '{yum_id}';"
        return query

    @staticmethod
    def get_hierarchy_user_by_yum_id(yum_id):
        query = f"""select u.vendor_tool , u.user_type , u.yum_id ,u.operational_role, u.user_primary_brand ,hd.* 
                    from t_hierarchy_detail hd
                    left join t_user u
                    on hd.user_id = u.id
                    where u.yum_id in ('{yum_id}')"""
        return query


class users_queries_execute:
    def __init__(self):
        self.cursor = data_connect.connect(load_db_config(section='users_dev'))

    def get_user_by_yum_id(self, yum_id):
        query = user_queries.get_user_by_yum_id(yum_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_hierarchy_user_by_yum_id(self, yum_id):
        query = user_queries.get_hierarchy_user_by_yum_id(yum_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    # queries_execute.get_user_by_yum_id('gcv2701')


abc = users_queries_execute()
test = abc.get_hierarchy_user_by_yum_id(yum_id='GCV2701')
print(test)

# print(next(test))
# x = [tup[0] for tup in test]
# print(x)
# while True:
#     try:
#         print("Received on next(): ", next(test))
#     except StopIteration:
#         break
