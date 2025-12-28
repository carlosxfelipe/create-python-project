import os
import platform
import shutil
import subprocess
import sys


def is_uv_installed() -> bool:
    """
    Verifica se o comando 'uv' está disponível no PATH.
    """
    return shutil.which("uv") is not None


def get_operating_system() -> str:
    """
    Detecta o sistema operacional.
    Retorna: 'windows', 'linux', 'macos' ou 'unknown'
    """
    system = platform.system().lower()

    if system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    elif system == "darwin":
        return "macos"
    else:
        return "unknown"


def run_command(command: str, cwd: str | None = None) -> None:
    """
    Executa um comando no shell e encerra o script em caso de erro.
    """
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as error:
        print(f"Erro ao executar o comando: {command}")
        sys.exit(error.returncode)


def install_uv_linux_macos() -> None:
    """
    Instala o uv em sistemas Linux ou macOS.
    """
    print("Instalando uv para Linux/macOS...")

    curl_command = "curl -LsSf https://astral.sh/uv/install.sh | sh"
    wget_command = "wget -qO- https://astral.sh/uv/install.sh | sh"

    if shutil.which("curl"):
        run_command(curl_command)
    elif shutil.which("wget"):
        run_command(wget_command)
    else:
        print("Nem curl nem wget estão instalados. Não é possível instalar o uv.")
        sys.exit(1)


def install_uv_windows() -> None:
    """
    Instala o uv no Windows usando PowerShell.
    """
    print("Instalando uv para Windows...")

    powershell_command = (
        "powershell -ExecutionPolicy ByPass -c "
        '"irm https://astral.sh/uv/install.ps1 | iex"'
    )

    run_command(powershell_command)


def install_uv() -> None:
    """
    Detecta o sistema operacional e instala o uv conforme necessário.
    """
    operating_system = get_operating_system()

    if operating_system in ("linux", "macos"):
        install_uv_linux_macos()
    elif operating_system == "windows":
        install_uv_windows()
    else:
        print("Sistema operacional não suportado.")
        sys.exit(1)


def ask_project_type() -> str:
    """
    Pergunta qual tipo de projeto o usuário deseja criar.
    """
    while True:
        print("\nQual tipo de projeto você deseja criar?")
        print("1 - Django")
        print("2 - FastAPI")

        choice = input("Escolha uma opção (1 ou 2): ").strip()

        if choice == "1":
            return "django"
        elif choice == "2":
            return "fastapi"
        else:
            print("Opção inválida. Tente novamente.")


def ask_project_name() -> str:
    """
    Pergunta o nome do projeto.
    """
    while True:
        project_name = input("Digite o nome do projeto: ").strip()

        if project_name:
            return project_name
        else:
            print("O nome do projeto não pode ser vazio.")


def create_dev_python_file(project_path: str, project_type: str) -> None:
    """
    Cria o arquivo dev.py para facilitar a execução do projeto.
    """
    if project_type == "django":
        command = "uv run python manage.py runserver"
    elif project_type == "fastapi":
        command = "uv run uvicorn main:app --reload"
    else:
        return

    dev_file_content = f"""import subprocess
import sys

def main() -> None:
    try:
        subprocess.run("{command}", shell=True, check=True)
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)

if __name__ == "__main__":
    main()
"""

    dev_file_path = os.path.join(project_path, "dev.py")

    with open(dev_file_path, "w", encoding="utf-8") as file:
        file.write(dev_file_content)


def create_django_project(project_name: str) -> None:
    """
    Cria e executa um projeto Django usando uv.
    """
    print(f"\nCriando projeto Django: {project_name}")

    run_command(f"uv init {project_name} --python 3.12")
    run_command("uv add django", cwd=project_name)
    run_command("uv run django-admin startproject config .", cwd=project_name)
    run_command("uv run python manage.py migrate", cwd=project_name)

    # Cria o arquivo dev.py
    create_dev_python_file(project_name, "django")

    print("\nProjeto Django criado com sucesso!")
    print("Iniciando servidor de desenvolvimento...\n")

    run_command("uv run python manage.py runserver", cwd=project_name)


def create_fastapi_main_file(project_path: str) -> None:
    """
    Cria o arquivo main.py básico para o FastAPI.
    """
    main_file_content = """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
"""
    main_file_path = os.path.join(project_path, "main.py")

    with open(main_file_path, "w", encoding="utf-8") as file:
        file.write(main_file_content)


def create_fastapi_project(project_name: str) -> None:
    """
    Cria e executa um projeto FastAPI usando uv.
    """
    print(f"\nCriando projeto FastAPI: {project_name}")

    run_command(f"uv init {project_name} --python 3.12")
    run_command("uv add fastapi uvicorn", cwd=project_name)

    # Cria automaticamente o main.py
    create_fastapi_main_file(project_name)

    # Cria o arquivo dev.py
    create_dev_python_file(project_name, "fastapi")

    print("\nProjeto FastAPI criado com sucesso!")
    print("Iniciando servidor de desenvolvimento...\n")

    run_command("uv run uvicorn main:app --reload", cwd=project_name)


def main() -> None:
    """
    Função principal do script.
    """
    if not is_uv_installed():
        print("O uv não está instalado.")
        install_uv()

        if not is_uv_installed():
            print("uv não encontrado no PATH. Reinicie o terminal e tente novamente.")
            sys.exit(1)

    print("uv está instalado e pronto para uso.")

    project_type = ask_project_type()
    project_name = ask_project_name()

    if project_type == "django":
        create_django_project(project_name)
    elif project_type == "fastapi":
        create_fastapi_project(project_name)


if __name__ == "__main__":
    main()
