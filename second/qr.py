import  qrcode as qr

img=qr.make("https://www.youtube.com/watch?v=QY0ItgxcriU")
img.save("song_youtube.png")
