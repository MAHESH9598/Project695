from django.shortcuts import render


def hello_view(request):
    if request.method == "POST":
        pass

    return render(request, "home.html")
