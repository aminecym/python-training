# encoding = utf-8


class BookModel(object):
    def __init__(self, title):
        self.title = title
        self.name = None

    def set_name_from_id(self, user_id, users):
        book_user = filter(lambda user: user['id'] is user_id, users)
        if book_user:
            self.name = book_user[0]['name']
        else:
            self.name = "None"
