# RL Construções Elétricas

Sistema em Django para cadastro de clientes, gerenciamento de documentos e contas a pagar/receber.

## Como iniciar

1. Instale as dependências:
   pip install -r requirements.txt

2. Crie as tabelas:
   python manage.py makemigrations
   python manage.py migrate

3. Rode o servidor:
   python manage.py runserver 0.0.0.0:8000

Acesse via navegador em:
   http://localhost:8000
Ou, via rede local (descubra seu IP local):
   http://192.168.0.100:8000 (exemplo)

## Scripts de Inicialização Automática no Windows

Crie um atalho com o comando:
```
cmd /k "cd C:\caminho\do\projeto && python manage.py runserver 0.0.0.0:8000"
```
E adicione esse atalho na pasta de inicialização automática do Windows.

## Alertas de contas

Para verificar quais contas possuem alerta na data atual, execute:
```
python manage.py verificar_alertas
```

## Gerar executável

É possível criar um executável do projeto com [PyInstaller](https://www.pyinstaller.org/). Após instalar o pacote, rode:
```
pyinstaller manage.py --name rl_construcoes --onefile
```
O executável gerado irá iniciar o Django e criar o banco de dados caso ainda não exista.
