from django.shortcuts import render
from .models import Progress
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Progress, Student

def progress_tracking(request):
    if request.user.is_authenticated:
        student = request.user.student
        progress_data = Progress.objects.filter(student=student)
        return render(request, 'progress_tracking.html', {'progress_data': progress_data})
    return render(request, 'progress_tracking.html')


@csrf_exempt
def update_time_spent(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        student = request.user.student
        content = data.get('content')
        time_spent = float(data.get('time_spent', 0.0))

        # Find or create the progress record for this student and content
        progress, created = Progress.objects.get_or_create(student=student, content=content)

        # Update the time spent
        progress.time_spent += time_spent
        progress.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)