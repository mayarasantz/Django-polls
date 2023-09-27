from django.urls import path

# importar da pasta atual o arquivo views.py
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('pergunta/', views.exibe_questao, name='exibe_questao'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('perguntas/list', views.ultimas_perguntas, name='polls_list'),
    path('pergunta/add', views.QuestionCreateView.as_view(), name="poll_add"),

    path('cadastrar',
        views.QuestionCreateView.as_view(),
        name = 'question-create'
    ),

    path('pergunta/<int:pk>/edit',
        views.QuestionUpdateView.as_view(),
        name="poll_edit"
    ),


]

# .\venv\Scripts\activate.bat
# python manage.py runserser