from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/signup', # caminho que vai carregar a view com o formulário
        views.AccountCreateView.as_view(),
        name="signup"
    ),

    path('', include('accounts.urls')), # rotas personalizadas como accounts/signup
    path('accounts/', include('django.contrib.auth.urls')), # rotas padrão fornecida pelo Django

]
