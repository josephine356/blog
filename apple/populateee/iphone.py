from populateee import base
from iphone.models import Iphone, Comment


titles = ['iPhone Xs', 'iPhone Xr', 'iPhone 8', 'iPhone 7']
comments = ['文章真棒', '並不認同您的觀點']


def populateee():
    print('Populating iphones and comments ... ', end='')
    Iphone.objects.all().delete()
    Comment.objects.all().delete()

    for title in titles:
        iphone = Iphone()
        iphone.title = title
        for j in range(20):
            iphone.content += title + '\n'
        iphone.save()
        for comment in comments:
            Comment.objects.create(iphone=iphone, content=comment)
    print('done')


if __name__ == '__main__':
    populateee()