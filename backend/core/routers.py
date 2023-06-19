from rest_framework.routers import DefaultRouter, SimpleRouter
from authentication.views import UserViewset
from events.views import EventViewset
from admission.views import AdmissionViewset
from news.views import NewsViewset

router = DefaultRouter()
router.register("auth", UserViewset)
router.register("event", EventViewset)
router.register("adm", AdmissionViewset)
router.register("news", NewsViewset)
