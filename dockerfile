FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

RUN pip install flask requests nudenet

WORKDIR /app

COPY . /app

COPY classifier_model.onnx /root/.NudeNet/classifier_model.onnx

EXPOSE 5000

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]

# ENTRYPOINT [ "python3" ]

# CMD [ "app.py" ]
