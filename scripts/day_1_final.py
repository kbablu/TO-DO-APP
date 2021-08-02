from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name


name = "Rohit Sharma"
list = [1, 1, 2, 3, 5, 8, 11]

objects = []
objects.append(Item("First"))
objects.append(Item("Second"))
objects.append(Item("Third"))
objects.append(Item("Fourth"))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", name=name, list=list, objects=objects)

if __name__ == "__main__":
    app.run(debug=True)