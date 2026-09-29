"""Rangkaian AC: reaktansi, impedansi, resonansi, sistem 3-fasa."""
import math


def reaktansi_kapasitif(f_hz, c_farad):
    """Xc (ohm) = 1 / (2*pi*f*C)."""
    if f_hz <= 0 or c_farad <= 0:
        raise ValueError("f dan C harus positif")
    return 1 / (2 * math.pi * f_hz * c_farad)


def reaktansi_induktif(f_hz, l_henry):
    """Xl (ohm) = 2*pi*f*L."""
    if f_hz <= 0 or l_henry <= 0:
        raise ValueError("f dan L harus positif")
    return 2 * math.pi * f_hz * l_henry


def impedansi(r_ohm, x_ohm):
    """Impedansi dari R dan X: -> {'Z': |Z|, 'sudut_derajat': phi}."""
    z = math.hypot(r_ohm, x_ohm)
    return {"Z": z, "sudut_derajat": math.degrees(math.atan2(x_ohm, r_ohm))}


def frekuensi_resonansi(l_henry, c_farad):
    """Frekuensi resonansi LC (Hz) = 1 / (2*pi*sqrt(L*C))."""
    if l_henry <= 0 or c_farad <= 0:
        raise ValueError("L dan C harus positif")
    return 1 / (2 * math.pi * math.sqrt(l_henry * c_farad))


def arus_ac(v_rms, z_ohm):
    """Arus AC (A rms) = V / |Z|."""
    return v_rms / z_ohm


# ---- Sistem 3-fasa ----
def v_ll_dari_ln(v_ln):
    """Tegangan line-to-line dari line-to-neutral: Vll = sqrt(3)*Vln."""
    return v_ln * math.sqrt(3)


def v_ln_dari_ll(v_ll):
    """Tegangan line-to-neutral dari line-to-line: Vln = Vll/sqrt(3)."""
    return v_ll / math.sqrt(3)


def daya_3fasa(v_ll, i_line, pf):
    """Daya aktif 3-fasa (W) = sqrt(3) * Vll * Il * pf."""
    return math.sqrt(3) * v_ll * i_line * pf


def arus_3fasa(p_watt, v_ll, pf):
    """Arus line 3-fasa (A) dari daya aktif."""
    return p_watt / (math.sqrt(3) * v_ll * pf)
