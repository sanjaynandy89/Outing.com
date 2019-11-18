from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    phoneno= forms.CharField(max_length=100)
    cc_myself = forms.BooleanField(required=False)    