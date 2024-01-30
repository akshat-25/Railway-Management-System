import uuid


def random_id_genrator():
    id = uuid.uuid1().int
    return id % 1000000