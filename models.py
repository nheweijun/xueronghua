import pymongo


def get_coll():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.nnn
    user = db.user_colletion
    return user


class User(object):
    def __init__(self, name, email, tel):
        self.tel = tel
        self.name = name
        self.email = email

    def save(self):
        user = {'name': self.name, 'email': self.email, 'tel': self.tel}
        coll = get_coll()
        idd = coll.insert(user)
        print idd

    @staticmethod
    def query_users():
        users = get_coll().find()
        return users

