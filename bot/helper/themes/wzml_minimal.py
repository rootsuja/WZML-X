#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🎉 Repo 💯'
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = 'Updates 💯'
    ST_BN2_URL = 'https://t.me/WZML-X'
    ST_MSG = '''<i>Bot ini dapat menggandakan semua tautan|file|torrent Anda ke Google Drive atau cloud rclone apa pun atau ke telegram atau ke server ddl.</i>
    <b>Ketik 🔐 {help_command} untuk mendapatkan daftar perintah yang tersedia</b>'''
    ST_BOTPM = '''<i>Sekarang, Bot ini akan mengirim semua file dan tautan Anda ke sini. Mulai Menggunakan 🚀...</i>'''
    ST_UNAUTH = '''<i>Anda bukan pengguna yang berwenang! Luncurkan bot WZML-X Mirror-Leech Anda sendiri ✨</i>'''
    OWN_TOKEN_GENERATE = '''<b>Token Sementara bukan milik Anda!</b>\n\n<i>Silakan buat sendiri 🔨.</i>'''
    USED_TOKEN = '''<b>Token Sementara sudah digunakan!</b>\n\n<i>Silakan buat yang baru 🔄.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Sudah Masuk melalui Kata Sandi 🔒</b>\n\n<i>Tidak Perlu Menerima Token Temp.</i>'''
    ACTIVATE_BUTTON = 'Aktifkan Token Sementara 🔌'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
    <b>Temp Token:</b> <code>{token}</code>
    <b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Bot Sudah Masuk! 🎉</b>'
    INVALID_PASS = '<b>Kata Sandi Tidak Valid! 🔐</b>\n\nSilakan masukkan Kata Sandi yang benar .'
    PASS_LOGGED = '<b>Bot Berhasil Masuk Permanen! 💯</b>'
    LOGIN_USED = '<b>Cara Penggunaan Login Bot:</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Tampilkan Log'
    WEB_PASTE_BT = '📨 Tempel Web (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
   BASIC_BT = 'Basic ⚙️'
    USER_BT = 'Users 👤'
    MICS_BT = 'Mics 🎤'
    O_S_BT = 'Owner & Sudos 👑'
    CLOSE_BT = 'Tutup ❌'
    HELP_HEADER = "<b><i>Menu Panduan Bantuan!</i></b>\n\n<b>CATATAN: <i>Klik CMD apa saja untuk melihat detail minor lainnya.</i></b>"
    # async def stats(client, message):
    BOT_STATS = '''<b><i>STATISTIK BOT :</i></b>
    ┖ <b>Uptime Bot :</b> {bot_uptime} ⏱️

    ┎ <b><i>RAM (MEMORI) :</i></b>
    ┃ {ram_bar} {ram}% 🐏
    ┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

    ┎ <b><i>MEMORI SWAP :</i></b>
    ┃ {swap_bar} {swap}% 🔁
    ┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

    ┎ <b><i>DISK :</i></b>
    ┃ {disk_bar} {disk}% 💿
    ┃ <b>Total Disk Read :</b> {disk_read}
    ┃ <b>Total Disk Write :</b> {disk_write}
    ┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}

    
    '''
    SYS_STATS = '''<b><i>SISTEM OS :</i></b>
┠ <b>Uptime OS :</b> {os_uptime} ⏱️
┠ <b>Versi OS :</b> {os_version} 🖥️
┖ <b>Arsitektur OS :</b> {os_arch} 💻

<b><i>STATISTIK JARINGAN :</i></b>
┠ <b>Data Unggah:</b> {up_data} 🔼
┠ <b>Data Unduh:</b> {dl_data} 🔽
┠ <b>Paket Terkirim:</b> {pkt_sent}k 📨
┠ <b>Paket Diterima:</b> {pkt_recv}k 📥
┖ <b>Total Data I/O:</b> {tl_data} 📡

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}% 📊
┠ <b>Frekuensi CPU :</b> {cpu_freq} GHz
┠ <b>Beban Rata-Rata Sistem :</b> {sys_load} ⚖️
┠ <b>P-Core(s):</b> {p_core} | <b>V-Core(s):</b> {v_core}
┠ <b>Total Core(s):</b> {total_core} Cores
┖ <b>CPU Usable:</b> {cpu_use} %
    '''
    REPO_STATS = '''<b><i>STATISTIK REPO :</i></b>
┠ <b>Bot Diperbarui :</b> {last_commit} 🔨
┠ <b>Versi Saat Ini :</b> {bot_version} ⚙️
┠ <b>Versi Terbaru :</b> {lat_version} 🆕
┖ <b>Log Perubahan Terakhir :</b> {commit_details} 🗒️

<b>CATATAN :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''<b><i>BATASAN BOT :</i></b>
┠ <b>Batas Langsung :</b> {DL} GB 📥
┠ <b>Batas Torrent :</b> {TL} GB 🔗
┠ <b>Batas GDrive :</b> {GL} GB ☁️
┠ <b>Batas YT-DLP :</b> {YL} GB 🎥
┠ <b>Batas Daftar Putar :</b> {PL} 🎶
┠ <b>Batas Mega :</b> {ML} GB 💾
┠ <b>Batas Kloning :</b> {CL} GB 🎭
┖ <b>Batas Leech :</b> {LL} GB 🧲

┎ <b>Validitas Token :</b> {TV} ⏳
┠ <b>Batas Waktu Pengguna :</b> {UTI} / tugas ⏱️
┠ <b>Tugas Paralel Pengguna :</b> {UT} 🤹‍♂️
┖ <b>Tugas Paralel Bot :</b> {BT} 🤖
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b><i>Berhasil Dihidupkan Ulang!</i></b> 🎉
┠ <b>Tanggal:</b> {date} 📅
┠ <b>Waktu:</b> {time} 🕒
┠ <b>Zona Waktu:</b> {timz} 🌎
┖ <b>Versi:</b> {version} ⚙️'''
    RESTARTED = '''<b><i>Bot Dihidupkan Ulang!</i></b> 🔁'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Memulai Ping..</i> 🏓'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code> 💨'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Tugas Dimulai</i></b> 🚀
┠ <b>Mode:</b> {Mode} ⚙️
┖ <b>Oleh:</b> {Tag}\n\n"""
LINKS_SOURCE = """➲ <b>Sumber:</b>
┖ <b>Ditambahkan Pada:</b> {On} 📆
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =      "➲ <b><u>Tugas Dimulai :</u></b>\n┃\n┖ <b>Tautan:</b> <a href='{msg_link}'>Klik Di Sini</a> 🔗"
    L_LOG_START =      "➲ <b><u>Leech Dimulai :</u></b>\n┃\n┠ <b>Pengguna :</b> {mention} ( #ID{uid} )\n┖ <b>Sumber :</b> <a href='{msg_link}'>Klik Di Sini</a> 🔗"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =         '<b><i>{Name}</i></b>\n┃\n'
    SIZE =         '┠ <b>Ukuran: </b>{Size} ⚖️\n'
    ELAPSE =        '┠ <b>Waktu berlalu: </b>{Time} ⏱️\n'
    MODE =         '┠ <b>Mode: </b>{Mode} ⚙️\n'

    # ----- LEECH -------
    L_TOTAL_FILES =     '┠ <b>Total File: </b>{Files} 📁\n'
    L_CORRUPTED_FILES =   '┠ <b>File Rusak: </b>{Corrupt} 🚫\n'
    L_CC =         '┖ <b>Oleh: </b>{Tag}\n\n'
    PM_BOT_MSG =      '➲ <b><i>File(s) telah Dikirim di atas</i></b> 📤'
    L_BOT_MSG =       '➲ <b><i>File(s) telah Dikirim ke PM (Pribadi) Bot</i></b> 📥'
    L_LL_MSG =       '➲ <b><i>File(s) telah Dikirim. Akses melalui Tautan...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =        '┠ <b>Jenis: </b>{Mimetype}\n'
    M_SUBFOLD =       '┠ <b>SubFolder: </b>{Folder}\n'
    TOTAL_FILES =      '┠ <b>File: </b>{Files}\n'
    RCPATH =        '┠ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =         '┖ <b>Oleh: </b>{Tag}\n\n'
    M_BOT_MSG =       '➲ <b><i>Link(s) telah Dikirim ke PM (Pribadi) Bot</i></b> 📥'
    # ----- BUTTONS -------
    CLOUD_LINK =   '☁️ Tautan Cloud'
    SAVE_MSG =    '📨 Simpan Pesan'
    RCLONE_LINK =   '♻️ Tautan RClone'
    DDL_LINK =    '📎 Tautan {Serv}'
    SOURCE_URL =   '🔐 Tautan Sumber'
    INDEX_LINK_F =  '🗂 Tautan Indeks'
    INDEX_LINK_D =  '⚡ Tautan Indeks'
    VIEW_LINK =    '🌐 Lihat Tautan'
    CHECK_PM =    '📥 Lihat di Bot PM'
    CHECK_LL =    '🖇 Lihat di Log Tautan'
    MEDIAINFO_LINK = '📃 MediaInfo'
    SCREENSHOTS =   '🖼 Screenshot'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =        '\n┃ {Bar} 📊'
    PROCESSED =     '\n┠ <b>Diproses:</b> {Processed} ⚖️'
    STATUS =      '\n┠ <b>Status:</b> <a href="{Url}">{Status}</a> ℹ️'
    ETA =                        ' | <b>ETA:</b> {Eta} ⏱️'
    SPEED =       '\n┠ <b>Kecepatan:</b> {Speed} 💨'
    ELAPSED =                   ' | <b>Waktu Berlalu:</b> {Elapsed} ⏱️'
    ENGINE =      '\n┠ <b>Mesin:</b> {Engine} ⚙️'
    STA_MODE =     '\n┠ <b>Mode:</b> {Mode} ⚙️'
    SEEDERS =      '\n┠ <b>Seeder:</b> {Seeders} 🌱'
    LEECHERS =                      ' | <b>Leecher:</b> {Leechers} 🧲'

    ####--------SEEDING----------
    SEED_SIZE =   '\n┠ <b>Ukuran: </b>{Size} ⚖️'
    SEED_SPEED =   '\n┠ <b>Kecepatan: </b> {Speed} 💨 | '
    UPLOADED =                   '<b>Diunggah: </b> {Upload} 📤'
    RATIO =     '\n┠ <b>Rasio: </b> {Ratio} 📈 | '
    TIME =                     '<b>Waktu: </b> {Time} ⏱️'
    SEED_ENGINE =  '\n┠ <b>Mesin:</b> {Engine} ⚙️'


    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =  '\n┠ <b>Ukuran: </b>{Size} ⚖️'
    NON_ENGINE =   '\n┠ <b>Mesin:</b> {Engine} ⚙️'

    ####--------OVERALL MSG FOOTER----------
    USER =       '\n┠ <b>Pengguna:</b> <code>{User}</code> 👤 | '
    ID =                            '<b>ID:</b> <code>{Id}</code> 🆔'
    BTSEL =     '\n┠ <b>Pilih:</b> {Btsel}'
    CANCEL =     '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '<b><i>Statistik Bot</i></b>\n'
    TASKS = '┠ <b>Tugas:</b> {Tasks} ⚙️\n'
    BOT_TASKS = '┠ <b>Tugas:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free} 🎭\n'
    Cpu = '┠ <b>CPU:</b> {cpu}% | '
    FREE =           '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>RAM:</b> {ram}% | '
    uptime =           '<b>UPTIME:</b> {uptime}'
    DL = '\n┖ <b>DL:</b> {DL}/s 📥 | '
    UL =            '<b>UL:</b> {UL}/s 📤'


    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder sudah ada di Drive.\nBerikut adalah {content} hasil pencarian:'

    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Menghitung:</b> <code>{LINK}</code> 🔢'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Ukuran: </b>{COUNT_SIZE} ⚖️\n'
    COUNT_TYPE = '┠ <b>Jenis: </b>{COUNT_TYPE} 📁\n'
    COUNT_SUB = '┠ <b>SubFolder: </b>{COUNT_SUB} 📂\n'
    COUNT_FILE = '┠ <b>File: </b>{COUNT_FILE} 📄\n'
    COUNT_CC =  '┖ <b>Oleh: </b>{COUNT_CC}\n'

    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Mencari <i>{NAME}</i></b> 🔎'
    LIST_FOUND = '<b>Ditemukan {NO} hasil untuk <i>{NAME}</i></b> 🔍'
    LIST_NOT_FOUND = 'Tidak ada hasil yang ditemukan untuk <i>{NAME}</i> 🔍'

    # ---------------------

    # async def mirror_status(_, message): ----> status.py
NO_ACTIVE_DL = '''<i>Tidak Ada Unduhan Aktif!</i>
   
<b><i>Statistik Bot</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''<b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''<b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''<b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
