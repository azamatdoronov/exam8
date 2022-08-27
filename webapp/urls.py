from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import CreateReviewView, UpdateReview, DeleteReview

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review/add/', CreateReviewView.as_view(), name="product_review_create"),
    path('reviews/<int:pk>/update/', UpdateReview.as_view(), name="update_review"),
    path('reviews/<int:pk>/delete/', DeleteReview.as_view(), name="delete_review"),
]
