from django.http.response import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Author, Practice, CodeLanguage, Question
from django.views import generic
from .forms import PracticeForm
import uuid
import datetime


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    authors = Author.objects.all()

    latest_upload_practice = Practice.objects.order_by('date_of_latest_submit')[0]

    context = {'authors': authors, 'latest_upload_practice': latest_upload_practice}

    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context,
    )


class PracticeListView(generic.ListView):
    model = Practice

    def practice_list_view(request):
        latest_questions = Question.objects.order_by('title')
        all_authors = Author.objects.all()

        context = {"latest_questions": latest_questions, "all_authors": all_authors}

        template_name = 'practice_list.html'
        return render(
            request,
            template_name,
            context,
        )


class SubmitPracticeView(generic.View):
    def get(self, request):
        crt_questions = Question.objects.all()
        context = {"crt_questions": crt_questions, }
        return render(request, 'practice_upload.html', context)

    def post(self, request):
        practice_id = uuid.uuid4()
        file = request.FILES.get('myfile')  # 获取指定的文件
        title = file.name
        question_id = request.POST.get('for_question')
        question = Question.objects.filter(id=question_id)[0]
        author_name = request.POST.get('name')
        author = Author.objects.filter(name=author_name)[0]
        date_of_first_submit = datetime.date.today()
        date_of_latest_submit = date_of_first_submit
        code_language = CodeLanguage.objects.filter(name='Python')[0]

        Practice.objects.create(id=practice_id, title=title, upload=file, question=question, author=author,
                                date_of_first_submit=date_of_first_submit, date_of_latest_submit=date_of_latest_submit,
                                code_language=code_language, )
        return HttpResponse('success')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PracticeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PracticeForm()

    return render(request, 'index.html', {'form': form})


class PracticeDetailView(generic.DetailView):
    model = Practice

    def practice_detail_view(request, pk):
        try:
            practice_id = Practice.objects.get(pk=pk)
        except Practice.DoesNotExist:
            raise Http404("Practice does not exist")

        return render(
            request,
            'practice_detail.html',
            context={'practice': practice_id, }
        )


class AuthorDetailView(generic.DetailView):
    model = Author
    slug_field = 'name'

    def author_detail_view(request, slug):
        try:
            author_name = Author.objects.get(author_name=slug)
        except Author.DoesNotExist:
            raise Http404("Author does not exist")

        return render(
            request,
            'author_detail.html',
            context={'author': author_name, }
        )


class AuthorListView(generic.ListView):
    pass
