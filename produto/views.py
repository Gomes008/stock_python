from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from produto.models import Produto


# Create your views here.


def lista(request):
    produto = Produto.objects.all()
    dados = {'produtos': produto}
    return render(request, 'produto.html', dados)


def adiciona(request):
    id_produto = request.GET.get('id')
    usuario = User.objects.all()
    dados = {'usuarios': usuario}
    if id_produto:
        dados['produto'] = Produto.objects.get(id=id_produto)
        prod = dados['produto']
        dados['user'] = User.objects.get(username=prod.responsavel)
    return render(request, 'adiciona.html', dados)


def adiciona_submit(request):
    if request.POST:
        id_produto = request.POST.get('id_produto')
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        responsavel = User.objects.get(id=request.POST["responsavel"])
        if id_produto:
            Produto.objects.filter(id=id_produto).update(nome=nome,
                                  quantidade=quantidade,
                                  valor=valor,
                                  responsavel=responsavel)
        else:
            Produto.objects.create(nome=nome,
                                   quantidade=quantidade,
                                   valor=valor,
                                   responsavel=responsavel)
    return redirect('/')


def apaga(request, id_produto):
    try:
        produto = Produto.objects.get(id=id_produto)
        produto.delete()
        return redirect('/')
    except Exception:
        raise Http404

