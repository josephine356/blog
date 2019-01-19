from populatee import base
from account.models import User


def populateee(): 
    print('Creating apple account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='apple', password='apple10614063', email=None)
    print('done')


if __name__ == '__main__':
    populateee()