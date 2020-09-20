from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import Http404
from django.views import generic 
from django.utils import timezone


from .models import Choice, Question, Comment

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    def get_queryset(self):
        """
        Excludes any questions taht aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class CommentsView(generic.TemplateView):
    model = Comment
    template_name = 'polls/comments.html'

    def display(request):
        if (request.method == "POST"):
            name = request.POST.get('name')
            comment_text = request.POST.get('comment')
            new_comment = Comment(name = name, comment_text = comment_text) 
            new_comment.save()
            return HttpResponseRedirect(reverse('polls:list'))
        return render(request, 'polls/comments.html')


def display_list(request):
    context = {
        'comments': Comment.objects.all(),
        'latest_question': Question.objects.filter(pub_date__lte=timezone.now()).last()
      }
    return render(request, 'polls/list.html', context)
