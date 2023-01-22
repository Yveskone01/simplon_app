from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Participants
from .participants_form import Participants_form, Form_Participation


# def signup(request):
#
#     if request.method == "POST":
#         form = Participants_form(request.method)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponse("<p>Merci d'avoir soumis la réponse</p>")
#
#     else:
#         form = Participants_form()
#     return render(request, 'index.html',{'form' : form})


def signup_participant(request):
    if request.method == 'POST':
        form = Form_Participation(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse("<p>Merci d'avoir soumis la réponse</p>")
    else:
        form = Form_Participation()

    return render(request, 'participants.html', {'form':form})


def view_list(request):
    participants = Participants.objects.all()
    print(participants)

    return render(request, 'liste_participants.html', {'participants': participants})
