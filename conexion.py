from mysql.connector import pooling
from mysql.connector import Error
from contextlib import contextmanager




class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    HOST = 'localhost'  
    DB_PORT = '3306'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None


    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    port=cls.DB_PORT
                )
                return cls.pool
            except Error as e:  
                print(f"Error al conectar al obtener pool: {e}")    
        else:
            return cls.pool
        
        
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion = None
        try:
            conexion = cls.obtener_pool().get_connection()
            yield conexion
        finally:
            if conexion and conexion.is_connected():
                conexion.reset_session()

if __name__ == '__main__':
    # Ejemplo de uso
    pool = Conexion.obtener_pool()
    print(f"Pool de conexiones creado: {pool}")
    conexion1 = Conexion.obtener_conexion()
    print(f"Conexión obtenida: {conexion1}")
    Conexion.liberar_conexion(conexion1)
    print("Conexión liberada")