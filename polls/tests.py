from django.test import TestCase
from polls.models import Question,Choice

# Create your tests here.
q=Question.objects.get(id=1)
q.choice_set.create(choice_text='aaa',vote=10)
