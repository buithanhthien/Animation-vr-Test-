film = {}
film["A Star Is Born"] = 7
film["Spider-man"] = 10
film["Kung Fu Monster"] = 6
film["All Is Well"] = 3

print "Ten cac bo phim: "
print "A Star Is Born"
print "Spider-man"
print "Kung Fu Monster"
print "All Is Well"

print ""

name = raw_input("Nhap ten bo phim: ")


if film[name] > 8:
    print "Phim hay"
if film[name] > 5 and film[name] < 8:
    print "Binh thuong"
if film[name] < 5:
    print "Ton tien"
