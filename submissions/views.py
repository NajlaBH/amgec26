# Views of submission app
# Created by Najla BH OCT 25

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.core.mail import send_mail
from .forms import AbstractSubmissionForm

from django.core.files.storage import FileSystemStorage

# __ HOME PAGE VIEW ___
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def abstractsubmit(request):
    page_title="ABSTRACT:SUBMISSION"
    if request.method == 'POST':
        form = AbstractSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            institution = form.cleaned_data['institution']
            laboratory = form.cleaned_data['laboratory']
            presentation = form.cleaned_data['presentation']
            subject = form.cleaned_data['subject']
            topic = form.cleaned_data['topic']
            document= form.cleaned_data['document']
            print(document)
            document_up = request.FILES['document']
            print(document_up)
            #doc to upload
            #document_upload = request.FILES['document']
            #with open(document_up.name, 'wb+') as destination:
            #    for chunk in document_up.chunks():
            #        destination.write(chunk)
                    
            fs=FileSystemStorage()
            filename= fs.save(f'documents/submissions/abstracts/{document_up.name}', document_up)
            form.save()
            return redirect('index')
            #return render(request, 'index', {'document': document})
        else:
            # Print form errors if validation fails
            print("Form is invalid. Errors:", form.errors)
    else:
        form = AbstractSubmissionForm()
    return render(request, 'abstractsubmission.html', {'page_title':page_title,'form': form})