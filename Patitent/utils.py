
import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_orderno_genrator(instance):

    orderno_new = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Orderno=orderno_new).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return orderno_new


def unique_slug_generator(instance, new_slug=None):
    if new_slug is None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
