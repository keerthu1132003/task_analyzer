from datetime import date
def score_task(t):
    today=date.today()
    d=(t['due_date']-today).days
    s=0
    if d<0:
        s+=100
    elif d<=3:
        s+=50
    s+=t['importance']*5
    if t['estimated_hours']<2:
        s+=10
    if len(t['dependencies'])>0:
        s+=len(t['dependencies'])*3
    return s
