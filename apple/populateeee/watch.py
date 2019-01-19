from populateeee import base
from watch.models import Watch, Comment


titles = ['Apple Watch Series4', 'Apple Watch Nike+', 'Apple Watch Hermes', 'Apple Watch  Series3']
comments = ['實用的手錶', '如果造型能更好看就好了']


def populateeee():
    print('Populating watchs and comments ... ', end='')
    Watch.objects.all().delete()
    Comment.objects.all().delete()

    for title in titles:
        watch = Watch()
        watch.title = title
        for j in range(20):
            watch.content += title + '\n'
        watch.save()
        for comment in comments:
            Comment.objects.create(watch=watch, content=comment)
    print('done')


if __name__ == '__main__':
    populateeee()