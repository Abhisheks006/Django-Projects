from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# READ: List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


# CREATE: Add new student
def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            age=request.POST['age']
        )
        return redirect('student_list')

    return render(request, 'students/student_form.html')


# UPDATE: Edit existing student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})


# DELETE: Delete student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})

