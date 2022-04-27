import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headrs (self):
        return {'Content-type': 'application/json',
                'Authorization': 'QAuth {}'}

    def upload(self, disk_file_path):
        files_url = 'http://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headrs()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        respons = requests.get(files_url, headers=headers, params=params)
        return respons.json()

    def upload_file_to_disk(self,disk_file_path,filename):
        href = self.upload(disk_file_path=disk_file_path).get('href','')
        respons = requests.put(href, data=open(filename, 'rb'))
        respons.raise_for_status()
        if respons.status_code == 201:
            print('success')


if __name__ == '__main__':
    uploader = YaUploader('Test.txt')
    result = uploader.upload_file_to_disk('Test.txt')