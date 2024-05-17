"""Base views for `company` view."""

from rest_framework.views import APIView
from documents.services import DocumentsService


class BaseDocumentView(APIView):
    """Base document view."""

    service_class = DocumentsService()
