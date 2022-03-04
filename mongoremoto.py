

import pymongo


from persona import*
myclient = pymongo.MongoClient("mongodb+srv://admin:admin@miprimercluster.ityon.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["ControlAnimalDB"]
mycol = mydb["DatosPersonaAnimal"]
class mongoremote(Persona):
        

    def insertarenmongo(self):
        persona1=Persona()
        persona1.nombre = input("ingresa nombre: ")
        persona1.apellido_paterno = input("ingresa apellido paterno: ")
        persona1.apellido_materno =input("ingresa apellido materno: ")
        persona1.edad =int(input("ingresa edad: "))
        persona1.sexo =input("ingresa sexo: ")
        persona1.tipo=input("ingresa tipo de mascota: ")
        persona1.nombre_mascota=input("ingresa nombre de tu mascota: ")
        mydict={"Nombre":persona1.nombre,"Apellido_paterno":persona1.apellido_paterno,"Apellido_materno":persona1.apellido_materno,"Edad":persona1.edad,"Sexo":persona1.sexo,"Mascotas":{"Tipo":persona1.tipo,"Nombre_mascota":persona1.nombre_mascota}}
        self=mycol.insert_one(mydict)
        print("Registro Exitoso")
    def mostrar(self):
        mycol=mydb["DatosPersonaAnimal"]
        for x in mycol.find({},{"_id":0,"Nombre":1}):
           print (x)
    def eliminarenmongo(self):
        persona2=Persona()
        persona2.nombre=input("Que persona deseas eliminar: ")
        myquery={"Nombre":persona2.nombre}
        self=mycol.delete_one(myquery)
        print("Persona Eliminada Correctamente")
    def modificarenmongo(self):
        persona3=Persona()
        persona4=Persona()
        persona3.nombre=input("Que persona deseas modificar: ")
        myquery={"Nombre":persona3.nombre}
        persona4.nombre=input("ingresa nuevo nombre: ")
        persona4.apellido_paterno=input("ingresa nuevo apellido paterno: ")
        persona4.apellido_materno=input("ingresa nuevo apellido materno: ")
        persona4.edad=int(input("ingresa nueva edad: "))
        persona4.sexo=input("ingresa nuevo sexo: ")
       
        nuevos={"$set":{"Nombre":persona4.nombre,"Apellido_paterno":persona4.apellido_paterno,"Apellido_materno":persona4.apellido_materno,"Edad":persona4.edad,"Sexo":persona4.sexo}}
        mycol.update_one(myquery, nuevos)
        print("Persona Modificada Correctamente")
    def mostrarenmongo(self):
        persona5=Persona()
        persona5.nombre=input("Que persona deseas mostrar: ")
        myquery={"Nombre":persona5.nombre}
        mydoc=mycol.find(myquery)

        for x in mydoc:
            print(x)


    


    def menuMongo(self):
        continuar=True
        while(continuar):
         opcioncorrecta=False
         while not(opcioncorrecta):
             print("-----Menu-----")
             print("1 Insertar")
             print("2 Eliminar")
             print("3 Modificar")
             print("4 Consultar")
             print("5 Salir")
             opcion=int(input("Selecciona la opcion: "))
             if(opcion<1 or opcion>5):
                 print("Opcion no valida, ingresa otro numero")
             if(opcion==1):
                self.insertarenmongo()
             if(opcion==2):
                 self.mostrar()
                 self.eliminarenmongo()
             if(opcion==3):
                 self.mostrar()
                 self.modificarenmongo()
             if(opcion==4):
                 self.mostrarenmongo()          
             elif(opcion==5):
                 continuar=False
                 print("saliendo...")
                 break
             else:
                 opcioncorrecta=True
if __name__=='__main__':
    ip=mongoremote()
    ip.menuMongo()
