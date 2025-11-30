import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .scoring import score_task
@csrf_exempt
def analyze(request):
    if request.method=='POST':
        data=json.loads(request.body.decode())
        out=[]
        for i in data:
            d=datetime.strptime(i['due_date'],'%Y-%m-%d').date()
            x={'title':i['title'],'due_date':d,'estimated_hours':i['estimated_hours'],'importance':i['importance'],'dependencies':i['dependencies']}
            sc=score_task(x)
            out.append({'title':i['title'],'score':sc,'due_date':i['due_date'],'estimated_hours':i['estimated_hours'],'importance':i['importance'],'dependencies':i['dependencies']})
        out=sorted(out,key=lambda k:k['score'],reverse=True)
        return JsonResponse(out,safe=False)
    return JsonResponse([],safe=False)
def suggest(request):
    return JsonResponse([],safe=False)
