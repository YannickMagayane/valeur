from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,View,TemplateView
from .models import ArchiveCategory, PhysicalDocument, Archive
from .forms import ArchiveCategoryForm, PhysicalDocumentForm, ArchiveForm, ArchiveSearchForm
from django.contrib import messages


# Views for ArchiveCategory
class ArchiveCategoryCreateView(CreateView):
    model = ArchiveCategory
    form_class = ArchiveCategoryForm
    template_name = 'archivecategory_form.html'
    success_url = reverse_lazy('archivecategory_list')

class ArchiveCategoryUpdateView(UpdateView):
    model = ArchiveCategory
    form_class = ArchiveCategoryForm
    template_name = 'archivecategory_form.html'
    success_url = reverse_lazy('archivecategory_list')

class ArchiveCategoryDeleteView(DeleteView):
    model = ArchiveCategory
    template_name = 'archivecategory_confirm_delete.html'
    success_url = reverse_lazy('archivecategory_list')

class ArchiveCategoryListView(ListView):
    model = ArchiveCategory
    template_name = 'archivecategory_list.html'
    context_object_name = 'categories'
    
# Views for PhysicalDocument
class PhysicalDocumentCreateView(CreateView):
    model = PhysicalDocument
    form_class = PhysicalDocumentForm
    template_name = 'physicaldocument_form.html'
    success_url = reverse_lazy('physicaldocument_list')

class PhysicalDocumentUpdateView(UpdateView):
    model = PhysicalDocument
    form_class = PhysicalDocumentForm
    template_name = 'physicaldocument_form.html'
    success_url = reverse_lazy('physicaldocument_list')

class PhysicalDocumentDeleteView(DeleteView):
    model = PhysicalDocument
    template_name = 'physicaldocument_confirm_delete.html'
    success_url = reverse_lazy('physicaldocument_list')

class PhysicalDocumentListView(ListView):
    model = PhysicalDocument
    template_name = 'physicaldocument_list.html'
    context_object_name = 'documents'

# Views for Archive
class ArchiveCreateView(CreateView):
    model = Archive
    form_class = ArchiveForm
    template_name = 'archive_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Archive créée avec succès.')
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{field}: {error}')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('archive_success', kwargs={'pk': self.object.pk})
    

class ArchiveSuccessView(TemplateView):
    template_name = 'archive_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archive'] = Archive.objects.get(pk=self.kwargs['pk'])
        return context

class ArchiveUpdateView(UpdateView):
    model = Archive
    form_class = ArchiveForm
    template_name = 'archive_form.html'
    success_url = reverse_lazy('archive_list')

class ArchiveDeleteView(DeleteView):
    model = Archive
    template_name = 'archive_confirm_delete.html'
    success_url = reverse_lazy('archive_list')

class ArchiveSearchView(View):
    template_name = 'archive_search.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        if code:
            archive = Archive.objects.filter(code=code).first()
            if archive:
                return redirect('archive_detail', code=archive.code)
            else:
                messages.error(request, 'Ce document n\'existe pas.')
        return render(request, self.template_name)

class ArchiveDetailView(View):
    template_name = 'archive_detail.html'

    def get(self, request, code, *args, **kwargs):
        archive = get_object_or_404(Archive, code=code)
        return render(request, self.template_name, {'archive': archive})


class ArchiveListView(ListView):
    model = Archive
    template_name = 'archive_list.html'
    context_object_name = 'archives'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(date_registered__year=year)
        queryset = queryset.order_by('-date_registered')  # Tri par date la plus récente
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.request.GET.get('year')
        context['year'] = year
        return context