import argparse
import requests

from save_tools import save_picture


def main():
    parser = argparse.ArgumentParser(description='Данный файл скачивает фотографии с последнего запуска')
    parser.add_argument('--id',
                        type=str,
                        default='5eb87d42ffd86e000604b384',
                        help='Введите id последнего запуска'
                        )
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Введите название папки')

    args = parser.parse_args()
    launch_id = args.id
    folder = args.folder

    url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    filename = 'spaceX_'
    for index, picture in enumerate(links, 1):
        full_name = f'{filename}{index}.jpg'
        save_picture(folder, picture, full_name)


if __name__ == '__main__':
    main()
