from io import BytesIO

import numpy as np
from PIL import Image
from keras.src.applications.resnet import preprocess_input, decode_predictions
from keras.applications.resnet import ResNet50


"""
    Recognition file.
    Model is ResNet50. Pretrained model to image recognition.
    If model recognize cat then returns response with first ten CAT predictions.
    If first prediction is not a cat then returns False.
    If prediction is not a cat (is not within list_of_labels) then skips this prediction.
    Format of response:
    {
        'label': {label}
        'score': {score}
    }
"""


model = ResNet50(weights='imagenet')


# PRIVATE Preprocess image method
def _preprocess_image(image):
    try:
        img = Image.open(BytesIO(image.read()))
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None


# Generate response
def _generate_response(decoded_predictions, list_of_labels):
    results = {}
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        if i == 0 and label not in list_of_labels:
            return None
        if score < 0.01:
            break
        if label in list_of_labels:
            results[len(results) + 1] = {"label": label, "score": round(float(score), 2)}
    return results


# Cat detection
def detect_cat(image_file, list_of_labels):
    img_array = _preprocess_image(image_file)
    prediction = model.predict(img_array)
    decoded_predictions = decode_predictions(prediction, top=10)[0]
    return _generate_response(decoded_predictions, list_of_labels)
