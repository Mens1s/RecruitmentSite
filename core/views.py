from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Person, Job
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    jobs = Job.objects

    return render(request, 'core/index.html',
            {
                'jobs': jobs.all(),
                'job_count': jobs.count(),
                'users': Person.objects.all(),
            }
    )

def profile(request, pk):
    try:
        user = get_object_or_404(Person, username = pk)
        return render(request, 'core/profile.html', {
            'user': user,
        })
    except:
        return render(request, 'core/index.html')

def logOut(request):
    logout(request)
    return index(request)

def logIn(request):
    if request.user.is_authenticated:
        return index(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'core/login.html', {
                'error': 'Username / Password does not match!'
            })
        login(request, user)

        return render(request, 'core/index.html')

    return render(request, 'core/login.html')


def register(request):
    if request.user.is_authenticated:
        return index(request)

    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        school = request.POST["school"]
        last_experience = request.POST["experience"]
        city = request.POST["city"]
        country = request.POST["country"]
        sector = request.POST["sector"]
        name = request.POST['name']
        last_name = request.POST['last_name']
        is_recruiter = request.POST["is_recruiter"]
        is_recruiter = is_recruiter == "YES"

        image = request.FILES["image"]
        if password2 != password1:
            return render(request, 'core/register.html', {
                'error': 'Passwords does not match',
            })
        if Person.objects.filter(email=email).exists():
            return render(request, 'core/register.html', {
                'error': 'Email is already using'
            })
        if Person.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {
                'error': 'Username is already using'
            })
        else:
            newPerson = Person.objects.create(
                first_name=name,
                last_name=last_name,
                username=username,
                email=email,
                password=password1,
                image=image,
                school=school,
                last_experience=last_experience,
                city=city,
                country=country,
                sector=sector,
                is_recruiter=is_recruiter
            )

            newPerson.set_password(password1)
            newPerson.save()
            newPerson = authenticate(request, username=username, password=password1)

            login(request, newPerson)
            return redirect('core:index')

    return render(request, 'core/register.html')
