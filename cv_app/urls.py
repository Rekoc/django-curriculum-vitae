from django.conf.urls import url
from cv_app import views


urlpatterns = [
    url(r'^$', views.cv, name='cv'),
    url(r'^about', views.about, name='about'),
    url(r'^skills_detailed', views.skills_detailed, name='skillss_detailed'),
    url(r'^skills', views.skills, name='skills'),
    url(r'^experience', views.experience, name='experience'),
    url(r'^education', views.education, name='education'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog')
]
