from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list, 
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try :
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

    # return HttpResponse("You are looking at question %s." %question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s"
    # return HttpResponse(response % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question , pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
   


# Create your views here.
