import mysql.connector

def conectar():  
    conexao = mysql.connector.connect(
        host="localhost",          
        user="root",                
        password="Senha",      
        database="catalogo_produtos"
    )
    return conexao  

def inserir_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    estoque = int(input("Quantidade em estoque: "))

    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO produtos(nome, preco, estoque) VALUES (%s, %s, %s)"
    valores = (nome, preco, estoque)

    cursor.execute(sql, valores)
    conn.commit()

    print("Produto inserido com sucesso!\n")

    cursor.close()
    conn.close()

def menu():
    while True:
        print("==MENU==")
        print("1. Inserir novo produto")
        print("2. Listar todos os produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    resultados = cursor.fetchall()

    if resultados:
        print("\n=== Lista de Produtos ===")
        for produto in resultados:
            id, nome, preco, estoque = produto
            print(f"ID: {id} | Nome: {nome} | Preço: R${preco:.2f} | Estoque: {estoque}")
    else:
        print("Nenhum produto encontrado.")
    
    cursor.close()
    conn.close()
    print("")

if __name__ == "__main__": 
    menu()
