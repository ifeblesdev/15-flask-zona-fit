from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)"
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                conexion.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id, )
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # Mapeo de clase-tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])            
            return cliente
        except Exception as e:
            print(f"Error al selecciona un cliente por id: {e}")
        finally:
            if conexion is not None:
                conexion.close()
                Conexion.liberar_conexion(conexion)                

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            if conexion is not None:
                conexion.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            if conexion is not None:
                conexion.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
        finally:
            if conexion is not None:
                conexion.close()
                Conexion.liberar_conexion(conexion)


if __name__ == "__main__":
    # # Insertar un nuevo cliente
    # nuevo_cliente = Cliente(nombre="Juan", apellido="Pérez", membresia=300)
    # resultado = ClienteDAO.insertar(nuevo_cliente)
    # if resultado:
    #     print(f"Cliente insertado: {nuevo_cliente}")
    # else:
    #     print("Error al insertar cliente")


    # # Actualizar un cliente existente
    # cliente_actualizado = Cliente(id=3, nombre="Alexa", apellido="Perez", membresia=400)   
    # resultado = ClienteDAO.actualizar(cliente_actualizado)
    # if resultado:
    #     print(f"Cliente actualizado: {cliente_actualizado} - {resultado} filas afectadas")
    # else:
    #     print("Error al actualizar cliente")

    # # Eliminar un cliente existente
    # cliente_eliminar = Cliente(id=3)  
    # resultado = ClienteDAO.eliminar(cliente_eliminar)
    # if resultado:
    #     print(f"Cliente eliminado: {cliente_eliminar} - {resultado} filas afectadas")
    # else:
    #     print("Error al eliminar cliente")


    # Seleccionar todos los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)