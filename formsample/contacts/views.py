from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return HttpResponse('This is contacts-view index.')


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(f"your_name={form.cleaned_data['your_name']}")
            print(f"subject={form.cleaned_data['subject']}")
            print(f"message={form.cleaned_data['message']}")
            print(f"cc_myself={form.cleaned_data['cc_myself']}")
            return HttpResponseRedirect('/contacts/thanks/')

    else:
        form = ContactForm()

    return render(request, 'contacts/contact.html', {'form': form})


def thanks(request):
    return render(request, 'contacts/thanks.html')
