from django.db import models


# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=350)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
class item_orcamento(models.Model):
    valor = models.DecimalField(max_digits=10,decimal_places=2) #max_lengmax_digits=10, 
    #valor_previsto = models.BooleanField(default=True)
    #mes = models.IntegerChoices()
    categoria_escolha = [
        ('Receita', (
                ('Renda de Investimentos', 'Renda de Investimentos'),
                ('Salario de Hermann', 'Salario de Hermann'),
                ('Refeicao de Hermann', 'Refeicao de Hermann'),
                ('Salario de Carla', 'Salario de Carla'),
                ('Refeicao de Carla', 'Refeicao de Carla'),
                ('Processo do Alphaville', 'Processo do Alphaville'),
            )
        ),
        ('Despesa', (
                ('Financiamento Bancario','Financiamento Bancario'),
                ('Plano de Previdencia','Plano de Previdencia'),
                ('Empregada','Empregada'),
                ('NuBank Hermann','NuBank Hermann'),
                ('Nubank Carla','Nubank Carl'),
                ('Escola','Escola'),
                ('Seguro','Seguro'),
                ('Internet','Internet'),
                ('Energia Celpe','Energia Celpe'),
                ('Energia Cosern','Energia Cosern'),
                ('INSS','INSS'),
                ('Celular Hermann','Celular Hermann'),
                ('Celular Carla','Celular Carla'),
                ('Condominio Maria Borba','Condominio Maria Borba'),
                ('Condominio Alphaville','Condominio Alphaville'),
                ('IPTU+BOMB','IPTU+BOMB'),
                ('IPVA+MULTA','IPVA+MULTA'),
                ('Alimentacao','Alimentacao'),
                ('Agua/Esgoto Pipa','Agua/Esgoto Pipa'),
                ('Advogado/Outros','Advogado/Outros'),
                ('Transf. Conta Invest','Transf. Conta Invest'),
            )
        ),
    ]
    categoria  = models.CharField(
        max_length=50,
        choices=categoria_escolha,
    )