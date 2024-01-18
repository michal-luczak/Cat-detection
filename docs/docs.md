# Api

Port -> 5000

endpoint -> api/v1/detect-cat

Key -> 'Image'

Value -> {UPLOADED_FILE}

Flask Rest API application to cat recognition.
If request is valid then send response with results of recognition.
If key named 'Image' in body does not occur then returns 400 (BAD REQUEST).
Otherwise, returns 200 with results of recognition.
Format of response:
```json
{
    "lang": "{users_lang}",
    "results": {
        "{filename}": {
            "isCat": "{is_cat}",
            "results": {
                "1": "{result}",
                "2": "{result}",
                "3": "{result}",
                "4": "{result}",
                "5": "{result}",
                "6": "{result}",
                "7": "{result}",
                "8": "{result}",
                "9": "{result}",
                "10": "{result}"
            }
        }
    },
    "errors": [
        "{error_message}",
        "{error_message}"
    ]
}
```
Format of result:
```json
    {
        "label": "{label}",
        "score": "{score}"
    }
```

Example response:
```json

```