"""Konversi satuan kelistrikan: dBm, watt, dBW, dan AWG."""
import math


def dbm_ke_mw(dbm):
    """dBm -> miliwatt. Rumus: P(mW) = 10^(dBm/10)."""
    return 10 ** (dbm / 10)


def mw_ke_dbm(mw):
    """Miliwatt -> dBm. Rumus: dBm = 10*log10(P_mW)."""
    if mw <= 0:
        raise ValueError("daya harus positif")
    return 10 * math.log10(mw)


def dbm_ke_watt(dbm):
    """dBm -> watt."""
    return dbm_ke_mw(dbm) / 1000


def watt_ke_dbm(watt):
    """Watt -> dBm."""
    return mw_ke_dbm(watt * 1000)


def dbm_ke_dbw(dbm):
    """dBm -> dBW (referensi 1 watt)."""
    return dbm - 30


def dbw_ke_dbm(dbw):
    """dBW -> dBm."""
    return dbw + 30


def awg_ke_mm2(awg):
    """Nomor AWG -> luas penampang (mm^2).

    Diameter: d(mm) = 0.127 * 92^((36-AWG)/39), lalu A = pi*(d/2)^2.
    """
    if not 1 <= awg <= 40:
        raise ValueError("AWG standar berada di rentang 1-40")
    d_mm = 0.127 * (92 ** ((36 - awg) / 39))
    return math.pi * (d_mm / 2) ** 2


def mm2_ke_awg(luas_mm2):
    """Luas penampang (mm^2) -> nomor AWG standar terdekat (1-40)."""
    if luas_mm2 <= 0:
        raise ValueError("luas harus positif")
    terbaik, selisih_min = None, float("inf")
    for awg in range(1, 41):
        selisih = abs(awg_ke_mm2(awg) - luas_mm2)
        if selisih < selisih_min:
            terbaik, selisih_min = awg, selisih
    return terbaik
