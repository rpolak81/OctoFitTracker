from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import views
import os


@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        scheme = 'https' if request.is_secure() else 'http'
        host = request.get_host()
        base_url = f"{scheme}://{host}/api/"
    return Response({
        'users':       base_url + 'users/',
        'teams':       base_url + 'teams/',
        'activities':  base_url + 'activities/',
        'workouts':    base_url + 'workouts/',
        'leaderboard': base_url + 'leaderboard/',
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',       views.users_list,       name='users-list'),
    path('api/teams/',       views.teams_list,       name='teams-list'),
    path('api/activities/',  views.activities_list,  name='activities-list'),
    path('api/workouts/',    views.workouts_list,    name='workouts-list'),
    path('api/leaderboard/', views.leaderboard_list, name='leaderboard-list'),
    path('',                 api_root,               name='api-root'),
]
