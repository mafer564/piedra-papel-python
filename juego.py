

print("Piedra papel o Python")
usuario=input("con que quiere jugar? piedra=0, papel=1 o Python=2")
opciones={
	"piedra"=="0"
	"papel"=="1"
	"Python"=="2"
}
import random
computadora=random.choice([0,2])
print("computadora: ",computadora)
print("usuario: ",usuario)
if computadora==usuario:
 	print("empate")

elif computadora ==2 and usuario==0:
	print("gana el usuario con: ", usuario, " a la computadora con: ",computadora)
elif computadora==0 and usuario==1:
	print("gana el usuario con: ",usuario,"a la computadora con: ",computadora)
elif computadora==1 and usuario==2:
	print("gana el usuario con: ",usuario, "a la computadora con: ",computadora)
else :
	print("gana la computadora con: ",computadora,"a el usuario con: ",usuario)


# if computadora==2 and usuario==0 or usuario==1:
	
# 	print("perdiste")



# if usuario==0:
# 	if computadora==1:
# 		print("perdiste")

# 	elif computadora==2:
# 		print("ganaste")

# if usuario==1:
# 	if computadora==0:
# 		print("ganaste")
# 	elif computadora==2:
# 		print("perdiste")

# if usuario==2:
# 	if computadora==0:
# 		print("perdiste")
# 	elif computadora==1:
# 		print("ganaste")






