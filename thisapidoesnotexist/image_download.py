from .image_classes import Cat, Person

__all__ = ['get_person', 'get_cat']


def get_person():
    """Função que retorna um objeto da classe Person
    com uma imagem já carregada"""
    person = Person()
    person.new_image()

    return person


def get_cat():
    """Função que retorna um objeto da classe Cat
    com uma imagem já carregada"""
    cat = Cat()
    cat.new_image()

    return cat
