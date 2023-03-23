from rest_framework_nested import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register("products", views.ProductViewSet)

product_router = routers.NestedDefaultRouter(router, "products", lookup='product')
product_router.register("ratings", views.RatingViewSet, basename = "rating")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls))
    
]

# products/1/ratings/1 

# pk

# product_pk
