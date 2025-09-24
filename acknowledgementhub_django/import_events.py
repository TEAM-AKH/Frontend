import os
import django
from bs4 import BeautifulSoup
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acknowledgementhub_django.settings')
django.setup()

from backend.models import Events_data

def import_events_from_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    event_cards = soup.find_all('div', class_='card')

    for card in event_cards:
        image_tag = card.find('img', class_='card-img-top')
        event_image = image_tag['src'] if image_tag else ''

        title_tag = card.find('h5', class_='card-title')
        event_title = title_tag.text.strip() if title_tag else 'No Title'

        date_tag = card.find('h6', class_='card-subtitle')
        event_date_str = date_tag.text.strip() if date_tag else ''

        # Parse and format the date
        try:
            # Example: "Dec. 20, 2025" -> "2025-12-20"
            event_date = datetime.datetime.strptime(event_date_str, '%b. %d, %Y').strftime('%Y-%m-%d')
        except ValueError:
            event_date = None # Or handle as appropriate, e.g., set a default date

        description_tag = card.find('p', class_='card-text')
        event_description = description_tag.text.strip() if description_tag else 'No Description'

        social_media_tag = card.find('a', class_='btn')
        social_media_link = social_media_tag['href'] if social_media_tag else ''

        # Remove '/static/' prefix from event_image if it exists
        if event_image.startswith('/static/'):
            event_image = event_image[len('/static/'):]

        # Check if an event with the same title already exists to avoid duplicates
        if not Events_data.objects.filter(event_title=event_title).exists():
            Events_data.objects.create(
                event_image=event_image,
                event_title=event_title,
                event_date=event_date,
                event_description=event_description,
                social_media=social_media_link
            )
            print(f"Added event: {event_title}")
        else:
            print(f"Event already exists: {event_title}")

if __name__ == '__main__':
    html_file = 'e:\\Acknolwedment\\event.html'
    import_events_from_html(html_file)