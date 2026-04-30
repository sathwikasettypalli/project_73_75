from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Student
from app1.forms import StudentForm
from app1.forms import student_delete_form
from django.http import HttpResponse


def Student_list(request):
    data = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    return render(request, 'student_list.html', {'data': data, 'form': form})


def Student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    return render(request, 'student_update.html', {'form': form})


# def delete_student(request, id):
#     def_username = 'Sathwika'
#     def_password = 'Sathwika123'

#     std = Student.objects.get(id=id)
#     del_form = student_delete_form()

#     if request.method == 'POST':
#         del_form = student_delete_form(request.POST)
#         if del_form.is_valid():
#             user = del_form.cleaned_data['username']
#             password = del_form.cleaned_data['password']

#             if user == def_username and password == def_password:
#                 std.delete()
#                 return redirect('home_page')
#             else:
#                 return HttpResponse('<h2> Invalid Password</h2>')

#     return render(request, 'delete_std.html', {'del_form': del_form})

def delete_student(request, id):
    def_username = 'Sathwika'
    def_password = 'Sathwika123'

    std = get_object_or_404(Student, id=id)
    del_form = student_delete_form()

    if request.method == 'POST':
        del_form = student_delete_form(request.POST)

        if del_form.is_valid():
            user = del_form.cleaned_data['username']
            password = del_form.cleaned_data['password']

            if user == def_username and password == def_password:
                std.delete()
                return redirect('home_page')
            else:
                return HttpResponse("<h2>Invalid Username or Password</h2>")

    return render(request, 'delete_std.html', {'del_form': del_form})