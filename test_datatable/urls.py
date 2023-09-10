from django.urls import path
from . import ajax_datatable_views
from . import views

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path('view/', views.view_data, name='view_data'),
    path('ajax_datatable/studies/', ajax_datatable_views.StudiesAjaxDatatableView.as_view(),
         name="ajax_datatable_studies"),

]