from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
# Step 1.1
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    # Step 3.3
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


# Step 3.1
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)


# Step 3.1
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Step 3.1
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
