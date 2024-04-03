import json
import psycopg2
import psycopg2.extras

host_name = 'hutbot-cluster-dev.cluster-caweiwcdspvo.eu-west-1.rds.amazonaws.com'
database = 'users_dev'
user_name = 'users_writer_dev'
pwd = 'yohp4uu7Rieg'
port_id = '5432'
connection = None
cursor = None


try:
    connection = psycopg2.connect(
        host=host_name,
        dbname=database,
        user=user_name,
        password=pwd,
        port=port_id)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    script = '''select u.user_type , u.yum_id ,u.operational_role, u.user_primary_brand ,hd.* from t_hierarchy_detail hd left join t_user u on hd.user_id = u.id  where u.yum_id in  ('gcv2701')'''
    cursor.execute(script)
    print([desc[0] for desc in cursor.description])
    rows = cursor.fetchall()
    print(rows)
    connection.commit()
except Exception as error:
    raise error
finally:
    if connection:
        cursor.close()
        connection.close()
