from django.test import TestCase
from ..forms import RegistrationForm, EMPTY_ITEM_ERROR


class RegistrationFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        form = RegistrationForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], [EMPTY_ITEM_ERROR])
