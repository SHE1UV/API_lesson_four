import os
import random
import time

import argparse
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")

    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(description='Данный файл отправляет случайные фотографии')
    parser.add_argument('--time',
                        type=int,
                        default=14400,
                        help='Введите с какой переодичностью отправлять картинки'
                        )
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Введите название папки, содержащей фотографии')
    args = parser.parse_args()
    folder = args.folder
    periodicity = args.time

    while True:
        all_files = []
        for root, _, files in os.walk(folder):
            all_files.extend([os.path.join(root, file) for file in files])

        if not all_files:
            print(f"Папка {folder} не содержит файлов.")
            break

        random_file = random.choice(all_files)
        try:
            with open(random_file, 'rb') as file:
                bot.send_document(chat_id=tg_chat_id, document=file)
            print(f"Отправлена фотография: {random_file}")
        except telegram.error.TelegramError as e:
            print(f"Произошла ошибка при отправке: {e}")

        time.sleep(periodicity)


if __name__ == '__main__':
    main()
