import requests
class XyzClient:
    def __init__(self, url,token):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': token})
        self.url = url

    def uploadFile(self, file_path):
        with open(file_path, 'rb') as f:
            files = {
                "file": (file_path, f)
            }

            response = self.session.post(self.url, files=files)

            return {
                'statusCode': response.status_code,
                'body': response.text
            }