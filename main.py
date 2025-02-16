import requests
import telegram
import os
import random


def get_last_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    last_number = response.json()['num']
    return last_number


def get_random_comics():
    url_template = 'https://xkcd.com/{}/info.0.json'
    last_number = get_last_number()
    number = random.randint(0, last_number)
    url = url_template.format(number)
    response = requests.get(url)
    response.raise_for_status()
    description = response.json()['alt']
    img_url = response.json()['img']
    img = requests.get(img_url)
    img.raise_for_status()
    image = img.content
    return description, image


def main():
    chat_id = os.environ['CHAT_ID']
    tg_token = os.environ['TG_TOKEN']
    description, image = get_random_comics()
    bot = telegram.Bot(tg_token)
    bot.send_photo(chat_id=chat_id, photo=image, caption=description)


if __name__ == '__main__':
    main()