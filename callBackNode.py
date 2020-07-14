from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/callBackNodeTester', methods=['POST'])
def callBackNodeTester():
    responseType = request.form.get("responseType")
    responseCode = request.form.get("responseCode")
    delay = request.form.get("delay")

    time.sleep(int(delay))
    return jsonify({"result": responseType, "Status Code": int(responseCode)}), int(responseCode)

if __name__ == '__main__':
    app.run(debug=True, port=5000)     
    