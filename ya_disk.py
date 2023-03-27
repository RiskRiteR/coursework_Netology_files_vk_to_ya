import requests


class YandexDisk:
    def __init__(self, token, name_folder):
        self.token = token
        self.name_folder = name_folder

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": self.name_folder, "url": link_url}
        response = requests.put(link_url, headers=headers, params=params)
        return response

    def link_url_get_upload_link(self, name_file, link_url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'{self.name_folder}/{name_file}', "url": link_url}
        response = requests.post(upload_url, headers=headers, params=params)
        return response

    # Что бы было, если нужно будет освежить память
    # def get_files_list(self):
    #     """
    #     Запрашиваем список файлов на диске.
    #     """
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     return response.json()
    #
    # def get_upload_link(self, disk_file_path):
    #     """
    #     Получаем адрес в виде ссылки где на диске будет храниться фаил.
    #     """
    #     upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    #     headers = self.get_headers()
    #     params = {"path": disk_file_path, "overwrite": "true"}
    #     response = requests.get(upload_url, headers=headers, params=params)
    #     data = response.json()
    #     url_to_load = data.get('href')
    #     return url_to_load
    #
    # def upload_file_to_disk(self, disk_file_path, local_file_path):
    #     """
    #     Загружаем фаил на диск.
    #     """
    #     href = self.get_upload_link(disk_file_path=disk_file_path)
    #     response = requests.put(href, data=open(local_file_path, 'rb'))
    #     if response.status_code == 201:
    #         print("Success")
