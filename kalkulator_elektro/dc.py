"""Rangkaian DC: hukum Ohm, pembagi, seri/paralel, kode warna resistor."""
import math

# ---- Hukum Ohm: beri tepat 2 dari V, I, R, P -> dapat keempatnya ----
def hukum_ohm(v=None, i=None, r=None, p=None):
    """Selesaikan rangkaian DC dari 2 parameter yang diketahui.

    Contoh: hukum_ohm(v=12, r=4) -> {'V':12, 'I':3.0, 'R':4, 'P':36.0}
    """
    params = {"V": v, "I": i, "R": r, "P": p}
    diketahui = {k: x for k, x in params.items() if x is not None}
    if len(diketahui) != 2:
        raise ValueError("berikan tepat 2 dari V, I, R, P")
    for k, x in diketahui.items():
        if x <= 0:
            raise ValueError(f"{k} harus positif")

    V, I, R, P = v, i, r, p
    if V is not None and I is not None:
        R, P = V / I, V * I
    elif V is not None and R is not None:
        I, P = V / R, V ** 2 / R
    elif V is not None and P is not None:
        I, R = P / V, V ** 2 / P
    elif I is not None and R is not None:
        V, P = I * R, I ** 2 * R
    elif I is not None and P is not None:
        V, R = P / I, P / I ** 2
    else:  # R dan P
        I, V = math.sqrt(P / R), math.sqrt(P * R)
    return {"V": V, "I": I, "R": R, "P": P}


def pembagi_tegangan(v_in, r1, r2):
    """Tegangan pada R2: Vout = Vin * R2/(R1+R2)."""
    return v_in * r2 / (r1 + r2)


def pembagi_arus(i_total, r_target, r_lain):
    """Arus lewat r_target (paralel dgn r_lain): I = Itot * Rlain/(Rtarget+Rlain)."""
    return i_total * r_lain / (r_target + r_lain)


def seri(*nilai):
    """Total seri (R, L, C): jumlah langsung."""
    return sum(nilai)


def paralel(*nilai):
    """Total paralel: 1/(1/x1 + 1/x2 + ...). Untuk R dan L."""
    if any(x == 0 for x in nilai):
        raise ValueError("nilai nol tidak valid untuk paralel")
    return 1 / sum(1 / x for x in nilai)


def kapasitor_paralel(*nilai):
    """Kapasitor diparalel dijumlah langsung."""
    return sum(nilai)


def kapasitor_seri(*nilai):
    """Kapasitor diseri: 1/(1/C1 + 1/C2 + ...)."""
    return paralel(*nilai)


# ---- Kode warna resistor ----
WARNA_DIGIT = {
    "hitam": 0, "coklat": 1, "merah": 2, "oranye": 3, "kuning": 4,
    "hijau": 5, "biru": 6, "ungu": 7, "abu-abu": 8, "putih": 9,
}
WARNA_TOLERANSI = {"coklat": 1, "merah": 2, "emas": 5, "perak": 10}


def resistor_warna(pita):
    """Decode 3/4 pita warna -> (ohm, toleransi_persen).

    Contoh: resistor_warna(['kuning','ungu','merah','emas']) -> (4700.0, 5)
    """
    pita = [w.lower() for w in pita]
    if len(pita) == 3:
        pita = pita + ["emas"]  # default toleransi bila tak disebut
    if len(pita) != 4:
        raise ValueError("gunakan 3 atau 4 pita warna")
    d1, d2, pengali, tol = pita
    try:
        ohm = (WARNA_DIGIT[d1] * 10 + WARNA_DIGIT[d2]) * (10 ** WARNA_DIGIT[pengali])
    except KeyError as e:
        raise ValueError(f"warna tidak dikenal: {e}")
    toleransi = WARNA_TOLERANSI.get(tol)
    if toleransi is None:
        raise ValueError(f"warna toleransi tidak dikenal: {tol}")
    return float(ohm), toleransi


E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
E24 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39,
       43, 47, 51, 56, 62, 68, 75, 82, 91]


def e_terdekat(nilai, seri="E12"):
    """Nilai standar E-series terdekat dari suatu resistansi."""
    basis = E12 if seri.upper() == "E12" else E24
    if nilai <= 0:
        raise ValueError("nilai harus positif")
    orde = 10 ** math.floor(math.log10(nilai))
    kandidat = ([b * orde / 10 for b in basis] + [b * orde for b in basis]
                + [b * orde * 10 for b in basis])
    return min(kandidat, key=lambda x: abs(x - nilai))
