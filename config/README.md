# Kay X Musik Configs

Config vars pada dasarnya variabel yang configure atau bot memodifikasi fungsi, yang merupakan kebutuhan dasar plugin atau kode untuk bekerja. Anda harus mengatur vars wajib yang tepat untuk membuatnya fungsional dan untuk memulai fitur dasar bot.


## Wajib Vars

- Ini adalah minimum vars diperlukan perlu setup untuk membuat Kay X Music fungsional.

1. `API_ID`: Dapatkan dari my.telegram.org
2. `API_HASH`: Dapatkan dari my.telegram.org
3. `BOT_TOKEN`: Dapatkan dari [Botfather] (http://t.me/BotFather) di Telegram
4. `MONGO_DB_URI`: Dapatkan mongo db [. Dari sini] (https://telegra.ph/How-To-get-Mongodb-URI-04-06)
5. `LOG_GROUP_ID`: Anda akan membutuhkan Swasta Kelompok ID untuk ini. Supergrup Dibutuhkan dengan id mulai dari -100
6. `MUSIC_BOT_NAME`: Nama untuk bot Musik Anda.
7. `OWNER_ID`: Pemilik ID Anda untuk mengelola bot Anda.
8. `STRING_SESSION`: Pyrogram Sesi Dibutuhkan, Menghasilkan string dari [🤖 String Session] (http://t.me/NichstringRobot) di Telegram.


## Non-Wajib Vars

- Ini adalah vars tambahan untuk fitur tambahan di dalam Music Bot. Anda dapat meninggalkan vars non wajib untuk saat ini dan dapat menambahkannya nanti.

1. `DURATION_LIMIT`: Custom max audio (musik) durasi untuk voice chat. Default ke 60 menit.
2. `SONG_DOWNLOAD_DURATION_LIMIT`: Batasi Durasi untuk mendownload Lagu dalam format MP3 atau MP4 dari bot. Default ke 180 menit.
3. `VIDEO_STREAM_LIMIT`: Jumlah maksimum panggilan video diperbolehkan di bot. Nanti dapat mengaturnya melalui / set_video_limit pada telegram. Default ke 3 chatting.
4. `SERVER_PLAYLIST_LIMIT`: Maksimum Batas Diizinkan bagi pengguna untuk menyimpan playlist di server bot ini. Default ke 30
5. `PLAYLIST_FETCH_LIMIT`: Batas maksimum untuk mengambil lagu playlist ini dari youtube, Spotify, link apel. Default ke 25
6. `CLEANMODE_MINS`: waktu Cleanmode setelah bot akan menghapus pesan lama dari chatting. Default ke 5 Menit.
7. `SUPPORT_CHANNEL`: Jika Anda sudah channel manapun untuk bot musik Anda, mengisinya dengan link saluran Anda
8. `SUPPORT_GROUP`: Jika Anda sudah ada dukungan kelompok untuk bot musik Anda, mengisinya dengan link saluran Anda


## Bot Vars

- ini semua vars digunakan untuk menyiapkan bot. Anda dapat mengedit ini vars jika Anda ingin, yang lain meninggalkan semua dari mereka seperti itu.

1. `PRIVATE_BOT_MODE` : Set benar jika Anda ingin bot Anda menjadi hanya pribadi atau Salah untuk semua kelompok. Default untuk False
2. `YOUTUBE_EDIT_SLEEP` : durasi tidur Time For Youtube Downloader. Default untuk 3 detik
3. `TELEGRAM_EDIT_SLEEP` : durasi tidur Time For Telegram Downloader. Default untuk 5 detik
4. `AUTO_LEAVING_ASSISTANT` : Set di Benar jika Anda ingin meninggalkan asisten Anda setelah waktu tertentu.
5. `ASSISTANT_LEAVE_TIME` : Waktu setelah asisten akun Anda akan meninggalkan chatting dilayani secara otomatis. Default ke 5400 menit, mis 90 Menit
6. `AUTO_DOWNLOADS_CLEAR` : Set itu Benar jika Anda ingin menghapus download setelah berakhir musik playout.
7. `AUTO_SUGGESTION_MODE` : Set itu Benar jika Anda ingin bot menyarankan tentang perintah bot untuk chatting acak bot Anda.


## Spotify Vars

- Anda dapat memainkan lagu atau playlist dari spotify dari Kay X Musik
- Anda akan membutuhkan dua ini vars untuk membuat spotify bermain kerja. Hal ini tidak penting, Anda dapat meninggalkan kosong mereka jika Anda ingin.

1. `SPOTIFY_CLIENT_ID` : Dapatkan dari https://developer.spotify.com/dashboard
2. `SPOTIFY_CLIENT_SECRET` : Dapatkan dari https://developer.spotify.com/dashboard


## Heroku Vars

- Untuk bekerja beberapa modul yang kompatibel Heroku, nilai var ini diperlukan untuk Akses akun Anda untuk penggunaan get_log, penggunaan, pembaruan dll perintah.
- Anda dapat mengisi var ini menggunakan kunci API atau tanda Otorisasi.

1. `HEROKU_API_KEY`: Dapatkan di dasboard heroku
2. `UPSTREAM_REPO` : URL Repo Upstream Anda atau Repo Bercabang.
3. `UPSTREAM_BRANCH` : Cabang Default dari URL Repo Hulu atau Repo Bercabang Anda.
4. `GIT_TOKEN` : GIT TOKEN Anda jika repo upstream Anda bersifat pribadi
5. `GITHUB_REPO` : URL Repo Github Anda, yang akan ditampilkan pada perintah /start



 ## Gambar/Thumbnail Vars

 - Anda dapat mengubah gambar yang digunakan di Kay X Music.
 - Anda dapat membuat tautan telegaph dari [KayXRobot](http://t.me/KayXRobot) dan menggunakannya di sini.

 1. `START_IMG_URL` : Gambar yang muncul pada perintah /start dalam pesan pribadi bot.
 2. `PING_IMG_URL` : Gambar yang muncul pada perintah /ping bot.
 3. `PLAYLIST_IMG_URL` : Gambar yang muncul pada perintah /play bot.
 4. `GLOBAL_IMG_URL` : Gambar yang muncul pada perintah /stats bot.
 5. `STATS_IMG_URL` : Gambar yang muncul pada perintah /stats bot.
 6. `TELEGRAM_AUDIO_URL` : Gambar ini muncul ketika seseorang memutar audio dari telegram.
 7. `TELEGRAM_VIDEO_URL` : Gambar ini muncul ketika seseorang memutar video dari telegram.
 8. `STREAM_IMG_URL` : gambarnya muncul ketika seseorang memainkan m3u8 atau tautan indeks.
 9. `SOUNCLOUD_IMG_URL` : Gambar ini muncul saat seseorang memutar musik dari soundcloud.
 10. `YOUTUBE_IMG_URL| : Gambar ini muncul jika generator thumbnail gagal membuat jempol bagaimanapun.
 11. `SPOTIFY_ARTIST_IMG_URL` : Gambar ini muncul ketika seseorang memainkan artis Spotify melalui tautan dalam mode sebaris.
 12. `SPOTIFY_ALBUM_IMG_URL` : Gambar ini muncul ketika seseorang memutar album Spotify melalui tautan dalam mode sebaris.
 13. `SPOTIFY_PLAYLIST_IMG_URL` : Gambar ini muncul ketika seseorang memutar album Spotify melalui tautan dalam mode sebaris.

 ## Mode Multi Asisten

 - Anda dapat menggunakan hingga 5 Asisten Klien (memungkinkan bot Anda setidaknya bekerja dalam 2000-2500 obrolan sekaligus)

 1. `STRING_SESSION2` : Diperlukan Sesi Pyrogram, Hasilkan string dari [🤖 Sesi String](http://t.me/NichstringRobot) di Telegram.
 2. `STRING_SESSION3` : Diperlukan Sesi Pyrogram, Hasilkan string dari [🤖 Sesi String](http://t.me/NichstringRobot) di Telegram.
 3. `STRING_SESSION4` : Diperlukan Sesi Pyrogram, Hasilkan string dari [🤖 Sesi String](http://t.me/NichstringRobot) di Telegram.
 4. `STRING_SESSION5` : Diperlukan Sesi Pyrogram, Hasilkan string dari [🤖 Sesi String](http://t.me/NichstringRobot) di Telegram.
