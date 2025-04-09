acl = int(input("Ingrese el número de ACL IPv4: "))

if acl >= 1 and acl <= 99:
    print("Es una ACL Estándar.")
elif acl >= 100 and acl <= 199:
    print("Es una ACL Extendida.")
else:
    print("El número no corresponde a una ACL válida.")

