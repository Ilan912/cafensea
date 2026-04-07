from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Student, Transaction
from .forms import StudentForm


@login_required
def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'home.html', {'products': products})


# ----------- PRODUCTS -----------

@login_required
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product_list.html', {'products': products})


# ----------- STUDENTS -----------

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {'student': student})


@login_required
def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not hasattr(request.user, 'student'):
        # User has no student profile
        return redirect('home')  # Or show error message

    student = request.user.student

    if product.stock > 0 and student.credit >= product.price:
        # Create transaction
        Transaction.objects.create(student=student, product=product)
        # Update stock and credit
        product.stock -= 1
        product.save()
        student.credit -= product.price
        student.credit_depense += product.price
        student.save()
        return redirect('home')
    else:
        # Error, not enough credit or stock
        return redirect('home')  # Or show message