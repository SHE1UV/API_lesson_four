import os

import argparse
import requests
from dotenv import load_dotenv

from save_tools import save_picture, get_extension


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_API_TOKEN')

    parser = argparse.ArgumentParser(description='Данный файл скачивает фотографии с сервиса NASA Astronomy Picture of the Day (APOD)')
    parser.add_argument('--count',
                        type=int,
                        default=30,
                        help='Введите кол-во фотографий которые вы хотите скачать'
                        )
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Введите название папки')
    args = parser.parse_args()
    count = args.count
    folder = args.folder

    payload = {'count': count, 'api_key': nasa_token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    filename = 'NASA_'

    for index, api_response in enumerate(response.json(), 1):
        url = api_response['url']
        extension = get_extension(url)
        full_name = f'{filename}{index}{extension}'
        save_picture(folder, url, full_name)


if __name__ == '__main__':
    main()
