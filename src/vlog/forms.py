import re

from django import forms

from ckeditor.widgets import CKEditorWidget
# from transliterate import translit
from transliterate import slugify
from transliterate.exceptions import LanguageDetectionError

from vlog import models


def transliterate(text):
    # pieces = str(re.sub('[\W]+]', ' ', text)).lower().split(' ')
    # result = []

    # for piece in pieces:
    # try:
        # result.append(translit(piece, reversed=True))
    # except LanguageDetectionError:
    #     return my_str

    # return '-'.join([r for r in result if r])
    my_str = slugify(text)
    return my_str


class PublicationForm(forms.ModelForm):
    def clean_slug(self):
        return transliterate(self.cleaned_data['title'])


class ArticleForm(PublicationForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Article
        fields = '__all__'


class CategoryForm(PublicationForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class TagForm(PublicationForm):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = '__all__'
