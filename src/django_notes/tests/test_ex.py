'''
polls/tests.py
'''

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() should return False for questions whose
        pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Questino(pub_date = time)
        self.assertEqual(future_question.was_published_recently(), False)

'''
For runnnig test.
Shell:

python manage.py test polls
'''

'''
Fix bug!
'''
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days = 1) <= self.pub_date <= now

'''
Add two more tests....
'''
def test_was_published_recently_with_old_question(self):
    time = timezone.now() - datetime.timedelta(days = 30)
    old_question = Question(pub_date = time)
    self.assertEqual(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    time = timezone.now() - datetime.timedelta(hours = 1)
    recent_question = Question(pub_date = time)
    self.assertEqual(recent_question.was_published_recently(), True)