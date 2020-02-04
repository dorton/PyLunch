from apiserver import ApiServer, ApiRoute
import requests
import json


class MyServer(ApiServer): 
       
        @ApiRoute("/lunch")
        def getLunch(req):
            
            r = requests.get('https://webapis.schoolcafe.com/api/CalendarView/GetWeeklyMenuitems?SchoolId=4e1c1aa8-8fbe-49b7-af51-61a61f0bc651&ServingDate=02%2F3%2F2020&ServingLine=Line%201&MealType=Lunch')

            return r.json()

MyServer("127.0.0.1",8888).serve_forever()