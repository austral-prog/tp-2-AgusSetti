def change():
    expense = 23.75
    money = 100
    vuelto = money -  expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido:\n{money}")
    print("\n" + "\n" + "Vuelto")
    print(f"\n\n Pesos:\n {pesos}")
    print(f"Centavos:\n {centavos}")
