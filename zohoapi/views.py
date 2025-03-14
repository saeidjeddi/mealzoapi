import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from permissions.userAuth import Member


# Create your views here.
class ZohoMealView(APIView):
    permission_classes = [Member]

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
            "client_id": "1000.VRPJQPM9K4QABZX0I1UMYV4VFJ15SU",
            "client_secret": "c83aff8e09e1880580d9db4268c1402d10be4dd867",
            "refresh_token": "1000.bf09b3d89a031cf971e5dce23266afab.7efd1f6b5ac537f12011a558057a8eda",
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
    







#  به دلیل تداخل در json قبلی نزدم 
# '''
# به احتمال تفاوت json 

# '''

#  -----------------------------------

# class ZohoMealView(APIView):
    # permission_classes = [Member]

#     def get(self, request):

#         field_string = (
#             "Account_Name", "Account_Number", "View_in_Mealzo", "Longitude", "Latitude",
#             "Rating", "Customer_Data_Base", "GB_Status", "Installation_date", "IOS_App_Link",
#             "Android_App_Link", "Landing_Page", "Last_Caller", "Delivery_Bag", "Billing_Code",
#             "Package", "Phone", "APOS", "Booking", "Mealzo_Card_Machine", "TV", "Self_Ordering_Kiosk",
#             "Social_Responsible", "Website"
#         )

#         refresh_url = 'https://accounts.zoho.eu/oauth/v2/token'
#         refresh_params = {
#             "client_id": "1000.VRPJQPM9K4QABZX0I1UMYV4VFJ15SU",
#             "client_secret": "c83aff8e09e1880580d9db4268c1402d10be4dd867",
#             "refresh_token": "1000.bf09b3d89a031cf971e5dce23266afab.7efd1f6b5ac537f12011a558057a8eda",
#             "grant_type": "refresh_token"
#         }

#         refresh_request = requests.post(refresh_url, refresh_params)
#         refresh_status_json = refresh_request.json()
#         access_token = refresh_status_json["access_token"]
#         module_url = 'https://www.zohoapis.eu/crm/v3/Accounts'
#         header = {'Authorization':'Zoho-oauthtoken {}'.format(access_token)}
#         module_request_json_list = []
#         not_end_of_module_records = True
#         module_parameters = {'fields':field_string};
#         while not_end_of_module_records:
#             module_request = requests.get(module_url, params=module_parameters, headers=header)
#             module_request_json_list.extend(module_request.json()["data"])
#             not_end_of_module_records = module_request.json()["info"]["more_records"]
#             module_parameters['page_token'] = module_request.json()["info"]["next_page_token"]


#         return Response(module_request_json_list, status=status.HTTP_200_OK)