from django import forms
from .models import Recipe, Comment, Profile

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'cook_time',
                 'difficulty', 'calories', 'file']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'avatar', 'bio', 'parser', 'be']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }