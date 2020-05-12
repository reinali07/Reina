from django.urls import path
from . import views
app_name = 'runexp'
urlpatterns = [
    path('create-session',views.SessionCreateView.as_view(),name='session_create'),
    path('run-experiment/<str:filename>',views.ExperimentCreateView.as_view(),name='session'),
    path('',views.SessionListView.as_view(),name='index'),
    path('session/<str:filename>/',views.SessionDetails.as_view(),name='session_details'),
    path('session/<str:filename>/experiment/<uuid:eid>',views.ExperimentEditView.as_view(),name='experiment_edit'),
    path('session/<str:filename>/delete-experiment',views.delete_experiment,name='delete_experiment'),
    path('delete-sessions',views.delete_sessions,name='delete_sessions'),
    path('download-sessions',views.download_sessions,name='download_sessions'),
    path('run-experiment/<str:filename>/delete_current_session',views.delete_current_session,name='delete_current_session'),
    path('run-experiment/<str:filename>/download_current_session',views.download_current_session,name='download_current_session'),
    path('run-experiment/<str:filename>/run',views.run_experiment,name='run_experiment')
]