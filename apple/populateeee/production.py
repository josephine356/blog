from populateee import base

from account.models import User


print('Creating apple account ... ', end='')
User.objects.create_superuser(username='apple', password='apple10614063, email=None, fullName='管理者')
print('done')
