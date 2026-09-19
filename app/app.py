import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "unknown")
    message = os.getenv("APP_MESSAGE", "Hello from Kubernetes")

    return f"""
	<h1>DevOps Final Project</h1>
	<p>Environment: {environment}</p>
	<p>{message}</p>
	<p>Running on Amazon EKS</p>
	"""


@app.route("/health")
def health():
    return "healthy", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
