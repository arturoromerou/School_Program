from pymongo import MongoClient, errors
from errors import escribir_al_log

######## CONEXION Y DESCONEXION DE MONGODB ########
class ConexionMDB:
    def __init__(self, cadena_cx, base_datos, alumnos, profesores):
        try:
            self.client = MongoClient(
                cadena_cx
            )
            self.db = self.client[base_datos]
            self.alumnos = self.db[alumnos]
            self.profesores = self.db[profesores]
            print(f"Conexion Exitosa!")
        except errors.ConnectionFailure as e:
            escribir_al_log(
                e,
                f"ocurrio un error al conectarse a la BD MongoDB {base_datos}"
            )
    # DESCONEXION #
   # def __del__(self):
    #   self.client.close()

################## INSERTAR DOCUMENTO ##################        
    def insertar_alumnos(self, datos_documento):
        resultado = None
        try:
            respuesta = self.alumnos.insert_one(
                datos_documento
            )
            resultado = respuesta.inserted_id
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                f"Ocurrio un fallo al insertar el  estudiante a la coleccion {datos_documento}"
            )
        return resultado

################## INSERTAR PROFESOR ##################        
    def insertar_profesor(self, datos_documento):
        resultado = None
        try:
            respuesta = self.profesores.insert_one(
                datos_documento
            )
            resultado = respuesta.inserted_id
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                f"Ocurrio un fallo al insertar el  profesor a la coleccion {datos_documento}"
            )
        return resultado

################## VER ALUMNOS EN SISTEMA ##################
    def alumnos_sistema(self):
        for x in self.alumnos.find():
            print(x)

################## VER PROFESORES EN SISTEMA ##################
    def profesores_sistema(self):
        for x in self.profesores.find():
            print(x)