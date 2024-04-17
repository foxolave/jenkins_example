from flask import Flask, jsonify

app = Flask(__name__)
ololo=5


@app.route('/status', methods=['GET'])
def get_status():
    status = {'status': 'running_v2'}
    return jsonify(status)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
