from biblioteca import Biblioteca
from libros import LibroFisico, Libro
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from usuarios import Estudiante, Profesor
from data import data_libros, data_estudiantes
from persistencia import Persistencia


persistencia = Persistencia()
biblioteca = persistencia.cargar_datos()

print("Bienvenido a Platzi Biblioteca")
print("Libros Disponibles:")

# Mostrar libros disponibles
for titulo in biblioteca.libros_disponibles():
    print(f"  -{titulo}")

print()

# Buscar usuario
cedula = input("Digite el numero cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.cedula, usuario.nombre)
except UsuarioNoEncontradoError as e:
    print(e)

# Buscar libro
titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que seleccionaste es {libro}")
except LibroNoDisponibleError as e:
    print(e)

# Solicitar libro
resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

# Prestar libro
try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)

# Guardar cambios
persistencia.guardar_datos(biblioteca)
