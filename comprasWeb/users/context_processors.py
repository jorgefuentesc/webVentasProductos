from .forms import LoginUsuario,RegistroUsuario

def login_form(request):
    login_form = LoginUsuario()
    registro_form = RegistroUsuario()
    return{
        'loginForm': login_form,
        'registroForm': registro_form
    }