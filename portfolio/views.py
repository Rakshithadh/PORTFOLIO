from django.shortcuts import render
from .models import Project, Blog, Skill

def home(request):
    return render(request, 'portfolio/home.html')

def about_view(request):
    skills = Skill.objects.all().order_by('category', 'name')

    # Prepare a list to store grouped skills
    grouped_skills = []
    current_category = None
    category_skills = []

    for skill in skills:
        if skill.category != current_category:
            if category_skills:
                grouped_skills.append({
                    'category': current_category,
                    'skills': category_skills
                })
            current_category = skill.category
            category_skills = []

        category_skills.append(skill)

    # Append the last category's skills
    if category_skills:
        grouped_skills.append({
            'category': current_category,
            'skills': category_skills
        })

    context = {
        'skills': grouped_skills,
    }

    return render(request, 'portfolio/about.html', context)

def projects(request):
    projects = Project.objects.all()
   
    return render(request, 'portfolio/projects.html', {'projects': projects})

def blog(request):
    posts = Blog.objects.all()
    return render(request, 'portfolio/blog.html', {'posts': posts})

def contact(request):
    return render(request, 'portfolio/contact.html')
