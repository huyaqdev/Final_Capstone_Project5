from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Welcome to Cloud Devops Capstone project page! My name is HuyAQ.</h1>"
    return html.format(format)

if __name__ == "__main__":
    # specify port = 80
    app.run(host='0.0.0.0', port=80, debug=True) 