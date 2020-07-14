from flask import Flask, jsonify
import random
import time


app = Flask(__name__)


def delayGenerator(lowerLimit=0, upperLimit=0):
    time.sleep(random.randrange(lowerLimit, upperLimit, 1))


"""2xx Errors"""


@app.route('/200_okay', methods=['POST'])
def _200_okay():
    time.sleep(3)
    return jsonify({"result": "success"}), 200


@app.route('/201_created', methods=['POST'])
def _201_created():
    time.sleep(3)
    return jsonify({"result": "success"}), 201


"""4xx Errors"""


@app.route('/400_badRequest', methods=['POST'])
def _400_badRequest():
    time.sleep(3)
    return jsonify({"result": "failed"}), 400


@app.route('/401_unauthorized', methods=['POST'])
def _401_unauthorized():
    time.sleep(3)
    return jsonify({"result": "failed"}), 401


@app.route('/403_forbidden', methods=['POST'])
def _403_forbidden():
    time.sleep(3)
    return jsonify({"result": "failed"}), 403


@app.route('/404_notFound', methods=['POST'])
def _404_notFound():
    time.sleep(3)
    return jsonify({"result": "failed"}), 404


@app.route('/405_notAllowed', methods=['POST'])
def _405_notAllowed():
    time.sleep(3)
    return jsonify({"result": "failed"}), 405


@app.route('/418_IamAteapot', methods=['POST'])
def _418_IamAteapot():
    time.sleep(3)
    return jsonify({"result": "failed"}), 418


"""5xx Errors"""


@app.route('/500_internalServerError', methods=['POST'])
def _500_notFound():
    time.sleep(3)
    return jsonify({"result": "failed"}), 500


@app.route('/501_notImplemented', methods=['POST'])
def _501_notImplemented():
    time.sleep(3)
    return jsonify({"result": "failed"}), 501


@app.route('/502_badGateway', methods=['POST'])
def _502_badGateway():
    time.sleep(3)
    return jsonify({"result": "failed"}), 502


@app.route('/503_serviceUnavailable', methods=['POST'])
def _503_serviceUnavailable():
    time.sleep(3)
    return jsonify({"result": "failed"}), 503


@app.route('/504_gatewayTimeOut', methods=['POST'])
def _504_gatewayTimeOut():
    time.sleep(3)
    return jsonify({"result": "failed"}), 504


if __name__ == '__main__':
    app.run(debug=True)
