from shorter import views
from django.urls import include, path


paths = [
    path('stats/', views.IpStatsAPIView.as_view(), name='ip_stats'),
    path('stats/<short_id>', views.UrlStatsAPIView.as_view(), name='url_stats'),
    path('url/<short_id>', views.UrlDeleteAPIView.as_view(), name='url_delete'),
    path('url/', views.UrlCreateAPIView.as_view(), name='url_create'),

]

urlpatterns = [
    path('api/', include(paths)),
    path('<short_id>/', views.RedirectUrlView.as_view(), name='url_redirect')
]
