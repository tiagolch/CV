from django.db import models


class link_social(models.Model):
    link = models.CharField(max_length=300, verbose_name='Link Social')

    def __str__(self):
        return self.link

    class Meta:
        db_table = 'link_social'

class pessoa(models.Model):
    nomeCompleto = models.CharField(max_length=50, verbose_name='Nome Completo', blank=False, null=False)
    nascimento = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=200, verbose_name='Endereço',blank=False, null=False)
    celular1 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular 1')
    celular2 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular 2')
    email = models.EmailField()
    nomeLinkSocial = models.ForeignKey(link_social, on_delete=models.DO_NOTHING, verbose_name='Link Social')
    foto_perfil = models.ImageField(verbose_name='Imagem Perfil')

    def __str__(self):
        return self.nomeCompleto

    def get_data_nascimento(self):
        return self.nascimento.strftime('%d/%m/%Y')

    class Meta:
        db_table = 'pessoa'

class projetos(models.Model):
    imagem = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Imagem do projeto')
    nomeProjeto = models.CharField(max_length=100, verbose_name='Nome do Projeto', blank=False, null=False)
    descricao = models.TextField(max_length=300, verbose_name='Descrição', blank=False, null=False)
    link_projeto = models.URLField(verbose_name='Link do Projeto')
    link_codigo = models.URLField(verbose_name='Link do Codigo')

    def __str__(self):
        return self.nomeProjeto

    class Meta:
        db_table = 'projetos'

class experiencia_profissional(models.Model):
    dataInicio = models.DateField(auto_now=True, verbose_name='Data Inicio', blank=False, null=False)
    dataFinal = models.DateField(auto_now=True, verbose_name='Data Final', blank=False, null=False)
    atual = models.BooleanField(default=True, verbose_name='Emprego Atual?', blank=False, null=False)
    empresa = models.CharField(max_length=100, verbose_name='Empresa', null=False, blank=False)
    cargo = models.CharField(max_length=50, verbose_name='Cargo', blank=False, null=False)
    descricaoFuncao = models.TextField(max_length=300, verbose_name='Descrição da função', blank=True, null=True)

    def __str__(self):
        return self.empresa

    def get_data_inicio(self):
        return self.dataInicio.strftime('%d/%m/%Y')

    def get_data_final(self):
        return self.dataFinal.strftime('%d/%m/%Y')

    class Meta:
        db_table = 'experiencia_profissional'


class formacao(models.Model):
    curso = models.CharField(max_length=100, verbose_name='Curso', blank=False, null=False)
    instituicao = models.CharField(max_length=100, verbose_name='Instituição de Ensino', blank=False, null=False)
    data_inicio = models.DateField(auto_now=True, verbose_name='Data Inicio', blank=False, null=False)
    data_conclusao = models.DateField(auto_now=True, verbose_name='Data Conclusão', blank=False, null=False)
    imagem = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Certificado')
    link = models.URLField(blank=True, null=True, verbose_name='Link Certificado')

    def __str__(self):
        return self.curso

    def get_data_inicio(self):
        return self.data_inicio.strftime('%d/%m/%Y')

    def get_data_conclusao(self):
        return self.data_conclusao.strftime('%d/%m/%Y')

    class Meta:
        db_table = 'formacao'

class depoimentos(models.Model):
    depoimento = models.TextField(max_length=200, verbose_name='Depoimento')
    nome = models.CharField(max_length=25, verbose_name='Nome', blank=False, null=False)
    cargo = models.CharField(max_length=25, verbose_name='Cargo', blank=False, null=False)
    empresa= models.CharField(max_length=50, verbose_name='Empresa', blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'depoimentos'







