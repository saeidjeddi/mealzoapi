from django.urls import path
from . import views



app_name = 'googleapi'

urlpatterns = [

        path('verifications/<str:locations_id>/',views.VerificationsView.as_view(), name='get_verifications'),
        path('update-open-hours/<str:location_id>/', views.UpdateOpenHoursView.as_view(), name='update-open-hours'),
        path('get-update-open/<str:location_id>/', views.GetUpdateOpenView.as_view(), name='get-update-open'),
        path('account/', views.GetAccountInfoView.as_view(), name='get-account-info'),
        path('business-info/front/<str:account_id>/', views.GetBusinessInfoFrontView.as_view(), name='get-business-info'),
        path('business-info/<str:account_id>/', views.GetBusinessInfoView.as_view(), name='get-business-info'),
        path('performance/<str:location_id>/', views.BusinessPerformanceView.as_view(), name='get-business-performance'),
        path('metric/search/<str:locations_id>/', views.MetricSearchView.as_view(), name='metric-search'),
        path('metric/maps/<str:locations_id>/', views.MetricMapView.as_view(), name='metric-map'),
        path('metric/web-call/<str:locations_id>/', views.WebCallMetricView.as_view(), name='web-call-metric'),
        path('metric/web-call-count/<str:locations_id>/', views.WebCallCountMetricView.as_view(), name='web-call-count-metric'),
        path('metric/mob-desk-map-count/<str:locations_id>/', views.MobDeskMapCountMetricView.as_view(), name='mob-desk-map-count-metric'),
        path('metric/mob-desk-search-count/<str:locations_id>/', views.MobDeskSearchCountMetricView.as_view(), name='mob-desk-search-count-metric'),


        path('update-title/<str:location_id>/', views.UpdateTitleView.as_view(), name='UpdateTitle'),
        path('get-title/<str:location_id>/', views.GetTitleView.as_view(), name='GetTitle'),

        path('update-phonenumber/<str:location_id>/', views.UpdatePhoneNumberView.as_view(), name='UpdatePhoneNumber'),
        path('get-phonenumber/<str:location_id>/', views.GetPhoneNumberView.as_view(), name='GetPhonenumber'),

        path('update-websurl/<str:location_id>/', views.UpdateWebView.as_view(), name='UpdateWebsiteUri'),
        path('get-websurl/<str:location_id>/', views.GetWebView.as_view(), name='GetWebsiteUri'),

]
