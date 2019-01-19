from django.db import models


class Iphone(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-pubDateTime']

class Comment(models.Model):
    iphone = models.ForeignKey(Iphone, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.article.title + '-' + str(self.id)
    class Meta:
        ordering = ['pubDateTime']

