from django.test import TestCase

from django.conf import settings
print(settings.TEST_RUNNER)

class AAATest(TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(1, 1)
