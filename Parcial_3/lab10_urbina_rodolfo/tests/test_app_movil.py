"""Lab 10 - Pruebas unitarias automatizadas con pytest para Models/app_movil.py."""
import pytest

from Models.app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


# ---------------------------------------------------------------------------
# 1. Aislamiento de estado (fixtures)
# ---------------------------------------------------------------------------
@pytest.fixture
def perfil():
    """Instancia nueva y estandarizada de PerfilMovil para cada prueba."""
    return PerfilMovil("rodolfo")


@pytest.fixture
def perfil_pro():
    """Instancia nueva de PerfilPro con 3 meses de suscripción."""
    return PerfilPro("rodolfo_pro", meses_suscripcion=3)


# ---------------------------------------------------------------------------
# 2. Integridad estructural y aserciones
# ---------------------------------------------------------------------------
def test_valores_iniciales(perfil):
    assert perfil.username == "rodolfo"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma_al_saldo(perfil):
    assert perfil.ganar_gemas(25) == 75
    assert perfil.gemas == 75


def test_gastar_gemas_resta_del_saldo(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_gastar_todo_el_saldo_deja_cero(perfil):
    assert perfil.gastar_gemas(50) == 0


def test_transacciones_consecutivas(perfil):
    perfil.ganar_gemas(10)   # 60
    perfil.gastar_gemas(35)  # 25
    perfil.ganar_gemas(5)    # 30
    assert perfil.gemas == 30


def test_fixture_aisla_el_estado(perfil):
    # Si el estado se compartiera entre pruebas, aquí no habría 50 gemas
    assert perfil.gemas == 50


# ---------------------------------------------------------------------------
# 3. Validación de excepciones (pytest.raises)
# ---------------------------------------------------------------------------
def test_gemas_iniciales_negativas_lanza_value_error():
    with pytest.raises(ValueError):
        PerfilMovil("invalido", gemas=-1)


def test_gastar_mas_de_lo_disponible_lanza_error(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)
    assert perfil.gemas == 50  # el saldo no cambia tras el error


@pytest.mark.parametrize("cantidad", [0, -1, -100])
def test_gastar_cantidad_no_positiva_lanza_value_error(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


@pytest.mark.parametrize("meses", [0, -1])
def test_perfil_pro_con_meses_invalidos_lanza_value_error(meses):
    with pytest.raises(ValueError):
        PerfilPro("pro_invalido", meses_suscripcion=meses)


def test_descarga_con_suscripcion_expirada(perfil_pro):
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


# ---------------------------------------------------------------------------
# 4. Pruebas parametrizadas (valores límite en ganar_gemas)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "cantidad, esperado",
    [
        (1, 51),          # mínimo válido
        (10, 60),
        (50, 100),
        (999_950, 1_000_000),  # valor grande
    ],
)
def test_ganar_gemas_valores_validos(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_ganar_gemas_valores_invalidos(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)
    assert perfil.gemas == 50


# ---------------------------------------------------------------------------
# 5. Verificación de tipo y jerarquía (isinstance)
# ---------------------------------------------------------------------------
def test_perfil_pro_hereda_de_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfil_movil_no_es_pro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_perfil_pro_estado_inicial(perfil_pro):
    assert perfil_pro.es_pro is True
    assert perfil_pro.meses_suscripcion == 3
    assert perfil_pro.gemas == 50  # atributo heredado


def test_perfil_pro_usa_metodos_heredados(perfil_pro):
    assert perfil_pro.ganar_gemas(10) == 60
    assert perfil_pro.gastar_gemas(60) == 0


def test_ciclo_de_vida_perfil_pro(perfil_pro):
    # Activo: la descarga funciona
    assert "completada" in perfil_pro.descargar_contenido_offline()
    # Pasan los meses hasta expirar
    perfil_pro.meses_suscripcion -= 3
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False
    # Sigue siendo un PerfilPro y un PerfilMovil
    assert isinstance(perfil_pro, PerfilMovil)
