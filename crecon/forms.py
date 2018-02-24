from django.forms import ModelForm
from django import forms
from .models import Article, Settings

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['file_obj']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['fbprophet', 'keras', 'arima']