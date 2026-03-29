def odd_numbers(n: int) -> list[int]:
    """
    Retorna os números ímpares de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista de números ímpares
    """
    novaLista = []
    for i in range(n+1):
        if i % 2 > 0:
            novaLista.append(i)
    return novaLista
