# encoding = utf-8


class UserModel(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_model(self):
        print('id:{},name:{}'.format(self.id, self.name))


class BookModel(object):
    def __init__(self, user_id, title):
        self.user_id = user_id
        self.title = title
        self.name = None

    def set_name_from_id(self, user_id, users):
        book_user = filter(lambda user: user['id'] is user_id, users)
        if book_user:
            self.name = book_user[0]['name']
        else:
            self.name = "The book's author is not existed"
        return self.name
