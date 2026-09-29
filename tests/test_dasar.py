"""Tests kalkulator-elektro v2.

Nilai ekspektasi diverifikasi dari jawaban Soal Sistem Transmisi:
  Soal 2: Pr repeater = -5,98 dBm ; Soal 3: C = 7,98 Mbps, M = 16.
"""
import math

from kalkulator_elektro import (
    dbm_ke_mw, mw_ke_dbm, dbm_ke_watt, watt_ke_dbm, awg_ke_mm2,
    snr_db_ke_linear, kapasitas_shannon, bit_per_simbol,
    level_optimal_shannon, link_budget,
    daya_semu, faktor_daya, daya_aktif, daya_reaktif,
    konversi, ke_dasar,
    db_daya, db_tegangan, dbm_ke_dbv, dbv_ke_dbm, dbuv_ke_dbv,
    dbi_ke_dbd,
    hukum_ohm, pembagi_tegangan, pembagi_arus, seri, paralel,
    resistor_warna, e_terdekat,
    reaktansi_kapasitif, reaktansi_induktif, impedansi,
    frekuensi_resonansi, v_ll_dari_ln, daya_3fasa,
    fspl_db, panjang_gelombang,
)


def test_konversi_dbm():
    assert dbm_ke_mw(0) == 1.0
    assert dbm_ke_mw(30) == 1000.0
    assert abs(mw_ke_dbm(1.0) - 0.0) < 1e-9
    assert abs(dbm_ke_watt(30) - 1.0) < 1e-9
    assert abs(watt_ke_dbm(1.0) - 30.0) < 1e-9


def test_awg():
    assert abs(awg_ke_mm2(12) - 3.31) < 0.05
    assert abs(awg_ke_mm2(10) - 5.26) < 0.05


def test_link_budget_soal2():
    pr = link_budget(6.02, losses_db=[12])
    assert abs(pr - (-5.98)) < 1e-9
    pr_akhir = link_budget(6.02, losses_db=[12, 10], gains_db=[35])
    assert abs(pr_akhir - 19.02) < 1e-9


def test_shannon_soal3():
    assert abs(snr_db_ke_linear(24) - 251.1886) < 1e-3
    c = kapasitas_shannon(1e6, 24)
    assert abs(c / 1e6 - 7.98) < 0.01
    assert level_optimal_shannon(1e6, 24) == 16
    assert bit_per_simbol(16) == 4.0


def test_segitiga_daya():
    s = daya_semu(1495, 1176)
    assert abs(s - 1902) < 2
    pf = faktor_daya(1495, s)
    assert abs(pf - 0.786) < 0.002
    assert abs(daya_aktif(s, pf) - 1495) < 2
    assert abs(daya_reaktif(s, pf) - 1176) < 2


def test_satuan_si():
    assert konversi(2.2, "kV", "V") == 2200.0
    assert abs(konversi(4700, "uF", "mF") - 4.7) < 1e-9
    assert abs(konversi(1, "MHz", "Hz") - 1e6) < 1e-3
    assert abs(konversi(3.3, "kohm", "ohm") - 3300) < 1e-6
    val, base = ke_dasar(2.2, "kV")
    assert val == 2200.0 and base == "V"


def test_desibel():
    assert abs(db_daya(100, 1) - 20) < 1e-9
    assert abs(db_tegangan(10, 1) - 20) < 1e-9
    # 0 dBm @50 ohm = 0.2236 V = -13.01 dBV
    assert abs(dbm_ke_dbv(0) - (-13.01)) < 0.02
    assert abs(dbv_ke_dbm(dbm_ke_dbv(0)) - 0) < 1e-6
    assert dbuv_ke_dbv(120) == 0
    assert abs(dbi_ke_dbd(5) - 2.85) < 1e-9


def test_dc():
    h = hukum_ohm(v=12, r=4)
    assert abs(h["I"] - 3.0) < 1e-9 and abs(h["P"] - 36.0) < 1e-9
    h2 = hukum_ohm(i=2, p=100)
    assert abs(h2["V"] - 50) < 1e-9 and abs(h2["R"] - 25) < 1e-9
    assert abs(pembagi_tegangan(12, 4, 8) - 8.0) < 1e-9
    assert abs(pembagi_arus(3, 4, 8) - 2.0) < 1e-9
    assert seri(10, 20, 30) == 60
    assert abs(paralel(10, 10) - 5.0) < 1e-9
    ohm, tol = resistor_warna(["kuning", "ungu", "merah", "emas"])
    assert ohm == 4700.0 and tol == 5
    assert e_terdekat(5000) == 4700


def test_ac():
    xc = reaktansi_kapasitif(50, 100e-6)
    assert abs(xc - 31.83) < 0.02
    xl = reaktansi_induktif(50, 0.1)
    assert abs(xl - 31.42) < 0.02
    z = impedansi(3, 4)
    assert abs(z["Z"] - 5.0) < 1e-9
    f0 = frekuensi_resonansi(10e-3, 100e-9)
    assert abs(f0 - 5032.9) < 1.0
    assert abs(v_ll_dari_ln(220) - 381.05) < 0.1
    assert abs(daya_3fasa(380, 10, 0.85) - 5594.4) < 1.0


def test_transmisi_baru():
    # FSPL 1 km @ 2400 MHz ~ 100.05 dB
    assert abs(fspl_db(1, 2400) - 100.05) < 0.05
    assert abs(panjang_gelombang(100e6) - 2.9979) < 0.001
