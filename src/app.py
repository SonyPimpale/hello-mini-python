from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
IPaddr = socket.gethostbyname(hostname)

# code
@app.route("/")
def hello():
    return ("Hello MiniKube, I am returing from: " + hostname + IPaddr)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
