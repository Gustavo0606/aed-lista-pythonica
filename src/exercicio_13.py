def shrink_guest_list(guests: list[str]) -> list[str]:
    """
    Reduz a lista para apenas dois convidados.

    Args:
        guests (list[str]): lista original

    Returns:
        list[str]: lista com apenas dois elementos
    """
    novaLista = []
    novaLista.append(guests[0])
    novaLista.append(guests[1])
    return novaLista
