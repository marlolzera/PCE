from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from interface.forms import UsuarioForm
from interface.forms import UsuarioInfoForm


def log_in(request):
    msg_erro = '*Usuário ou Senha inválido'
    erro = False

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            # is_active é um campo da tabela auth_user, indica se o usuário foi "desligado" ou ainda existe
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                erro = True
        else:
            erro = True

    return render(request, 'interface/login.html', locals())


def log_out(request):
    logout(request)
    return redirect('/')


def nova_conta(request):
    usuario_form = UsuarioForm(data=request.POST)
    usuarioinfo_form = UsuarioInfoForm(data=request.POST)

    if request.method == 'POST':
        if usuario_form.is_valid() and usuarioinfo_form.is_valid():
            usuario = usuario_form.save()
            usuario.set_password(usuario.password)
            usuario.save()

            usuarioinfo = usuarioinfo_form.save(commit=False)
            usuarioinfo.user = usuario
            usuarioinfo.save()

            # loga o usuário cadastrado no sistema
            username = request.POST['username']
            password = request.POST['password']
            login(request, authenticate(username=username, password=password))

            return redirect('/home')
    else:
        usuario_form = UsuarioForm()
        usuarioinfo_form = UsuarioInfoForm()

    return render(request, 'interface/nova_conta.html',
                  {'usuario_form': usuario_form,
                   'usuarioinfo_form': usuarioinfo_form})
