from flask import Flask, send_file
import qrcode
import os

app = Flask(_name_)

BASE_DIR = os.path.dirname(os.path.abspath(_file_))

@app.route("/generate")
def generate_qr():
    url = "https://taste-maker-sooty.vercel.app/"
    file_path = os.path.join(BASE_DIR, "qr.png")

    img = qrcode.make(url)
    img.save(file_path)

    return send_file(file_path, mimetype="image/png")

if _name_ == "_main_":
    app.run(debug=True)