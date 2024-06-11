import datetime

import tortoise

from database.models import User, Application


class UserWorking:
    @staticmethod
    async def add_user(user_id, username, time):
        try:
            return await User.get(userid=user_id)
        except tortoise.exceptions.DoesNotExist:
            print(f"Created user {username}")
            await User.create(userid=user_id, username=username, role_='member', profit=0, date=time)

    @staticmethod
    async def check_user(user_id):
        return await User.get_or_none(userid=user_id)

    @staticmethod
    async def get_id_from_name(username):

        user = await User.get(username=username)
        return user.userid

    @staticmethod
    async def get_name_from_id(user_id):

        return await User.get_or_none(userid=user_id)

    @staticmethod
    async def get_user(user_id):
        user = await User.get(userid=user_id)
        return user

    @staticmethod
    async def role_update(username, role):

        user = await User.get(username=username)
        user.role_ = role
        user.is_employee = False
        if role == 'admin' or role == 'support':
            user.is_employee = True

        await user.save()


class AdminWorking:
    @staticmethod
    async def get_all_admins_and_suppots():
        return await User.filter(is_employee=True)

    @staticmethod
    async def add_admin(user_id, username, time):
        try:
            return await User.get(userid=user_id)
        except tortoise.exceptions.DoesNotExist:

            await User.create(userid=user_id, username=username, role_='admin', profit=0, is_employee=True, date = time)

    @staticmethod
    async def check_admin(user_id):
        user = await User.get(userid=user_id)
        return user.role_

    @staticmethod
    async def profit_update(username, profit):
        user = await User.get(username=username)
        user.profit = int(profit)
        print(f"Сменили профит у {username} на {profit}!")
        await user.save()


class ApplicationWorking:
    @staticmethod
    async def add_application(user_id, username, date, url, exp, free_time):
        try:
            app = await Application.get_or_none(user_id=user_id)
            if app:
                await Application.delete(app)
                await Application.create(user_id=user_id, username=username, date=date, url=url, exp=exp,
                                         free_time=free_time)
        except tortoise.exceptions.DoesNotExist:
            await Application.create(user_id=user_id, username=username, date=date, url=url, exp=exp,
                                     free_time=free_time)

    @staticmethod
    async def get_app_by_id(user_id):
        app = await Application.get(user_id=user_id)
        return

    @staticmethod
    async def get_app_by_name(username):
        return await Application.get(username=username)

    @staticmethod
    async def accept_app(user_id):
        app = await Application.get(user_id=user_id)
        app.is_accepted = True
        await app.save()
