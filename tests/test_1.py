import os

from werkzeug.datastructures import FileStorage

from main import app


def test_upload_file():
    with app.test_client() as test_client:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, "./img/tiger_cat/cat1.jpg")
        image = FileStorage(
            stream=open(image_path, "rb"),
            filename="cat1.jpg",
            content_type="image/jpeg",
        )

        response = test_client.post('/api/v1/detect-cat', data={'image': image}, content_type='multipart/form-data')
        assert response.status_code == 200
