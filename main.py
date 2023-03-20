import os
import ya_disk
import vk
import datetime as dt
import json


def get_a_token_from_a_file(file_name):
    with open(os.path.join(os.getcwd(), 'tokens', file_name), 'r') as token_file:
        token = token_file.readline()
    return token


def date_convert(unix_time):
    date = dt.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d_%H:%M:%S')
    return date


def looking_for_unknown():
    list_name_file = []
    dict_photos = akk_vk_1.get_photos()
    for _ in dict_photos:
        dict_photos[_][1] = date_convert(dict_photos[_][1])
        if list_name_file.count(dict_photos[_][0]):
            list_name_file.append([dict_photos[_][0], dict_photos[_][1]])
            dict_photos[_].append(str(dict_photos[_][0]) + '_' +
                                  str(dict_photos[_][1]).replace('-', '_').replace(':', '_'))
        else:
            list_name_file.append(dict_photos[_][0])
            dict_photos[_].append(dict_photos[_][0])
    return dict_photos


def get_vk_to_ya():
    dict_backup = []
    all_info_photos = looking_for_unknown()
    with open('backup_info.json', 'w') as file:
        for _ in all_info_photos:
            link_photo = all_info_photos[_][4]
            name_photo = all_info_photos[_][5]
            type_photo = all_info_photos[_][2]
            akk_ya_1.link_url_get_upload_link(f'test/{name_photo}.jpg', link_photo)
            dict_backup.append({'file_name': name_photo, 'size': type_photo})
        json.dump(dict_backup, file, indent=2)


if __name__ == '__main__':
    token_vk = 'token_vk.txt'
    token_ya_disk = 'token_ya_disk.txt'

    akk_vk_1 = vk.Vkontakte(get_a_token_from_a_file(token_vk))
    akk_ya_1 = ya_disk.YandexDisk(get_a_token_from_a_file(token_ya_disk))

    get_vk_to_ya()
