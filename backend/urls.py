
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from backend import customerviews



# CustomerRouter = DefaultRouter()
# CustomerRouter.register(r'user/category/$', customerviews.Workers.as_view()),



# WorkerRouter = DefaultRouter()



urlpatterns = [
    re_path(r'user/category/$', customerviews.Workers.as_view()),
    path('user/worker/<int:pk>/', customerviews.WorkerProfile.as_view()),
    # path('worker/', include(WorkerRouter.urls)),

]