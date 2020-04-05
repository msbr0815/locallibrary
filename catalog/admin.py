from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

# Inlines
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book
    fields = ('title', 'isbn', 'genre')
    exclude = ('summary', 'language')
    extra = 0

# Views
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name','middle_name'), ('last_name', 'name_suffix'), ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
    #pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    #pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    #pass

# Either set decorator or use next line for author:
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(ModelAdmin)
#admin.site.register(Book)
#admin.site.register(BookInstance)
# no nooed to change thw following two lines
admin.site.register(Genre)
admin.site.register(Language)
