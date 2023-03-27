from dotenv import load_dotenv, find_dotenv
import os
import json
import vkontakte
import ya_disk


def get_vk_to_ya(name_akk_ya_disk):
    name_akk_ya_disk.create_folder()
    all_info_photos = akk_vk_1.create_name_for_photo()
    for _ in all_info_photos:
        link_photo = all_info_photos[_][4]
        name_photo = all_info_photos[_][5]['name']
        name_akk_ya_disk.link_url_get_upload_link(f'{name_photo}.jpg', link_photo)


def saves_info_photos(name_akk_vk):
    dict_backup = []
    with open('backup_info.json', 'w') as file:
        all_info_photos = name_akk_vk.create_name_for_photo()
        for _ in all_info_photos:
            name_photo = all_info_photos[_][5]['name']
            type_photo = all_info_photos[_][2]
            dict_backup.append({'file_name': f'{name_photo}.jpg', 'size': type_photo})
        json.dump(dict_backup, file, indent=2)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    akk_vk_1 = vkontakte.Vkontakte(os.getenv('VK_TOKEN'), input('Введите id или screen_name пользователя: '))
    akk_ya_1 = ya_disk.YandexDisk(os.getenv('YA_TOKEN'), input('Введите имя папки что бы создать бекап: '))
    print(f"Обнаружено {akk_vk_1.get_photos()['response']['count']} фотографий.")
    akk_vk_1.sort_photos(int(input('Введите количество фото для загрузки: ')))

    get_vk_to_ya(akk_ya_1)
    saves_info_photos(akk_vk_1)
