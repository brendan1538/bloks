from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.json
    headers = request.headers
    print(f"repo url: {headers['Host']}/{data['repository']['full_name']}")

    return(f"repo url: {headers['Origin']}{data['repository']['full_name']}")

app.run(host='0.0.0.0', port=80, debug=True)
