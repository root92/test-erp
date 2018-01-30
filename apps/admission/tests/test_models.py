from django.test import TestCase
from ..models import Registration, Country
from apps.departement.models import ClassLevel
from apps.school.models import AcademicYear


class RegistrationTestModel(TestCase): 

    def setUp(self):
        self.level = ClassLevel.objects.create(label='3eme Annee')
        self.year = AcademicYear.objects.create(start_date='2017-09-15', end_date='2018-06-11',
                                            label='2017-2018')
        self.country = Country.objects.create(name='Guinée')
        self.first_student = Registration.objects.create(
                              first_name='thierno', last_name='souleymane', gender='Male',
                              date_of_birth='2001-10-12', nationality=self.country, fathers_name='bob',
                              mothers_name='alice', address='34 road', phone_number='+22 23456',
                              email='test1@gmail.com', birth_certificate_number='3344',
                              guardian_name='bela', guardian_phone='+234444',
                              guardian_email='g@gmail.com', guardian_address='2-3 street',
                              school_origin='moon', class_level=self.level, active_year=self.year)
     
    def test_student_info(self):
        self.assertEqual(self.first_student.first_name, 'thierno')
        self.assertNotEqual(self.first_student.first_name, 'bah')
        self.assertEqual(str(self.first_student.class_level), '3eme Annee')

    def test__str__(self):
        self.assertEqual(
            self.first_student.__str__(),
            'thierno souleymane'  # This is the default username for self.make_user()
        )


    def test_get_absolute_url(self):
        self.assertEqual(
                       self.first_student.get_absolute_url(),
                       '/admission/registration/%d/' % (self.first_student.id,)
                    )
