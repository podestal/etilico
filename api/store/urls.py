from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('promotions', views.PromotionViewSet)
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)
router.register('customers', views.CustomerViewSet)
router.register('carts', views.CartViewSet)
# router.register('cartItems', views.CartItemViewSet)
router.register('orders', views.OrderViewSet)
# router.register('products', views.ProductViewSet)


urlpatterns = router.urls