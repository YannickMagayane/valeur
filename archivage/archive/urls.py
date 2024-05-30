from django.urls import path
from .views import (
    ArchiveCategoryCreateView, ArchiveCategoryUpdateView, ArchiveCategoryDeleteView, ArchiveCategoryListView,
    PhysicalDocumentCreateView, PhysicalDocumentUpdateView, PhysicalDocumentDeleteView, PhysicalDocumentListView,
    ArchiveCreateView, ArchiveUpdateView, ArchiveDeleteView, ArchiveSearchView, ArchiveListView,ArchiveDetailView,ArchiveSuccessView
)

urlpatterns = [
    # URLs for ArchiveCategory
    path('archivecategory/add/', ArchiveCategoryCreateView.as_view(), name='archivecategory_add'),
    path('archivecategory/<int:pk>/edit/', ArchiveCategoryUpdateView.as_view(), name='archivecategory_edit'),
    path('archivecategory/<int:pk>/delete/', ArchiveCategoryDeleteView.as_view(), name='archivecategory_delete'),
    path('archivecategory/', ArchiveCategoryListView.as_view(), name='archivecategory_list'),

    # URLs for PhysicalDocument
    path('physicaldocument/add/', PhysicalDocumentCreateView.as_view(), name='physicaldocument_add'),
    path('physicaldocument/<int:pk>/edit/', PhysicalDocumentUpdateView.as_view(), name='physicaldocument_edit'),
    path('physicaldocument/<int:pk>/delete/', PhysicalDocumentDeleteView.as_view(), name='physicaldocument_delete'),
    path('physicaldocument/', PhysicalDocumentListView.as_view(), name='physicaldocument_list'),

    # URLs for Archive
    path('archive/add/', ArchiveCreateView.as_view(), name='archive_add'),
    path('archive/<int:pk>/edit/', ArchiveUpdateView.as_view(), name='archive_edit'),
    path('archive/<int:pk>/delete/', ArchiveDeleteView.as_view(), name='archive_delete'),
    path('', ArchiveSearchView.as_view(), name='archive_search'),
    path('archive/', ArchiveListView.as_view(), name='archive_list'),
    path('archive/detail/<str:code>/', ArchiveDetailView.as_view(), name='archive_detail'),
    path('archive/success/<int:pk>/', ArchiveSuccessView.as_view(), name='archive_success'),


]
