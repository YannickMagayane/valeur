from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DeleteView
from django.urls import reverse_lazy

from .models import User

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ""
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.poste == 'administrateur':
                    login(request, user)
                    return redirect('user_list')
                elif user.poste == 'agent':
                    login(request,user)
                    return redirect ('unprocessed_repportinformation_list')
                
                elif user.poste == 'maire':
                    login(request,user)
                    return redirect ('repportinformation_mayor_list')
                
                elif user.poste == 'secretaire':
                    login(request,user)
                    return redirect ('repportinformation_secretary_list')
                elif user.poste == 'archiviste':
                    login(request,user)
                    return redirect ('repportinformation_archivist_list')
                
                else :
                    msg = " vous n'avez pas de poste"
                
            else:
                msg = 'Information invalide'
        else:
            msg = 'Email ou mot de passe invalide'
    else:
        msg = 'Erreur de validation'
    return render(request, 'login.html', {'form': form, 'msg': msg })


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            msg = 'Utilisateur créé'
            return redirect('login')
        else:
            msg = 'Informations invalides'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def get_object(self, queryset=None):
        # Assurez-vous que l'utilisateur ne peut pas se supprimer lui-même
        obj = super().get_object(queryset)
        if obj == self.request.user:
            raise PermissionDenied("Tu ne peux pas supprimer ton compte.") # type: ignore
        return obj