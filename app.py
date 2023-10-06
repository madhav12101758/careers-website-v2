from flask import Flask,render_template,jsonify
from database import get_jobs_from_db


app=Flask(__name__)



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
  
  