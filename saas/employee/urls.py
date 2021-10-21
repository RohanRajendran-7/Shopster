from django.contrib.auth.views import LoginView
from django.urls import path
from .views import Home,EmployeeDetail, CreateEmployee,UpdateEmployee,DeleteEmployee, UserLogin, VisitorHome, VisitorDetail,CreateVisitor,UpdateVisitor,DeleteVisitor
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', UserLogin.as_view(),name= 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'),name= 'logout'),
    path('', Home.as_view(),name= 'home'),
    path('visitor', VisitorHome.as_view(),name= 'visitor'),
    path('employee/<int:pk>', EmployeeDetail.as_view(),name= 'employee'),
    path('create-employee', CreateEmployee.as_view(),name= 'create-employee'),
    path('employee-update/<int:pk>', UpdateEmployee.as_view(),name= 'employee-update'),
    path('employee-delete/<int:pk>', DeleteEmployee.as_view(),name= 'employee-delete'),
    path('visitor/<int:pk>', VisitorDetail.as_view(),name= 'visitor'),
    path('create-visitor', CreateVisitor.as_view(),name= 'create-visitor'),
    path('visitor-update/<int:pk>', UpdateVisitor.as_view(),name= 'visitor-update'),
    path('visitor-delete/<int:pk>', DeleteVisitor.as_view(),name= 'visitor-delete'),
]
