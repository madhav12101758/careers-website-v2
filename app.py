from flask import Flask,render_template,jsonify
from database import engine
from sqlalchemy import text

app=Flask(__name__)

def get_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    result_all=result.all()
    jobs=[]
    for row in result_all:
      jobs.append(row._mapping)
    return jobs

@app.route('/')
def hello_world():
  jobs=get_jobs_from_db()
  return render_template('home.html',jobs=jobs,company_name=' THE OASIS')

@app.route('/api/jobs')
def list_jobs():
  JOBS=get_jobs_from_db()
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  
  