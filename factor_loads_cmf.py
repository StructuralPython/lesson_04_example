def factor_loads(
    dead_load: float, 
    dead_load_factor: float, 
    live_load: float, 
    live_load_factor: float
) -> float:
    """
    Returns a float representing the factored load for the given
    load and load factors.
    """
    factored_load = dead_load * dead_load_factor + live_load * live_load_factor
    return factored_load
    
    
def cantilever_reactions(
    backspan: float, 
    cantilever: float, 
    udl_magnitude: float
) -> tuple[float]:
    """
    Returns a tuple representing the reactions R1 and R2 on a
    cantilever beam where R1 represents the "backspan" reaction
    and R2 represents the "cantilever" reaction.
    """
    equiv_pl = length * udl_magnitude
    acting_pl = length / 2
    R2 = equiv_pl * acting_pl / backspan
    R1 = equiv_pl - R2
    return (R1, R2)