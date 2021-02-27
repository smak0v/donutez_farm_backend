from django.urls import path

from core.views import ListCreateTokensView, RetrieveTokensForUserView, ListCreateYFsView, RetrieveYFsForUserView

core_urlpatterns = [
    path('tokens/', ListCreateTokensView.as_view(), name='list_create_tokens'),
    path('tokens/<str:user>/', RetrieveTokensForUserView.as_view(), name='retrieve_tokens_for_user'),

    path('yfs/', ListCreateYFsView.as_view(), name='list_create_yfs'),
    path('yfs/<str:user>/', RetrieveYFsForUserView.as_view(), name='retrieve_yss_for_user'),
]
