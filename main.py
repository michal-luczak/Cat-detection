from flask import Flask, request, jsonify, session

from cat_detection import is_cat

# Define flask app
app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/detect-cat', methods=['POST'])
def upload_file():
    # 'Key' in body should be named as 'image'. Type should be 'File' and in 'Value' we should upload image from disc.
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': "File name is empty. Please name a file."}), 400
    max_class, max_prob = is_cat(file)

    # Save result in session
    session['result'] = max_class, max_prob

    # Tworzenie komunikatu na podstawie wyniku analizy zdjęcia
    translator = {
        281: "tabby cat",
        282: "tiger cat",
        283: "persian cat",
        284: "siamese cat",
        285: "egyptian cat"
    }
    if max_prob is not None:
        result = f"The image is recognized as '{translator[max_class]}' with a probability of {round(max_prob * 100, 2)}%"
    else:
        result = f"The image is not recognized as a class within the range 281-285 ({max_class})"

    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run(debug=True)
