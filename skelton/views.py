# Views of skelton app
# Created by Najla BH OCT 25

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


from django.core.mail import send_mail
from .forms import ASKfrom



# __ HOME PAGE VIEW ___
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    page_title="Home"
    return render(request,'index.html',{'page_title':page_title})


# __ ABOUT PAGE VIEW ___
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def about(request):
    page_title="About"
    return render(request,'about.html',{'page_title':page_title})


# __ CONTACT PAGE VIEW ___
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def contact(request):
    page_title="Contact:FORM"
    if request.method == 'POST':
        form = ASKfrom(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            demande = form.cleaned_data['demande']
            message = form.cleaned_data['message']
            recipient_list = 'najlabh.freelance@gmail.com'
            send_mail(
                f"{demande}",
                f"Message: {message}",
                f"{email}",
                ["najlabh.freelance@gmail.com"],
                fail_silently=False,
            )
            #send_mail(first_name, last_name, email, phone, demande, message, recipient_list)
            #pass
            form.save()
        return redirect('index')
    else:
        form = ASKfrom()
    return render(request, 'contact.html', {'page_title':page_title,'form': form})


# __ SPONSORS PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sponsors(request):
    page_title="Sponsors"
    return render(request,'sponsors.html',{'page_title':page_title})



# __ TOPICS PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def topics(request):
    page_title="Topics"
    return render(request,'topics.html',{'page_title':page_title})

# __ COMMITTEES PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def committees(request):
    page_title="Committees"
    return render(request,'committees.html',{'page_title':page_title})


# __ COMMITTEES PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workshop(request):
    page_title="workshop"
    return render(request,'workshop.html',{'page_title':page_title})


# __ Fees PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fees(request):
    page_title="Fees"
    return render(request,'fees.html',{'page_title':page_title})


# __ PROGRAM PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def program(request):
    page_title="Program"
    return render(request,'program.html',{'page_title':page_title})

# __ ABOUT PAGE VIEW ___

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def private(request):
    page_title="Private"
    return render(request,'private.html',{'page_title':page_title})

