from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ApiPostsViewSet, ApiCommentsViewSet
from .views import ApiGroupViewSet, ApiFollowViewSet

app_name = 'api'

router = SimpleRouter()

router.register(
    r'posts/(?P<post_id>\d+)/comments', ApiCommentsViewSet, basename='comment'
)
router.register('posts', ApiPostsViewSet)
router.register('groups', ApiGroupViewSet)
router.register('follow', ApiFollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    # path('v1/token/', include('djoser.urls')), # --- Требуется тестами именно v1/ эндпоинт
    # path('v1/token/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
