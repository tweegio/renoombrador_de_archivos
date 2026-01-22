from flask import Flask, render_template, request, send_file
import os
import zipfile
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("files")
        prefijo = request.form.get("prefijo", "img_")

        temp_dir = tempfile.mkdtemp()
        zip_path = os.path.join(temp_dir, "archivos_renombrados.zip")

        with zipfile.ZipFile(zip_path, "w") as zipf:
            for file in files:
                new_name = prefijo + file.filename
                file_path = os.path.join(temp_dir, new_name)
                file.save(file_path)
                zipf.write(file_path, new_name)

        return send_file(zip_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
