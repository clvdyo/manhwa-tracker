from django.urls import path
from main.views import show_main, create_manhwa, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_manhwa, delete_manhwa, add_manhwa_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-manhwa', create_manhwa, name='create_manhwa'),
    path('edit-manhwa/<int:id>', edit_manhwa, name='edit_manhwa'),
    path('delete/<int:id>', delete_manhwa, name='delete_manhwa'),
    path('create-manhwa-ajax/', add_manhwa_ajax, name='add_manhwa_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]