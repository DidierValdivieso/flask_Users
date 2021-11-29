from bd import obtener_conexion


def insertar_producto(nombre, precio, id_proveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto(nombre, precio, id_proveedor) VALUES (%s, %s, %s)",
                       (nombre, precio, id_proveedor))
    conexion.commit()
    conexion.close()

def obtener_proveedor_producto():
    conexion = obtener_conexion()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM proveedor")
        proveedores = cursor.fetchall()
    conexion.close()
    return proveedores

def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT E2.id, E2.nombre, E2.precio, E1.nombre FROM proveedor E1 JOIN producto E2 ON E1.id = E2.id_proveedor")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT E2.id, E2.nombre, E2.precio, E1.id, E1.nombre FROM proveedor E1 JOIN producto E2 ON E2.id= %s AND E2.id_proveedor=E1.id", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_producto(nombre, precio, id_proveedor, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, id_proveedor = %s WHERE id = %s",
                       (nombre, precio, id_proveedor, id))
    conexion.commit()
    conexion.close()