import hashlib
import requests

__all__ = ['Person', 'Cat']


class Imagens:
    """
    Classe super das classes Person e Cat
    onde os atributos e metodos gerais estão definidos
    """
    def __init__(self, url: str):
        """
        Inicializador da classe

        Parameters:
        url (str): url do site para download das imagens
        """
        self._image = None
        self._hash = None
        self._url = url
        self._headers = {'User-Agent': 'Mozzila/5.0'}

    @property
    def image(self):
        """
        Retorna a imagem
        """
        return self._image

    @property
    def hash(self):
        """
        Retorna a hash produzida pela imagem
        """
        return self._hash

    def _get_image(self):
        """
        Realiza o dowload de uma nova imagem e a salva
        no atributo image
        """
        r = requests.get(self._url, headers=self._headers)
        self._image = r.content

    def _get_hash(self):
        """
        Realiza a hash em md5 da imagem e salva no
        atributo hash
        """
        self._hash = hashlib.md5(self._image).hexdigest()

    def new_image(self):
        """
        Realiza o download de uma nova imagem e encontra
        sua hash
        """
        self._get_image()
        self._get_hash()

    def save_image(self, file_name: str = ''):
        """
        Salva a imagem

        Parameters:
        file_name (str): Nome com o qual a imagem
        deve ser salva. Default é a hash da imagem em
        formato jpeg
        """
        if not file_name:
            file_name = self._hash+'.jpeg'

        with open(file_name, 'wb') as f:
            f.write(self._image)


class Person(Imagens):
    """
    Classe que trabalha com a imagem de pessoas
    """
    def __init__(self):
        """
        Função de inicialização com a url do site
        thispersondoesnotexist
        """
        url = 'https://thispersondoesnotexist.com/image'

        super().__init__(url)


class Cat(Imagens):
    """
    Classe que trabalha com a imagem de gatos
    """
    def __init__(self):
        """
        Função de inicialização com a url do site
        thiscatdoesnotexist
        """
        url = 'https://thiscatdoesnotexist.com/'

        super().__init__(url)
