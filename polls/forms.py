from django import forms
from ckeditor.fields import RichTextField

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50)
    fromEmail = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    commentText = forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.commentText} by {self.name}"