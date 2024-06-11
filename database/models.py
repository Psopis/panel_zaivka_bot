from tortoise import Model, fields


class User(Model):
    id = fields.IntField(primary_key=True)
    userid = fields.TextField()
    username = fields.TextField()
    role_ = fields.TextField()
    profit = fields.IntField()
    date = fields.DateField()
    is_employee = fields.BooleanField(default=False)

    def __str__(self):
        return self.username, self.userid


class Application(Model):
    id = fields.IntField(primary_key=True)
    user_id = fields.TextField()
    username = fields.TextField()
    date = fields.DateField()
    url = fields.TextField()
    exp = fields.TextField()
    free_time = fields.TextField()
    is_accepted = fields.BooleanField(default=False)

    def __str__(self):
        return self.username
