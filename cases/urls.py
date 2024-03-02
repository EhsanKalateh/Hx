from django.urls import path
from .views import (CasesListView,
                     CaseDetailView, 
                     CaseUpdateView, 
                     CaseDeleteView, 
                     CaseCreateView)


urlpatterns = [
    path("", CasesListView.as_view(), name="cases_list"),
    path("<slug:slug>/", CaseDetailView.as_view(), name="case_detail"),
    path("<slug:slug>/edit", CaseUpdateView.as_view(), name="case_edit"),
    path("<slug:slug>/delete", CaseDeleteView.as_view(), name="case_delete"),
    path("new", CaseCreateView.as_view(), name="case_new"),
    
]
