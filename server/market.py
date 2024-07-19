from flask import Flask

app = Flask(__name__)
#route or endpoints
@app.route("/")
def hello_world():
    return "Hello, World!"
@app.route('/cool_app')
def cool_app():
    return "cool world app"

if __name__=="__main__":
    app.run(debug=True)