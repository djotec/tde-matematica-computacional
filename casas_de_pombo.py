def principio_casas_pombo(itens, grupos):
    if itens > grupos:
        minimo_no_mesmo_grupo = (itens // grupos) + (1 if itens % grupos != 0 else 0)
        return (
            f"Como há {itens} itens em {grupos} grupos, \n"
            f"pelo Princípio das Casas de Pombo, pelo menos um grupo terá "
            f"no mínimo {minimo_no_mesmo_grupo} itens."
        )
    else:
        return (
            f"Como há {itens} itens e {grupos} grupos, \n"
            "o princípio das casas de pombo NÃO GARANTE que algum grupo terá mais de um item."
        )
