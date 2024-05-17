"""Utility functions for `documents`"""

import os
from idcu import settings

from documents.models import OrderFile


def get_full_url_for_media_files(media_file: OrderFile):
    """Get full url for media files."""
    base_url = settings.BASE_DIR
    file_url = media_file.file.url.lstrip('/')

    return os.path.join(base_url, file_url)
