@echo off
setlocal

:: Caminho absoluto do projeto
set "PROJETO_DIR=C:/Users/Willyan/PycharmProjects/RL_construcoes"

:: Caminho absoluto do Python
set "PYTHON_EXE=C:\Users\Willyan\AppData\Local\Programs\Python\Python312\python.exe"

:: Vai até o diretório do projeto
cd /d "%PROJETO_DIR%"

:: Verifica se o Python está instalado
"%PYTHON_EXE%" --version >nul 2>&1
if errorlevel 1 (
    echo Python não está instalado. Instale o Python e tente novamente.
    pause
    exit /b
)

:: Verifica se o ambiente virtual já existe
if not exist venv (
    echo Criando ambiente virtual...
    "%PYTHON_EXE%" -m venv venv
)

:: Ativa o ambiente virtual
call venv\Scripts\activate

:: Verifica se o arquivo requirements.txt existe
if not exist requirements.txt (
    echo requirements.txt não encontrado!
    pause
    exit /b
)

:: Instala os requisitos
echo Instalando dependências...
pip install --upgrade pip >nul
pip install -r requirements.txt

:: Aplica as migrações
echo Aplicando migrações...
python manage.py makemigrations
python manage.py migrate

:: Abre o navegador padrão
start http://localhost:8000

:: Inicia o servidor
echo Iniciando o servidor Django...
python manage.py runserver 0.0.0.0:8000

endlocal
