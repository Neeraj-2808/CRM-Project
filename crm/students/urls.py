
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/',views.DashBoardView.as_view(),name='dashboard'),
    path('students-lists/',views.StudentsListView.as_view(),name='students-lists'),
    path('registration-form/',views.StudentRegistrationView.as_view(),name='registration-form'),
    path('course/',views.CourseView.as_view(),name='course'),
    path('batch/',views.BatchView.as_view(),name='batch'),
    path('student-detail/<str:uuid>/',views.StundentDetailsView.as_view(),name='student-detail'),
    path('student-delete/<str:uuid>/',views.StundentDeleteView.as_view(),name='student-delete'),
    path('student-update/<str:uuid>/',views.StudentUpdateView.as_view(),name='student-update'),

]
