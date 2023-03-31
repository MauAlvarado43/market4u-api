"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from seed.app.routes import CartViewSet
from seed.app.routes import CategoryViewSet
from seed.app.routes import CompanyViewSet
from seed.app.routes import MessageViewSet
from seed.app.routes import OpinionViewSet
from seed.app.routes import PaymentViewSet
from seed.app.routes import ProductViewSet
from seed.app.routes import PurchaseViewSet
from seed.app.routes import SaleViewSet
from seed.app.routes import UserViewSet
from seed.app.routes import FileView

router = DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'opinions', OpinionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]