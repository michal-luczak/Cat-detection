from flask import Flask, request, Response, json
from cat_detection import detect_cat
from language_label_mapper import translate
from validator import validate

""" 
    Flask Rest API application to cat recognition.
    If request is valid then send response with results of recognition.
    If key named 'Image' in body does not occurred then returns 400 (BAD REQUEST).
    Otherwise returns 200 with results of recognition.
    Format of response:
        {
            "lang": {users_lang},
            "results": {
                {filename}: {
                    "isCat": {is_cat},
                    "results": {
                        "1": {result}
                        "2": {result}
                        "3": {result}
                        ...
                        "10" {result}
                    }
                },
                ...
            },
            errors[
                {error_message},
                {error_message},
                ...
            ]
        }
    To see result format -> cat_detection.py
"""


# Define flask app
app = Flask(__name__)
app.secret_key = 'secret_key'

# Available cats
list_of_labels = [
    'lynx',
    'lion',
    'tiger',
    'cheetah',
    'leopard',
    'jaguar',
    'tabby',
    'Egyptian_cat',
    'cougar',
    'Persian_cat',
    'Siamese_cat',
    'snow_leopard',
    'tiger_cat'
]

# Available languages
languages = {'pl', 'en'}


@app.route('/api/v1/detect-cat', methods=['POST'])
def upload_file():
    # Validate request
    error_messages = validate(request)

    # If any errors occurred, return 400 (BAD REQUEST)
    if len(error_messages) > 0:
        errors = json.dumps(
            {
                'errors': error_messages
            }
        )
        return Response(errors, status=400, mimetype='application/json')

    # Get files from request
    files = request.files.getlist('image')

    # Get user's language (Value in header 'Accept-Language'). Default value is English
    lang = request.accept_languages.best_match(languages, default='en')

    # Define JSON structure for results
    results = {
        'lang': lang,
        'results': {},
        'errors': []
    }

    # Generate results
    for file in files:
        predictions = detect_cat(file, list_of_labels)
        if predictions is not None:
            predictions, error_messages = translate(predictions, lang)
        results['results'][file.filename] = {
            'isCat': False if not predictions else True,
            **({'predictions': predictions} if predictions is not None else {})
        }
        if len(error_messages) > 1:
            results['errors'].append(error_messages)

    # Send response with 200 (Success)
    return Response(json.dumps(results), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
