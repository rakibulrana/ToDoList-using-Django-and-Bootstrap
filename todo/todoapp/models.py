from django.db import models
from django.forms import ModelForm

class Todo(models.Model):

    text = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text
class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ['text',]
