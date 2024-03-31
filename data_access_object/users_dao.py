import psycopg2
import data_connect
from load_db_config import load_config


class user_queries:
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


class queries_execute:
    def __init__(self):
        self.cursor = data_connect.connect(load_config)

    def get_user_by_yum_id(self, yum_id):
        query = user_queries.get_user_by_yum_id(yum_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        yield rows

    def get_hierarchy_user_by_yum_id(self, yum_id):
        query = user_queries.get_hierarchy_user_by_yum_id(yum_id.lower())
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        yield rows

    # queries_execute.get_user_by_yum_id('gcv2701')


abc = queries_execute()
test = abc.get_hierarchy_user_by_yum_id(yum_id='GCV2701')
# print(test[0]['user_type'])
x = [tup[0] for tup in test]
print(x)
# for x in test:
#     print(x[1]['brand'])
