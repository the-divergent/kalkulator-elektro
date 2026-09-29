"""Segitiga daya: P (watt), Q (var), S (VA), dan faktor daya."""
import math


def daya_semu(p_watt, q_var):
    """Daya semu S (VA) dari P dan Q: S = sqrt(P^2 + Q^2)."""
    return math.hypot(p_watt, q_var)


def faktor_daya(p_watt, s_va):
    """Faktor daya (cos phi) = P / S."""
    if s_va == 0:
        raise ValueError("S tidak boleh nol")
    return p_watt / s_va


def daya_aktif(s_va, pf):
    """Daya aktif P (watt) = S * cos(phi)."""
    return s_va * pf


def daya_reaktif(s_va, pf):
    """Daya reaktif Q (var) = S * sin(phi), dengan sin dari pf."""
    if not 0 <= abs(pf) <= 1:
        raise ValueError("faktor daya harus di rentang 0-1")
    return s_va * math.sqrt(1 - pf ** 2)


def sudut_dari_pf(pf):
    """Sudut phi (derajat) dari faktor daya: phi = arccos(pf)."""
    if not 0 <= abs(pf) <= 1:
        raise ValueError("faktor daya harus di rentang 0-1")
    return math.degrees(math.acos(pf))
