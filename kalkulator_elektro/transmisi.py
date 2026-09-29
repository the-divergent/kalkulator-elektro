"""Kalkulator sistem transmisi: Shannon, modulasi M-ary, link budget."""
import math


def snr_db_ke_linear(snr_db):
    """SNR dari dB ke bentuk linier: SNR = 10^(SNRdB/10)."""
    return 10 ** (snr_db / 10)


def kapasitas_shannon(bandwidth_hz, snr_db):
    """Kapasitas kanal (bps) menurut teorema Shannon.

    C = B * log2(1 + SNR), dengan SNR dalam bentuk linier.
    """
    snr = snr_db_ke_linear(snr_db)
    return bandwidth_hz * math.log2(1 + snr)


def bit_per_simbol(m):
    """Jumlah bit per simbol untuk modulasi M-ary: log2(M)."""
    if m < 2:
        raise ValueError("M minimal 2")
    return math.log2(m)


def level_dari_bit(jumlah_bit):
    """Jumlah level sinyal M dari bit per simbol: M = 2^bit."""
    return 2 ** jumlah_bit


def level_optimal_shannon(bandwidth_hz, snr_db):
    """Level sinyal M optimal: samakan Nyquist dgn Shannon.

    2B*log2(M) = B*log2(1+SNR)  ->  M = 2^(0.5*log2(1+SNR)),
    dibulatkan ke pangkat 2 terdekat (4, 8, 16, ...).
    """
    m_ideal = 2 ** (0.5 * math.log2(1 + snr_db_ke_linear(snr_db)))
    # pangkat 2 terdekat
    pangkat = round(math.log2(m_ideal))
    return 2 ** max(pangkat, 1)


def link_budget(pt_dbm, losses_db=(), gains_db=()):
    """Daya terima (dBm) dari anggaran link.

    Pr = Pt - sum(rugi-rugi) + sum(gain).
    losses_db / gains_db: daftar nilai dB, mis. losses_db=[12, 10].
    """
    return pt_dbm - sum(losses_db) + sum(gains_db)


def fspl_db(jarak_km, frek_mhz):
    """Free-Space Path Loss (dB) = 20log10(d) + 20log10(f) + 32.44.

    jarak_km: jarak dalam kilometer, frek_mhz: frekuensi dalam MHz.
    """
    if jarak_km <= 0 or frek_mhz <= 0:
        raise ValueError("jarak dan frekuensi harus positif")
    return (20 * math.log10(jarak_km) + 20 * math.log10(frek_mhz)
            + 32.44)


def panjang_gelombang(frek_hz):
    """Panjang gelombang (meter) = c / f, c = 299.792.458 m/s."""
    if frek_hz <= 0:
        raise ValueError("frekuensi harus positif")
    return 299792458 / frek_hz


def frek_dari_lambda(panjang_m):
    """Frekuensi (Hz) dari panjang gelombang (meter)."""
    if panjang_m <= 0:
        raise ValueError("panjang gelombang harus positif")
    return 299792458 / panjang_m
