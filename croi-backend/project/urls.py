from django.urls import path, include
from .views.viewsCategory import *
from .views.viewsMedia import *
from .views.viewsProject import *
from .views.viewsRequestForm import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'category_view', CategoryViewSet, basename='category_view')
router.register(r'project_view', ProjectViewSet, basename='project_view')
#router.register(r'project_view', CategoryViewSet, basename='project_view')
#router.register(r'request_view', CategoryViewSet, basename='request_view')

urlpatterns = [
    #path('category-view/', views.CategoryViewSet.as_view()),
    path('', include(router.urls))
]
