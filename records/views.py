from django.http.response import HttpResponseServerError
from records.models import Plan, Person
from records.forms import PersonForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required(login_url='/login_view/')
def records(req):
    return render(req, "records/records.html", {
        'profiles': Person.objects.all(),
    })


@login_required()
def addProfile(req):
    if req.method == 'POST':
        user_form = PersonForm(req.POST, req.FILES)
        if user_form.is_valid():
            user_form.save()
            plans = user_form.cleaned_data['any_plans']
            name = user_form.cleaned_data['name']
            if plans:
                user = user_form.cleaned_data['name']
                # req.method = 'GET'
                return redirect('/add-plans/' + user + '/')
            else:
                print('notplans')
                return render(req, 'records/records.html')
        else:
            return render(req, 'records/post.html', {
                'form': user_form,
            })
    else:
        user_form = PersonForm()

    return render(req, 'records/post.html', {
        'form': user_form,
    })


@login_required()
def addPlans(req, user):
    print("this is user->: ", user)
    if req.method == "POST":
        print("inside post user: ", user)
        profile = Person.objects.filter(name=user)[0]
        plans = req.POST['plans']
        date = req.POST['date']
        time = req.POST['time']
        Plan.objects.create(profile=profile, plans=plans, date=date, time=time)
        return redirect('/add-plans/' + user + '/')

    return render(req, 'records/plans.html', {'user': user})


@login_required()
def seePlans(req, user):
    return render(req, 'records/seePlans.html', {
        'plans': Plan.objects.filter(profile__name=user),
    })


@login_required()
def updateProfile(req, user):
    if req.method == 'POST':
        user_profile = get_object_or_404(Person, name=user)
        user_form = PersonForm(req.POST, req.FILES, instance=user_profile)

        if user_form.is_valid():
            user_form.save()
        if user_form.cleaned_data['update_plans']:
            return redirect(f'/update-plans/{user}/')

        return redirect('/')
    else:
        user = Person.objects.filter(name=user)
        if (not user):
            return HttpResponseServerError("Error")
        user = user[0]
        return render(
            req, 'records/updateProfile.html', {
                'form':
                PersonForm(
                    initial={
                        'name': user.name,
                        'age': user.age,
                        'email': user.email,
                        'phone': user.phone,
                        'image': user.image,
                        'first_meeting': user.first_meeting,
                        'friendship': user.friendship,
                        'choices': user.choices,
                        'any_plans': user.any_plans,
                    }),
                'user':
                user.name,
            })


@login_required()
def updatePlans(req, user):
    if (req.method == 'POST'):
        pk = req.POST['id']
        plans = req.POST['plan']
        date = req.POST['date']
        time = req.POST['time']
        Plan.objects.filter(pk=pk).update(plans=plans, date=date, time=time)

        return redirect('/')

    else:
        plans = Plan.objects.filter(profile__name=user)
        if plans:
            return render(req, 'records/updatePlans.html', {
                'plans': plans,
                'user': user
            })
        else:
            return render(req, 'records/plans.html', {
                'user': user,
            })


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'records/login.html')
