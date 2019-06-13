from django.shortcuts import render
from .models import Board
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
# Create your views here.

def photo_list(request):
    #boards = Board.objects.all()
    all_board = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_board, 6)

    boards = paginator.get_page(page)
    return render(request,"index.html",{'boards':boards})



class PhotoDetailView(DetailView):
    model = Board
    template_name = 'detail.html'

