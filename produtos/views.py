from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produto = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': produto})

def new_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'produto_form.html', {'forms': form})

def update_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'produto_form.html', {'forms': form})

def delete_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method =='POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'delete_confirm_produto.html', {'produtos': produto})

