import pytest
from django.urls import reverse
from rest_framework import status

from document_merge_service.api.data import django_file


@pytest.mark.parametrize(
    "target_format,response_content_type",
    [
        ("pdf", "application/pdf"),
    ],
)
def test_convert(db, client, target_format, response_content_type):
    url = reverse("convert")
    file_to_convert = django_file("docx-template.docx")

    data = {"file": file_to_convert.file, "target_format": target_format}
    response = client.post(url, data=data, format="multipart")

    assert response.status_code == status.HTTP_200_OK
    assert response.headers.get("Content-Type") == response_content_type


def test_incorrect_file_type(db, client):
    url = reverse("convert")
    file_to_convert = django_file("invalid-template.xlsx")

    data = {"file": file_to_convert.file, "target_format": "pdf"}
    response = client.post(url, data=data, format="multipart")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
