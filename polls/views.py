from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user(request, first_name, last_name):
    context = {'first_name': first_name, 'last_name': last_name}
    return render(request, 'users/user.html', context)
