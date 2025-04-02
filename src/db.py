import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="usuario_jogos",
            password="DaQu@#1805",
            database="mygamelog"
        )
        print("Conexão bem sucedida!")
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    

def inserir_jogo(nome, genero, plataforma, horas_jogadas, data_inicio, ultima_sessao, parei_quando, nota, observacoes):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO jogos (nome, genero, plataforma, horas_jogadas, data_inicio, ultima_sessao, parei_quando, nota, observacoes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, genero, plataforma, horas_jogadas, data_inicio, ultima_sessao, parei_quando, nota, observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Jogo '{nome}' inserido com sucesso!")

    cursor.close()
    conexao.close()


def listar_jogos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()

    for jogo in jogos:
        print(jogo)

    cursor.close()
    conexao.close()