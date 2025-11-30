from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Sample in-memory storage
questions = [
    {"id": 1, "course_id": 1, "question": "What is Python?"},
    {"id": 2, "course_id": 1, "question": "What is Django?"}
]

@csrf_exempt
def question_list(request):
    if request.method == 'GET':
        return JsonResponse(questions, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        new_question = {"id": len(questions)+1, **body}
        questions.append(new_question)
        return JsonResponse({"message": "Question created", "data": new_question}, status=201)

@csrf_exempt
def question_detail(request, id):
    question = next((q for q in questions if q["id"] == id), None)
    if not question:
        return JsonResponse({"error": "Question not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse(question)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        question.update(body)
        return JsonResponse({"message": "Question updated", "data": question})
    elif request.method == 'DELETE':
        questions.remove(question)
        return JsonResponse({"message": "Question deleted"})
