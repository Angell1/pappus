import requests


class download(object):
    def download(self, url):
        if url is None:
            return None
        else:

            response = requests.get(url)
            if response.status_code != 200:
                return None
            return response.text