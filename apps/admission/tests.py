import datetime
from django.test import TestCase
from .models import Registration
from apps.departement.models import Department


class RegistrationTestModel(TestCase):

    def test_student_card(self):
        dep = Department.objects.create(name='cool')

        first_student = Registration.objects.create(
            first_name='test1',last_name='test1',gender='Male',
            date_of_birth=datetime.datetime.now().date(),nationality='france',
            fathers_name='bob',mothers_name='alice',
            address='34 road',phone_number='+22 23456',email='test1@gmail.com',
            id_number='3344', department=dep)
        
        second_student = Registration.objects.create(
            first_name='test2',last_name='test2',gender='Female',
            date_of_birth=datetime.datetime.now().date(),nationality='france',
            fathers_name='bob',mothers_name='alice',
            address='34 road',phone_number='+33 45366',email='test2@gmail.com',
            id_number='3322', department=dep)

        self.assertEqual(first_student.student_card, '00001')
        self.assertNotEqual(first_student.student_card,
                            second_student.student_card)
        self.assertEqual(second_student.student_card, '00002')
