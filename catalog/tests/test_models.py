from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Book, Genre

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='justagenre')

    def test_genre_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='testbook', summary='testsummary', isbn='1234567891234')
        Author.objects.create(first_name='testfirst', last_name='testlast')
        Genre.objects.create(name='testgenre')
        Book.author = Author.objects.filter(id=1)
        Book.genre = Genre.objects.filter(id=1)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(),'/catalog/book/1')

    def test_get_author(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(str(book.author.get()), 'testlast, testfirst')

    def test_get_genre(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(book.display_genre(),'testgenre')

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Bob', last_name='Stevens', middle_name='Big', name_suffix='the Finder')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_middle_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('middle_name').verbose_name
        self.assertEquals(field_label, 'middle name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_name_suffix_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name_suffix').verbose_name
        self.assertEquals(field_label, 'name suffix')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_nationality_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('nationality').verbose_name
        self.assertEquals(field_label, 'nationality')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name_middle_suffix(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name} {author.middle_name[0]} {author.name_suffix}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')
