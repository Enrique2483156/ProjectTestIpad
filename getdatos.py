from pymongo import MongoClient
from urllib.parse import quote_plus



usuario = "Sergioenriqueatencio"
contraseña = "developer@123"

usuario = quote_plus(usuario)
contraseña = quote_plus(contraseña) 

# Reemplaza con tu cadena de conexión
cadena_conexion = f"mongodb+srv://{usuario}:{contraseña}@testcluster.ljo9kqz.mongodb.net/CustomerDB?retryWrites=true&w=majority"

#esre es un comentario de test para saber si hace upload commit.


try:
    cliente = MongoClient(cadena_conexion, tls=True, tlsAllowInvalidCertificates=True)

    db = cliente['CustomerDB']  # Reemplaza 'test' con el nombre de tu base de datos
    coleccion = db['Employee']

    #for documento in coleccion.find({}):
    #   print(documento)

       # Solo prueba de conexión
    print("✅ Conexión exitosa a MongoDB Atlas")
    print("Bases de datos disponibles:", cliente.list_database_names())
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")


cliente.close()

