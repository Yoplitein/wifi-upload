from datetime import datetime
from os import path
import os

from flask import Flask, request, render_template

os.makedirs("uploads", exist_ok = True)

app = Flask("wifi_upload")

@app.get("/")
def index():
    return render_template("index.html", success = None)

@app.post("/")
def upload():
    try:
        file = request.files["file"]
        assert file.filename != ""
        ext = path.splitext(file.filename)[1].strip(".")
        assert ext != ""
        name = get_filename(ext)
        file.save(path.join("uploads", name))
        return render_template("index.html", success = True)
    except:
        return render_template("index.html", success = False)

def get_filename(ext):
    return datetime.now().strftime(f"%Y-%m-%d_%H-%M-%S.{ext}")
