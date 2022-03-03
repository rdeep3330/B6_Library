from distutils.log import log
import sre_constants
import traceback
from django.forms import fields_for_model

from django.http import HttpResponse
from django.shortcuts import redirect, render

from book.models import Book, Employee
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# request.POST.getlist("books")  # ["book1", ]

# function based view / class based view

def homepage(request):              # request -- HTTPRequest -- 
    # print(request.method)
    # print(request.POST, type(request.POST))
    # print(request.POST)
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")

    if request.method == "POST":
        if not request.POST.get("bid"):  
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name, book_qty, book_price)
            Book.objects.create(name=book_name, price=book_price, qty=book_qty)  # create book
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect("show_all_books")

    # print(request.build_absolute_uri())
    # statements -- 
    # a = [1,2,3,4]
    # print(a)
    elif request.method == "GET":
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, "home1.html", context=data)
        # return render(request, template_name="home1.html")
    # return HttpResponse("<h3>Hi Hello</h3><h5>Good Evening..!</h5>")

# HTTP Status Codes --  200 -- info -- 

# http://127.0.0.1:8000/home/  -- Base URL --  

def show_all_books(request):
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request, "show_books.html", context=data)

def edit_data(request, id):
    book = Book.objects.get(id=id)
    return render(request, template_name="home1.html", context={"single_book": book})

def delete_data(request, id):
    print(request.method)
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()  # detailed exception msg
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not allowed..! Only POST method is allowed")


# Assignment:- 
# zip file   -- 
# PEP8 rule
# indentation
# =
# comments added -- docstrings -- 


# using custom model manager -- 
# delete all book -- jaha show all books -- waha  delete all boo  -- sare delete
# soft delete  --- soft delete  -- SoftDelete  --
# hard delete - HardDelete
# soft delete all ---
# page -- soft deleted show books --   restore


# Date:- 2nd Feb --- 
# Full timers --  1st Feb -- 

# loggers -- 5th Feb -- integrate with this project  -- 


# django debugger tool -- 31st Jan -- 


# 750 lines code -- 120 line code -- 
# django queries  -- 


# 7 crore -- hist table -- 


# book = Book.objects.filter(id=1)
# if book.exists():   # 
    # data = book[0]
    # print(data)


# same -- 

# data migration -- 
# oracle -- mysql -- 


# oracle
# psql
# mongodb
# data table
# django templates


# videos -- youtube -- projects -- 10 videos -- 


# from django.shortcuts import render




from book.forms import AddressForm, BookForm, EmployeeForm
from django.contrib import messages
# Create your views here.   ---- 

def form_home(request):  # Funcion Based View
    if request.method == "POST":
        print(request.POST, "request method")
        print("in POST request")
        form  = BookForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data["name"])
            form.save()
            print(form)
            messages.success(request, 'Data Saved successfully!')  # <-
            messages.info(request, 'Redirecting to home page')
        else:
            messages.error(request, 'Invalid Data..!')
        return redirect("form_home")

    elif request.method == "GET":
        print("in get request")
        context = {"form": BookForm()}
        return render(request, "form_home.html", context=context)
    else:
        return HttpResponse("Invalid HTTP Method", status=405)


# HTTP Methods-- GET, POST, PUT, DELETE, PATCH


# class ABCD(View):
#     def get(request):   #   by default -- get
#         pass

#     def post():    # 
#         pass
    
from django.views import View

class HomePage(View):
    def get(self, request):
        print("in get request")
        return HttpResponse("In GET")

    def post(self, request):
        print(request.POST)  # 
        return HttpResponse("In POST", status=201)

    def delete(self, request):
        print("in delete request")
        return HttpResponse("In DELETE", status=204)

    def put(self, request):
        print("in put request")
        return HttpResponse("In PUT")

    def patch(self, request):
        print("in patch request")
        return HttpResponse("In PATCH")

# - idempotent -- 
# - non-idempotent --
from django.views.generic.base import TemplateView, RedirectView

class CBVTemplateView(RedirectView):
    url = "homepage"

from django.urls import reverse, reverse_lazy  

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# generic views

class EmployeeCreate(CreateView):    # employee_form.html
    model = Employee  
    fields = '__all__'  
    success_url = reverse_lazy("EmployeeCreate") #"http://127.0.0.1:8000/emp-gcreate/"
    # return render(request, "employee_form.html", {"form": EmployeeForm})


class EmployeeRetrieve(ListView):  
    model = Employee  
    # return render(request, "employee_list.html", {"object_list": data})
    


class EmployeeDetail(DetailView):  
    model = Employee  
    # return render(request, "employee_detail.html", {"object": data})


# Ass-9   - 9th Feb 2022 -- 

def student():
    print("ABC")

def product_video(request):
    print("In product video", "hello")
    return HttpResponse("Video")

def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username, password)
    if user:
        login(request, user)
        return HttpResponse("Successfully Logged In..!")
