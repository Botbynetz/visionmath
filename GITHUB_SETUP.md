# 🚀 GITHUB SETUP INSTRUCTIONS

## LANGKAH 1: Create Repository di GitHub

1. **Login ke GitHub** dengan akun `botbynetzg@gmail.com`:
   - Buka: https://github.com/login
   - Email: `botbynetzg@gmail.com`
   - Password: [masukkan password kamu]

2. **Buat Repository Baru**:
   - Klik icon **+** (top right) → **New repository**
   - Atau buka: https://github.com/new

3. **Fill Form**:
   - **Repository name**: `mathvision`
   - **Description**: `Professional Mathematics Learning Platform`
   - **Visibility**: **Public** ✅
   - **Initialize repository**: JANGAN centang apa-apa (Leave Empty)
   - Klik **Create repository**

4. **Copy Setup Commands** dari GitHub (setelah create):
   - Akan ada pilihan HTTP atau SSH
   - Pilih **HTTP** (lebih mudah)
   - Copy tulisan yang dimulai dengan: `git remote add origin...`

---

## LANGKAH 2: Push ke GitHub (Setelah Repository Ada)

**Setelah** repository dibuat, jalankan di PowerShell:

```powershell
cd "d:\tania's project"

# Jika belum ada remote, tambah:
git remote add origin https://github.com/Botbyentz/mathvision.git

# Push ke GitHub
git push -u origin master
```

**Pertama kali push**, GitHub akan minta login:
- Pilih **Login with a web browser**
- Atau buat **Personal Access Token** (lebih aman)

---

## LANGKAH 3: Verify di GitHub

Setelah push selesai:
1. Refresh: https://github.com/Botbyentz/mathvision
2. Pastikan file-file sudah muncul (main.py, web/, modules/, dll)

---

## Next: Deploy ke PythonAnywhere

Setelah GitHub setup sukses, tunggu instruksi deployment PythonAnywhere.

---

**Status**: ⏳ Menunggu repository dibuat di GitHub
