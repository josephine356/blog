from populate import base
from article.models import Article, Comment


titles = ['MacBook', 'MacBook Pro','MacBook Air','iMac','iMac Pro']
comments = ['MacBook機型我很喜歡','如果有更多顏色可以選擇就好']


def populate():
    print('Populating articles and comments ... ', end='')
    Article.objects.all().delete()
    Comment.objects.all().delete()

    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment)
    print('done')


if __name__ == '__main__':
    populate()