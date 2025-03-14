import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from datetime import datetime, timedelta
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated
from deepdiff import DeepDiff

from .models import TitleLoge, PhoneLoge, WebsiteLoge, OpenHoursLoge

from exTokenApp.models import GoogleToken


from permissions.marketing import Member, MemberAdmin, GbDashboardCountMap,GbDashboardCountWeb,GbDashboardsercheCount,GbDashboardKeywords

access_token = GoogleToken.objects.order_by('access_token').first()
client_id = "1048682282344-fj3k4m0quarn2bt7eag3m9jdush8ca3j.apps.googleusercontent.com"
client_secret = "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"
refresh_token = GoogleToken.objects.order_by('refresh_token').first()


refresh_url = "https://oauth2.googleapis.com/token"


def refresh_access_token(refresh_token):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }

    response = requests.post(refresh_url, data=payload)

    if response.status_code == 200:
        token_info = response.json()
        new_access_token = token_info['access_token']
        expires_in = token_info.get('expires_in', 3600)
        return new_access_token, expires_in

    else:
        message = "Google has run out of tokens. [refresh_token] & [access_token]"
        token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
        USER_id = ["1289771453", "7154234782", '182466950', '5365525060']
        for id in USER_id:
            url = f"https://api.telegram.org/bot{token_id}/sendMessage?chat_id={id}&text={message}"
            response_1 = requests.get(url)
        return response.status_code, response.text




class GetBusinessInfoFrontPostView(APIView):
    def get(self, request, account_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{account_id}/locations'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            'read_mask': 'storefrontAddress',
            'pageSize': 100,
        }

        unique_postal_codes = set()

        while True:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 401:
                access_token, _ = refresh_access_token(refresh_token)
                headers['Authorization'] = f'Bearer {access_token}'
                response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                time.sleep(1)
                data = response.json()
                locations = data.get('locations', [])

                for location in locations:
                    storefront_address = location.get('storefrontAddress', {})
                    postal_code = storefront_address.get('postalCode')
                    if postal_code:
                        unique_postal_codes.add(postal_code)

                next_page_token = data.get('nextPageToken')
                if not next_page_token:
                    break
                params['pageToken'] = next_page_token
            elif response.status_code == 503:
                time.sleep(1)
                continue
            else:
                return Response({"detail": response.text}, status=response.status_code)

        postal_codes = [{"postCode": code} for code in unique_postal_codes]

        return Response(postal_codes, status=status.HTTP_200_OK)




class UpdatePhoneNumberView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, location_id):
        global access_token, refresh_token

        phone_numbers = request.data.get("phoneNumbers")

        if not phone_numbers or not isinstance(phone_numbers, dict):
            return Response({"detail": "A valid 'phoneNumbers' dictionary is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        primary_phone = phone_numbers.get("primaryPhone")

        if not primary_phone:
            return Response({"detail": "A valid 'primaryPhone' is required."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        data = {"phoneNumbers": {"primaryPhone": primary_phone}}
        params = {"updateMask": "phoneNumbers"}
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."},
                            status=status.HTTP_404_NOT_FOUND)
        if response.status_code == 200:
            token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
            user_id = "-1002487707008"
            data_url = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-shop-attribute/{location_id}/"

            response_1 = requests.get(data_url)
            response_1.raise_for_status()
            json_data = response_1.json()
            primary_phone = json_data.get("location", {}).get("phoneNumbers", {}).get("primaryPhone",
                                                                                      "Phone number not found")

            data_url2 = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-title/{location_id}/"

            response_2 = requests.get(data_url2)
            response_2.raise_for_status()
            json_data_1 = response_2.json()

            primary_title = json_data_1.get("location", {}).get("title", {})

            json_text = f"The phone number of this shop has been changed.\n👤 username : {request.user.username} \n✉️ Email : {request.user.email} \n🏪 Shop Name : {primary_title} \n⌚ Time : {now().strftime('%Y-%m-%d %H:%M')} \n\n ---------- \n🔔 Change: Phone(  {primary_phone} ) \n ---------"
            telegram_url = f"https://api.telegram.org/bot{token_id}/sendMessage"
            payload = {
                "chat_id": user_id,
                "text": json_text
            }
            telegram_response = requests.get(telegram_url, data=payload)
            telegram_response.raise_for_status()

            PhoneLoge.objects.create(
                username=request.user.username,
                email=request.user.email,
                shop=primary_title,
                time=now().strftime('%Y-%m-%d %H:%M'),
                chenge = primary_phone,
                location=location_id,
            )

            return Response(response.json(), status=status.HTTP_200_OK)

        return Response({"detail": response.text}, status=response.status_code)


class UpdateTitleView(APIView):
    permission_classes = [MemberAdmin]

    def post(self, request, location_id):
        global access_token, refresh_token

        title = request.data.get("title")

        if not title:
            return Response({"detail": "A valid 'title' is required."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        data = {"title": title}
        params = {"updateMask": "title"}
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.patch(url, headers=headers, json=data, params=params)

        print("Initial Response:", response.status_code, response.text)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

            print("Response After Refresh Token:", response.status_code, response.text)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."},
                            status=status.HTTP_404_NOT_FOUND)

        if response.status_code == 200:
            token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
            user_id = "-1002487707008"

            data_url = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-title/{location_id}/"

            response_1 = requests.get(data_url)
            response_1.raise_for_status()
            json_data = response_1.json()

            data_url_2 = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-shop-attribute/{location_id}/"

            response_2 = requests.get(data_url_2)
            response_2.raise_for_status()
            json_data_1 = response_2.json()

            website_uri = json_data_1.get("location", {}).get("websiteUri")

            primary_title = json_data.get("location", {}).get("title", {})

            json_text = f"The title  of this shop has been changed.\n👤 username : {request.user.username}  \n✉️ Email : {request.user.email} \n🌐 web : {website_uri} \n⌚ Time : {now().strftime('%Y-%m-%d %H:%M')} \n\n ---------- \n🔔 Change: - Shop Name ( {primary_title} )\n ---------"

            telegram_url = f"https://api.telegram.org/bot{token_id}/sendMessage"
            payload = {
                "chat_id": user_id,
                "text": json_text
            }

            telegram_response = requests.get(telegram_url, data=payload)
            telegram_response.raise_for_status()


            TitleLoge.objects.create(
                username=request.user.username,
                email=request.user.email,
                website=website_uri,
                time=now().strftime('%Y-%m-%d %H:%M'),
                chenge = primary_title,
                location=location_id,
            )


            return Response(response.json(), status=status.HTTP_200_OK)



        return Response({"detail": response.text}, status=response.status_code)


class UpdateWebView(APIView):
    permission_classes = [MemberAdmin]

    def post(self, request, location_id):
        global access_token, refresh_token

        websiteUri = request.data.get("websiteUri")

        if not websiteUri:
            return Response({"detail": "websiteUri is required."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        data = {"websiteUri": websiteUri}
        params = {"updateMask": "websiteUri"}
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."},
                            status=status.HTTP_404_NOT_FOUND)

        if response.status_code == 200:
            token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
            user_id = "-1002487707008"

            data_url = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-shop-attribute/{location_id}/"

            response_1 = requests.get(data_url)
            response_1.raise_for_status()
            json_data = response_1.json()

            website_uri = json_data.get("location", {}).get("websiteUri")

            data_url2 = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-title/{location_id}/"

            response_2 = requests.get(data_url2)
            response_2.raise_for_status()
            json_data_1 = response_2.json()

            primary_title = json_data_1.get("location", {}).get("title", {})

            json_text = f"The website  of this shop has been changed.\n👤 username : {request.user.username} \n✉️ Email : {request.user.email} \n🏪 Shop Name : {primary_title} \n⌚ Time : {now().strftime('%Y-%m-%d %H:%M')} \n\n ---------- \n🔔 Change : Websit (  {website_uri} )\n ---------"

            telegram_url = f"https://api.telegram.org/bot{token_id}/sendMessage"
            payload = {
                "chat_id": user_id,
                "text": json_text
            }

            telegram_response = requests.get(telegram_url, data=payload)
            telegram_response.raise_for_status()


            WebsiteLoge.objects.create(
                username=request.user.username,
                email=request.user.email,
                shop=primary_title,
                time=now().strftime('%Y-%m-%d %H:%M'),
                chenge = website_uri,
                location=location_id,
            )

            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"detail": response.text}, status=response.status_code)




class UpdateOpenHoursView(APIView):
    permission_classes = [MemberAdmin]

    def post(self, request, location_id):
        global access_token, refresh_token

        hours = request.data.get("periods")
        if not hours or not isinstance(hours, list):
            return Response({"detail": "A valid 'periods' list is required."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        headers = {'Authorization': f'Bearer {access_token}'}
        params = {'read_mask': 'regularHours.periods'}

        original_response = requests.get(url, headers=headers, params=params)
        if original_response.status_code == 401:
            try:
                access_token, refresh_token = refresh_access_token(refresh_token)
                headers['Authorization'] = f'Bearer {access_token}'
                original_response = requests.get(url, headers=headers, params=params)
            except Exception as e:
                return Response({"detail": "Failed to refresh access token.", "error": str(e)},
                                status=status.HTTP_401_UNAUTHORIZED)

        if original_response.status_code != 200:
            return Response({
                "detail": "Failed to fetch original data.",
                "status_code": original_response.status_code,
                "error_message": original_response.text
            }, status=original_response.status_code)

        original_data = original_response.json().get("regularHours", {}).get("periods", [])

        data = {"regularHours": {"periods": hours}}
        params = {"updateMask": "regularHours.periods"}
        response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 401:
            access_token, refresh_token = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."},
                            status=status.HTTP_404_NOT_FOUND)

        if response.status_code == 200:
            updated_response = requests.get(url, headers=headers, params=params)
            updated_data = updated_response.json().get("regularHours", {}).get("periods", [])

            differences = DeepDiff(original_data, updated_data, ignore_order=True).to_dict()

            changes_text = "Changes:\n"
            if "values_changed" in differences:
                changes_text += "Updated:\n"
                for _, change in differences["values_changed"].items():
                    old = change['old_value']
                    new = change['new_value']
                    changes_text += f" - From {old} to {new}\n"

            if "iterable_item_added" in differences:
                changes_text += "Added:\n"
                for _, added in differences["iterable_item_added"].items():
                    changes_text += f" - {added}\n"

            if "iterable_item_removed" in differences:
                changes_text += "-\n"
                for _, removed in differences["iterable_item_removed"].items():
                    day = removed.get("openDay")
                    open_time = removed.get("openTime", {})
                    close_time = removed.get("closeTime", {})
                    changes_text += (
                        f" • {day}, Open: {open_time.get('hours', 'N/A')}:{open_time.get('minutes', '00')}, "
                        f"Close: {close_time.get('hours', 'N/A')}:{close_time.get('minutes', '00')}\n"
                    )

            if changes_text == "Changes:\n":
                changes_text += "No significant changes were made."

            token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
            user_id = "-1002487707008"

            data_url = f"https://takeawaytracker.mealzo.co.uk/api/v1/google/get-title/{location_id}/"

            response_1 = requests.get(data_url)
            response_1.raise_for_status()
            json_data = response_1.json()

            primary_title = json_data.get("location", {}).get("title", {})
            json_text = (
                f"open hours of this shop have been changed.\n"
                f"👤 Username: {request.user.username}\n"
                f"✉️ Email: {request.user.email}\n"
                f"🏪 Shop Name : {primary_title}\n"
                f"⌚ Time: {now().strftime('%Y-%m-%d %H:%M')}\n\n"
                f"🔔 {changes_text}"
            )
            telegram_url = f"https://api.telegram.org/bot{token_id}/sendMessage"
            payload = {
                "chat_id": user_id,
                "text": json_text
            }
            telegram_response = requests.get(telegram_url, data=payload)
            telegram_response.raise_for_status()

            OpenHoursLoge.objects.create(
                username=request.user.username,
                email=request.user.email,
                shop=primary_title,
                time=now().strftime('%Y-%m-%d %H:%M'),
                chenge = changes_text,
                location=location_id,
            )

            return Response(response.json(), status=status.HTTP_200_OK)



        return Response({"detail": response.text}, status=response.status_code)



class VerificationsView(APIView):


    def get(self, request, locations_id):
        global access_token

        url = f'https://mybusinessverifications.googleapis.com/v1/locations/{locations_id}/verifications'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return Response(response.json())

        else:
            return Response({'status': response.status_code, 'error': response.text}, status=response.status_code)


class GetUpdateOpenView(APIView):
    permission_classes = [Member]

    def get(self, request, location_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}:getGoogleUpdated'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            "readMask": 'regularHours.periods'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"detail": response.text}, status=response.status_code)


class Getwebsiteurl(APIView):


    def get(self, request, location_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}:getGoogleUpdated'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            "readMask": 'websiteUri,phoneNumbers,storefrontAddress'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"detail": response.text}, status=response.status_code)


class GetUpdateOpenStatusView(APIView):

    def get(self, request, location_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}:getGoogleUpdated'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            "readMask": 'openInfo'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"detail": response.text}, status=response.status_code)


class GetAccountInfoView(APIView):
    def get(self, request):
        global access_token, refresh_token

        url = 'https://mybusinessaccountmanagement.googleapis.com/v1/accounts'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"detail": response.text}, status=response.status_code)

class GetBusinessInfoFrontView(APIView):
    permission_classes = [Member]
    def get(self, request, account_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{account_id}/locations'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            'read_mask': 'name,title,websiteUri,phoneNumbers,metadata,regularHours,storefrontAddress,latlng,categories',
            'pageSize': 100,
        }

        all_locations = []

        while True:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 401:
                new_tokens = refresh_access_token(refresh_token)
                if new_tokens:
                    access_token, refresh_token = new_tokens
                    headers['Authorization'] = f'Bearer {access_token}'
                    response = requests.get(url, headers=headers, params=params)
                else:
                    return Response({"detail": "Failed to refresh access token."}, status=status.HTTP_401_UNAUTHORIZED)

            if response.status_code == 200:
                time.sleep(1)
                data = response.json()
                all_locations.extend(data.get('locations', []))

                next_page_token = data.get('nextPageToken')
                if not next_page_token:
                    break
                params['pageToken'] = next_page_token
                print(f'{next_page_token}')
            elif response.status_code == 503:
                time.sleep(1)
                continue
            else:
                return Response({"detail": response.text}, status=response.status_code)

        return Response(all_locations, status=status.HTTP_200_OK)


class BusinessPerformanceView(APIView):
    permission_classes = [GbDashboardKeywords]

    def get(self, request, location_id):
        global access_token, refresh_token

        days = int(request.query_params.get("days", 180))
        today = datetime.today().date()
        six_months_ago = today - timedelta(days=days)

        monthlyRange_endMonth_day = today.day
        monthlyRange_endMonth_month = today.month
        monthlyRange_endMonth_year = today.year

        monthlyRange_startMonth_day = six_months_ago.day
        monthlyRange_startMonth_month = six_months_ago.month
        monthlyRange_startMonth_year = six_months_ago.year

        params = {
            'monthlyRange.end_month.day': monthlyRange_endMonth_day,
            'monthlyRange.end_month.month': monthlyRange_endMonth_month,
            'monthlyRange.end_month.year': monthlyRange_endMonth_year,
            'monthlyRange.start_month.day': monthlyRange_startMonth_day,
            'monthlyRange.start_month.month': monthlyRange_startMonth_month,
            'monthlyRange.start_month.year': monthlyRange_startMonth_year,
            'pageSize': 100,
        }

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{location_id}/searchkeywords/impressions/monthly'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        max_retries = 3
        retry_delay = 5
        pageToken = ''
        all_results = []

        while True:
            for attempt in range(max_retries):
                try:
                    if pageToken:
                        params['pageToken'] = pageToken
                    response = requests.get(url, headers=headers, params=params)

                    if response.status_code == 401:
                        access_token, _ = refresh_access_token(refresh_token)
                        headers['Authorization'] = f'Bearer {access_token}'
                        response = requests.get(url, headers=headers, params=params)

                    response.raise_for_status()

                    result = response.json()
                    search_keywords = result.get('searchKeywordsCounts', [])
                    all_results.extend(search_keywords)

                    pageToken = result.get('nextPageToken')
                    if not pageToken:
                        return Response({"allResults": all_results}, status=status.HTTP_200_OK)
                except Exception as e:
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                    else:
                        raise APIException(f"Error fetching data after retries: {e}")


class MetricSearchView(APIView):
    permission_classes = [Member]
    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
                "BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            raise APIException(detail=response.text, code=response.status_code)


class MetricMapView(APIView):


    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
                "BUSINESS_IMPRESSIONS_MOBILE_MAPS",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            raise APIException(detail=response.text, code=response.status_code)


class WebCallMetricView(APIView):
    


    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "CALL_CLICKS",
                "WEBSITE_CLICKS",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            raise APIException(detail=response.text, code=response.status_code)


class WebCallCountMetricView(APIView):
    permission_classes = [GbDashboardCountWeb]


    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "CALL_CLICKS",
                "WEBSITE_CLICKS",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            total_call_clicks = 0
            total_website_clicks = 0

            for metric in data['multiDailyMetricTimeSeries']:
                for daily_metric in metric['dailyMetricTimeSeries']:
                    if daily_metric['dailyMetric'] == "CALL_CLICKS":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_call_clicks += int(value)
                    elif daily_metric['dailyMetric'] == "WEBSITE_CLICKS":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_website_clicks += int(value)

            return Response({
                "total_call_clicks": total_call_clicks,
                "total_website_clicks": total_website_clicks
            }, status=status.HTTP_200_OK)

        else:
            raise APIException(detail=response.text, code=response.status_code)


class MobDeskMapCountMetricView(APIView):
    permission_classes = [GbDashboardCountMap]


    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
                "BUSINESS_IMPRESSIONS_MOBILE_MAPS",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            total_desktop_maps = 0
            total_mobile_maps = 0

            for metric in data['multiDailyMetricTimeSeries']:
                for daily_metric in metric['dailyMetricTimeSeries']:
                    if daily_metric['dailyMetric'] == "BUSINESS_IMPRESSIONS_DESKTOP_MAPS":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_desktop_maps += int(value)
                    elif daily_metric['dailyMetric'] == "BUSINESS_IMPRESSIONS_MOBILE_MAPS":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_mobile_maps += int(value)

            return Response({
                "BUSINESS_IMPRESSIONS_DESKTOP_MAPS": total_desktop_maps,
                "BUSINESS_IMPRESSIONS_MOBILE_MAPS": total_mobile_maps
            }, status=status.HTTP_200_OK)

        else:
            raise APIException(detail=response.text, code=response.status_code)


class MobDeskSearchCountMetricView(APIView):

    permission_classes = [GbDashboardsercheCount]


    def get(self, request, locations_id):
        global access_token, refresh_token

        start_year = int(request.query_params.get('dailyRange.start_date.year', None) or 0)
        start_month = int(request.query_params.get('dailyRange.start_date.month', None) or 0)
        start_day = int(request.query_params.get('dailyRange.start_date.day', None) or 0)
        end_year = int(request.query_params.get('dailyRange.end_date.year', None) or 0)
        end_month = int(request.query_params.get('dailyRange.end_date.month', None) or 0)
        end_day = int(request.query_params.get('dailyRange.end_date.day', None) or 0)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        start_year = start_year or start_date.year
        start_month = start_month or start_date.month
        start_day = start_day or start_date.day
        end_year = end_year or end_date.year
        end_month = end_month or end_date.month
        end_day = end_day or end_date.day

        url = f'https://businessprofileperformance.googleapis.com/v1/locations/{locations_id}:fetchMultiDailyMetricsTimeSeries'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'dailyMetrics': [
                "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
                "BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
            ],
            'dailyRange.start_date.year': start_year,
            'dailyRange.start_date.month': start_month,
            'dailyRange.start_date.day': start_day,
            'dailyRange.end_date.year': end_year,
            'dailyRange.end_date.month': end_month,
            'dailyRange.end_date.day': end_day,
        }

        response = requests.get(url, headers=headers, params=params)

        # Handle expired access token
        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            total_desktop_search = 0
            total_mobile_search = 0

            for metric in data['multiDailyMetricTimeSeries']:
                for daily_metric in metric['dailyMetricTimeSeries']:
                    if daily_metric['dailyMetric'] == "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_desktop_search += int(value)
                    elif daily_metric['dailyMetric'] == "BUSINESS_IMPRESSIONS_MOBILE_SEARCH":
                        for dated_value in daily_metric['timeSeries']['datedValues']:
                            value = dated_value.get('value')
                            if value is not None:
                                total_mobile_search += int(value)

            return Response({
                "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH": total_desktop_search,
                "BUSINESS_IMPRESSIONS_MOBILE_SEARCH": total_mobile_search
            }, status=status.HTTP_200_OK)

        else:
            raise APIException(detail=response.text, code=response.status_code)


class GetTitleView(APIView):


    def get(self, request, location_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}:getGoogleUpdated'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        params = {
            "readMask": 'title'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"detail": response.text}, status=response.status_code)







# class GetBusinessInfoView(APIView):
#     def get(self, request, account_id):
#         global access_token, refresh_token
#
#         url = f'https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{account_id}/locations'
#         headers = {
#             'Authorization': f'Bearer {access_token}',
#             'Content-Type': 'application/json',
#         }
#
#         params = {
#             'read_mask': 'name,title,websiteUri,categories',
#             'pageSize': 100,
#         }
#
#         all_locations = []
#
#         while True:
#             response = requests.get(url, headers=headers, params=params)
#
#             if response.status_code == 401:
#                 access_token, _ = refresh_access_token(refresh_token)
#                 headers['Authorization'] = f'Bearer {access_token}'
#                 response = requests.get(url, headers=headers, params=params)
#
#             if response.status_code == 200:
#                 data = response.json()
#                 all_locations.extend(data.get('locations', []))
#
#                 next_page_token = data.get('nextPageToken')
#                 if not next_page_token:
#                     break
#                 params['pageToken'] = next_page_token
#             else:
#                 return Response({"detail": response.text}, status=response.status_code)
#
#         return Response(all_locations, status=status.HTTP_200_OK)
