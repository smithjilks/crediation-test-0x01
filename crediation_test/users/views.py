from django.shortcuts import render
import json
from uuid import uuid4

from django.http import HttpResponse, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import User
from django.core import serializers


file_path = 'file.json'

class UsersList(APIView):
        def get(self, request):
                if request.GET.get('email', ''):
                        with open(file_path, 'r', encoding='utf-8') as f:
                                user_data = json.load(f)
                                for k, v in user_data.items():
                                        if request.GET.get('email', '') == v["fields"]["email"]:
                                                return Response(v["fields"])   
                
                                return Response([{"Error": "Could not find user"}],status=status.HTTP_400_BAD_REQUEST)

                with open(file_path, 'r', encoding='utf-8') as f:
                        user_data = json.load(f)
                        user_list = []
                        for k,v in user_data.items():
                                user_list.append(v["fields"])
                        return Response(user_list)
                

                

        def post(self, request):
                pay_load = json.loads(request.body)
                try:
                        first_name = pay_load['firstname']
                        last_name = pay_load['lastname']
                        email = pay_load['email']
                        if first_name == "" or last_name == "" or email == "":
                                return Response({"Error": "Missing fields"},status=status.HTTP_400_BAD_REQUEST)
                except Exception:
                        return Response({"Error": "Missing fields"},status=status.HTTP_400_BAD_REQUEST)
                
                id = str(uuid4())
                new_user = User(firstname=first_name, lastname=last_name, email=email, id=id)
               
                user_json = json.loads(serializers.serialize("json", [new_user,]))
                
                data = {}
                with open(file_path, 'r', encoding='utf-8') as f:
                        """read json file"""
                        dict_map = json.load(f)
                        dict = dict_map.items()
                        dict = {k: v for k, v in dict}

                        """new user"""
                        dict[user_json[0]["pk"]] = user_json[0]
                        data = {k: v for k, v in dict.items()}

                with open(file_path, 'w') as f:
                        json.dump(data, f)
                        return Response({"message":"success"}, status=status.HTTP_201_CREATED)
              
