from django.shortcuts import render
from .models import Course
from .forms import CourseSearchForm

def search_course(request):
    courses = None
    form = CourseSearchForm(request.GET)

    if form.is_valid():
        course_code = form.cleaned_data['course_code']
        courses = Course.objects.filter(course_code__icontains=course_code)

    return render(request, 'courses/search.html', {'form': form, 'courses': courses})
