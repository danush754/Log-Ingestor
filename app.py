from flask import Flask, request, jsonify

app  = Flask(__name__)

logs = []

@app.route('/ingest', methods=['POST'])
def ingest():
    try:

        log_data = request.json 
        if not isinstance(log_data,dict):
            return jsonify({'error' : 'Invalid Json format'}),400
        
        logs.append(log_data)

        return jsonify({'message' : 'Log ingestion successfull !'})
    except Exception as e:
        return jsonify({'error':str(e)}),500

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify({'logs' : logs})
        
        
    

if(__name__ == '__main__'):
    app.run(port=3000)
