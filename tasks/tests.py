from django.test import TestCase
from datetime import date
from tasks.scoring import score_task
class T(TestCase):
    def test_s(self):
        x={'title':'a','due_date':date.today(),'estimated_hours':1,'importance':5,'dependencies':[]}
        y=score_task(x)
        self.assertTrue(isinstance(y,int))
