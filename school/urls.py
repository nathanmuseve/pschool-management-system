from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import settings
from django.conf.urls import static
from django.conf import settings

#application name
app_name = "school"

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('philosopy/', views.philosopy, name='philosopy'),
    path('mission/', views.mission, name='mission'),
    path('vission/', views.vission, name='vission'),
    path('goal/', views.goal, name='goal'),
    path('values/', views.values, name='values'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('admission/', views.admission, name='admission'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('subjects/', views.subjects, name='subjects'),
    path('departments/', views.departments, name='departments'),
    path('student_portal/', views.student_portal, name='student_portal'),
    path('student_registration', views.student_registration, name='student_registration'),
    path('student_login/', views.student_login, name='student_login'),
    path('student_logout/', views.student_logout, name='student_logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('student_profile_update/', views.student_profile_update, name='student_profile_update'),
    path('student_pic_update/', views.student_pic_update, name='student_pic_update'),
    path('staff_portal/', views.staff_portal, name='staff_portal'),
    path('staff_registration/', views.staff_registration, name='staff_registration'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
    path('staff_profile_update/', views.staff_profile_update, name='staff_profile_update'),
    path('staff_pic_update/', views.staff_pic_update, name='staff_pic_update'),
    path('non_staff_portal/', views.non_staff_portal, name='non_staff_portal'),
    path('non_staff_registration/', views.non_staff_registration, name='non_staff_registration'),
    path('non_staff_login/', views.non_staff_login, name='non_staff_login'),
    path('non_staff_logout/', views.non_staff_logout, name='non_staff_logout'),
    path('non_staff_profile_update', views.non_staff_profile_update, name='non_staff_profile_update'),
    path('non_staff_pic_update', views.non_staff_pic_update, name='non_staff_pic_update'),
    path('Marks', views.Marks, name='Marks'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

