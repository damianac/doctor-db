from flask import Flask, Response, jsonify

app = Flask(__name__)

data = {'name' : 'doctor-B', 'contact' : +3354234555775}

@app.route('/api/data', methods = ['GET'])
def api_hello():
    resp = jsonify(data)
    resp.status_code = 200

    return resp

if __name__ == '__main__':
    app.run(debug=True)