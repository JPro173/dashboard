from django.test import TestCase
from django.core.urlresolvers import resolve

from notes.views import NotesListView


class SmokeTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        import ipdb; ipdb.set_trace()
        self.assertEqual(found.func, NotesListView)
