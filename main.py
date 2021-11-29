from flask import Flask, render_template, request, redirect, flash
import controlador_proveedor
import controlador_producto
import controlador_usuario

app= Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/agregar_proveedor")
def formulario_agregar_proveedor():
    return render_template("agregar_proveedor.html")

@app.route("/guardar_proveedor", methods=["POST"])
def guardar_proveedor():
    nombre = request.form["nombre"]
    password = request.form["password"]
    controlador_proveedor.insertar_proveedor(nombre, password)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/proveedor")

#@app.route("/")
@app.route("/proveedor")
def proveedor():
    proveedores = controlador_proveedor.obtener_proveedor()
    return render_template("proveedor.html", proveedores=proveedores)

@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    controlador_proveedor.eliminar_proveedor(request.form["id"])
    return redirect("/proveedor")

@app.route("/formulario_editar_proveedor/<int:id>")
def editar_proveedor(id):
    # Obtener el proveedor por ID
    proveedor = controlador_proveedor.obtener_proveedor_por_id(id)
    return render_template("editar_proveedor.html", proveedor=proveedor)

@app.route("/actualizar_proveedor", methods=["POST"])
def actualizar_proveedor():
    id = request.form["id"]
    nombre = request.form["nombre"]
    password = request.form["password"]
    controlador_proveedor.actualizar_proveedor(nombre, password, id)
    return redirect("/proveedor")

#producto

@app.route("/agregar_producto")
def formulario_agregar_producto():
    proveedores = controlador_producto.obtener_proveedor_producto()
    return render_template("agregar_producto.html", proveedores=proveedores)

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_proveedor = request.form["id_proveedor"]
    controlador_producto.insertar_producto(nombre, precio, id_proveedor)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/producto")

#@app.route("/")
@app.route("/producto")
def producto():
    productos = controlador_producto.obtener_producto()
    return render_template("producto.html", productos=productos)

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_producto.eliminar_producto(request.form["id"])
    return redirect("/producto")

@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # Obtener el producto por ID
    proveedores = controlador_producto.obtener_proveedor_producto()
    producto = controlador_producto.obtener_producto_por_id(id)
    return render_template("editar_producto.html", producto=producto, proveedores=proveedores)

@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_proveedor = request.form["id_proveedor"]
    controlador_producto.actualizar_producto(nombre, precio, id_proveedor, id)
    return redirect("/producto")

#usuario

@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    return render_template("agregar_usuario.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    password = request.form["password"]
    ciudad = request.form["ciudad"]
    controlador_usuario.insertar_usuario(nombre, apellido, correo, password, ciudad)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuario")

#@app.route("/")
@app.route("/usuario")
def usuario():
    usuarios = controlador_usuario.obtener_usuario()
    return render_template("usuario.html", usuarios=usuarios)

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_usuario.eliminar_usuario(request.form["id"])
    return redirect("/usuario")

@app.route("/formulario_editar_usuario/<int:id>")
def editar_usuario(id):
    # Obtener el usuario por ID
    usuario = controlador_usuario.obtener_usuario_por_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    password = request.form["password"]
    ciudad = request.form["ciudad"]
    controlador_usuario.actualizar_usuario(nombre, apellido, correo, password, ciudad, id)
    return redirect("/usuario")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)