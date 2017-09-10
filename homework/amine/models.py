# encoding = utf-8


class UserModel(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_model(self):
        print('id:{},name:{}'.format(self.id, self.name))


class BookModel(object):
    user_Id = int()
    title = str()
    name = str()

    def __init__(self):
        pass

    def set_name_from_id(self, user_id, users):
        book_user = filter(lambda user: user['id'] is user_id, users)
        if book_user:
            self.name = book_user[0]['name']
            return self.name
        else:
            return "The book's author is not existed"
