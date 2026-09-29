# kalkulator-elektro v2.0

Utilitas teknik elektro dalam Python — dari konversi satuan sampai sistem transmisi — plus **web app** siap pakai.

Terinspirasi filosofi *small modules*: tiap fungsi mengerjakan satu hal dengan baik.

## Web App

Buka `docs/index.html` di browser (atau hosting via GitHub Pages) — kalkulator interaktif berbahasa Indonesia, responsif untuk HP:
- Konversi Satuan SI
- Desibel (dBm, dBV, rasio)
- DC: hukum Ohm, seri/paralel, pembagi tegangan
- Resistor: kode warna + E12
- AC & Daya: segitiga daya, 3-fasa, reaktansi, resonansi
- Transmisi: Shannon, link budget, FSPL

## Instalasi (library Python)

```bash
git clone https://github.com/the-divergent/kalkulator-elektro.git
cd kalkulator-elektro
```

Tanpa dependency eksternal — murni Python standar (3.8+).

## Pemakaian cepat

```python
from kalkulator_elektro import konversi, hukum_ohm, kapasitas_shannon, daya_3fasa

konversi(2.2, 'kV', 'V')          # 2200.0
konversi(4700, 'uF', 'mF')        # 4.7
hukum_ohm(v=12, r=4)              # {'V':12, 'I':3.0, 'R':4, 'P':36.0}
kapasitas_shannon(1e6, 24)        # 7.98e6 bps
daya_3fasa(380, 10, 0.85)         # ±5594 W
```

Lihat `contoh.py` untuk contoh lengkap.

## Modul (53 fungsi)

| Modul | Isi |
|---|---|
| `satuan` | `konversi` (prefix SI p–T), `ke_dasar`, `daftar_satuan` — V, A, W, J, Wh, ohm, F, H, Hz, C, S, Wb |
| `konversi` | `dbm_ke_mw`, `mw_ke_dbm`, `dbm_ke_watt`, `watt_ke_dbm`, `dbm_ke_dbw`, `dbw_ke_dbm`, `awg_ke_mm2`, `mm2_ke_awg` |
| `desibel` | `db_daya`, `db_tegangan`, `db_ke_rasio_daya`, `db_ke_rasio_tegangan`, `dbm_ke_dbv`, `dbv_ke_dbm`, `dbuv_ke_dbv`, `dbv_ke_dbuv`, `dbi_ke_dbd`, `dbd_ke_dbi` |
| `dc` | `hukum_ohm` (solver 2-dari-4), `pembagi_tegangan`, `pembagi_arus`, `seri`, `paralel`, `kapasitor_seri`, `kapasitor_paralel`, `resistor_warna`, `e_terdekat` |
| `ac` | `reaktansi_kapasitif`, `reaktansi_induktif`, `impedansi`, `frekuensi_resonansi`, `arus_ac`, `v_ll_dari_ln`, `v_ln_dari_ll`, `daya_3fasa`, `arus_3fasa` |
| `daya` | `daya_semu`, `faktor_daya`, `daya_aktif`, `daya_reaktif`, `sudut_dari_pf` |
| `transmisi` | `kapasitas_shannon`, `snr_db_ke_linear`, `bit_per_simbol`, `level_dari_bit`, `level_optimal_shannon`, `link_budget`, `fspl_db`, `panjang_gelombang`, `frek_dari_lambda` |

## Rumus acuan

- Shannon: `C = B · log2(1 + SNR)` · Nyquist: `C = 2B · log2(M)`
- Link budget: `Pr = Pt − Σ(rugi) + Σ(gain)`
- FSPL: `L = 20log10(d) + 20log10(f) + 32,44`
- Segitiga daya: `S = √(P² + Q²)`, `pf = P/S`
- 3-fasa: `P = √3 · Vll · Il · cos φ`
- Resonansi: `f₀ = 1/(2π√(LC))`
- AWG: `d(mm) = 0,127 · 92^((36−AWG)/39)`

## Tests

```bash
python3 -m pytest tests/ -v   # atau: python3 -c "import tests.test_dasar" manual
```
