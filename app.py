from flask import Flask, jsonify, request
from nudenet import NudeClassifier
import requests
import psutil

pid = psutil.Process()
initial_cpu = pid.cpu_percent()
initial_ram = pid.memory_info().rss / 1024 / 1024

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
            'message': format(str(e))
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
        final_cpu = pid.cpu_percent()
        final_ram = pid.memory_info().rss / 1024 / 1024

        print(f"CPU usage: {initial_cpu - initial_cpu}%")
        print(f"RAM usage: {initial_ram - initial_ram} MB")

        print(f"CPU usage: {final_cpu - initial_cpu}%")
        print(f"RAM usage: {final_ram - initial_ram} MB")
        return jsonify(jsonResponse), 200
    except Exception as e:
        jsonResponse = {
            'success': False,
            'message': format(str(e))
        }
        return jsonify(jsonResponse), 200


@app.route("/tes")
def tes():
    return "tes"


if __name__ == "__main__":
    app.run()
