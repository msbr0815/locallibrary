from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

class AuthorListView(generic.ListView):
    model = Author
    #paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #Pattern:
    #1. Get existing context from superclass (here: Book)
    #2. Add new context information: define output function
    #3. Return updated content
    #

class BookDetailView(generic.DetailView):
    model = Book

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on load to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_all_borrowed.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

class MaintenanceListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_see_maintenance'
    template_name = 'catalog/bookinstance_list_maintenance.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='m').order_by('due_back')

def index(request):
    """View function for the home page of the site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_der = Book.objects.filter(title__icontains='der').count()

    num_instances = BookInstance.objects.all().count()

    #Available books (status = "a")
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # "all()" is implied by default.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    # Count the number of visits to this view, as counted in the sessions variable
    num_visits = request.session.get('num_visits', 0) # 0 is a default value
    request.session['num_visits'] = num_visits + 1

    dict_context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_der': num_der,
        'num_visits': num_visits
    }

    #Render the HTML templace index.html with the data in the context variable
    return render(request, 'index.html', context = dict_context)
