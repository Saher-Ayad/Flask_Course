from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    user = "Saher"
    return render_template("index.html", title="Home", main_title="Home Page", name=user)

if __name__ == "__main__":
    app.run(debug=True)
