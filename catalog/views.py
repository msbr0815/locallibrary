from django.shortcuts import render

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

def index(request):
    """View function for the home page of the site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_der = Book.objects.filter(title__icontains='der').count()

    num_instances = BookInstance.objects.all().count()

    #Available books (status = "a")
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #"all()" is implied by default.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    dict_context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_der': num_der
    }

    #Render the HTML templace index.html with the data in the context variable
    return render(request, 'index.html', context = dict_context)
