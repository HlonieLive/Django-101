from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views import View



# Create your views here.
class genre(generic.ListView):
    template_name = 'genre/indextemplate.html'
    context_object_name = 'all_collections'

    def get_queryset(self):
        return Collection.objects.all()
    

class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailstemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pitem'] = Piece.objects.filter(collection_id=self.kwargs['pk'])
        return context
    
class UserFormView(generic.TemplateView):
    form_class = UserForm
    template_name = 'genre/adminform.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            newuser = authenticate(username=username, password=password)
            
            if newuser is not None:
                if newuser.is_active:
                    login(request, newuser)
                    return redirect('/genre')
        
        return render(request, self.template_name, {'form': form})