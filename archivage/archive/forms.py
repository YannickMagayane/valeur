from django import forms
from .models import ArchiveCategory, PhysicalDocument, Archive,RepportInformation

class ArchiveCategoryForm(forms.ModelForm):
    class Meta:
        model = ArchiveCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
        }

class PhysicalDocumentForm(forms.ModelForm):
    class Meta:
        model = PhysicalDocument
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'description': forms.Textarea(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
        }

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = [ 'name','nom_propietaire','adresse', 'document', 'physical_document']
        widgets = {
           
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'nom_propietaire': forms.TextInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'adresse': forms.TextInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'document': forms.FileInput(attrs={'class': 'mt-1 block w-full'}),
            'physical_document': forms.Select(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
        }

class ArchiveSearchForm(forms.Form):
    code = forms.CharField(max_length=50, label='Document Code', widget=forms.TextInput(attrs={'class': 'form-input'}))



class RepportInformationForm(forms.ModelForm):
    class Meta:
        model = RepportInformation
        fields = [ 'detail', 'content_page', 'photo_document']
        widgets = {
            #'user': forms.Select(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'detail': forms.Textarea(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'content_page': forms.NumberInput(attrs={'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'photo_document': forms.FileInput(attrs={'class': 'mt-1 block w-full'}),
        }