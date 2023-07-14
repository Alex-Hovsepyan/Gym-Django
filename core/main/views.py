from django.shortcuts import render, redirect
from .models import *
from .forms import ContactModelForm
from random import choice
# Create your views here.

def double_content():
    header = Header.objects.all()[0]
    footer_content = FooterContent.objects.all()
    footer = Footer.objects.all()[0]
    titles = Title.objects.all()[0]
    reason = Reason.objects.all()
    appointment = Appointment.objects.all()[0]
    pricing = Pricing.objects.all()
    team = Team.objects.all()
    services_content = Services.objects.all()
    random_class = choice(Services.objects.all())
    return [header, footer_content, footer, titles, appointment, pricing, reason, team, services_content, random_class]

def index(request):
    homepage = Homepage.objects.all()
    offer = Offer.objects.all()
    home_gallery = HomeGallery.objects.all()[0]
    return render(request, 'index.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'homepage':homepage,
        'titles':double_content()[3],
        'reason':double_content()[6],
        'offer':offer,
        'appointment':double_content()[4],
        'pricing':double_content()[5],
        'home_gallery':home_gallery,
        'team':double_content()[7],
        'random_class':double_content()[9]
    })

def about(request):
    aboutpage = Aboutpage.objects.all()[0]
    about = About.objects.all()[0]
    about_fill = AboutFill.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'about.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'appointment':double_content()[4],
        'aboutpage':aboutpage,
        'reason':double_content()[6],
        'about':about,
        'about_fill':about_fill,
        'testimonial':testimonial,
        'team':double_content()[7],
        'random_class':double_content()[9]
    })

def services(request):
    servicespage = Servicespage.objects.all()[0]

    return render(request, 'services.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'appointment':double_content()[4],
        'pricing':double_content()[5],
        'servicespage':servicespage,
        'services_content':double_content()[8],
        'random_class':double_content()[9]
    })

def team(request):
    teampage = Teampage.objects.all()[0]

    return render(request, 'team.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'teampage':teampage,
        'appointment':double_content()[4],
        'team':double_content()[7],
        'random_class':double_content()[9]
    })

def classes(request, slug):
    fitness_type = Services.objects.get(slug=slug)
    classespage = Classespage.objects.all()[0]

    
    return render(request, 'classes.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'fitness_type':fitness_type,
        'services_content':double_content()[8],
        'classespage':classespage,
        'random_class':double_content()[9]
    })

def gallery(request):
    gallerypage = Gallerypage.objects.all()[0]
    gallery = Gallery.objects.all()[0]

    return render(request, 'gallery.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'gallerypage':gallerypage,
        'gallery':gallery,
        'random_class':double_content()[9]
    })

def bmi(request):
    calculatorpage = Calculatorpage.objects.all()[0]
    calculator_bmi = CalculatorBMI.objects.all()[0]
    bmi_status = BMI_STATUS.objects.all()

    return render(request, 'bmi.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'calculatorpage':calculatorpage,
        'calculator_bmi':calculator_bmi,
        'bmi_status':bmi_status,
        'random_class':double_content()[9]
    })

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()
    contactpage = Contactpage.objects.all()[0]
    contact_info = Contact.objects.all()[0]

    return render(request, 'contact.html', context={
        'header':double_content()[0],
        'footer_content':double_content()[1],
        'footer':double_content()[2],
        'titles':double_content()[3],
        'contactpage':contactpage,
        'contact_info':contact_info,
        'random_class':double_content()[9]
    })