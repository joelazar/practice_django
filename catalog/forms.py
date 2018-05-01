from django import forms

from .models import Presentation

class PresentationForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = ('picture', 'title',)
        widgets = {'title': forms.Textarea(attrs={'cols': 70, 'rows': 1}),
                   'picture': forms.Textarea(attrs={'cols': 50, 'rows': 1})}
