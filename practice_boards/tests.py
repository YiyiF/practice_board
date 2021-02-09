import datetime

from django.test import TestCase
# from django.utils import timezone

from .models import Practice


class PracticeModelTests(TestCase):

    def test_get_absolute_url(self):
        practice_id = Practice(id='abc123,')
        self.assertIs(practice_id.get_absolute_url(), 'abc123,')

