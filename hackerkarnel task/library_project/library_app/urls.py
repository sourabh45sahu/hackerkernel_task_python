from django.urls import path
from .views import (
    AuthorListView, BookListView, BorrowRecordListView,
    AuthorCreateView, BookCreateView, BorrowRecordCreateView,
    export_to_excel
)

urlpatterns = [
    path('', AuthorListView.as_view(), name='author_list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author_add'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('borrowrecords/', BorrowRecordListView.as_view(), name='borrowrecord_list'),
    path('borrowrecords/add/', BorrowRecordCreateView.as_view(), name='borrowrecord_add'),
    path('export/', export_to_excel, name='export_to_excel'),
]
