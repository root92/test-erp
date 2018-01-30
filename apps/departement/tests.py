# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from .models import Department, Course


# class DepartmentModelTest(TestCase):

#     def test_default_text(self):
#         department = Department()
#         self.assertEqual(department.name, 'Computer Science')

#     def test_str_representation(self):
#         department = Department(name='awesome')
#         self.assertEqual(str(department), 'awesome')

#     def test_duplicate_departments_are_invalid(self):
#         Department.objects.create(name='test1')
#         with self.assertRaises(ValidationError):
#             department = Department(name='test1')
#             department.full_clean()


# class CourseModelTest(TestCase):

#     def setUp(self):
#         self.department = Department.objects.create(name='best department')

#     def test_default_text(self):
#         course = Course(level='one', department=self.department)
#         self.assertEqual(course.title, 'Hacking')

#     def test_str_representation(self):
#         course = Course(title='best', level='two', department=self.department)
#         self.assertEqual(str(course), 'best')

#     def test_level_is_required(self):
#         course = Course(title='yes', department=self.department)
#         with self.assertRaises(ValidationError):
#             course.save()
#             course.full_clean()

#     def test_course_is_related_to_department(self):
#         course = Course(title='good', level='three',
#                         department=self.department)
#         course.save()
#         self.assertIn(course, self.department.courses.all())

#     def test_duplicate_courses_are_invalid(self):
#         Course.objects.create(title='ideas', level='one',
#                               department=self.department)
#         with self.assertRaises(ValidationError):
#             course = Course(title='ideas', level='one',
#                             department=self.department)
#             course.full_clean()
