from django.utils.text import slugify

from home import models

import string
import random


def generate_random_string(Num):
    res = "-".join(random.choices(string.ascii_uppercase + string.digits, k = Num))
    return res


def generate_slug(text):
    
    gen_slug = slugify(text)
    
    if models.BlogModel.objects.filter(slug = gen_slug).exists():
       gen_slug = gen_slug + generate_random_string(5)
        
    return gen_slug


# import string, random


# from django.utils.text import slugify

# def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
# 	return ''.join(random.choice(chars) for _ in range(size))

# def unique_slug_generator(instance, new_slug = None):
# 	if new_slug is not None:
# 		slug = new_slug
# 	else:
# 		slug = slugify(instance.title)
# 	Klass = instance.__class__
# 	max_length = Klass._meta.get_field('slug').max_length
# 	slug = slug[:max_length]
# 	qs_exists = Klass.objects.filter(slug = slug).exists()
	
# 	if qs_exists:
# 		new_slug = "{slug}-{randstr}".format(
# 			slug = slug[:max_length-5], randstr = random_string_generator(size = 4))
			
# 		return unique_slug_generator(instance, new_slug = new_slug)
# 	return slug
