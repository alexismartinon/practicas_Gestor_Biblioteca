class BibliotecaError(Exception):
    """Clase base para errores relacionados con la biblioteca."""
    pass


class LimitePrestamosError(BibliotecaError):
    """Se exedio el limite de prestamos permitidos"""


class TituloInvalidoError(BibliotecaError):
    """El titulo del libro no es valido"""
    pass


class LibroNoDisponibleError(BibliotecaError):
    """El libro no esta disponible para prestamo"""
    pass


class UsuarioNoEncontradoError(BibliotecaError):
    """El usuario no fue encontrado en el sistema"""
    pass
