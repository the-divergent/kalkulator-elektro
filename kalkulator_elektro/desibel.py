"""Keluarga desibel: dB daya/tegangan, dBm, dBW, dBV, dBuV, dBi/dBd."""
import math


def db_daya(p1, p2):
    """Rasio daya dalam dB = 10*log10(P1/P2)."""
    return 10 * math.log10(p1 / p2)


def db_tegangan(v1, v2):
    """Rasio tegangan dalam dB = 20*log10(V1/V2)."""
    return 20 * math.log10(v1 / v2)


def db_ke_rasio_daya(db):
    """dB -> rasio daya linier."""
    return 10 ** (db / 10)


def db_ke_rasio_tegangan(db):
    """dB -> rasio tegangan linier."""
    return 10 ** (db / 20)


def dbm_ke_dbv(dbm, z_ohm=50):
    """dBm -> dBV pada impedansi Z (default 50 ohm).

    P(dBm) -> P(watt) -> V = sqrt(P*Z) -> dBV = 20*log10(V).
    """
    p_watt = (10 ** (dbm / 10)) / 1000
    v = math.sqrt(p_watt * z_ohm)
    return 20 * math.log10(v)


def dbv_ke_dbm(dbv, z_ohm=50):
    """dBV -> dBm pada impedansi Z (default 50 ohm)."""
    v = 10 ** (dbv / 20)
    p_watt = v ** 2 / z_ohm
    return 10 * math.log10(p_watt * 1000)


def dbuv_ke_dbv(dbuv):
    """dBuV -> dBV (selisih 120 dB)."""
    return dbuv - 120


def dbv_ke_dbuv(dbv):
    """dBV -> dBuV."""
    return dbv + 120


def dbi_ke_dbd(dbi):
    """Gain antena dBi -> dBd (dBd = dBi - 2.15)."""
    return dbi - 2.15


def dbd_ke_dbi(dbd):
    """Gain antena dBd -> dBi."""
    return dbd + 2.15
