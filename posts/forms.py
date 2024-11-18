from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Category

class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = True
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Title'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Short summary of the post'
                },
            ),
            'content': CKEditor5Widget(
                attrs={
                    'class': 'django_ckeditor_5'
                },
                config_name='extends',
            ),
        }
    

class EditPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Title'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Short summary of the post'
                },
            ),
            'content': CKEditor5Widget(
                attrs={
                    'class': 'django_ckeditor_5'
                },
                config_name='extends',
            ),
        }
        