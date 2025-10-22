# Ordena ignorando a diferença entre maiúsculas e minúsculas (de forma case-insensitive)

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
print(mercado)
mercado.sort(key=str.casefold)
print(mercado)
