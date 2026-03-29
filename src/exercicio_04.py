def format_name(name: str) -> tuple[str, str, str]:
    """
    Retorna o nome em diferentes formatos.

    Args:
        name (str): nome de entrada

    Returns:
        tuple[str, str, str]: (lowercase, uppercase, titlecase)
    """
    nomeLower = name.lower()
    nomeUpper = name.upper()
    nomeTitle = name.title()
    return (nomeLower, nomeUpper, nomeTitle)
