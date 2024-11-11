import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from datetime import datetime, timedelta



class ZohoMealView(APIView):

    def get(self, request):
     
        page = 0
        field_string = (
            "Account_Name", "Account_Number", "View_in_Mealzo", "Longitude", "Latitude",
            "Rating", "Customer_Data_Base", "GB_Status", "Installation_date", "IOS_App_Link",
            "Android_App_Link", "Landing_Page", "Last_Caller", "Delivery_Bag", "Billing_Code",
            "Package", "Phone", "APOS", "Booking", "Mealzo_Card_Machine", "TV", "Self_Ordering_Kiosk", 
            "Social_Responsible", "Website"
        )

        refresh_url = 'https://accounts.zoho.eu/oauth/v2/token'
        refresh_params = {
            "client_id": "1000.CQ2TAF66KOHH7TZKU8ZY9AOMH6PRTP",
            "client_secret": "2905ee96ad89cfe1de0b8806986cff0c906af00690",
            "refresh_token": "1000.abd3af3162b8ecb3e6814670faf37cfa.89b876b54c16a69aca66931bd0a8f307",
            "grant_type": "refresh_token"
        }

        refresh_request = requests.post(refresh_url, data=refresh_params)
        refresh_status_json = refresh_request.json()
        access_token = refresh_status_json.get("access_token")

        if not access_token:
            return Response({"error": "Failed to retrieve access token"}, status=status.HTTP_400_BAD_REQUEST)

        module_url = 'https://www.zohoapis.eu/crm/v3/Accounts'
        headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}
        module_request_json_list = []

        while True:
            module_parameters = {'fields': ','.join(field_string), 'page': page}
            module_request = requests.get(module_url, params=module_parameters, headers=headers)

            if module_request.status_code == 200:
                response_json = module_request.json()
                module_request_json_list.extend(response_json.get("data", []))
                page += 1
            else:
                break

        return Response(module_request_json_list, status=status.HTTP_200_OK)