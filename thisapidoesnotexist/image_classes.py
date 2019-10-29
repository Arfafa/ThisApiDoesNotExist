import hashlib
import requests

__all__ = ['Person', 'Cat']


class Imagens:
    def __init__(self, url):
        self._image = None
        self._hash = None
        self._url = url
        self._headers = {'User-Agent': 'Mozzila/5.0'}

    @property
    def image(self):
        return self._image

    @property
    def hash(self):
        return self._hash

    def _get_image(self):
        r = requests.get(self._url, headers=self._headers)
        self._image = r.content

    def _get_hash(self):
        self._hash = hashlib.md5(self._image).hexdigest()

    def new_image(self):
        self._get_image()
        self._get_hash()

    def save_image(self, file_name=None):
        if file_name is None:
            file_name = self._hash+'.jpeg'

        with open(file_name, 'wb') as f:
            f.write(self.image)


class Person(Imagens):
    def __init__(self):
        url = 'https://thispersondoesnotexist.com/image'

        super().__init__(url)


class Cat(Imagens):
    def __init__(self):
        url = 'https://thiscatdoesnotexist.com/'

        super().__init__(url)
