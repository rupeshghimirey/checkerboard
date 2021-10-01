from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<int:num>')
def checkerFourBoard(num):
    return render_template("eight_by_4.html", xValue = num)


@app.route('/<int:xNum>/<int:yNum>')
def checkerBoard(xNum, yNum ):
    return render_template("random.html", xValue = xNum, yValue = yNum)

@app.route('/<int:xNum>/<int:yNum>/<string:color1>/<string:color2>')
def checkerBoard1(xNum, yNum,color1, color2 ):
    return render_template("color.html", xValue = xNum, yValue = yNum, colorOne = color1, colorTwo=color2)

if __name__=="__main__":
    app.run(debug=True) 