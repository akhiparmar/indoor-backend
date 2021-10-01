
from django.urls import path, re_path

from backend import customerviews, workerviews



urlpatterns = [
    re_path(r'user/category/$', customerviews.Workers.as_view()),
    path('user/worker/<int:pk>/', customerviews.WorkerProfile.as_view()),
    path('user/worker/reviews/<int:pk>/', customerviews.WorkerReviews.as_view()),
    path('user/worker/book/', customerviews.BookWorker.as_view()),
    path('user/profile/', customerviews.Profile.as_view()),
    path('user/bookings/', customerviews.MyBookings.as_view()),



    path('worker/bookings/', workerviews.MyBookings.as_view()),
    path('worker/profile/', workerviews.Profile.as_view()),
    path('worker/customer/book/<int:pk>/', workerviews.BookCustomer.as_view()),


]