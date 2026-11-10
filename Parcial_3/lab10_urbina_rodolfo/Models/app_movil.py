"""Lab 10 - Lógica de perfiles para una aplicación móvil (POO + excepciones)."""


# ---------------------------------------------------------------------------
# 1. Jerarquía de excepciones del dominio
# ---------------------------------------------------------------------------
class SuscripcionExpiradaError(Exception):
    """Se lanza al intentar una operación restringida sin membresía activa."""


class PuntosInsuficientesError(Exception):
    """Se lanza cuando una transacción supera el saldo de gemas disponible."""


# ---------------------------------------------------------------------------
# 2. Clase base
# ---------------------------------------------------------------------------
class PerfilMovil:
    """Perfil de usuario estándar de la aplicación móvil."""

    def __init__(self, username, gemas=50, racha_dias=1, notificaciones_activas=True):
        if gemas < 0:
            raise ValueError("Las gemas iniciales no pueden ser negativas.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        """Suma gemas al saldo. La cantidad debe ser estrictamente positiva."""
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a ganar debe ser mayor que cero.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        """Resta gemas del saldo después de verificar que alcancen."""
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a gastar debe ser mayor que cero.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Saldo insuficiente: tienes {self.gemas} gemas e intentas gastar {cantidad}."
            )
        self.gemas -= cantidad
        return self.gemas


# ---------------------------------------------------------------------------
# 3. Subclase derivada
# ---------------------------------------------------------------------------
class PerfilPro(PerfilMovil):
    """Perfil con suscripción Pro: hereda de PerfilMovil y agrega contenido offline."""

    def __init__(self, username, meses_suscripcion, gemas=50, racha_dias=1,
                 notificaciones_activas=True):
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial de suscripción debe ser mayor que cero.")
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        """Permite descargar contenido solo si la suscripción sigue vigente."""
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError(
                "Tu suscripción Pro expiró. Renueva para descargar contenido offline."
            )
        return f"Descarga offline completada para {self.username}."
