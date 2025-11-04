# Sistema de Gestão de Benefícios - FACOM/UFU (SGB)

> **Projeto de TCC (Trabalho de Conclusão de Curso) apresentado à Faculdade de Computação (FACOM) da Universidade Federal de Uberlândia (UFU).**

O SGB é um sistema web desenvolvido para centralizar, gerenciar e dar transparência aos registros de concessões de benefícios (como diárias, passagens e inscrições em eventos) oferecidos a servidores e alunos da Faculdade de Computação.

O sistema possui duas frentes principais:
1.  Uma **Área Pública** de consulta, permitindo que qualquer pessoa filtre e visualize os dados consolidados.
2.  Uma **Área Administrativa** restrita para gestão completa (CRUD) de todos os dados de apoio e concessões.

---

## ✨ Principais Funcionalidades

O sistema foi modelado com base em um levantamento de requisitos detalhado, definindo dois atores principais: o **Público Geral** (externo) e o **Administrador/Técnico** (interno).

### Funcionalidades Públicas (`public_list.html`)
* **Consulta Pública:** Página aberta para visualização de todas as concessões.
* **Filtragem Avançada:** Permite filtrar os dados por:
    * Período (Data de Início e Fim)
    * Tipo de Benefício
    * Centro de Custo
    * Fonte de Recurso
    * Nome do Beneficiário
* **Exportação de Dados:** Funcionalidade para exportar os dados filtrados para um arquivo `.csv`.
* **Interface Responsiva:** O layout se adapta a dispositivos móveis, construído com Bootstrap 5.

### Funcionalidades Administrativas (Área Restrita)
* **Login Seguro:** Autenticação de usuários para acesso à área de gerenciamento.
* **Dashboard Personalizado:** Interface de administração customizada com **Django Jazzmin** para uma experiência de usuário intuitiva.
* **Gestão de Concessões (CRUD):** Controle total para criar, ler, atualizar e deletar registros de concessões.
* **Gestão de Dados de Apoio (CRUD):** Controle total das tabelas de apoio:
    * Beneficiários
    * Tipos de Benefício
    * Centros de Custo
    * Fontes de Recurso
* **Gerenciamento de Usuários:** Administração de usuários e grupos de permissão.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Backend:**
    * **Python**
    * **Django:** Framework principal para o desenvolvimento web.
* **Frontend:**
    * **HTML5**
    * **CSS3** (com arquivos estáticos personalizados)
    * **Bootstrap 5:** Framework CSS para design responsivo e componentes de UI.
    * **Bootstrap Icons:** Biblioteca de ícones.
    * **Django Templates (DTL):** Para renderização dinâmica das páginas.
* **Banco de Dados:**
    * **SQLite 3:** Banco de dados padrão do Django utilizado no desenvolvimento.
* **Admin & Pacotes:**
    * **Django Admin:** Interface de administração nativa.
    * **Django Jazzmin:** Tema moderno para customizar o Django Admin.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/thaisdam/sgb.git](https://github.com/thaisdam/sgb.git)
    cd sgb
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv

    # Se o comando 'activate' abaixo falhar, execute isto primeiro:
    # (Isso permite que o PowerShell execute scripts locais nesta sessão)
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    
    .\.venv\Scripts\activate
    
    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário** (para acessar a área de admin):
    ```bash
    python manage.py createsuperuser
    ```
    *(Siga as instruções para criar seu usuário e senha)*

6.  **Execute o servidor:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o sistema:**
    * **Página Pública:** `http://127.0.0.1:8000/concessoes/`
    * **Área Admin:** `http://127.0.0.1:8000/admin/`

---

## 👤 Autor

**Thais Damasceno Silva**
* **GitHub:** [thaisdam](https://github.com/thaisdam)
* **LinkedIn:** [https://www.linkedin.com/in/thaisdam/]
