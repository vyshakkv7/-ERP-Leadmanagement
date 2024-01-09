from django.urls import path
from smart_selects.views import ChainedSelectView, ChainedSelectMultiple

urlpatterns = [
    path('chained_select/', ChainedSelectView.as_view(), name='chained_filter'),
    path('chained_select_multiple/', ChainedSelectMultiple.as_view(), name='chained_filter_multiple'),
]