from django.shortcuts import render, redirect
from .models import *

def home(request):

    # SAVE CONTACT FORM

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        ContactMessage.objects.create(

            name=name,
            email=email,
            message=message

        )

        return redirect('/')

    # FETCH DATA

    about = About.objects.first()

    projects = Project.objects.all()

    skill_categories = SkillCategory.objects.prefetch_related('skills').all()

    services = Service.objects.all()

    hero = Hero.objects.first()

    socials = SocialLink.objects.all()

    counters = Counter.objects.all()

    timelines = Timeline.objects.all()

    contacts = ContactInfo.objects.all()
    resume = Resume.objects.first()
    educations = Education.objects.all()
    achievements=Achievement.objects.all()
    context = {
        'success':True,
        'about': about,
        'projects': projects,
        'skill_categories': skill_categories,
        'services': services,

        'hero': hero,
        'socials': socials,
        'counters': counters,
        'timelines': timelines,
        'contacts': contacts,
        'resume': resume,
        'educations': educations,
        'achievements':achievements,

    }

    return render(
        request,
        'index1.html',
        context
    )