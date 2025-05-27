# 📦 Catálogo de Produtos

Este projeto é um sistema simples de **catálogo de produtos** desenvolvido em **Python** com banco de dados **MySQL**. Ele está em fase de desenvolvimento e tem como objetivo registrar, listar e gerenciar produtos de forma prática via terminal.

## 🚧 Status do Projeto

🔧 **Em desenvolvimento** — funcionalidades básicas estão sendo implementadas e novas melhorias virão nas próximas versões.

## 🛠 Tecnologias utilizadas

- **Python 3**
- **MySQL**
- **MySQL Connector/Python**
- Git & GitHub

## ✅ Funcionalidades atuais

- Inserir novos produtos (nome, preço, estoque)
- Listar todos os produtos cadastrados

## 📌 Requisitos para rodar

- Python instalado
- MySQL instalado e em execução
- Banco de dados criado com a tabela `produtos`

SQL para criar o banco:
```sql
CREATE DATABASE catalogo_produtos;

USE catalogo_produtos;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    preco FLOAT,
    estoque INT
);
```

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/InatanCs/catalogo-produtos.git
```

2. Instale o conector MySQL para Python:
```bash
pip install mysql-connector-python
```

3. Execute o script no terminal:
```bash
python nome_do_arquivo.py
```

## 📋 Próximas etapas

- [ ] Atualizar produtos
- [ ] Deletar produtos
- [ ] Interface gráfica (talvez)
- [ ] Melhorar validações de entrada

## 👨‍💻 Autor

Desenvolvido por [Inatan Colares Seixas](https://github.com/InatanCs) 🚀  
Projeto criado para estudos e prática em Python + MySQL.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e contribuir!
