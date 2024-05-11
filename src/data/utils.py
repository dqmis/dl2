"""
A collection of helper functions to be used for the datasets. These are
adapted from the original repositories of these datasets. So they can be
used without adding unnecessary dependencies.
"""

from PIL import Image
from typing import Optional, List

# Adapted from LLM PuzzleTest repository, AlgoPuzzleVQA/modelling.py
MAX_IMAGE_SIZE = 1024


def resize_image(image: Image) -> Image:
    """
    Resizes the image if the image is too big to process.
    Adapted from LLM PuzzleTest repository, AlgoPuzzleVQA/modelling.py
    """
    h, w = image.size
    if h <= MAX_IMAGE_SIZE and w <= MAX_IMAGE_SIZE:
        return image

    factor = MAX_IMAGE_SIZE / max(h, w)
    h = round(h * factor)
    w = round(w * factor)
    print(dict(old=image.size, resized=(h, w)))
    if image.mode == "RGBA":
        image = image.convert("RGB")
    image = image.resize((h, w), Image.LANCZOS)
    return image
