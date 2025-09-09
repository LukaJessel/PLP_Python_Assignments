import os
import requests
from urllib.parse import urlparse
import uuid
from typing import Optional

def get_image_filename(url: str, default_ext: str = ".jpg") -> str:
    """
    Extract filename from URL or generate a UUID-based one.
    Args:
        url (str): The image URL.
        default_ext (str): Default extension if none found.
    Returns:
        str: Filename for saving the image.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = f"image_{uuid.uuid4().hex}{default_ext}"
    return filename

def fetch_image(
    url: str,
    save_dir: str = "Fetched_Images",
    filename: Optional[str] = None,
    show_progress: bool = True
) -> Optional[str]:
    """
    Download and save image from URL.
    Args:
        url (str): Image URL.
        save_dir (str): Directory to save image.
        filename (Optional[str]): Custom filename. If None, auto-generated.
        show_progress (bool): Show download progress if possible.
    Returns:
        Optional[str]: Path to saved image, or None if failed.
    """
    os.makedirs(save_dir, exist_ok=True)
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        if filename is None:
            filename = get_image_filename(url)
        filepath = os.path.join(save_dir, filename)

        # Handle file overwrite
        base, ext = os.path.splitext(filepath)
        counter = 1
        while os.path.exists(filepath):
            filepath = f"{base}_{counter}{ext}"
            counter += 1

        total = int(response.headers.get('content-length', 0))
        downloaded = 0
        chunk_size = 8192

        with open(filepath, 'wb') as file:
            if show_progress and total > 0:
                print(f"⬇️  Downloading to {filepath} ({total // 1024} KB)...")
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    if show_progress and total > 0:
                        downloaded += len(chunk)
                        percent = int(downloaded * 100 / total)
                        print(f"\rProgress: {percent}%", end="")
            if show_progress and total > 0:
                print("\n✅ Download complete.")

        print(f"✅ Image successfully saved as: {filepath}")
        return filepath

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include 'http://' or 'https://'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"❌ A network error occurred: {err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None

def main():
    """
    Command-line interface for fetching images.
    """
    print("🌍 Ubuntu Image Fetcher")
    image_url = input("🔗 Enter the image URL: ").strip()
    if not image_url:
        print("❌ No URL provided. Exiting.")
        return
    fetch_image(image_url)

if __name__ == "__main__":
    main()
