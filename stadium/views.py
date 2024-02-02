from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status
from stadium.serializers import *
from stadium.models import *


class PhotoListCreateAPIView(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PossibilitieSetView(APIView):

    def post(self, request):
            serializer = PossibilitieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"statuscode":200,"status":"success", "message":'کاربر با موفقیت ایجاد شد.'})
            else:
                print(serializer.errors)
                return Response({"status":402, "data":serializer.errors}) 



class SportFieldView(APIView):

    def post(self, request):
            serializer = SportFieldSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"statuscode":200,"status":"success", "message":'کاربر با موفقیت ایجاد شد.'})
            else:
                print(serializer.errors)
                return Response({"status":402, "data":serializer.errors}) 
            



class StudiumSetView(APIView):

    def post(self, request):
            serializer = StudiumSetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"statuscode":200,"status":"success", "message":'کاربر با موفقیت ایجاد شد.'})
            else:
                print(serializer.errors)
                return Response({"status":402, "data":serializer.errors}) 




class ListStudiumSetView(APIView):

    def get(self, request): 
        studiumsets = StudiumSet.objects.all()

        studiumset_list = []
        for studiumset in studiumsets:
            
            user_info = {
                'id':studiumset.id ,
                'title': studiumset.title,
                'rate': studiumset.rate,  
                'address': studiumset.address,  
                'price': studiumset.price,  
                'discount': studiumset.discount,  
                'state': studiumset.state,  
                'city': studiumset.city,  
                'area': studiumset.area,  
                 
            }
            studiumset_list.append(user_info)

        response_data = {
            "statuscode": 200,
            "status": "success",
            'user_info': studiumset_list,
        }

        return Response(response_data) 



class GetOneStudiumSetView(APIView):
     
    def get(self, request, id): 
        studiumset = StudiumSet.objects.get(id=id)

        user_info = {
                'id':studiumset.id ,
                'title': studiumset.title,
                'rate': studiumset.rate,  
                'address': studiumset.address,  
                'price': studiumset.price,  
                'discount': studiumset.discount,  
                'state': studiumset.state,  
                'city': studiumset.city,  
                'area': studiumset.area,  
                 
            }

        response_data = {
            "statuscode": 200,
            "status": "success",
            'user_info': user_info,
        }

        return Response(response_data) 
    

class ClassTimeView(APIView):

    def post(self, request):
            serializer = ClassTimeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"statuscode":200,"status":"success", "message":' با موفقیت انجام شد.'})
            else:
                print(serializer.errors)
                return Response({"status":402, "data":serializer.errors})




class WeeklyReservationView(APIView):

    def post(self, request):
            serializer = WeeklyReservationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"statuscode":200,"status":"success", "message":' با موفقیت انجام شد.'})
            else:
                print(serializer.errors)
                return Response({"status":402, "data":serializer.errors})
            


class StudiumSetPossibilitieFilter(APIView):

    def get(self, request): 

        title = request.data.get('title')
        try:
            possibilitie_obj = Possibilitie.objects.get(title=title)
        except ObjectDoesNotExist:
            return Response({"statuscode":404,"status":"NotFound", "data":[]})
        
        id = possibilitie_obj.id
        studiumsets = StudiumSet.objects.filter(possibilitie_id = id)

        if list(studiumsets) == []:
            return Response({"statuscode":404,"status":"NotFound", "data":[]})
        else:
            serializer = StudiumSetSerializer(studiumsets, many=True)
            studiumsets_data = serializer.data
            return Response({"statuscode":200,"status":"success", "data":studiumsets_data})




class StudiumSetSportFieldFilter(APIView):

    def get(self, request): 
     
        title = request.data.get('title')
        try:   
            sportfield_obj = SportField.objects.get(title=title)
        except ObjectDoesNotExist:
            return Response({"statuscode":404,"status":"NotFound", "data":[]})
        id = sportfield_obj.id

        studiumsets = StudiumSet.objects.filter(sportfield_id = id)
        if list(studiumsets) == []:
            return Response({"statuscode":404,"status":"NotFound", "data":[]})
        else:
            serializer = StudiumSetSerializer(studiumsets, many=True)
            studiumsets_data = serializer.data
            return Response({"statuscode":200,"status":"success", "data":studiumsets_data})
        

class StudiumSetstateFilter(APIView):

    def get(self, request):
        state = request.data.get('state')
        city = request.data.get('city')
        area = request.data.get('area')

        state_filter = Q(state=state) if state else Q()
        city_filter = Q(city=city) if city else Q()
        area_filter = Q(area=area) if area else Q()

        studiumsets = StudiumSet.objects.filter(state_filter & city_filter & area_filter)
        if list(studiumsets) == []:
            return Response({"statuscode":404,"status":"NotFound", "data":[]})
        else:
            serializer = StudiumSetSerializer(studiumsets, many=True)
            studiumsets_data = serializer.data
            return Response({"statuscode": 200, "status": "success", "data": studiumsets_data})



class Rating(APIView):
    def post(self , request):
        id = request.data.get('id')
        rate = request.data.get('rate')

        if int(rate) >= 0 and int(rate) < 6:

            studiumset = StudiumSet.objects.get(id=id)
            rate_data = studiumset.rate
            number_people_rate = studiumset.number_people_rate
            sum_rate = studiumset.sum_rate
            new_number_people_rate = number_people_rate + 1
            sum_all_rate = int(rate) + int(sum_rate)

            result = float(sum_all_rate / new_number_people_rate)
            resultt = round(result ,1)

            studiumset.rate = str(resultt)
            studiumset.number_people_rate = new_number_people_rate
            studiumset.sum_rate = str(sum_all_rate)
            studiumset.save()

            user_info = {
                    'id':studiumset.id ,
                    'title': studiumset.title,
                    'rate': studiumset.rate,  
                    'address': studiumset.address,  
                    'price': studiumset.price,  
                    'discount': studiumset.discount,  
                    'state': studiumset.state,  
                    'city': studiumset.city,  
                    'area': studiumset.area,  
                    
                }

            response_data = {
                "statuscode": 200,
                "status": "success",
                'user_info': user_info,
            }
        
            return Response(response_data)
        else:
            return Response('enter number between 0 ,5')

    



