from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def contact(request):
    template_name = 'contact.html'
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        is_sent = sending(request, contact_form)
        if is_sent:
            return HttpResponse('お問い合わせありがとうございます。内容は送信されました')
        else:
            return HttpResponse('送信に失敗しました。管理者へ連絡してください')
    context = {
        'contact_form': contact_form,
    }
    return render(request, template_name, context)


def sending(request, form):
    form_mail = form.cleaned_data.get("mail")
    form_content = form.cleaned_data.get("content")
    form_name = form.cleaned_data.get("name")

    subject = '問合せを受信しました'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['youraddress@yours.com']
    contact_message = '{}: {} via {}'.format(form_name, form_content, form_mail)
    is_sent = send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

    return is_sent
