"""Kalkulator Elektro — utilitas kecil teknik elektro (v2.0).

Modul:
    satuan     : konversi satuan umum dengan prefix SI
    konversi   : dBm, watt, dBW, AWG <-> mm2
    desibel    : keluarga dB (dBm/dBW/dBV/dBuV/dBi/dBd)
    dc         : hukum Ohm, pembagi, seri/paralel, kode warna resistor
    ac         : reaktansi, impedansi, resonansi, sistem 3-fasa
    daya       : segitiga daya P (watt), Q (var), S (VA), faktor daya
    transmisi  : Shannon, M-ary, link budget, FSPL, panjang gelombang
"""

from .konversi import (
    dbm_ke_mw, mw_ke_dbm, dbm_ke_watt, watt_ke_dbm,
    dbm_ke_dbw, dbw_ke_dbm, awg_ke_mm2, mm2_ke_awg,
)
from .satuan import konversi, ke_dasar, daftar_satuan
from .desibel import (
    db_daya, db_tegangan, db_ke_rasio_daya, db_ke_rasio_tegangan,
    dbm_ke_dbv, dbv_ke_dbm, dbuv_ke_dbv, dbv_ke_dbuv,
    dbi_ke_dbd, dbd_ke_dbi,
)
from .dc import (
    hukum_ohm, pembagi_tegangan, pembagi_arus, seri, paralel,
    kapasitor_seri, kapasitor_paralel, resistor_warna, e_terdekat,
)
from .ac import (
    reaktansi_kapasitif, reaktansi_induktif, impedansi,
    frekuensi_resonansi, arus_ac,
    v_ll_dari_ln, v_ln_dari_ll, daya_3fasa, arus_3fasa,
)
from .transmisi import (
    snr_db_ke_linear, kapasitas_shannon, bit_per_simbol,
    level_dari_bit, level_optimal_shannon, link_budget,
    fspl_db, panjang_gelombang, frek_dari_lambda,
)
from .daya import (
    daya_semu, faktor_daya, daya_aktif, daya_reaktif, sudut_dari_pf,
)

__version__ = "2.0.0"
__all__ = [
    # konversi & satuan
    "dbm_ke_mw", "mw_ke_dbm", "dbm_ke_watt", "watt_ke_dbm",
    "dbm_ke_dbw", "dbw_ke_dbm", "awg_ke_mm2", "mm2_ke_awg",
    "konversi", "ke_dasar", "daftar_satuan",
    # desibel
    "db_daya", "db_tegangan", "db_ke_rasio_daya", "db_ke_rasio_tegangan",
    "dbm_ke_dbv", "dbv_ke_dbm", "dbuv_ke_dbv", "dbv_ke_dbuv",
    "dbi_ke_dbd", "dbd_ke_dbi",
    # dc
    "hukum_ohm", "pembagi_tegangan", "pembagi_arus", "seri", "paralel",
    "kapasitor_seri", "kapasitor_paralel", "resistor_warna", "e_terdekat",
    # ac
    "reaktansi_kapasitif", "reaktansi_induktif", "impedansi",
    "frekuensi_resonansi", "arus_ac",
    "v_ll_dari_ln", "v_ln_dari_ll", "daya_3fasa", "arus_3fasa",
    # transmisi
    "snr_db_ke_linear", "kapasitas_shannon", "bit_per_simbol",
    "level_dari_bit", "level_optimal_shannon", "link_budget",
    "fspl_db", "panjang_gelombang", "frek_dari_lambda",
    # daya
    "daya_semu", "faktor_daya", "daya_aktif", "daya_reaktif",
    "sudut_dari_pf",
]
