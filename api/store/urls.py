from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('promotions', views.PromotionViewSet)
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('carts', views.CartViewSet)
router.register('orders', views.OrderViewSet)

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='carts')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

order_router = routers.NestedDefaultRouter(router, 'orders', lookup='orders')
order_router.register('items', views.OrderItemViewSet, basename='order-items')

urlpatterns = router.urls + cart_router.urls + order_router.urls