from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Usuarios
from .forms import UsuarioForm

# Create your views here.

# View para listar todos os usuários
class UsuarioListView(ListView):
    model = Usuarios
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

# View para criar um novo usuário
class UsuarioCreateView(CreateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário criado com sucesso!')
        return super().form_valid(form)

# View para editar um usuário existente
class UsuarioUpdateView(UpdateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)

# View para excluir um usuário
class UsuarioDeleteView(DeleteView):
    model = Usuarios
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Usuário excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
