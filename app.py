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
        files = request.files.getlist("file")
        files = [f for f in files if f.filename != ""]
        assert len(files) > 0
        for i, file in enumerate(files):
            ext = path.splitext(file.filename)[1].strip(".")
            assert ext != ""
            name = get_filename(ext, (i + 1) if len(files) > 1 else None)
            file.save(path.join("uploads", name))
        return render_template("index.html", success = True)
    except:
        return render_template("index.html", success = False)

def get_filename(ext, seq):
    if seq != None:
        seq = f"_{seq}"
    else:
        seq = ""
    return datetime.now().strftime(f"%Y-%m-%d_%H-%M-%S{seq}.{ext}")
