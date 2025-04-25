from django.shortcuts import render,redirect,get_object_or_404
from .forms import EmployeForm
from .models import Employe
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    employees = Employe.objects.all()  # Retrieve all employees
    paginator = Paginator(employees, 3)  # Pagination: 5 employees per page
    
    page_number = request.GET.get('page')  # Get page number from query parameters
    page_obj = paginator.get_page(page_number)  # Retrieve the employees for the current page
    
    return render(request, 'index.html', {'page_obj': page_obj})  # Pass page_obj to template


def add_emp(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeForm()
    return render(request, 'form_emp.html', {'form': form, 'title': 'Add Employee'})

def up_emp(request, pk):
    emp = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES, instance=emp)
        if form.is_valid():
            emp = form.save(commit=False)  # Prevents saving immediately
            emp.save()  # Triggers your custom salary calculation
            return redirect('index')
    else:
        form = EmployeForm(instance=emp)
    return render(request, 'form_emp.html', {'form': form, 'title': 'Update Employee'})



def dlt_emp(request,pk):
    emp = get_object_or_404(Employe,pk=pk)
    emp.delete()
    return redirect('index')

     




