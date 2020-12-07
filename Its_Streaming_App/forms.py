from django import forms
from Its_Streaming_App.models import Videos, Comment

class UploadForm(forms.ModelForm):

    class Meta:
        model = Videos
        fields = ('video_title', 'video_content', 'thumbnail')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)