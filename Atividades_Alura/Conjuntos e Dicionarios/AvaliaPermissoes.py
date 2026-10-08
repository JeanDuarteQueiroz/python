def avaliaPermissao (lista1, lista2):
    if lista1.issuperset(lista2):
        return print("As permissões solicitadas fazem parte das permissões principais.")
    return print("As permissões solicitadas não fazem parte das permissões principais.")

lista_principal = set(p.strip() for p in input("Informe as permissões principais: ").lower().split(", "));
lista_secundaria = set(p.strip() for p in input("Informe as permissões secundarias: ").lower().split(", "));

avaliaPermissao(lista_principal,lista_secundaria);