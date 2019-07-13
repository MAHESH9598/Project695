from django.shortcuts import render

from website.models import UserProfile


def hello_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("pn_no")
        place = request.POST.get("place")

        data_dict = dict()
        data_dict["name"] = name
        data_dict["place"] = place
        data_dict["mobile_no"] = mobile_no
        data_dict["email"] = email

        up = UserProfile(**data_dict)
        up.save()

        ups = UserProfile.objects.all()[:10]

    return render(request, "home.html", locals())
