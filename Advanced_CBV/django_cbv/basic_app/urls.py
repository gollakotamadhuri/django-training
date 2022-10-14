from django.urls import path

from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path("help/", views.HelpView.as_view(), name="help"),
    path("schools/", views.SchoolListView.as_view(),name="schools"),
    path("schools/<int:pk>", views.SchoolDetailsView.as_view(),name="school_details"),
    path("schools/create/",views.SchoolCreateView.as_view(),name="create"),
    path("schools/<int:pk>/update/", views.SchoolUpdateView.as_view(),name="update"),
    path("schools/<int:pk>/delete/", views.SchoolDeleteView.as_view(),name="delete")
]
