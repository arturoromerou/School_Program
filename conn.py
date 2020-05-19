from pymongo import MongoClient, errors
from errors import escribir_al_log

######## CONEXION Y DESCONEXION DE MONGODB ########
class ConexionMDB:
    def __init__(self, cadena_conexion, base_datos, coleccion):
        try:
            self.client = MongoClient(
                cadena_conexion
            )
            self.db = self.client[base_datos]
            self.coleccion = self.db[coleccion]
        except errors.ConnectionFailure as e:
            escribir_al_log(
                e,
                f"ocurrio un error al conectarse a la BD MongoDB {base_datos}"
            )

    def __del__(self):
        self.client.close()

################## INSERTAR DOCUMENTO ##################        
    def insertar_documento(self, registro):
        resultado = self.coleccion.insert_one(registro)
        print(f"se inserto un elemento a la coleccion {resultado.inserted_id}")
