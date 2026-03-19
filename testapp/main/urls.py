from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.RecordList.as_view(), name='index'),
   path('directory', views.DirectoryList.as_view(), name='directory'),

   path('createRecord', views.RecordAdd.as_view(), name='createRecord'),
   path('recordUpdate/<int:pk>', views.RecordUpdate.as_view(), name='updateRecord'),
   path('recordDelete/<int:pk>', views.RecordDelete.as_view(), name='deleteRecord'),

   path('createType/', views.CreateType.as_view(), name='createType'),
   path('updateType/<int:pk>', views.UpdateType.as_view(), name='updateType'),
   path('deleteType/<int:pk>', views.DeleteType.as_view(), name='deleteType'),

   path('createCategory/', views.CreateCategory.as_view(), name='createCategory'),
   path('updateCategory/<int:pk>', views.UpdateCategory.as_view(), name='updateCategory'),
   path('deleteCategory/<int:pk>', views.DeleteCategory.as_view(), name='deleteCategory'),

   path('createSubcategory/', views.CreateSubcategory.as_view(), name='createSubcategory'),
   path('updateSubcategory/<int:pk>', views.UpdateSubcategory.as_view(), name='updateSubcategory'),
   path('deleteSubcategory/<int:pk>', views.DeleteSubcategory.as_view(), name='deleteSubcategory'),

   path('createStatus/', views.CreateStatus.as_view(), name='createStatus'),
   path('updateStatus/<int:pk>', views.UpdateStatus.as_view(), name='updateStatus'),
   path('deleteStatus/<int:pk>', views.DeleteStatus.as_view(), name='deleteStatus'),

   path('getCategories', views.get_categories, name='getCategories'),
   path('getSubcategories', views.get_subcategories, name='getSubcategories')
]
