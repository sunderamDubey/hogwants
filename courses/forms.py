from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'category', 'short_description', 'description', 'video_url',
                  'outcome', 'requirements', 'language', 'price', 'level', 'thumbnail']
