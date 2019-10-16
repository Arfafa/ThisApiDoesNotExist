from .image_classes import Cat, Person

__all__ = ['get_person', 'get_cat']


def get_person():
    person = Person()
    person._get_image()
    person._get_hash()

    return person


def get_cat():
    cat = Cat()
    cat._get_image()
    cat._get_hash()

    return cat
