from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Author, Practice, CodeLanguage
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    authors = Author.objects.all()
    num_authors = Author.objects.all().count()
    num_practices = Practice.objects.count()  # The 'all()' is implied by default.
    # Specific author (author = 'FuYiyi')
    num_practice_specific_author = Practice.objects.filter(author__name='FuYiyi').count()

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

    def practice_list_view(self, request):
        # context_object_name = 'my_practice_list'  # your own name for the list as a template variable
        queryset = Practice.objects.filter()[:5]  # Get 5 practices
        template_name = 'practice_list.html'
        return render(
            request,
            template_name,
            context={'practice_list': queryset}
        )


class PracticeDetailView(generic.DetailView):
    model = Practice

    # slug_field = 'id'

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
