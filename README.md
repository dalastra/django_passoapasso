# Projeto Django - Sistema de Contatos

Este é um projeto desenvolvido com Django que possui um sistema simples de contatos, permitindo cadastrar mensagens e imagens através de um formulário.

---

## Funcionalidades

- Página inicial
- Formulário de contato
- Upload de imagens
- Listagem de contatos cadastrados
- API JSON com os contatos
- Validação de formulário
- Interface simples e minimalista

---

## Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- SQLite3

---

## Estrutura do Projeto

```bash
django_passoapasso/
│
├── config/               # Configurações do projeto Django
├── core/                 # Aplicação principal
│   ├── templates/        # Templates HTML
│   ├── static/           # Arquivos estáticos (CSS)
│   ├── models.py         # Modelos do banco
│   ├── views.py          # Views do sistema
│   ├── forms.py          # Formulários
│   └── urls.py           # Rotas
│
├── media/                # Uploads de imagens
├── db.sqlite3            # Banco de dados SQLite
└── manage.py             # Gerenciador do Django
```

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

### 2. Entre na pasta do projeto

```bash
cd django_passoapasso
```

---

### 3. Crie o ambiente virtual

```bash
python -m venv venv
```

---

### 4. Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

---

### 5. Instale as dependências

```bash
pip install django pillow
```

---

### 6. Execute as migrações

```bash
python manage.py migrate
```

---

### 7. Inicie o servidor

```bash
python manage.py runserver
```

---

## Acesse no navegador

```bash
http://127.0.0.1:8000/
```

---

## Rotas do projeto

| Rota | Descrição |
|------|------------|
| `/` | Página inicial |
| `/contato/` | Formulário de contato |
| `/contatos/` | Lista de contatos |
| `/contatos/json/` | API JSON |
| `/sucesso/` | Página de sucesso |

---

## Modelo do banco de dados

O sistema utiliza o modelo `Contato`:

```python
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='contatos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
```

---

## Objetivo do projeto

Este projeto foi criado para praticar:

- Django
- CRUD básico
- Formulários
- Upload de arquivos
- Templates
- Rotas
- Banco de dados SQLite
- Organização de projetos web

---

## Autor

Desenvolvido por Nicolas Campos Dalastra.
