from apiserver import ApiServer, ApiRoute
import arrow
import requests
import json


class MyServer(ApiServer): 
       
        @ApiRoute("/lunch")
        def getLunch(req):
            monday = arrow.utcnow().shift(weeks=-1, weekday=0).format('MM-DD-YYYY')
            menu_params = 'GetWeeklyMenuitems'
            meal_type = 'Lunch'
            school_id = '4e1c1aa8-8fbe-49b7-af51-61a61f0bc651'

            url = f'https://webapis.schoolcafe.com/api/CalendarView/{menu_params}?SchoolId={school_id}&ServingDate={monday}&ServingLine=Line%201&MealType={meal_type}'

            r = requests.get(url)
            return r.json()
            

MyServer("127.0.0.1",8888).serve_forever()