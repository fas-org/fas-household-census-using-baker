from django.conf.urls import url, include
from ..views import home_view

urlpatterns = [
    url(r'^$', home_view.init, name='home'),
    url(r'^introduction/', include('fas_questionnaire.urls.introduction_urls'))
]