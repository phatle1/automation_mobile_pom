import psycopg2

host_name = 'hutbot-cluster-dev.cluster-caweiwcdspvo.eu-west-1.rds.amazonaws.com'
database = 'users_dev'
user_name = 'users_writer_dev'
pwd = 'yohp4uu7Rieg'
port_id = '5432'
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=host_name,
        dbname=database,
        user=user_name,
        password=pwd,
        port=port_id)
    cur = conn.cursor()

    script = '''select *  from t_user tu where yum_id in ('gcv2701')'''

    cur.execute(script)
    print(cur.fetchall())

    conn.commit()
except Exception as error:
    raise error
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
