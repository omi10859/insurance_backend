from django.urls import path

from .views import UserPolicyListView, UserPolicyView, UserPolicyChartView

urlpatterns = [
    path('list/', UserPolicyListView.as_view()),
    path('detail/<int:pk>/', UserPolicyView.as_view()),
    path('chart/', UserPolicyChartView.as_view()),
]