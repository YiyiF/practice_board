from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Author, Practice, CodeLanguage, Question
from django.views import generic


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