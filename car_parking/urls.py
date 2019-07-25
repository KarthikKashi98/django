from django.conf.urls import url
from django.contrib import admin
# import testview from sample_app/view
from assignment1.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # create url for test view r’^ indicates global path, after this path we gonna add

    url(r'^testview/', test_view),
    url(r'^parking/', sample_db_test),
]