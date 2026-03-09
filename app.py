from flask import Flask, request, jsonify
from PIL import Image
from PIL.ExifTags import TAGS

app = Flask(__name__)

@app.route("/extract_metadata", methods=["POST"])
def extract_metadata():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    image = Image.open(file)

    exif_data = image._getexif()

    metadata = {}
from flask import Flask, request, jsonify
from PIL import Image
from PIL.ExifTags import TAGS

app = Flask(__name__)

@app.route("/")
def home():
    return "Metadata API running"

@app.route("/extract_metadata", methods=["POST"])
def extract_metadata():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    image = Image.open(file)
    exif_data = image._getexif()

    metadata = {}

    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = str(value)

    gps_info = metadata.get("GPSInfo", None)

    return jsonify({
        "metadata": metadata,
        "gps_info": gps_info
    })
    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = str(value)

    gps_info = metadata.get("GPSInfo", None)

    response = {
        "metadata": metadata,
        "gps_info": gps_info
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
