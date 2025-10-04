# 🇧🇷 DatabaseManager (pt-BR)

> 📘 Leia esse documento  em outros idiomas:  
> 🇺🇸 [English Version](#-databasemanager-en)

[![PyPI version](https://badge.fury.io/py/rpa-db-manager.svg)](https://pypi.org/project/rpa-db-manager/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**DatabaseManager** é uma biblioteca utilitária para **manipulação de bancos de dados e DataFrames de forma simples e integrada**, construída sobre **SQLAlchemy** e **pandas**.  

Ela fornece uma interface unificada para:
- Gerenciar conexões de banco de dados e tabelas ORM.
- Inserir dados de forma individual, em massa ou diretamente a partir de DataFrames.
- Executar consultas SQL simples.
- Manipular e padronizar DataFrames de maneira prática.

---

## 🚀 Instalação

```bash
pip install rpa-db-manager
```

Dependências:
- [SQLAlchemy](https://www.sqlalchemy.org/) >= 2.0.43  
- [pandas](https://pandas.pydata.org/) >= 2.3.3

---

## ⚡ Exemplo rápido

```python
import pandas as pd
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String
from db_manager import DatabaseManager, DataframeHandler

# Define base ORM
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)

# --- Gerenciamento de banco de dados ---
db_url = "sqlite:///example.db"
db = DatabaseManager(db_url, Base)

# Inserção individual
new_user = User(name="Alice", age=30)
db.insert_data(new_user)

# Inserção em massa via DataFrame
df = pd.DataFrame([
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 40},
])
db.bulk_insert_dataframe(df, User)

# Inserção direta com pandas.to_sql()
df2 = pd.DataFrame([
    {"id": 3, "name": "Daniel", "age": 35}
])
db.to_sql_dataframe(df2, "users", if_exists="append")

# Consulta
users = db.select_all(User)
print(users)

# --- Manipulação de DataFrames ---
handler = DataframeHandler()

# Normaliza nomes de colunas
df = pd.DataFrame({" First Name ": ["Ana"], "Last Name": ["Souza"]})
df = handler.normalize_column_names(df)
print(df.columns)  # ['first_name', 'last_name']

# Cria uma coluna de chave única
df = handler.create_unique_key_column(df, ["first_name", "last_name"])
print(df)
```

---

## 🛠️ Classes e Métodos

### 🧩 `DatabaseManager`
Classe para gerenciamento e manipulação de bancos de dados via SQLAlchemy.

#### Métodos principais

| Método | Descrição |
|--------|------------|
| `insert_data(model_instance)` | Insere uma instância ORM no banco de dados. |
| `bulk_insert_dataframe(df, model_cls)` | Insere um DataFrame inteiro via `bulk_insert_mappings`. |
| `to_sql_dataframe(df, table_name, if_exists="append")` | Insere DataFrame diretamente via `pandas.to_sql()`. |
| `select_all(model)` | Retorna todos os registros da tabela como lista de dicionários. |

---

### 🧮 `DataframeHandler`
Classe auxiliar para manipulação e padronização de DataFrames.

#### Métodos principais

| Método | Descrição |
|--------|------------|
| `normalize_column_names(df)` | Remove espaços, converte nomes de colunas para minúsculas e substitui espaços por `_`. |
| `create_unique_key_column(df, key_columns, new_column_name="unique_key")` | Cria uma nova coluna concatenando os valores de outras colunas (útil para gerar chaves únicas). |

---

## 📂 Estrutura mínima do projeto

```
src/
 └── database_manager/
      ├── __init__.py
      ├── db_manager.py
      └── dataframe_handler.py
```

---

## 📘 Roadmap
- [ ] Adicionar suporte assíncrono (AsyncSession com SQLAlchemy async).  
- [ ] Adicionar validações automáticas de schema.  
- [ ] Criar integração com bancos NoSQL (ex.: MongoDB, DuckDB).  

---

## 📜 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.


# 🇺🇸 DatabaseManager (EN)

> 📘 Read this document in other languages:  
> 🇧🇷 [Versão em Português (pt-BR)](#-databasemanager-pt-br)

[![PyPI version](https://badge.fury.io/py/rpa-db-manager.svg)](https://pypi.org/project/rpa-db-manager/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**DatabaseManager** is a utility library for **simple and integrated management of databases and DataFrames**, built on top of **SQLAlchemy** and **pandas**.  

It provides a unified interface to:
- Manage database connections and ORM models.
- Insert data individually, in bulk, or directly from DataFrames.
- Execute simple SQL queries.
- Manipulate and standardize DataFrames easily.

---

## 🚀 Installation

```bash
pip install rpa-db-manager
```

Dependencies:
- [SQLAlchemy](https://www.sqlalchemy.org/) >= 2.0  
- [pandas](https://pandas.pydata.org/) >= 2.0  

---

## ⚡ Quick Example

```python
import pandas as pd
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String
from db_manager import DatabaseManager, DataframeHandler

# Define ORM base
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)

# --- Database management ---
db_url = "sqlite:///example.db"
db = DatabaseManager(db_url, Base)

# Single insert
new_user = User(name="Alice", age=30)
db.insert_data(new_user)

# Bulk insert using DataFrame
df = pd.DataFrame([
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 40},
])
db.bulk_insert_dataframe(df, User)

# Direct insert using pandas.to_sql()
df2 = pd.DataFrame([
    {"id": 3, "name": "Daniel", "age": 35}
])
db.to_sql_dataframe(df2, "users", if_exists="append")

# Query
users = db.select_all(User)
print(users)

# --- DataFrame handling ---
handler = DataframeHandler()

# Normalize column names
df = pd.DataFrame({" First Name ": ["Ana"], "Last Name": ["Souza"]})
df = handler.normalize_column_names(df)
print(df.columns)  # ['first_name', 'last_name']

# Create a unique key column
df = handler.create_unique_key_column(df, ["first_name", "last_name"])
print(df)
```

---

## 🛠️ Classes and Methods

### 🧩 `DatabaseManager`
Class for managing and interacting with databases using SQLAlchemy.

#### Main Methods

| Method | Description |
|--------|-------------|
| `insert_data(model_instance)` | Inserts an ORM instance into the database. |
| `bulk_insert_dataframe(df, model_cls)` | Inserts an entire DataFrame via `bulk_insert_mappings`. |
| `to_sql_dataframe(df, table_name, if_exists="append")` | Inserts a DataFrame directly using `pandas.to_sql()`. |
| `select_all(model)` | Returns all table rows as a list of dictionaries. |

---

### 🧮 `DataframeHandler`
Helper class for manipulating and standardizing DataFrames.

#### Main Methods

| Method | Description |
|--------|-------------|
| `normalize_column_names(df)` | Removes spaces, converts column names to lowercase, and replaces spaces with underscores. |
| `create_unique_key_column(df, key_columns, new_column_name="unique_key")` | Creates a new column concatenating the values of other columns (useful for generating unique keys). |

---

## 📂 Minimal Project Structure

```
src/
 └── database_manager/
      ├── __init__.py
      ├── db_manager.py
      └── dataframe_handler.py
```

---

## 📘 Roadmap
- [ ] Add asynchronous support (AsyncSession with SQLAlchemy async).  
- [ ] Add automatic schema validation.  
- [ ] Create integration with NoSQL databases (e.g., MongoDB, DuckDB).  

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.