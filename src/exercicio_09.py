def is_even(n: int) -> bool:
    """
    Verifica se um número é par.

    Args:
        n (int): número inteiro

    Returns:
        bool: True se for par, False caso contrário
    """
    par = False
    if n % 2 == 0:
        par = True
    else:
        par = False
    return par
