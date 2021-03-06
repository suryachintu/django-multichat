from django.conf.urls import url
from event import views as event_views
from dashboard import views as dashboard_views

urlpatterns = [

	url(r'^create/$', event_views.create_event, name='create_event'),
	url(r'^(?P<event_id>\d+)/edit/$', event_views.edit_event, name='edit_event'),
	url(r'^(?P<event_id>\d+)/details/$', event_views.view_event, name='view_event'),
	url(r'^(?P<event_id>\d+)/qr/$',event_views.show_event_qr, name='view_event_qr'),
	url(r'^(?P<event_id>\d+)/dashboard/$',dashboard_views.view_dashboard, name='view_dashboard'),
	url(r'^(?P<event_id>\d+)/dashboard/questions/$',dashboard_views.session_data, name='session_data'),
	url(r'^(?P<event_id>\d+)/addquestion/$',event_views.add_question, name='add_question'),
	url(r'^toggleactive/(?P<question_id>\d+)$',event_views.toggle_status, name='toggle_status'),
]
