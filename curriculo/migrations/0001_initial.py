# Generated by Django 3.0.8 on 2020-07-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='depoimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depoimento', models.TextField(max_length=200, verbose_name='Depoimento')),
                ('nome', models.CharField(max_length=25, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=25, verbose_name='Cargo')),
                ('empresa', models.CharField(max_length=50, verbose_name='Empresa')),
            ],
            options={
                'db_table': 'depoimentos',
            },
        ),
        migrations.CreateModel(
            name='experiencia_profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField(auto_now=True, verbose_name='Data Inicio')),
                ('dataFinal', models.DateField(auto_now=True, verbose_name='Data Final')),
                ('atual', models.BooleanField(default=True, verbose_name='Emprego Atual?')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('descricaoFuncao', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descrição da função')),
            ],
            options={
                'db_table': 'experiencia_profissional',
            },
        ),
        migrations.CreateModel(
            name='formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100, verbose_name='Curso')),
                ('instituicao', models.CharField(max_length=100, verbose_name='Instituição de Ensino')),
                ('data_inicio', models.DateField(auto_now=True, verbose_name='Data Inicio')),
                ('data_conclusao', models.DateField(auto_now=True, verbose_name='Data Conclusão')),
                ('imagem', models.DateField(auto_now=True, null=True, verbose_name='Certificado')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link Certificado')),
            ],
            options={
                'db_table': 'formacao',
            },
        ),
        migrations.CreateModel(
            name='link_social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300, verbose_name='Link Social')),
            ],
            options={
                'db_table': 'link_social',
            },
        ),
        migrations.CreateModel(
            name='projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.DateField(auto_now=True, null=True, verbose_name='Imagem do projeto')),
                ('nomeProjeto', models.CharField(max_length=100, verbose_name='Nome do Projeto')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('link_projeto', models.URLField(verbose_name='Link do Projeto')),
                ('link_codigo', models.URLField(verbose_name='Link do Codigo')),
            ],
            options={
                'db_table': 'projetos',
            },
        ),
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('nascimento', models.DateField(auto_now=True, null=True, verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('celular1', models.CharField(blank=True, max_length=11, null=True, verbose_name='Celular 1')),
                ('celular2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Celular 2')),
                ('email', models.EmailField(max_length=254)),
                ('foto_perfil', models.ImageField(upload_to='', verbose_name='Imagem Perfil')),
                ('nomeLinkSocial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.link_social', verbose_name='Link Social')),
            ],
            options={
                'db_table': 'pessoa',
            },
        ),
    ]
