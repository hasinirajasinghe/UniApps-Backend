from django.urls import path
from . import views

urlpatterns = [
    path('applicants/', views.ApplicantList.as_view(), name='applicant_list'),
    path('applicants/<int:id>/', views.ApplicantDetail.as_view(), name='applicant_detail'),
    path('applications/', views.ApplicationList.as_view(), name='application_list'),
    path('applications/<int:id>/', views.ApplicationDetail.as_view(), name='application_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('checkToken/', views.CheckToken.as_view(), name='checkToken'),
    path('majors/', views.get_all_majors, name='majors'),
    path('enrollment-statuses/', views.get_all_enrollment_status, name='enrollment_statuses'),
    path('terms/', views.get_all_terms, name='terms'),
    path('application-statuses/', views.get_all_application_status, name='application_statuses'),
]