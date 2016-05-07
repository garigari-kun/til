
'''
<form action = "" method = "POST">
    <label for = "your_name">Your name: </label>
    <input type = "text" name = "your_name" id = "your_name" value = "{{ current_name }}">
    <input type = "submit" value = "OK">
</form>
'''


# Buildin form in Django
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label = 'Your name', max_length = 100)


# views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


# template
# name.html
'''
<form action = "/your_name/" method = "POST">
    {% csrf_token %}
    {{ form }}
    <input type = "submit" value = "Submit">
</form>
'''

# More on fields
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.TextArea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required = False)

# views.py
from django.core.mail import send_mail

if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')

# https://docs.djangoproject.com/en/1.9/topics/forms/
# Working with form templates
