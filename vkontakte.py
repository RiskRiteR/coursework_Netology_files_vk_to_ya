import requests
import datetime as dt


class Vkontakte:
    def __init__(self, token, uni_id, quantity=0, ver='5.131'):
        self.token = token
        self.ver = ver
        self.auth_params = {
            'access_token': token,
            'v': '5.131'
        }
        self.uni_id = uni_id
        self.quantity = quantity

    def get_object_id(self):
        url = 'https://api.vk.com/method/utils.resolveScreenName'
        params = {
            'screen_name': self.uni_id
        }
        response = requests.get(url, params={**self.auth_params, **params}).json()
        return response['response']['object_id']

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        if self.uni_id.isdecimal():
            params = {
                'owner_id': f'{self.uni_id}',
                'album_id': 'profile',
                'extended': '1'
            }
            response = requests.get(url, params={**self.auth_params, **params}).json()
        else:
            params = {
                'owner_id': f'{self.get_object_id()}',
                'album_id': 'profile',
                'extended': '1'
            }
            response = requests.get(url, params={**self.auth_params, **params}).json()
        return response

    def sort_photos(self, quantity):
        self.quantity = quantity
        dict_photos = {}
        all_photo = int(self.get_photos()['response']['count'])
        for _, i in enumerate(self.get_photos()['response']['items']):
            if _ >= all_photo - self.quantity:
                dict_photos.setdefault(i['id'])
                for j in i['sizes']:
                    if dict_photos[i['id']] is None or dict_photos[i['id']][3] < j['height'] * j['width']:
                        dict_photos[i['id']] = \
                            [i['likes']['count'], i['date'], j['type'], j['height'] * j['width'], j['url']]
        return dict_photos

    @staticmethod
    def date_convert(unix_time):
        date = dt.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d_%H:%M:%S')
        return date

    def create_name_for_photo(self):
        list_name_file = []
        dict_photos = self.sort_photos(self.quantity)
        for _ in dict_photos:
            dict_photos[_][1] = self.date_convert(dict_photos[_][1])
            if list_name_file.count(dict_photos[_][0]):
                list_name_file.append([dict_photos[_][0], dict_photos[_][1]])
                dict_photos[_].append({'name': str(dict_photos[_][0]) + '_' +
                                      str(dict_photos[_][1]).replace('-', '_').replace(':', '_')})
            else:
                list_name_file.append(dict_photos[_][0])
                dict_photos[_].append({'name': dict_photos[_][0]})
        return dict_photos
