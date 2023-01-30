from flask import Flask, jsonify, request
from nudenet import NudeClassifier
import requests
import json

classifier = NudeClassifier()
app = Flask(__name__)


@app.route("/check-image")
def check_image():
    try:
        url = request.args.get("url")
        response = requests.get(url)
        open("image.jpg", "wb").write(response.content)
        jsonResult = classifier.classify('image.jpg')
        unSafe = jsonResult['image.jpg']['unsafe']
        jsonResponse = {
            'success': bool(unSafe < 0.5),
            'unSafe': float(unSafe)
        }
        return jsonify(jsonResponse), 200
    except Exception as e:
        jsonResponse = {
            'success': False,
            'messages': format(str(e))
        }
        return jsonify(jsonResponse), 200


@app.route("/check-video")
def check_video():
    try:
        url = request.args.get("url")
        response = requests.get(url)
        open("video.mp4", "wb").write(response.content)
        jsonResult = classifier.classify_video('video.mp4')
        maxUnsafe = max(jsonResult["preds"][i]["unsafe"]
                        for i in jsonResult["preds"])
        jsonResponse = {
            'success': bool(maxUnsafe < 0.5),
            'maxUnsafe': float(maxUnsafe)
        }
        return jsonify(jsonResponse), 200
    except Exception as e:
        jsonResponse = {
            'success': False,
            'messages': format(str(e))
        }
        return jsonify(jsonResponse), 200


@app.route("/tes")
def tes():
    return "tes"


if __name__ == "__main__":
    app.run()
