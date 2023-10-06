from sqlalchemy import create_engine,text

db_connection_string="mysql+pymysql://umhcv3eetm3r68ur393v:pscale_pw_lf8zjVcqjfxNCXrRN0soSg0xGNC2Re7CmHU8Vc3DC6X@aws.connect.psdb.cloud/oasis?charset=utf8mb4"
engine = create_engine(db_connection_string,connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    })

def get_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    result_all=result.all()
    jobs=[]
    for row in result_all:
      jobs.append(row._mapping)
    return jobs


