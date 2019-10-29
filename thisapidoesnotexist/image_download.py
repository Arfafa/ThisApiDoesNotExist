from .image_classes import Cat, Person

__all__ = ['get_person', 'get_cat']


def get_person():
    person = Person()
    person.new_image()

    return person


def get_cat():
    cat = Cat()
    cat.new_image()

    return cat
