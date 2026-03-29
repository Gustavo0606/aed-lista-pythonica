def generate_numbers(n: int) -> list[int]:
    """
    Gera uma lista de números de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista [1, 2, ..., n]
    """
    novaLista = []
    for i in range(n):
        novaLista.append(i+1)
    return novaLista
