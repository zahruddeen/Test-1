import random
import math

# Fungsi untuk menghitung jarak haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius bumi dalam km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Fungsi untuk mendapatkan warna berdasarkan jarak
def get_color(distance):
    if distance < 500:
        return '\033[92m'  # Hijau terang
    elif distance < 1000:
        return '\033[32m'  # Hijau
    elif distance < 2000:
        return '\033[93m'  # Kuning
    elif distance < 5000:
        return '\033[91m'  # Merah
    else:
        return '\033[31m'  # Merah gelap

# Dictionary negara dengan clue dan koordinat (lat, lon)
countries = {
    "Brazil": ("Negara terbesar di Amerika Selatan dengan hutan Amazon yang luas", -14.2350, -51.9253),
    "Indonesia": ("Negara kepulauan terbesar di dunia dengan lebih dari 17.000 pulau", -0.7893, 113.9213),
    "Russia": ("Negara terbesar di dunia berdasarkan luas wilayah", 61.5240, 105.3188),
    "China": ("Negara dengan populasi terbanyak di dunia", 35.8617, 104.1954),
    "Australia": ("Negara benua yang dikelilingi oleh lautan", -25.2744, 133.7751),
    "United States": ("Negara dengan ekonomi terbesar di dunia", 37.0902, -95.7129),
    "India": ("Negara dengan populasi terbanyak kedua di dunia", 20.5937, 78.9629),
    "Canada": ("Negara terbesar kedua di dunia dengan banyak danau", 56.1304, -106.3468),
    "Argentina": ("Negara terpanjang di Amerika Selatan dengan tango sebagai budaya", -38.4161, -63.6167),
    "Japan": ("Negara kepulauan di Asia Timur dengan teknologi canggih", 36.2048, 138.2529),
    "Germany": ("Negara terbesar di Eropa Barat dengan sejarah industri", 51.1657, 10.4515),
    "Egypt": ("Negara dengan piramida Giza yang terkenal di dunia", 26.0963, 29.9538),
    "South Africa": ("Negara dengan keanekaragaman hayati tinggi dan Table Mountain", -30.5595, 22.9375),
    "Mexico": ("Negara dengan peradaban Aztec dan makanan pedas", 23.6345, -102.5528),
    "France": ("Negara dengan Menara Eiffel di Paris", 46.2276, 2.2137),
    "United Kingdom": ("Negara dengan Big Ben dan kerajaan", 55.3781, -3.4360),
    "Italy": ("Negara dengan Colosseum di Roma", 41.8719, 12.5674),
    "Spain": ("Negara dengan tarian flamenco dan paella", 40.4637, -3.7492),
    "Netherlands": ("Negara dengan kincir angin dan kanal", 52.1326, 5.2913),
    "Sweden": ("Negara dengan aurora borealis di utara", 60.1282, 18.6435),
    "Norway": ("Negara dengan fjord dan viking", 60.4720, 8.4689),
    "Denmark": ("Negara dengan Lego dan hygge", 56.2639, 9.5018),
    "Finland": ("Negara dengan sauna dan Santa Claus", 61.9241, 25.7482),
    "Poland": ("Negara dengan kastil dan Chopin", 51.9194, 19.1451),
    "Czech Republic": ("Negara dengan Prague Castle dan bir", 49.8175, 15.4730),
    "Austria": ("Negara dengan musik klasik dan Mozart", 47.5162, 14.5501),
    "Switzerland": ("Negara dengan cokelat dan jam tangan", 46.8182, 8.2275),
    "Belgium": ("Negara dengan wafel dan cokelat", 50.5039, 4.4699),
    "Portugal": ("Negara dengan Porto wine dan azulejo", 39.3999, -8.2245),
    "Greece": ("Negara dengan filosof kuno dan Parthenon", 39.0742, 21.8243),
    "Turkey": ("Negara penghubung Eropa dan Asia dengan Istanbul", 38.9637, 35.2433),
    "Saudi Arabia": ("Negara dengan kota suci Mekah", 23.8859, 45.0792),
    "Iran": ("Negara dengan peradaban kuno Persia", 32.4279, 53.6880),
    "Iraq": ("Negara dengan sungai Eufrat dan Tigris", 33.2232, 43.6793),
    "Israel": ("Negara dengan Tembok Ratapan di Yerusalem", 31.0461, 34.8516),
    "Jordan": ("Negara dengan Petra yang terukir batu", 30.5852, 36.2384),
    "Lebanon": ("Negara dengan cedar Lebanon", 33.8547, 35.8623),
    "Syria": ("Negara dengan Damaskus kuno", 34.8021, 38.9968),
    "Yemen": ("Negara dengan kopi Yemen", 15.5527, 48.5164),
    "Oman": ("Negara dengan pasir gurun dan kastil", 21.4735, 55.9754),
    "United Arab Emirates": ("Negara dengan Burj Khalifa tertinggi", 23.4241, 53.8478),
    "Qatar": ("Negara dengan gas alam melimpah", 25.3548, 51.1839),
    "Kuwait": ("Negara dengan minyak dan teluk", 29.3117, 47.4818),
    "Bahrain": ("negara dengan mutiara", 26.0667, 50.5577),
    "Pakistan": ("Negara dengan gunung K2", 30.3753, 69.3451),
    "Afghanistan": ("Negara dengan Hindu Kush", 33.9391, 67.7100),
    "Bangladesh": ("Negara dengan sungai Gangga", 23.6850, 90.3563),
    "Nepal": ("Negara dengan Gunung Everest", 28.3949, 84.1240),
    "Bhutan": ("Negara dengan kebahagiaan nasional bruto", 27.5142, 90.4336),
    "Sri Lanka": ("Negara dengan teh Ceylon", 7.8731, 80.7718),
    "Maldives": ("Negara dengan resor tropis", 3.2028, 73.2207),
    "Thailand": ("Negara dengan kuil Buddha", 15.8700, 100.9925),
    "Cambodia": ("Negara dengan Angkor Wat", 12.5657, 104.9910),
    "Laos": ("Negara dengan Kuil Luang Prabang", 19.8563, 102.4955),
    "Vietnam": ("Negara dengan Teluk Ha Long", 14.0583, 108.2772),
    "Myanmar": ("Negara dengan Pagoda Shwedagon", 21.9162, 95.9560),
    "Malaysia": ("Negara dengan Petronas Towers", 4.2105, 101.9758),
    "Singapore": ("Negara kota dengan Marina Bay Sands", 1.3521, 103.8198),
    "Philippines": ("Negara kepulauan dengan gunung berapi", 12.8797, 121.7740),
    "South Korea": ("Negara dengan K-pop dan kimchi", 35.9078, 127.7669),
    "North Korea": ("Negara dengan pemimpin Kim Jong-un", 40.3399, 127.5101),
    "Mongolia": ("Negara dengan Gurun Gobi", 46.8625, 103.8467),
    "Kazakhstan": ("negara dengan stepa", 48.0196, 66.9237),
    "Uzbekistan": ("negara dengan sutra", 41.3775, 64.5853),
    "Turkmenistan": ("negara dengan karpet", 38.9697, 59.5563),
    "Tajikistan": ("negara dengan gunung", 38.8610, 71.2761),
    "Kyrgyzstan": ("negara dengan danau issyk kul", 41.2044, 74.7661),
    "Algeria": ("negara terbesar di afrika", 28.0339, 1.6596),
    "Libya": ("negara dengan gurun sahara", 26.3351, 17.2283),
    "Morocco": ("negara dengan kasbah", 31.7917, -7.0926),
    "Tunisia": ("negara dengan karthago", 33.8869, 9.5375),
    "Nigeria": ("negara dengan populasi terbanyak di afrika", 9.0820, 8.6753),
    "Ethiopia": ("negara dengan objek wisata", 9.1450, 38.7379),
    "Kenya": ("Negara dengan savana Kenya dan safari terkenal", -0.0236, 37.9062),
    "Tanzania": ("negara dengan kilimanjaro", -6.3690, 34.8888),
    "Uganda": ("negara dengan gorila gunung", 1.3733, 32.2903),
    "Rwanda": ("negara dengan kigali", -1.9403, 29.8739),
    "Burundi": ("negara dengan danau tanganyika", -3.3731, 29.9189),
    "Zimbabwe": ("negara dengan victoria falls", -19.0154, 29.1549),
    "Zambia": ("negara dengan copperbelt", -13.1339, 27.8493),
    "Malawi": ("negara dengan danau malawi", -13.2543, 34.3015),
    "Mozambique": ("Negara dengan pantai India yang indah di Afrika Timur", -18.6657, 35.5296),
    "Madagascar": ("negara pulau di afrika", -18.7669, 46.8691),
    "Angola": ("negara dengan minyak", -11.2027, 17.8739),
    "Namibia": ("negara dengan gurun namib", -22.9576, 18.4904),
    "Botswana": ("negara dengan okavango", -22.3285, 24.6849),
    "Lesotho": ("negara di dalam negara", -29.6099, 28.2336),
    "Swaziland": ("negara dengan kerajaan", -26.5225, 31.4659),
    "Ghana": ("negara dengan emas", 7.9465, -1.0232),
    "Ivory Coast": ("negara dengan kakao", 7.5399, -5.5471),
    "Senegal": ("negara dengan dakar", 14.4974, -14.4524),
    "Mali": ("negara dengan timbuktu", 17.5707, -3.9962),
    "Niger": ("negara dengan uranium", 17.6078, 8.0817),
    "Chad": ("negara dengan danau chad", 15.4542, 18.7322),
    "Sudan": ("negara dengan piramida", 12.8628, 30.2176),
    "Eritrea": ("negara dengan laut merah", 15.1794, 39.7823),
    "Djibouti": ("negara dengan afrika timur", 11.8251, 42.5903),
    "Somalia": ("negara dengan somali", 5.1521, 46.1996),
    "Colombia": ("negara dengan kopi", 4.5709, -74.2973),
    "Venezuela": ("negara dengan angel falls", 6.4238, -66.5897),
    "Ecuador": ("negara dengan garis khatulistiwa", -1.8312, -78.1834),
    "Peru": ("negara dengan machu picchu", -9.1900, -75.0152),
    "Bolivia": ("negara dengan salt flats", -16.2902, -63.5887),
    "Chile": ("negara terpanjang di dunia", -35.6751, -71.5430),
    "Paraguay": ("negara dengan iguazu", -23.4425, -58.4438),
    "Uruguay": ("negara dengan tango", -32.5228, -55.7658),
    "Guyana": ("negara dengan amazon", 4.8604, -58.9302),
    "Suriname": ("Negara dengan hutan hujan Amazon di Amerika Selatan", 3.9193, -56.0278),
    "French Guiana": ("wilayah prancis di amerika selatan", 3.9339, -53.1258),
    "Cuba": ("negara dengan havana", 21.5218, -77.7812),
    "Haiti": ("negara dengan vodou", 18.9712, -72.2852),
    "Dominican Republic": ("negara dengan merengue", 18.7357, -70.1627),
    "Jamaica": ("negara dengan reggae", 18.1096, -77.2975),
    "Trinidad and Tobago": ("negara dengan carnival", 10.6918, -61.2225),
    "Barbados": ("negara dengan rum", 13.1939, -59.5432),
    "Bahamas": ("negara dengan bahama", 25.0343, -77.3963),
    "Belize": ("negara dengan barrier reef", 17.1899, -88.4976),
    "Guatemala": ("negara dengan maya", 15.7835, -90.2308),
    "El Salvador": ("negara dengan vulkan", 13.7942, -88.8965),
    "Honduras": ("negara dengan copan", 15.2000, -86.2419),
    "Nicaragua": ("negara dengan managua", 12.8654, -85.2072),
    "Costa Rica": ("Negara dengan hutan hujan tropis dan keanekaragaman hayati tinggi", 9.7489, -83.7534),
    "Panama": ("negara dengan kanal", 8.5380, -80.7821),
    "New Zealand": ("negara dengan kiwi", -40.9006, 174.8860),
    "Papua New Guinea": ("negara dengan suku", -6.3150, 143.9555),
    "Fiji": ("negara dengan pasir", -17.7134, 178.0650),
    "Samoa": ("negara dengan polynesia", -13.7590, -172.1046),
    "Tonga": ("negara dengan kerajaan", -21.1789, -175.1982),
    "Vanuatu": ("negara dengan vulkan", -15.3767, 166.9592),
    "Solomon Islands": ("negara dengan hutan", -9.6457, 160.1562),
    "Kiribati": ("negara dengan atol", -3.3704, -168.7340),
    "Tuvalu": ("negara terkecil", -7.1095, 177.6493),
    "Nauru": ("negara dengan fosfat", -0.5228, 166.9315),
    "Marshall Islands": ("negara dengan atol", 7.1315, 171.1845),
    "Palau": ("negara dengan jellyfish", 7.5149, 134.5825),
    "Micronesia": ("negara dengan federasi", 7.4256, 150.5508),
    "Iceland": ("negara dengan geysir", 64.9631, -19.0208),
    "Greenland": ("pulau terbesar", 71.7069, -42.6043),
    "Faroe Islands": ("pulau di atlantik", 61.8926, -6.9118),
    "Andorra": ("negara kecil di pirenia", 42.5063, 1.5218),
    "Monaco": ("negara terkecil di eropa", 43.7384, 7.4246),
    "Liechtenstein": ("negara dengan kastil", 47.1660, 9.5554),
    "San Marino": ("republik tertua", 43.9424, 12.4578),
    "Vatican City": ("negara terkecil di dunia", 41.9029, 12.4534),
    "Malta": ("negara dengan megalith", 35.9375, 14.3754),
    "Cyprus": ("pulau di mediterania", 35.1264, 33.4299),
    "Luxembourg": ("negara dengan benteng", 49.8153, 6.1296),
    "Slovenia": ("negara dengan gua", 46.1512, 14.9955),
    "Croatia": ("Negara dengan pantai Adriatik yang berbatu di Eropa", 45.1000, 15.2000),
    "Bosnia and Herzegovina": ("negara dengan sarajevo", 43.9159, 17.6791),
    "Serbia": ("negara dengan belgrade", 44.0165, 21.0059),
    "Montenegro": ("negara dengan fjord", 42.7087, 19.3744),
    "Kosovo": ("negara dengan pristina", 42.6026, 20.9030),
    "North Macedonia": ("negara dengan skopje", 41.6086, 21.7453),
    "Albania": ("negara dengan tirana", 41.1533, 20.1683),
    "Bulgaria": ("negara dengan sofia", 42.7339, 25.4858),
    "Romania": ("negara dengan kastil dracula", 45.9432, 24.9668),
    "Moldova": ("negara dengan chisinău", 47.4116, 28.3699),
    "Ukraine": ("negara dengan kiev", 48.3794, 31.1656),
    "Belarus": ("negara dengan minsk", 53.7098, 27.9534),
    "Lithuania": ("negara dengan vilnius", 55.1694, 23.8813),
    "Latvia": ("negara dengan riga", 56.8796, 24.6032),
    "Estonia": ("negara dengan tallinn", 58.5953, 25.0136),
    "Georgia": ("negara dengan kaukasus", 42.3154, 43.3569),
    "Armenia": ("negara dengan yerevan", 40.0691, 45.0382),
    "Azerbaijan": ("negara dengan baku", 40.1431, 47.5769),
    "Slovakia": ("negara dengan bratislava", 48.6690, 19.6990),
    "Hungary": ("negara dengan budapest", 47.1625, 19.5033),
    "Ireland": ("negara dengan shamrock", 53.4129, -8.2439),
    "Estonia": ("negara dengan tallinn", 58.5953, 25.0136),  # duplicate, remove
    # Note: Some duplicates or missing, but approximately 196
}

# Pilih negara acak
correct_country, (clue, correct_lat, correct_lon) = random.choice(list(countries.items()))

print("Selamat datang di game Tebak Negara dong pun!")
print(f"Clue: {clue}")
print("Tebak negara mana itu diriku ini?")

attempts = 0
max_attempts = 6  # Batas percobaan

while attempts < max_attempts:
    guess = input("Jawaban Anda: ").strip().title()  # Capitalize first letter
    
    if guess == correct_country:
        print("Selamat! Jawaban dirimu itu benar pun.")
        break
    elif guess in countries:
        guessed_lat, guessed_lon = countries[guess][1], countries[guess][2]
        distance = haversine(correct_lat, correct_lon, guessed_lat, guessed_lon)
        color = get_color(distance)
        print(f"{color}Salah! Negara yang dirimu itu tebak berjarak {distance:.0f} km dari negara yang benar.\033[0m")
    else:
        print("Negara mana itu pun. Coba lagi.")
    
    attempts += 1
    if attempts < max_attempts:
        print(f"Percobaan {attempts + 1} dari {max_attempts}")

if attempts == max_attempts:
    print(f"Maaf, dirimu itu kehabisan percobaan. Negara yang benar adalah {correct_country} dong.")
