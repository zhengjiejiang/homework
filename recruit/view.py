from rest_framework import status, response, views
from foundation.models import MilitaryRecruitmentDB

class AddNewRecruiteAPIView(views.APIView):
    def post(self, request):
        recruite_name = request.data.get('name', None)
        recruite_age = request.data.get('age', None)
        has_glasses = request.data.get('has_glasses', None)


        if recruite_name == None and recruite_age == None and has_glasses == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                  'message': 'Missing field.',
                  })
        else:
            memory =  MilitaryRecruitmentDB.objects.create(name = recruite_name, age = recruite_age, has_glasses = has_glasses),

            print(recruite_name+" "+recruite_age+" "+has_glasses)
            print(bool(has_glasses))
            return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'message': 'Recruite was Registered  Successfully!',
                 })


class AcceptedRecruitsAPIView(views.APIView):
    def get(self,request):
        accepted_recruits_list = []
        recruit_records = MilitaryRecruitmentDB.objects.all().order_by('id').values('name','age','has_glasses')
        for recruite in recruit_records:
            if recruite['age'] > 18:
                accepted_recruits_list.append(recruite['name'])
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Accepted Recruites': accepted_recruits_list,
                }
                )

class RejectedRecruitsAPIView(views.APIView):
    def get(self,request):
        rejected_recruits_list = []
        recruit_records = MilitaryRecruitmentDB.objects.all().order_by('id').values('name','age','has_glasses')
        for recruite in recruit_records:
            if recruite['age'] < 18:
                rejected_recruits_list.append(recruite['name'])
        return response.Response(
            status=status.HTTP_200_OK,
            data={
            'Rejected Recruites': rejected_recruits_list,
                 })


class PotentialAirforceRecruitsAPIView(views.APIView):
    def get(self,request):
        potential_air_force_recruits_list = []
        recruit_records = MilitaryRecruitmentDB.objects.all().order_by('id').values('name','age','has_glasses')

        for recruite in recruit_records:
            if bool(recruite['has_glasses']) == False:
                potential_air_force_recruits_list.append(recruite['name'])
        return response.Response(
            status=status.HTTP_200_OK,
            data={
            'Potential Air-Force Recruites': potential_air_force_recruits_list,
                 })
