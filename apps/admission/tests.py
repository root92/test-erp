# import datetime
# from django.test import TestCase
# from .models import Registration
# from apps.departement.models import Department


# class RegistrationTestModel(TestCase):

#     def test_student_card(self):
#         dep = Department.objects.create(name='cool')

#       first_student = Registration.objects.create(
#            first_name='test1',last_name='test1',gender='Male',
#            date_of_birth=datetime.datetime.now().date(),nationality='france',
#            fathers_name='bob',mothers_name='alice',
#            address='34 road',phone_number='+22 23456',email='test1@gmail.com',
#            id_number='3344',guardian_name='bela',guardian_phone='+234444',
#            guardian_email='g@gmail.com',guardian_address='2-3 street',
#            school_origin='moon',department=dep)

#        self.assertEqual(first_student.student_card, '00001')
#        self.assertNotEqual(first_student.student_card,
#                            second_student.student_card)
#        self.assertEqual(second_student.student_card, '00002')
