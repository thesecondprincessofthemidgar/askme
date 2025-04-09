from my_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('question/<int:question_id>', views.question, name='one_question'),
    path('tag/<str:tag_name>', views.tag, name="tag"),
    path('not_found/', views.not_found, name="not_found"),
    path('settings/', views.settings, name='settings'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask_question, name="ask"),
]
