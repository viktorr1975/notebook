from rest_framework.routers import DefaultRouter
from .views import NotesViewSet, GroupsViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter(trailing_slash=False)

app_name = "notesapp"


router.register(
    prefix="notes",
    viewset=NotesViewSet,
    basename="notes",
)
router.register(
    prefix="groups",
    viewset=GroupsViewSet,
    basename="groups",
)

urlpatterns = router.urls
