"""
For a hero image (1200x630):

    $ python transform_cloudinary_url.py https://res.cloudinary.com/your_cloud_name/image/upload/v1234567890/sample.jpg --size hero

For an inline image (700x400):

    $ python transform_cloudinary_url.py https://res.cloudinary.com/your_cloud_name/image/upload/v1234567890/sample.jpg --size inline
"""


import argparse
from urllib.parse import urlparse

def transform_cloudinary_url(original_url, width, height):
    """
    Transforms a Cloudinary image URL by inserting transformation parameters.

    Parameters:
    original_url (str): The original Cloudinary image URL.
    width (int): Desired width of the transformed image.
    height (int): Desired height of the transformed image.

    Returns:
    str: The transformed Cloudinary image URL with optimization parameters.
    """
    parsed_url = urlparse(original_url)
    path_parts = parsed_url.path.split('/')

    try:
        # Find the index of 'upload' to insert transformation parameters after it
        upload_index = path_parts.index('upload')
    except ValueError:
        raise ValueError("The provided URL does not contain 'upload' segment.")

    # Define transformation parameters
    transformation = f'w_{width},h_{height},c_fill,q_auto,f_auto'

    # Insert transformation parameters into the path
    path_parts.insert(upload_index + 1, transformation)

    # Reconstruct the transformed path
    transformed_path = '/'.join(path_parts)

    # Build the transformed URL
    transformed_url = f"{parsed_url.scheme}://{parsed_url.netloc}{transformed_path}"

    return transformed_url

def main():
    parser = argparse.ArgumentParser(description="Transform a Cloudinary image URL with optimization parameters.")
    parser.add_argument('original_url', help='The original Cloudinary image URL to be transformed.')
    parser.add_argument('--size', required=True, choices=['hero', 'inline'],
                        help='Preset size for the image transformation: "hero" (1200x630) or "inline" (700x400).')
    args = parser.parse_args()

    # Define size presets
    size_presets = {
        'hero': (1200, 630),
        'inline': (700, 400)
    }

    width, height = size_presets[args.size]

    try:
        transformed_url = transform_cloudinary_url(args.original_url, width, height)
        print("Transformed and Optimized Image URL:")
        print(transformed_url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
