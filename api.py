from flask import Flask, request
from main import main_process

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_bloks():
    data = request.json
    headers = request.headers

    main_process(headers['Origin'] + data['repository']['full_name'])

    return({ "status": 200 })

app.run(host='0.0.0.0', port=80, debug=True)
