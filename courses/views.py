from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Sample in-memory storage for testing
courses = [
    {"id": 1, "title": "Python Basics", "description": "Intro course"},
    {"id": 2, "title": "Django for Beginners", "description": "Web dev"}
]

@csrf_exempt
def course_list(request):
    if request.method == 'GET':
        return JsonResponse(courses, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        new_course = {"id": len(courses)+1, **body}
        courses.append(new_course)
        return JsonResponse({"message": "Course created", "data": new_course}, status=201)

@csrf_exempt
def course_detail(request, id):
    course = next((c for c in courses if c["id"] == id), None)
    if not course:
        return JsonResponse({"error": "Course not found"}, status=404)
    
    if request.method == 'GET':
        return JsonResponse(course)
    
    elif request.method == 'PUT':
        body = json.loads(request.body)
        course.update(body)
        return JsonResponse({"message": "Course updated", "data": course})
    
    elif request.method == 'DELETE':
        courses.remove(course)
        return JsonResponse({"message": "Course deleted"})
