from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app  = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///logs.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.String(50))
    message = db.Column(db.Text)
    resoureID = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    traceID = db.Column(db.String(50))
    spanID = db.Column(db.String(50))
    commit = db.Column(db.String(50))
    parentResourceId = db.Column(db.String(50))

    def __repr__(self):
        return f"Log {self.id} : {self.message}"
        

logs = []

@app.route('/ingest', methods=['POST'])
def ingest():
    try:

        log_data = request.json 
        if not isinstance(log_data,dict):
            return jsonify({'error' : 'Invalid Json format'}),400
        
        

        return jsonify({'message' : 'Log ingestion successfull !'}),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify({'logs' : logs})



        
    

if(__name__ == '__main__'):
    app.run(port=3000)
