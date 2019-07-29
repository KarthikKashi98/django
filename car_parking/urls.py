from django.conf.urls import url
from django.contrib import admin
from src.views.userview import UserView
# import testview from sample_app/views
from assignment1.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # create url for test views r’^ indicates global path, after this path we gonna add

    url(r'^user/', UserView.as_view()),

]