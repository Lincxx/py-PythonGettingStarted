from flask import Flask, render_template, redirect, url_for, request

from student import  Student

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student_page():
    return "Hello World!"

if __name__ == "__main__":
    app.run()