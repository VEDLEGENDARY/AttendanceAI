import os
import base64
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Path to save images
SAVE_PATH = "student_list"

# Ensure the directory exists
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

@app.route('/save-snapshot', methods=['POST'])
def save_snapshot():
    data = request.json
    image_data = data.get('image')

    if not image_data:
        return jsonify({"message": "No image data received."}), 400

    try:
        # Decode the base64 image
        img_data = base64.b64decode(image_data.split(',')[1])  # Strip the data URL part

        # Create a filename with a timestamp
        filename = f"{SAVE_PATH}/snapshot_{len(os.listdir(SAVE_PATH)) + 1}.png"

        # Save the image
        with open(filename, 'wb') as f:
            f.write(img_data)

        return jsonify({"message": f"Image saved successfully as {filename}."}), 200
    except Exception as e:
        # Print the error to the console for debugging
        print(f"Error saving image: {e}")
        return jsonify({"message": f"Failed to save image: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
