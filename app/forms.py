from django.forms import ModelForm
from myapp.models import Funcionarios

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ["funcionario", "funcao", "idade"]
#criando campos com funções de nome de funcionario, função e idade        