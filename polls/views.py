from django.shortcuts import render

# Create your views here.
# Step 1.1
from django.http import HttpResponse

from .models import Question


def index(request):
    # Step 3.3
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


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
