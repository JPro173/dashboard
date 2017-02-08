import os
import unittest

import django

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
django.setup()

from notes.models import Note


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:5000')

        self.assertIn('EU² – Notes', self.browser.title)

        # TODO: Add sorting by created_date
        first_note_title = Note.objects.first().title
        found_note_text = self.browser.find_elements_by_css_selector(
            '.note')[0].text
        self.assertEqual(first_note_title, found_note_text)


if __name__ == '__main__':
    unittest.main()
