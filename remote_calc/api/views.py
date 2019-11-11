"""
api/views.py
"""
from rest_framework import status, response, views
from foundation.models import CalculatorMemory
MEMORY_ID=1
class VersionAPIView(views.APIView):
   def get(self, request):
       return response.Response(
           status=status.HTTP_200_OK,
           data={
               'version': '1.0',
           }
       )
class AddAPIView(views.APIView):
   def post(self, request):
       unsanitized_number = request.data.get('number', None)
       if unsanitized_number == None: # This is a validation error.
           return response.Response(
               status=status.HTTP_400_BAD_REQUEST,
               data={
                   'message': 'Missing number field.',
               }
           )
       else:
           try:
               sanitized_number = float(unsanitized_number)
           except Exception as e:
               return response.Response(
                   status=status.HTTP_400_BAD_REQUEST,
                   data={
                       'message': 'The number you submitted is not a number.',
                   }
               )
           print("Received number:", sanitized_number)
           # CREATE OR RETRIEVE THE MEMORY.
           try:
               memory = CalculatorMemory.objects.get(id=MEMORY_ID)
           except Exception as e:
               memory = CalculatorMemory.objects.create(
                   id=MEMORY_ID,
                   value=0,
               )
           # Perform our calculation and save to database.
           memory.value = memory.value + sanitized_number
           memory.save()
           # Return success message.
           return response.Response(
               status=status.HTTP_200_OK,
               data={
                   'message': 'Successfully added the number.',
               }
           )
class ResultsAPIView(views.APIView):
   def get(self, request):
       # CREATE OR RETRIEVE THE MEMORY.
       try:
           memory = CalculatorMemory.objects.get(id=MEMORY_ID)
       except Exception as e:
           memory = CalculatorMemory.objects.create(
               id=MEMORY_ID,
               value=0,
           )
       return response.Response(
           status=status.HTTP_200_OK,
           data={
               'result': memory.value,
           }
       )
class ClearAPIView(views.APIView):
   def post(self, request):
       # CREATE OR RETRIEVE THE MEMORY.
       try:
           memory = CalculatorMemory.objects.get(id=MEMORY_ID)
       except Exception as e:
           memory = CalculatorMemory.objects.create(
               id=MEMORY_ID,
               value=0,
           )
       memory.value = 0;
       memory.save()
       return response.Response(
           status=status.HTTP_200_OK,
           data={
               'result': memory.value,
           }
       )
