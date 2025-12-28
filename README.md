# Create Python Project

Este projeto é um utilitário interativo para criar rapidamente projetos Django ou FastAPI já configurados com o gerenciador de pacotes [uv](https://github.com/astral-sh/uv).

## Como executar

No terminal, execute o comando conforme seu sistema operacional:

- **Windows:**
  ```
  python create-python-project.py
  ```
- **Linux/macOS:**
  ```
  python3 create-python-project.py
  ```

Ou, em qualquer sistema, usando uv:

```
uv run create-python-project.py
```

## Opções disponíveis

Ao rodar o script, você poderá escolher:

- **1 - Django**: Cria um projeto Django já configurado e pronto para uso.
- **2 - FastAPI**: Cria um projeto FastAPI básico com um endpoint inicial.

Você também será solicitado a informar o nome do projeto.

## Sobre o arquivo `dev.py`

Após a criação do projeto, um arquivo `dev.py` será gerado dentro da pasta do projeto. Ele serve para facilitar a execução do servidor de desenvolvimento:

- Para projetos Django: executa `uv run python manage.py runserver`
- Para projetos FastAPI: executa `uv run uvicorn main:app --reload`

Basta rodar:

```
uv run dev.py
```

Assim, o servidor de desenvolvimento será iniciado rapidamente.

---

Este utilitário automatiza a configuração inicial de projetos Django e FastAPI, tornando o processo mais ágil e padronizado.
