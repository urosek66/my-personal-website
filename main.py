from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("/fakebook/index.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("/boogle/index.html")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("/hair-salon/index.html")


if __name__ == '__main__':
    app.run(debug=True)
