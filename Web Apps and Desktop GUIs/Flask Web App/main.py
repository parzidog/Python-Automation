from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def Home():
    print("Get Request")
    return render_template("index.html")


@app.route("/", methods=["POST"])
def Post():
    dim1 = request.form["first"]
    dim2 = request.form["second"]
    dim3 = request.form["third"]

    volume = int(dim1) * int(dim2) * int(dim3)
    print("Post request")
    return render_template("index.html", output=volume, dim1=dim1, dim2=dim2, dim3=dim3)


app.run()
