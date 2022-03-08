HELP_1 = """✅<u>**Perintah Admin:**</u>

**c** Singkatan dari Channel Play.

/pause atau /cpause - Jeda musik bermain.
/resume atau /cresume- Lanjutkan musik yang dijeda.
/mute atau /cmute- Bisukan musik yang diputar.
/unmute atau /cunmute- Suarakan musik yang dibisukan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Hentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.

✅<u>**Specifik Melewatkan:**</u>
/skip or /cskip [Nomor(Contoh: 3)] 
    - Melewati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Loop Play:**</u>
/loop or /cloop [enable/disable] atau [Angka antara 1-10] 
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

✅<u>**Pengguna Auth:**</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Username] - Tambahkan pengguna ke DAFTAR AUTH grup .
/unauth [Username] - Hapus pengguna dari DAFTAR AUTH grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅<u>**Perintah Play:**</u>

**cplay** atau **cstream** Singkatan dari Channel Play.
**vplay** Singkatan dari Video Play.

/play atau /vplay atau /cplay  - Bot akan mulai memainkan permintaan yang Anda berikan di obrolan suara.

/stream atau /cstream - Streaming tautan langsung di obrolan suara.

/channelplay [Nama pengguna atau id obrolan] atau [Nonaktifkan] - Hubungkan Channel ke grup dan streaming musik di obrolan suara Channel dari grup Anda.


✅<u>**Playlists Server Bot:**</u>
/playlist  - Cek Playlist yang tersimpan di Server.
/deleteplaylist - Hapus semua musik yang tersimpan di daftar putar Anda.
/play  - Mulai mainkan Playlist Tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Perintah Bot:**</u>

/stats - Dapatkan 10 Trek Global Stats Teratas, 10 Pengguna Bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll. .

/sudolist - Periksa Pengguna Sudo Bot Musik

/lyrics [Judul Musik] - Pencarian lirik untuk musik tertentu di web.

/song [Nama Trek] atau [Link Youtube] - Unduh lagu apapun dari youtube dalam format mp3 atau mp4.

**c** Singkatan dari Channel Play.
/queue atau /cqueue- Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Perintah Ekstra:**</u>
/start - Mulai Bot Musik .
/help  - Dapatkan Menu Pembantu Perintah dengan penjelasan rinci tentang perintah.
/ping- Ping Bot dan periksa statistik Ram, Cpu dll dari Music.

✅<u>**Pengaturan Grup:**</u>
/settings - Dapatkan pengaturan grup lengkap dengan tombol Inline

🔗 **Opsi di Pengaturan:**

1️⃣ Anda dapat mengatur **Kualitas Audio** yang ingin Anda streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** yang ingin Anda streaming di obrolan suara.

3️⃣ **Auth Users**:- Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang hadir di grup Anda akan dapat menggunakan perintah admin(like /skip, /stop etc)

4️⃣ **Clean Mode:** Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Command Clean** : Saat diaktifkan, Bot akan menghapus perintah yang dieksekusi (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **Play Settings:**

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol tempat Anda dapat mengatur pengaturan pemutaran grup Anda. 

<u>Options in playmode:</u>

1️⃣ **Search Mode** [Direct or Inline] - Perubahan mode pencarian Anda saat Anda memberi /play mode. 

2️⃣ **Play Mode** [Group or Channel] - Ubah mode Putar Anda ke Channel atau Grup dan streaming musik hanya di sana.

3️⃣ **Play Type** [Everyone or Admins] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>Tambahkan & Hapus pengguna sudo :</u>**
/addsudo [Username atau Balas pesan pengguna]
/delsudo [Username atau Balas Pesan Pengguna]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Dapatkan config var dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Var Name] [Value] - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

🤖**<u>BOT COMMANDS:</u>**
/restart - Restart Bot. 
/update - Update Bot.
/speedtest - Periksa kecepatan server
/maintenance [enable / disable] 
/logger [enable / disable] - Bot mencatat Permintaan yang dicari di grup logger.
/get_log [Number of Lines] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Cek obrolan suara aktif di bot.
/activevideo - Cek obrolan suara aktif di bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan apa pun dari menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Daftar putih yang ngobrol ngobrol dari menggunakan bot musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username atau Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Username atau Balas ke pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Cek daftar pengguna yang diblokir

👤**<u>GBAN FUNCTION:</u>**
/gban [Username atau Balas ke pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan bot Anda.
/ungban [Username atau Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Jumlah Obrolan] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara default ke M3u8. Anda dapat menggunakan mode unduh saat kueri apa pun tidak diputar dalam mode m3u8.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/unauthorize [CHAT_ID] - Larang obrolan menggunakan bot Anda.
/authorized - Periksa semua obrolan bot Anda yang diizinkan.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Pesan atau balas ke pesan] - Siarkan pesan apa pun ke Obrolan yang Dilayani Bot.

<u>**pengaturan untuk broadcast:**</u>
**-pin** : Ini akan menyematkan pesan Anda 
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-assistant** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan

**Contoh:** `/broadcast -user -assistant -pin Hello Testing`

"""
