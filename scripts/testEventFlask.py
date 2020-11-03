from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route('/eventRcv', methods=['POST'])
def eventRcv():
    data = request.data
    headers = request.headers
    f_data = open('flask.txt', 'w')
    f_data.close()
    print('>>>>>>>>>:', headers)
    print('>>>>>>>>>:', data)
    return jsonify({
        "code": 200,
        "message": "success",
        "desc": "",
        "data": {}
    })


if __name__ == '__main__':
    app.run(host='10.9.110.89', port=10086)
    # http://10.9.110.118:10086/eventRcv
