def periodo_do_dia(timestamp): # função para categorizar o período do dia baseado no timestamp
    hora = timestamp.hour
    if 6 <= hora < 12:
        return 'MANHA'
    elif 12 <= hora < 18:
        return 'TARDE'
    elif 18 <= hora < 24:
        return 'NOITE'
    else:
        return 'MADRUGADA'
    

def menu(dataset_files): # função para imprimir o menu de opções para o usuário
    print("\nEscolha um dataset para análise:")
    for idx, file in enumerate(dataset_files, start = 1):
        print(f"{idx} - {file}")
    print("0 - Sair")
