# Simulasi database pengguna
pengguna = {
    "Thorik": {
        "password": "thorik123",
        "nama": "Thorik",
        "kelas": "TEK A2",
        "nilai": {
            "Matematika": 85,
            "Algoritma": 92,
            "Bahasa Inggris": 78,
            "Pemrograman": 88
        }
    },
    "Hilal": {
        "password": "hilal123",
        "nama": "Hilal",
        "kelas": "TEK A1",
        "nilai": {
            "Matematika": 67,
            "Algoritma": 73,
            "Bahasa Inggris": 80,
            "Pemrograman": 75
        }
    }
}

# Fungsi untuk proses login
def login():
    max_percobaan = 3
    percobaan = 0

    while percobaan < max_percobaan:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in pengguna and pengguna[username]["password"] == password:
            print(f"\n✅ Login berhasil! Selamat datang, {pengguna[username]['nama']} dari kelas {pengguna[username]['kelas']}.\n")
            return username
        else:
            percobaan += 1
            sisa = max_percobaan - percobaan
            print(f"❌ Username atau password salah. Kesempatan tersisa: {sisa}\n")

    print("🚫 Terlalu banyak percobaan. Akses diblokir.")
    return None

# Fungsi untuk menampilkan nilai
def tampilkan_nilai(username):
    data_nilai = pengguna[username]["nilai"]
    print("📊 Nilai Mata Kuliah:")
    for matkul, nilai in data_nilai.items():
        status = "Lulus" if nilai >= 75 else "Tidak Lulus"
        print(f" - {matkul}: {nilai} ({status})")

# Program utama
def main():
    user = login()
    if user:
        tampilkan_nilai(user)

if __name__ == "__main__":
    main()