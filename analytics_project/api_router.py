from rest_framework import routers
from sales.api import (
    ReportViewSet,
    SellerCreateListViewSet,
    BrandCreateListViewSet,
    ReportTypeCreateListViewSet
)


router = routers.DefaultRouter()
router.register('reports', ReportViewSet)
router.register('sellers', SellerCreateListViewSet)
router.register('brands', BrandCreateListViewSet)
router.register('report-types', ReportTypeCreateListViewSet)
urlpatterns = router.urls