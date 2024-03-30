import random
import re
import string

from slugify import slugify as slug_convert


def generate_random_string(length=128):
    """
    Generate a random string of given length
    :param length: length of the random string
    :return: random string
    e.g.
    generate_random_string(5) -> 'aBcDe'
    generate_random_string(10) -> 'aBcDeFgHi'
    """
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string


def generate_random_3(length=3):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string.upper()


def generate_account_id(length=22):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string


def generate_chat_id(length=10):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = "".join(random.choice(letters) for _ in range(length))
    return random_string


def generate_number(length=6):
    letters = string.digits
    return "".join(random.choice(letters) for _ in range(length))


def slugify(text):
    """
    :param text: text to slugify
    :return: slugified text
    e.g.
    slugify('Hello World') -> 'hello-world-PqBh'
    slugify('Hello World') -> 'hello-world-GvSX'
    slugify('Hello World') -> 'hello-world-hzne'
    """
    if not text:
        text = generate_account_id()
    text = slug_convert(text)
    random_string = "".join(random.choice(string.ascii_letters) for _ in range(4))
    slug = re.sub(r"[\W_]+", "-", text)
    return f"{slug}-{random_string}"


def slugify_title(text):
    """
    e.g.
    slugify_title('Hello World') -> 'jji-hello-world'
    slugify_title('Hello World') -> 'Txn-hello-world'
    slugify_title('Hello World') -> 'Ggm-hello-world'
    """
    text = slug_convert(text=text)
    random_string = "".join(random.choice(string.ascii_letters) for _ in range(3))
    slug = re.sub(r"[\W_]+", "-", text)
    return f"{random_string}-{slug}"


def generate_api_key(length=60):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = "".join(random.choice(letters) for _ in range(length))
    return "sk-" + random_string
