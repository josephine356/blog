from populateeee import base
from account.models import User


def populateeee(): 
    print('Creating apple account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='apple', password='apple10614063', email=None)
    print('done')


if __name__ == '__main__':
    populateeee()