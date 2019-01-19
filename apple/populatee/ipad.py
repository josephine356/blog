from populatee import base
from ipad.models import Ipad, Comment


titles = ['iPad Pro', 'iPad mini4', 'iPad Pro 10.5', 'iPad 9.7']
comments = ['文章真棒', '並不認同您的觀點']


def populatee():
    print('Populating ipads and comments ... ', end='')
    Ipad.objects.all().delete()
    Comment.objects.all().delete()

    for title in titles:
        ipad = Ipad()
        ipad.title = title
        for j in range(20):
            ipad.content += title + '\n'
        ipad.save()
        for comment in comments:
            Comment.objects.create(ipad=ipad, content=comment)
    print('done')


if __name__ == '__main__':
    populatee()