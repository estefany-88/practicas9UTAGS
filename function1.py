usuario="admin"
pwds="123d*"
print("**Ingrese usuario y contraseña**")
print("Usuario: ")
user=input()
print("Contraseña: ")
pwd1=input()
if user==usuario and pwd1==pwds:
    print("Acceso correcto")
else:
    print("Usuario o contraseña incorrectos")
