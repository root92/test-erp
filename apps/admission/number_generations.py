

# def registration_number():
#     current_year = datetime.date.today().year
#     prefix = "Reg-%d-%07d"
#     try:
#         last_reg = Registration.objects.latest('id')
#     except Registration.DoesNotExist:
#         last_reg = None
    
#     if not last_reg:
#         return(prefix % (current_year, 1))
#     last_id = last_reg.id
#     current_id = int(last_id) + 1
#     return (prefix % (current_year, current_id))


# def student_number():
#     current_year = datetime.date.today().year
#     prefix = "Mat-%d-%07d"
#     try:
#         last_student = Admission.objects.latest('id')
#     except Admission.DoesNotExist:
#         last_student = None
   
#     if not last_student:
#         return(prefix % (current_year, 1))
#     last_id = last_student.id
#     current_id = int(last_id) + 1
#     return(prefix % (current_year, 1))

