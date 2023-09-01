import argparse
import os

from dotenv import load_dotenv
import requests

from save_tools import save_picture


def main():
    load_dotenv()
    nasa_token = os.environ.get('NASA_API_TOKEN')

    parser = argparse.ArgumentParser(description='Данный файл скачивает фотографии с сервиса NASA Astronomy Picture of the Day (APOD)')
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Укажите название папки, в которую будут сохранены скачанные фотографии.')

    args = parser.parse_args()
    folder = args.folder

    payload = {'api_key': nasa_token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_epic_answers = response.json()

    for answer_number, answer in enumerate(nasa_epic_answers):
        file_name = f'epic_{answer_number}.png'
        date = answer['date'].split()[0]
        date = date.split('-')
        name = answer['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png'
        save_picture(folder, epic_image_url, file_name, payload)


if __name__ == '__main__':
    main()
