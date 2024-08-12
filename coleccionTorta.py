import pymongo
from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017")

class MongoDBHandler:
    def __init__(self, database_name, collection_name, connection_string):
        self.client = MongoClient(connection_string)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def insert_document(self, document):
        self.collection.insert_one(document)

    def delete_document(self, filter):
        self.collection.delete_one(filter)

    def update_document(self, filter, update):
        self.collection.update_one(filter, {"$set": update})

    def get_documents(self, filter):
        return list(self.collection.find(filter))

def add_document(mongo_handler):
    name = input("Ingrese tipo de torta: ")
    age = int(input("Ingrese precio: "))

    document = {
        "name": name,
        "precio": age
    }

    mongo_handler.insert_document(document)
    print("Torta agregada.")

def delete_document(mongo_handler):
    name = input("Ingrese la torta a borrar: ")

    filter = {"name": name}
    mongo_handler.delete_document(filter)
    print("Torta borrada.")

def edit_document(mongo_handler):
    name = input("Ingrese el nombre de la torta a editar: ")
    new_age = int(input("Ingrese precio: "))

    filter = {"name": name}
    update = {"age": new_age}
    mongo_handler.update_document(filter, update)
    print("Torta editado.")

def main():
    connection_string = "mongodb://localhost:27017"
    database_name = "tiendaVirtual"
    collection_name = "tortas"

    mongo_handler = MongoDBHandler(database_name, collection_name, connection_string)

    while True:
        print("Menú de MongoDB")
        print("1. Agregar Torta")
        print("2. Borrar Torta")
        print("3. Editar Torta")
        print("4. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            add_document(mongo_handler)
        elif option == "2":
            delete_document(mongo_handler)
        elif option == "3":
            edit_document(mongo_handler)
        elif option == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()