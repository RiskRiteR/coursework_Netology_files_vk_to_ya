import requests


class Vkontakte:
    def __init__(self, token, ver='5.131'):
        self.token = token
        self.ver = ver
        self.auth_params = {
            'access_token': token,
            'v': '5.131'
        }

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'album_id': 'profile',
            'extended': '1',
        }
        response = requests.get(url, params={**self.auth_params, **params}).json()
        dict_photos = {}
        for i in response['response']['items']:
            dict_photos.setdefault(i['id'])
            for j in i['sizes']:
                if dict_photos[i['id']] is None or dict_photos[i['id']][3] < j['height'] * j['width']:
                    dict_photos[i['id']] = \
                        [i['likes']['count'], i['date'], j['type'], j['height'] * j['width'], j['url']]
        return dict_photos
