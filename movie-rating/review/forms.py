from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'review')
        lables = {
            'name': 'Movie Name',
            'review': 'Review Content' 
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args, **kwargs)

