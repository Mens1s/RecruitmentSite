from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Job, Person
from .models import Applications


# Create your views here.
@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        city = request.POST['city']
        country = request.POST['country']
        sector = request.POST['sector']
        job_nature = request.POST['job_nature']
        salary = request.POST['salary']

        currentUser = Person.objects.filter(username=request.user.username).get()
        newJob = Job.objects.create(
            title=title,
            description=description,
            company=currentUser.last_experience,
            city=city,
            country=country,
            sector=sector,
            creator=currentUser,
            job_nature=job_nature,
            salary=salary,
        )

        newJob.save()
        return render(request, 'job/jobs.html')
    return render(request, 'job/add.html')


def jobs(request):

    jobs = Job.objects
    return render(request, 'job/jobs.html', {
        'count': jobs.count,
        'Job': jobs.all
    })


def detail(request, pk):
    if request.method == 'POST':
        if request.method == 'POST':
            Applications.objects.create(
                job_id=pk,
                applicant_username=request.user.username,
            ).save()

    job = Job.objects.filter(id=pk).first()
    applicants = (Applications.objects.filter(job_id=pk)).all()
    is_enrolled = applicants.filter(applicant_username=request.user.username)
    is_creator = (str(job.creator) == str(request.user.username))

    if job:
        return render(request, 'job/detail.html', {
            'job': job,
            'applicants': applicants,
            'is_enrolled': is_enrolled,
            'is_creator': is_creator
        })
    return render(request, 'core/index.html')
