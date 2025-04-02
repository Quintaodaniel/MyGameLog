from db import inserir_jogo, listar_jogos

inserir_jogo(
    nome="The Witcher 3",
    plataforma="PC",
    genero="RPG",
    horas_jogadas=100,
    data_inicio="2024-03-01",
    ultima_sessao="2024-03-30",
    parei_quando="Finalizado",
    nota=9.5,
    observacoes="Ótima história e jogabilidade!"
)

listar_jogos()