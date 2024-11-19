import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializer import RegularHoursSerializer, TimePeriodSerializer, UpdateTitleSerializer, UpdatePhoneNumbers, UpdateWebsiteUriSerializer
from datetime import datetime, timedelta


access_token =" ya29.a0AeDClZBoSOS-rfF1cd5wUOcWyW4lDT6Zthr_bLGxsCmZjgosafbrv7H88w1Fy52x9_8uQMgYK004PemvnHcRDRF5DEdW3lcZsX5ygwLBV3gd2tqOfZSzck8ldJ1gKkuyC_zVDT36ARKAmprliNwIuCExIgi7dfI0fBIsu0DmaCgYKAcsSARISFQHGX2MirIEWRlLwLdKeVND6SumCRA0175"
client_id = "1048682282344-fj3k4m0quarn2bt7eag3m9jdush8ca3j.apps.googleusercontent.com"
client_secret = "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"
refresh_token = "1//03gZpsDE8PILzCgYIARAAGAMSNwF-L9IrQjKtUQ1GXCTv2P4W7B7Lzpxzfo3zCZPu-Tqq4781_7mvbBx5kqdWWBU_3qjwRPmRElA"
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
        return response.status_code, response.text


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
        



class UpdateOpenHoursView(APIView):
    def post(self, request, location_id):
        global access_token, refresh_token

        serializer = RegularHoursSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        hours = serializer.validated_data

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        data = {"regularHours": hours}
        params = {"updateMask": "regularHours.periods"}
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."}, status=status.HTTP_404_NOT_FOUND)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)

        return Response({"detail": response.text}, status=response.status_code)


    
class UpdateTitleView(APIView):
    def post(self, request, location_id):
        global access_token, refresh_token

        serializer = UpdateTitleSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get("title")

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
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."}, status=status.HTTP_404_NOT_FOUND)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)

        return Response({"detail": response.text}, status=response.status_code)



class UpdatePhoneNumberView(APIView):
    def post(self, request, location_id):
        global access_token, refresh_token

        serializer = UpdatePhoneNumbers(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get("phoneNumbers").get("primaryPhone")

        url = f"https://mybusinessbusinessinformation.googleapis.com/v1/locations/{location_id}"
        data = {"phoneNumbers": {"primaryPhone": phone}}
        params = {"updateMask": "phoneNumbers"}
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 401:
            access_token, _ = refresh_access_token(refresh_token)
            headers['Authorization'] = f'Bearer {access_token}'
            response = requests.patch(url, headers=headers, json=data, params=params)

        if response.status_code == 404:
            return Response({"detail": f"Location ID '{location_id}' not found. Please check the ID."}, status=status.HTTP_404_NOT_FOUND)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"detail": response.text}, status=response.status_code)


class UpdateWebView(APIView):
    def post(self, request, location_id):
        global access_token, refresh_token

        serializer = UpdateWebsiteUriSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        websiteUri = serializer.validated_data.get("websiteUri")

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
            return Response(response.json(), status=status.HTTP_200_OK)

        return Response({"detail": response.text}, status=response.status_code)


class GetUpdateOpenView(APIView):
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
    def get(self, request, account_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{account_id}/locations'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'read_mask': 'name,title,websiteUri,phoneNumbers,metadata,regularHours,storefrontAddress,latlng',
            'pageSize': 100,
        }

        all_locations = []

        while True:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 401:
                access_token, _ = refresh_access_token(refresh_token)
                headers['Authorization'] = f'Bearer {access_token}'
                response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                all_locations.extend(data.get('locations', []))

                next_page_token = data.get('nextPageToken')
                if not next_page_token:
                    break
                params['pageToken'] = next_page_token
            else:
                return Response({"detail": response.text}, status=response.status_code)

        return Response(all_locations, status=status.HTTP_200_OK)
    




class GetBusinessInfoView(APIView):
    def get(self, request, account_id):
        global access_token, refresh_token

        url = f'https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{account_id}/locations'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        params = {
            'read_mask': 'name,title',
            'pageSize': 100,
        }

        all_locations = []

        while True:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 401:
                access_token, _ = refresh_access_token(refresh_token)
                headers['Authorization'] = f'Bearer {access_token}'
                response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                all_locations.extend(data.get('locations', []))

                next_page_token = data.get('nextPageToken')
                if not next_page_token:
                    breaki
                params['pageToken'] = next_page_token
            else:
                return Response({"detail": response.text}, status=response.status_code)

        return Response(all_locations, status=status.HTTP_200_OK)
    


class BusinessPerformanceView(APIView):
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
