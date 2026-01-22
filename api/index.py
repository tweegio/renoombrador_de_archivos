from flask import Flask, request, send_file
import os
import zipfile
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask OK en Vercel"

handler = app


