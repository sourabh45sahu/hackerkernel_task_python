# hackerkernel_task_python
 Create a Django web application to manage an online library system where admins can manage books, authors, and their borrow records. The application should allow admins to add books, authors, and assign books to authors. Additionally, admins should be able to export the library data to an Excel sheet.
Models: Define three models: Author, Book, and BorrowRecord.
Author:
Fields: name, email, bio
Auto-generated ID
Book:
Fields: title, genre, published_date, author (ForeignKey to Author)
Auto-generated ID
BorrowRecord:
Fields: user_name, book (ForeignKey to Book), borrow_date, return_date
Auto-generated ID
Forms:
Create a form to add authors with fields for name, email, and bio. Implement form validation for the email field.
Create a form to add books with fields for title, genre, published_date, and a dropdown to select an author from the database.
Create a form to add borrow records with fields for user_name, book, borrow_date, and return_date.
Views:
Implement views to handle adding authors, adding books, and adding borrow records.
Implement views to display a paginated list of authors, books, and borrow records.
Implement a view to export all authors, books, and borrow records to separate sheets in an Excel file.
Pagination:
Utilize Django's built-in pagination feature to paginate the lists of authors, books, and borrow records.
Export to Excel:
Implement functionality to export author, book, and borrow record data to separate sheets in an Excel file.
Use libraries like django-excel or Django's built-in support for Excel file generation.

1 Apply the migrations:

   * python manage.py makemigrations
    
   * python manage.py migrate

2 Create a superuser:

    * python manage.py createsuperuser
    
3 Run the development server:
    
    * python manage.py runserver
