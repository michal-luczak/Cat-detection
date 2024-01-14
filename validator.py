import imghdr

"""
    Validation method.
    If everything fine then returns empty list.
    Else returns list of error messages.
"""

# Allowed extensions
allowed_extensions = {'jpg', 'jpeg', 'png'}


def validate(request):
    errors = []
    try:
        images = request.files.getlist('image')

        # Case 1 - > request has no 'Image' Key in body
        if images is None:
            raise KeyError("'Image' key not found in request.")

        # Case 2 - > if some of the images has no filename
        if not images or all(img.filename == '' for img in images):
            raise ValueError("Value of 'Image' key is empty.")

        # Case 3 -> if some of the images has wrong extension
        for img in images:
            if imghdr.what(img) not in allowed_extensions:
                raise ValueError(f"Given file '{img.filename}' has no allowed extension. "
                                 f"Allowed extensions: {allowed_extensions}.")
    except Exception as e:
        errors.append(e.args[0])
    return errors
