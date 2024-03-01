
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template import loader
from .models import my_details, Project, Icon, Doc
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.conf import settings
from smtplib import SMTPException

#https://youtu.be/Ej_02ICOIgs

def home(request):
    Mydetails = my_details.objects.all()
    context = {
        "Mydetails": Mydetails,
    }
    my_doc = Doc.objects.all()
    context = {
        "my_doc": my_doc
    }
    my_icon=Icon.objects.all()
    context ={
        "my_icon": my_icon,
    }
    return render(request, "home/my_profile.html", {"Mydetails":Mydetails, "my_doc":my_doc, "my_icon":my_icon})
    #return render(request, "home/my_profile.html")
def about(request):
    my_skills={"JavaScript":"JavaScript is a scripting language that makes it possible to create and control dynamic website content. It is useful in ensuring easy interaction with the website.", 
               "Python":"This is an interpreted high-level language that can serve several purposes. It is useful in web development, data science, machine learning, and artificial intelligence.", 
               "Django":"Django is a pytho framework used for web development. It is secure and up-to-date, implying that you will not have security issues with your website.", 
               "CSS":"Cascading Style Sheets helps in styling the web page so that the interface is user friendly and follows the basic design principles.", 
               "SQL":"Standard Query Language is used to used to query the database to ensure the user gets updated data at the time of request."}
    context = {
        "my_skills": my_skills,
    }
    return render(request, "home/about.html", context)
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = settings.EMAIL_HOST_USER
            to_email = ["paulokweso7@gmail.com"]
            password = settings.EMAIL_HOST_PASSWORD
            message = form.cleaned_data["from_email"]+ "\n" +form.cleaned_data["message"]
            subject1 = "Thank you message"
            message1 = "Thank you for contacting Paul Okweso. I will get back to you as soon as possible"
            try:
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                if send_mail:
                    return redirect(Paul)
                    #response_data = {"Thank you for reaching out. Your message has been sent successfully"}
                    #return JsonResponse(response_data)
                else:
                    response_data = {'status': 'error'}
                    return JsonResponse(response_data, status=500)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except SMTPException as e:
                return HttpResponse("Ooops, an error occured. "+e)
            #except gaierror:
                # return HttpResponse("Please connect to the internet and try again")
            send_mail(subject1, message1, from_email, [form.cleaned_data["from_email"]], fail_silently=False)
    return render(request, 'home/contact.html', {"form":form})                         
def project(request):
    data = Project.objects.all()
    context = {
        "data": data,
    }
    return render(request, "home/project.html", context)
    #return render(request, "home/project.html")

def Paul(request):
    
    return render(request, 'home/success.html')
    
'''def my_data(request):
    Mydetails = my_details.objects.all().values()
    template = loader.get_template('my_profile.html')
    context = {
        "Mydetails": Mydetails,
    }
    return HttpResponse(template.render(context, request))

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["paulokweso7@gmail.com"], fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("success")
    return render(request, 'contact.html', {"form":form})
def successView(request):
    return HttpResponse("The message has been sent")'''
