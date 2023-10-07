import os

from sqlalchemy import create_engine, text

db_connection_string=os.environ['DB_CONNECTION_STRING']
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
def load_job_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(
      text("SELECT*FROM jobs WHERE  id = :val"),
      {"val": id}
    )
    rows = result.fetchone()
    if rows is None:
      return None
    else:
      job_dict = dict(zip(result.keys(), rows))
      return job_dict

def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query,
                 {"job_id":job_id,
                 "full_name":application['full_name'],
                 "email":application['email_id'],
                 "linkedin_url":application['linkidin_url'],
                 "education":application['education'],
                 "work_experience":application['work_experience'],
                 "resume_url":application['resume_url']}
                )


