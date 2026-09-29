"""Konversi satuan umum dengan prefix SI.

Contoh: konversi(2.2, 'kV', 'V') -> 2200.0
Prefix yang didukung: p, n, u/µ, m, (tanpa), k, M, G, T.
Satuan dasar: V, A, W, VA, var, J, Wh, ohm, F, H, Hz, C, S, Wb.
"""
import math

PREFIX = {
    "p": 1e-12, "n": 1e-9, "u": 1e-6, "µ": 1e-6, "m": 1e-3,
    "": 1.0,
    "k": 1e3, "M": 1e6, "G": 1e9, "T": 1e12,
}

BASE_UNITS = ["Wh", "VA", "var", "ohm", "Wb", "Hz",
              "V", "A", "W", "J", "F", "H", "C", "S"]


def _urai(satuan):
    """Pecah 'kV' -> ('k', 'V'). Raise ValueError bila tidak dikenal."""
    s = satuan.strip().replace("Ω", "ohm").replace("µ", "u")
    for base in sorted(BASE_UNITS, key=len, reverse=True):
        if s == base:
            return "", base
        if s.endswith(base):
            pref = s[:-len(base)]
            if pref in PREFIX:
                return pref, base
    raise ValueError(f"satuan tidak dikenal: {satuan!r}")


def konversi(nilai, dari, ke):
    """Konversi nilai dari satu satuan ke satuan lain yang sejenis.

    Contoh: konversi(4700, 'uF', 'mF') -> 4.7
    """
    pref_dari, base_dari = _urai(dari)
    pref_ke, base_ke = _urai(ke)
    if base_dari != base_ke:
        raise ValueError(f"tidak sejenis: {dari!r} vs {ke!r}")
    dalam_dasar = nilai * PREFIX[pref_dari]
    return dalam_dasar / PREFIX[pref_ke]


def ke_dasar(nilai, satuan):
    """Ubah ke satuan dasar SI (mis. 2.2 kV -> 2200.0 V)."""
    pref, base = _urai(satuan)
    return nilai * PREFIX[pref], base


def daftar_satuan():
    """Daftar satuan dasar yang didukung."""
    return sorted(BASE_UNITS)
