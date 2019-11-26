from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name please.', max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)
