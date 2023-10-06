from sqlalchemy import create_engine

db_connection_string="mysql+pymysql://umhcv3eetm3r68ur393v:pscale_pw_lf8zjVcqjfxNCXrRN0soSg0xGNC2Re7CmHU8Vc3DC6X@aws.connect.psdb.cloud/oasis?charset=utf8mb4"
engine = create_engine(db_connection_string,connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    })


