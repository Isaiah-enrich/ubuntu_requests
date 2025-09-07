import os
import requests
from urllib.parse import urlparse

def ubuntu_image_fetcher():
    print("🌍 Ubuntu Image Fetcher: 'I am because we are'")

    # Prompt user for an image URL
    url = input("Enter the image URL: ").strip()

    # Directory where images will be saved
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        save_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image saved successfully at: {save_path}")

    except requests.exceptions.MissingSchema:
        print("⚠️ Invalid URL. Please include 'http://' or 'https://'.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    ubuntu_image_fetcher()
