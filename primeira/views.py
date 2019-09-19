from django.shortcuts import render, redirect
from . models import Produto
from . forms import ProdutoForm

def home(request):
    return render (request, 'home.html',)

def produto_list(request):
    if (request.method == 'POST'):
        form = request.POST.get('select')  
        produtos = Produto.objects.filter(categoria__icontains=form)
        return render(request, 'produto/list.html', {'produtos':produtos})
    else:
        produtos = Produto.objects.all()
        return render(request, 'produto/list.html', {'produtos':produtos})  


def produto_form(request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        form.save()
        return redirect('/primeira/produto/')
        
    else:
        form = ProdutoForm()
        return render(request, 'produto/form.html' ,{'form':form})


def produto_show(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    return render(request, 'produto/show.html',{'produto':produto})

def produto_editar(request, produto_id):
    if (request.method == 'POST'):
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(request.POST, instance =produto)
        if (form.is_valid()):
            form.save()
            return redirect ('/primeira/produto/')
        else:
            return render(request, 'produto/editar.html', {'form':form, 'produto_id': produto_id})
    else:
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(instance = produto)
        return render (request, 'produto/editar.html', {'form':form, 'produto_id':produto_id})

def produto_delete(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    produto.delete()
    return redirect('/primeira/produto/')
    

    













