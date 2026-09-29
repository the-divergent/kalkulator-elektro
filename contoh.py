"""Contoh pemakaian kalkulator-elektro.

Angka-angka di bawah diambil dari soal Sistem Transmisi (terverifikasi):
  - Soal 2: Pt = 6,02 dBm, rugi lintasan 12 dB -> Pr repeater = -5,98 dBm
  - Soal 3: B = 1 MHz, SNR = 24 dB -> C = 7,98 Mbps, M = 16
"""
from kalkulator_elektro import (
    kapasitas_shannon, level_optimal_shannon, link_budget,
    dbm_ke_watt, dbm_ke_mw, awg_ke_mm2, daya_semu, faktor_daya,
)

print("=== Soal 2: Link budget ===")
pr_rep = link_budget(6.02, losses_db=[12])
print(f"Daya diterima repeater : {pr_rep:.2f} dBm")
pr_akhir = link_budget(6.02, losses_db=[12, 10], gains_db=[35])
print(f"Daya di penerima akhir : {pr_akhir:.2f} dBm")
print(f"(-5,98 dBm = {dbm_ke_watt(-5.98)*1000:.4f} mW)")

print("\n=== Soal 3: Kapasitas Shannon ===")
c = kapasitas_shannon(1e6, 24)
print(f"Kapasitas kanal : {c/1e6:.2f} Mbps")
print(f"Level sinyal optimal : M = {level_optimal_shannon(1e6, 24)}")

print("\n=== Konversi satuan ===")
print(f"0 dBm  = {dbm_ke_mw(0):.1f} mW")
print(f"30 dBm = {dbm_ke_watt(30):.1f} watt")
print(f"AWG 12 = {awg_ke_mm2(12):.2f} mm^2")

print("\n=== Segitiga daya ===")
s = daya_semu(1495, 1176)
print(f"P=1495 W, Q=1176 var -> S = {s:.0f} VA, pf = {faktor_daya(1495, s):.3f}")
