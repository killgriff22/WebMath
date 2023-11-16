import flask
from flask import Flask, redirect, url_for, render_template, request, make_response, jsonify
import json
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


@app.route('/')
def hello():
    return render_template('base.html', content="""<h1>Welcome to WebMath!</h1>
<h2>This is a project I created for my senior project.</h2>
It is a web app that can solve basic math problems.<br>
Feel free to take a look around!<br>""")


@app.route('/point', methods=['GET', 'POST'])
def pointsolver():
    content = """<form action="/point" method="POST">
    <input = "text" name="equation" id="equation" placeholder="Enter your equation">
    <input type="submit" value="Submit">
    </form>"""
    if request.method == 'POST':
        equation = request.form['equation']
        content = f"""<form action="/point" method="POST">
        <input = "text" name="equation" id="equation" placeholder="{equation}">
        <input type="submit" value="Submit">
        </form>"""
        try:
            i = 0
            while i:
                char = equation[i]
                if char == "(":
                    return_to = i
                    mini = ""
                    i += 1
                    while equation[i] != ")":
                        mini += equation[i]
                        i += 1
                    mini = eval(mini)
                    equation = equation[:return_to] + \
                        str(mini) + equation[i+1:]
                    print(equation)
                    i = None
            x = eval(equation)
            content += f"\n{str(x)}"
        except:
            content = "Invalid Equation"
    return render_template('base.html', content=content)


@app.route('/quad', methods=['GET', 'POST'])
def quadratic():
    content = """<form action="/quad" method="POST">
    <input = "text" name="equation" id="equation" placeholder="Enter your equation">
    <input type="submit" value="Submit">
    </form>"""
    if request.method == 'POST':
        equation = request.form['equation']
        content = f"""<form action="/quad" method="POST">
        <input = "text" name="equation" id="equation" placeholder="{equation}">
        <input type="submit" value="Submit">
        </form>"""
        try:
            equation = equation.split(" ")
            a = int(equation[0])
            b = int(equation[1])
            c = int(equation[2])
            x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
            x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
            content += f"\n{x1} and {x2}"
        except:
            content = "Invalid Equation"

    return render_template('base.html', content=content)


app.run("0.0.0.0", debug=True)
