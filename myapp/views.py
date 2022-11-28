from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import FormDetails
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "myapp/home.html")


def apply_job(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully submited")
            return redirect("listing-page")
    content = {"form": form}
    return render(request, "myapp/application_form.html", content)


def edit_page(request, pk):
    application = FormDetails.objects.get(id=pk)
    form = RegistrationForm(instance=application)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Edited successfully")
            return redirect("listing-page")
    content = {"form": form}
    return render(request, "myapp/application_form.html", content)


def delete_page(request, pk):
    application = FormDetails.objects.get(id=pk)
    application.delete()
    messages.success(request, "Deleted successfully")
    return redirect("listing-page")


def listing_page(request):
    submit_data = FormDetails.objects.all().order_by("-id")
    content = {"submit_data": submit_data}
    return render(request, "myapp/listing_page.html", content)
