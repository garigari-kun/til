import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    model_name = instance.__class__
    code_exists = model_name.objects.filter(shortcode=new_code)
    if code_exists:
        return create_shortcode(size=size)
    return new_code
