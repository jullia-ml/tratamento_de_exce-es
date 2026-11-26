try:
    PIX = (input("Insira sua chave PIX: "))
    if len(PIX) == 11:
        print("chave PIX validada")
    elif ((len(PIX)) > 11):
        raise ValueError("a chave PIX deve conter apenas 11 digitos")
    elif ((len(PIX)) < 11):
        raise ValueError("a chave PIX contem menos de 11 dígitos")

except ValueError as error:
    print(f"{error}: digite a chave PIX novamente")
    input("Chave PIX: ")
