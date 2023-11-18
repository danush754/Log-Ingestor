from flask import Flask, request

app  = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest():
    log_data = request.data.decode('utf-8')
    print(f"Recieved the log data: {log_data}")
    return "Log ingestion successful :)"

if(__name__ == '__main__'):
    app.run(port=3000)
