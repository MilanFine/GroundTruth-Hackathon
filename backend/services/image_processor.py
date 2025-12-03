from PIL import Image
import io
import zipfile
import requests

class ImageProcessor:
    def process_assets(self, logo_data: bytes, product_image_data: bytes) -> Image.Image:
        """
        Processes the uploaded logo and product image.
        For now, just returns the product image, but could composite logo.
        """
        product_img = Image.open(io.BytesIO(product_image_data))
        # logo_img = Image.open(io.BytesIO(logo_data))
        # Here we would resize and composite the logo if needed
        return product_img

    def create_zip_archive(self, images: list[str], captions: list[str]) -> io.BytesIO:
        """
        Creates a zip file containing the generated images and a text file with captions.
        Images are downloaded from the URLs.
        """
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            # Add captions
            captions_text = "\n\n".join(captions)
            zip_file.writestr("captions.txt", captions_text)
            
            # Add images
            for i, img_url in enumerate(images):
                try:
                    response = requests.get(img_url)
                    if response.status_code == 200:
                        zip_file.writestr(f"variation_{i+1}.png", response.content)
                except Exception as e:
                    print(f"Failed to download image {img_url}: {e}")
                    
        zip_buffer.seek(0)
        return zip_buffer

image_processor = ImageProcessor()
