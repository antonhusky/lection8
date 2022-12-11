import requests

host = 'https://cloud-api.yandex.net/'
token = 'y0_AgAAAAA5KOwPAADLWwAAAADWcYQKpCkeR8d4S4WxBygj_z3D0C-QdnI'


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def get_upload_link(self, file_name):
        url = host + 'v1/disk/resources/upload'
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()

    def upload_file(self, file_name):
        href = self.get_upload_link(file_name=file_name).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    yandex_disk = YandexDisk(token)
    file_to_upload = input('Enter file name: ')
    yandex_disk.upload_file(file_to_upload)
