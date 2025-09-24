import os
import django
from django.conf import settings
from django.core.files import File
from bs4 import BeautifulSoup

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acknowledgementhub_django.settings')
django.setup()

from backend.models import Products_data

def import_single_product(image_src, title, description, social_media):
    # The image_src already contains the full static path, so no need to modify it.
    # if image_src.startswith('/static/'):
    #     image_src = image_src[len('/static/'):]

    if not Products_data.objects.filter(Product_title=product_title).exists():
        Products_data.objects.create(
            image=image_src,
            Product_title=product_title,
            Product_description=product_description,
            social_media=social_media_link
        )
        print(f"Added product: {product_title}")
    else:
        print(f"Product already exists: {product_title}")

def import_products_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    product_cards = soup.find_all('div', class_='flip-card')

    for card in product_cards:
        image_tag = card.find('img', class_='flip-card-img')
        image_src = image_tag['src'] if image_tag else ''

        title_tag = card.find('div', class_='flip-card-title')
        product_title = title_tag.text.strip() if title_tag else 'No Title'

        description_tag = card.find('div', class_='flip-card-desc')
        product_description = description_tag.text.strip() if description_tag else 'No Description'

        social_media_tag = card.find('a', class_='flip-card-btn')
        social_media_link = social_media_tag['href'] if social_media_tag else ''

        # Check if the product already exists
        try:
            product = Products_data.objects.get(product_title=title)
            # Update existing product
            product.product_description = description
            product.social_media = social_media
            product.save()
            print(f"Updated existing product: {title}")
        except Products_data.DoesNotExist:
            # Create new product
            product = Products_data(
                product_title=title,
                product_description=description,
                social_media=social_media
            )
            product.save()
            print(f"Added new product: {title}")


def import_products_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    product_elements = soup.select('.product-item')

    for product_element in product_elements:
        image_src = product_element.select_one('.product-thumb img')['src']
        product_title = product_element.select_one('.product-title').get_text(strip=True)
        product_description = product_element.select_one('.product-description').get_text(strip=True)
        social_media_tag = product_element.select_one('.social-media a')
        social_media_link = social_media_tag['href'] if social_media_tag else ''

        import_single_product(image_src, product_title, product_description, social_media_link)

if __name__ == '__main__':
    # Path to your products.html file
    html_file_path = os.path.join(settings.BASE_DIR, 'products.html')
    import_products_from_html(html_file_path)