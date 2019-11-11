from rest_framework import status, response, views
from foundation.models import StudentDB

class AddAPIView(views.APIView):
    def post(self, request):
        student_first_name = request.data.get('firstname', None)
        student_last_name = request.data.get('lastname', None)
        student_age = request.data.get('age', None)
        student_email = request.data.get('email', None)

        if student_first_name == None and student_last_name == None and student_age == None and student_email == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                  'message': 'Missing field.',
                  })
        else:
            first_name = student_first_name
            last_name = student_last_name
            age = float(student_age)
            email = student_email
            memory =  StudentDB.objects.create(firstname = first_name, lastname = last_name, age = student_age, email = student_email)
            memory.save()
            print(first_name+" "+last_name+" "+str(age) +" " + email)
            return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'message': 'Student Registered  Successfully!',
                 })


class StudentListAPIView(views.APIView):
    def get(self,request):
        student_list = []
        student_data = StudentDB.objects.all().order_by('id').values('firstname','lastname','age')
        for student_datum in student_data:
            student_list.append(student_datum['firstname'])
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Student List': str(student_list),
                }
                )
class StudentDetailAPIView(views.APIView):
    def get(self,request,id):
        try:
            student_detail = StudentDB.objects.get(pk=id)
            return response.Response(
                status=status.HTTP_200_OK,
                data={
                'Student First Name': student_detail.firstname,
                'Student Last Name': student_detail.lastname,
                'Student age': student_detail.age,
                'Student Email': student_detail.email,
                })

        except Exception as e:
            return response.Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                'message': 'No details found',
                     })
class StudentUpdateAPIView(views.APIView):
    def post(self, request, id):
        first_name = request.data.get('fastname', None)
        last_name = request.data.get('lastname', None)
        age = request.data.get('age', None)
        email = request.data.get('email', None)
        if first_name == None or last_name == None or age == None or email == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
            'message': 'Missing field',
                 })
        else:
            try:
                memory = StudentDB.objects.get(id = id)
                memory.fastname = first_name
                memory.lastname = last_name
                memory.age= age
                memory.email = email
                memory.save()
                return response.Response(
                status=status.HTTP_200_OK,
                data={
                'Student Updation Status': 'Student Detail Successfully Updated',
                'Student First Name': memory.firstname,
                'Student Last Name': memory.lastname,
                'Student Age': memory.age,
                'Student Email': memory.email,
                     })

            except Exception as e:
                return response.Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                'message': 'Updation failed due to '+str(e),
                     })


class ClearStudentRecordsAPIView(views.APIView):
    def post(self,request):
        memory =  StudentDB.objects.all()
        memory.delete()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': "Memory has been cleared successfully!",
            }
        )
