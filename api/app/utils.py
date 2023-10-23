import hashlib


def user_id_from_email(email):
    return hashlib.md5(email.encode("utf-8")).hexdigest()
