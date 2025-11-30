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
    """
    GET /api/courses/
    Returns a list of all courses.

    POST /api/courses/
    Creates a new course.
    Request body JSON format:
        {
            "title": "Course Title",
            "description": "Course Description"
        }
    Response JSON:
        {
            "message": "Course created",
            "data": {course object}
        }
    """
    if request.method == 'GET':
        return JsonResponse(courses, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        new_course = {"id": len(courses)+1, **body}
        courses.append(new_course)
        return JsonResponse({"message": "Course created", "data": new_course}, status=201)

@csrf_exempt
def course_detail(request, id):
    """
    GET /api/courses/<id>/
    Retrieves details of a single course by ID.

    PUT /api/courses/<id>/
    Updates the course with the given ID.
    Request body JSON can include any of the course fields:
        {
            "title": "New Title",
            "description": "New Description"
        }

    DELETE /api/courses/<id>/
    Deletes the course with the given ID.
    """
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
