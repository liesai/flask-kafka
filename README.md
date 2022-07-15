# flask-kafka

Prerequisite : 
- Follow these steps : https://www.confluent.io/blog/set-up-and-run-kafka-on-windows-linux-wsl-2/ to have kafka env up and running
- Create these 3 topics : EMAIL, NOTIFICATION, INFERENCE
- Create an virtual env with flask, gunicorn and kafka-flask installed
- run gunicorn with app.py

Description
- Then start app.py with gunicorn - some help below
app.py contains the API backend to make requests to the producer
- Start the 3 python scripts left

inference file is the producer connected to kafka INFERENCE topic
notification file is the consumer of NOTIFICATION topic
email file is the consumer of kafka EMAIL topic


Reference to https://medium.com/geekculture/streaming-model-inference-using-flask-and-kafka-3476d9ff5ca5


