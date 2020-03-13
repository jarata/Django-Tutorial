from django.shortcuts import render

# Create your views here.
# Step 1.1
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Step 3.1
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# Step 3.1
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Step 3.1
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
