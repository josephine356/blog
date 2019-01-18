from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='產品內容', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'content']