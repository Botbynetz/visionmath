"""
Program Utama - Matematika UNIVERSITY LEVEL untuk Programmer
Sistem menu interaktif untuk mengakses semua fungsi matematika tingkat universitas
"""

import sys
import os
try:
    # Inisialisasi colorama agar ANSI escape (jika muncul) dirender di Windows lama
    from colorama import just_fix_windows_console
    just_fix_windows_console()
except Exception:
    pass

# Menambahkan path modules ke sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules import arithmetic, number_theory, geometry, statistics, algebra
try:
    from modules import quiz
except ImportError:
    quiz = None

# Import university-level modules
try:
    from modules import calculus, differential_equations, visualization_3d, latex_renderer, word_problem_solver
    UNIVERSITY_MODULES = True
except ImportError:
    UNIVERSITY_MODULES = False
    print("Warning: Some university-level modules not available. Install dependencies: pip install sympy matplotlib scipy")

# Import expert-level modules with individual error handling
EXPERT_MODULES = {}
try:
    from modules import symbolic_analysis
    EXPERT_MODULES['symbolic_analysis'] = True
except ImportError as e:
    EXPERT_MODULES['symbolic_analysis'] = False
    print(f"Warning: symbolic_analysis not available: {e}")

try:
    from modules import number_theory_cryptography
    EXPERT_MODULES['number_theory_cryptography'] = True
except ImportError as e:
    EXPERT_MODULES['number_theory_cryptography'] = False
    print(f"Warning: number_theory_cryptography not available: {e}")

try:
    from modules import topology_differential_geometry
    EXPERT_MODULES['topology_differential_geometry'] = True
except ImportError as e:
    EXPERT_MODULES['topology_differential_geometry'] = False
    print(f"Warning: topology_differential_geometry not available: {e}")

try:
    from modules import mathematical_logic_proof_system
    EXPERT_MODULES['mathematical_logic_proof_system'] = True
except ImportError as e:
    EXPERT_MODULES['mathematical_logic_proof_system'] = False
    print(f"Warning: mathematical_logic_proof_system not available: {e}")

try:
    from modules import simulation_mathematical_modeling
    EXPERT_MODULES['simulation_mathematical_modeling'] = True
except ImportError as e:
    EXPERT_MODULES['simulation_mathematical_modeling'] = False
    print(f"Warning: simulation_mathematical_modeling not available: {e}")

try:
    from modules import algorithm_analysis_integration
    EXPERT_MODULES['algorithm_analysis_integration'] = True
except ImportError as e:
    EXPERT_MODULES['algorithm_analysis_integration'] = False
    print(f"Warning: algorithm_analysis_integration not available: {e}")

# Check if all expert modules are available
ALL_EXPERT_MODULES = all(EXPERT_MODULES.values())
AVAILABLE_EXPERT_COUNT = sum(EXPERT_MODULES.values())

# Import researcher-level modules with individual error handling
RESEARCHER_MODULES = {}
try:
    from modules import automated_theorem_proving
    RESEARCHER_MODULES['automated_theorem_proving'] = True
except ImportError as e:
    RESEARCHER_MODULES['automated_theorem_proving'] = False
    print(f"Warning: automated_theorem_proving not available: {e}")

try:
    from modules import advanced_mathematical_modeling
    RESEARCHER_MODULES['advanced_mathematical_modeling'] = True
except ImportError as e:
    RESEARCHER_MODULES['advanced_mathematical_modeling'] = False
    print(f"Warning: advanced_mathematical_modeling not available: {e}")

try:
    from modules import mathematical_experimentation
    RESEARCHER_MODULES['mathematical_experimentation'] = True
except ImportError as e:
    RESEARCHER_MODULES['mathematical_experimentation'] = False
    print(f"Warning: mathematical_experimentation not available: {e}")

try:
    from modules import researcher_symbolic_analysis
    RESEARCHER_MODULES['researcher_symbolic_analysis'] = True
except ImportError as e:
    RESEARCHER_MODULES['researcher_symbolic_analysis'] = False
    print(f"Warning: researcher_symbolic_analysis not available: {e}")

# Check if all researcher modules are available
ALL_RESEARCHER_MODULES = all(RESEARCHER_MODULES.values())
AVAILABLE_RESEARCHER_COUNT = sum(RESEARCHER_MODULES.values())

# Import innovator-level modules with individual error handling
INNOVATOR_MODULES = {}
try:
    from modules import conjecture_generator
    INNOVATOR_MODULES['conjecture_generator'] = True
except ImportError as e:
    INNOVATOR_MODULES['conjecture_generator'] = False
    print(f"Warning: conjecture_generator not available: {e}")

try:
    from modules import theoretical_framework_builder
    INNOVATOR_MODULES['theoretical_framework_builder'] = True
except ImportError as e:
    INNOVATOR_MODULES['theoretical_framework_builder'] = False
    print(f"Warning: theoretical_framework_builder not available: {e}")

try:
    from modules import interdisciplinary_integrator
    INNOVATOR_MODULES['interdisciplinary_integrator'] = True
except ImportError as e:
    INNOVATOR_MODULES['interdisciplinary_integrator'] = False
    print(f"Warning: interdisciplinary_integrator not available: {e}")

try:
    from modules import ai_algorithm_designer
    INNOVATOR_MODULES['ai_algorithm_designer'] = True
except ImportError as e:
    INNOVATOR_MODULES['ai_algorithm_designer'] = False
    print(f"Warning: ai_algorithm_designer not available: {e}")

# Check if all innovator modules are available
ALL_INNOVATOR_MODULES = all(INNOVATOR_MODULES.values())
AVAILABLE_INNOVATOR_COUNT = sum(INNOVATOR_MODULES.values())

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    RICH_AVAILABLE = True
    console = Console(force_terminal=True, markup=True, soft_wrap=True)
except Exception:
    RICH_AVAILABLE = False
    console = None

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter_to_continue():
    """Menunggu user menekan enter"""
    input("\nTekan Enter untuk melanjutkan...")

def display_main_menu():
    """Menampilkan menu utama"""
    print("="*70)
    print("     MATEMATIKA UNIVERSITY LEVEL UNTUK PROGRAMMER")
    print("="*70)
    # Display module status
    core_status = "✓ LOADED" 
    university_status = "✓ LOADED" if UNIVERSITY_MODULES else "✗ MISSING DEPS"
    expert_status = f"✓ {AVAILABLE_EXPERT_COUNT}/6 LOADED" if AVAILABLE_EXPERT_COUNT > 0 else "✗ MISSING DEPS"
    researcher_status = f"✓ {AVAILABLE_RESEARCHER_COUNT}/4 LOADED" if AVAILABLE_RESEARCHER_COUNT > 0 else "✗ MISSING DEPS"
    innovator_status = f"✓ {AVAILABLE_INNOVATOR_COUNT}/4 LOADED" if AVAILABLE_INNOVATOR_COUNT > 0 else "✗ MISSING DEPS"
    
    print(f"STATUS: Core [{core_status}] | University [{university_status}] | Expert [{expert_status}] | Researcher [{researcher_status}] | Innovator [{innovator_status}]")
    print("="*70)
    print("CORE MODULES:")
    print("1. Aritmatika Dasar")
    print("2. Teori Bilangan") 
    print("3. Geometri & Trigonometri Advanced")
    print("4. Statistik & Probabilitas")
    print("5. Aljabar Advanced (Sistem 3x3, Faktorisasi, Binomial)")
    print()
    print("UNIVERSITY LEVEL MODULES:")
    if UNIVERSITY_MODULES:
        print("6. Kalkulus Advanced (Turunan, Integral, Limit, Taylor)")
        print("7. Persamaan Diferensial (ODE, PDE, Laplace)")
        print("8. Visualisasi 3D & Plotting")
        print("9. LaTeX Integration & Rendering")
        print("10. Word Problem Solver (NLP)")
    else:
        print("6-10. [Not Available - Install: pip install sympy matplotlib scipy]")
    print()
    print("TOOLS & LEARNING:")
    print("11. Kalkulator Interaktif")
    print("12. Demo Semua Modul")
    print("13. Tutor Mode (Belajar Interaktif)")
    print("14. Kuis Adaptif")
    print()
    print("EXPERT LEVEL MODULES (TINGKAT PAKAR):")
    if ALL_EXPERT_MODULES:
        print("15. Symbolic Analysis Engine (Analisis Simbolik)")
        print("16. Number Theory & Cryptography (Teori Bilangan & Kriptografi)")
        print("17. Topology & Differential Geometry (Topologi & Geometri Diferensial)")
        print("18. Mathematical Logic & Proof System (Logika & Sistem Pembuktian)")
        print("19. Simulation & Mathematical Modeling (Simulasi & Pemodelan)")
        print("20. Algorithm Analysis & Integration (Analisis Algoritma)")
    elif AVAILABLE_EXPERT_COUNT > 0:
        # Show available modules individually
        if EXPERT_MODULES.get('symbolic_analysis', False):
            print("15. Symbolic Analysis Engine (Analisis Simbolik) ✓")
        else:
            print("15. [Not Available - Symbolic Analysis loading error]")
            
        if EXPERT_MODULES.get('number_theory_cryptography', False):
            print("16. Number Theory & Cryptography (Teori Bilangan & Kriptografi) ✓")
        else:
            print("16. [Not Available - Number Theory & Cryptography loading error]")
            
        if EXPERT_MODULES.get('topology_differential_geometry', False):
            print("17. Topology & Differential Geometry (Topologi & Geometri Diferensial) ✓")
        else:
            print("17. [Not Available - Topology & Differential Geometry loading error]")
            
        if EXPERT_MODULES.get('mathematical_logic_proof_system', False):
            print("18. Mathematical Logic & Proof System (Logika & Sistem Pembuktian) ✓")
        else:
            print("18. [Not Available - Mathematical Logic & Proof System loading error]")
            
        if EXPERT_MODULES.get('simulation_mathematical_modeling', False):
            print("19. Simulation & Mathematical Modeling (Simulasi & Pemodelan) ✓")
        else:
            print("19. [Not Available - Simulation & Mathematical Modeling loading error]")
            
        if EXPERT_MODULES.get('algorithm_analysis_integration', False):
            print("20. Algorithm Analysis & Integration (Analisis Algoritma) ✓")
        else:
            print("20. [Not Available - Algorithm Analysis & Integration loading error]")
    else:
        print("15-20. [Not Available - All expert modules loading error]")
        print("       Install dependencies: pip install sympy scipy matplotlib networkx pandas")
    print()
    print("RESEARCHER LEVEL MODULES (TINGKAT PENELITI - ULTIMATE):")
    if ALL_RESEARCHER_MODULES:
        print("21. Automated Theorem Proving (Pembuktian Teorema Otomatis)")
        print("22. Advanced Mathematical Modeling (Pemodelan Matematika Lanjut)")
        print("23. Mathematical Experimentation (Eksperimentasi Matematika)")
        print("24. Advanced Symbolic Analysis (Analisis Simbolik Ultimate)")
    elif AVAILABLE_RESEARCHER_COUNT > 0:
        # Show available modules individually
        if RESEARCHER_MODULES.get('automated_theorem_proving', False):
            print("21. Automated Theorem Proving (Pembuktian Teorema Otomatis) ✓")
        else:
            print("21. [Not Available - Automated Theorem Proving loading error]")
            
        if RESEARCHER_MODULES.get('advanced_mathematical_modeling', False):
            print("22. Advanced Mathematical Modeling (Pemodelan Matematika Lanjut) ✓")
        else:
            print("22. [Not Available - Advanced Mathematical Modeling loading error]")
            
        if RESEARCHER_MODULES.get('mathematical_experimentation', False):
            print("23. Mathematical Experimentation (Eksperimentasi Matematika) ✓")
        else:
            print("23. [Not Available - Mathematical Experimentation loading error]")
            
        if RESEARCHER_MODULES.get('researcher_symbolic_analysis', False):
            print("24. Advanced Symbolic Analysis (Analisis Simbolik Ultimate) ✓")
        else:
            print("24. [Not Available - Advanced Symbolic Analysis loading error]")
    else:
        print("21-24. [Not Available - All researcher modules loading error]")
        print("       Install dependencies: pip install sympy z3-solver scikit-learn pandas")
    print()
    print("INNOVATOR LEVEL MODULES (TINGKAT INOVATOR - AI MATHEMATICAL CREATIVITY):")
    if ALL_INNOVATOR_MODULES:
        print("25. Automated Conjecture Generator (Generator Dugaan Otomatis)")
        print("26. Theoretical Framework Builder (Pembuat Kerangka Teoretis)")
        print("27. Interdisciplinary Integrator (Integrator Lintas Disiplin)")
        print("28. AI Algorithm Designer (Perancang Algoritma AI)")
    elif AVAILABLE_INNOVATOR_COUNT > 0:
        # Show available modules individually
        if INNOVATOR_MODULES.get('conjecture_generator', False):
            print("25. Automated Conjecture Generator (Generator Dugaan Otomatis) ✓")
        else:
            print("25. [Not Available - Conjecture Generator loading error]")
            
        if INNOVATOR_MODULES.get('theoretical_framework_builder', False):
            print("26. Theoretical Framework Builder (Pembuat Kerangka Teoretis) ✓")
        else:
            print("26. [Not Available - Framework Builder loading error]")
            
        if INNOVATOR_MODULES.get('interdisciplinary_integrator', False):
            print("27. Interdisciplinary Integrator (Integrator Lintas Disiplin) ✓")
        else:
            print("27. [Not Available - Interdisciplinary Integrator loading error]")
            
        if INNOVATOR_MODULES.get('ai_algorithm_designer', False):
            print("28. AI Algorithm Designer (Perancang Algoritma AI) ✓")
        else:
            print("28. [Not Available - AI Algorithm Designer loading error]")
    else:
        print("25-28. [Not Available - All innovator modules loading error]")
        print("       Install dependencies: pip install tensorflow pytorch scikit-learn networkx")
    print()
    print("VISIONARY LEVEL (LEVEL 6 — Orchestration):")
    print("29. Visionary Tracks — End-to-end AI Math Pipeline")
    print()
    print("ADVANCED:")
    print("A. OCR Matematika (Conceptual Demo)")
    print("B. Advanced Statistics Dashboard")
    print("C. Geometry Visualizer")
    print()
    print("0. Keluar")
    print("="*70)

def arithmetic_menu():
    """Menu aritmatika dasar"""
    while True:
        clear_screen()
        print("=== MENU ARITMATIKA DASAR ===")
        print("1. Operasi Dasar (+, -, ×, ÷)")
        print("2. Perpangkatan & Akar Kuadrat")
        print("3. Konversi Suhu")
        print("4. Hitung BMI")
        print("5. Bunga Majemuk")
        print("6. Demo Aritmatika")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-6): ")
        
        if choice == "1":
            try:
                a = float(input("Masukkan bilangan pertama: "))
                b = float(input("Masukkan bilangan kedua: "))
                print(f"\nHasil:")
                print(f"{a} + {b} = {arithmetic.add(a, b)}")
                print(f"{a} - {b} = {arithmetic.subtract(a, b)}")
                print(f"{a} × {b} = {arithmetic.multiply(a, b)}")
                if b != 0:
                    print(f"{a} ÷ {b} = {arithmetic.divide(a, b):.4f}")
                    print(f"{a} % {b} = {arithmetic.modulus(a, b)}")
                print(f"{a}^{b} = {arithmetic.power(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                num = float(input("Masukkan bilangan: "))
                exp = float(input("Masukkan pangkat: "))
                print(f"{num}^{exp} = {arithmetic.power(num, exp)}")
                if num >= 0:
                    print(f"√{num} = {arithmetic.square_root(num):.4f}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            temp = float(input("Masukkan suhu: "))
            unit = input("Celsius atau Fahrenheit? (C/F): ").upper()
            if unit == "C":
                result = arithmetic.celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.1f}°F")
            elif unit == "F":
                result = arithmetic.fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.1f}°C")
        
        elif choice == "4":
            try:
                weight = float(input("Berat badan (kg): "))
                height = float(input("Tinggi badan (m): "))
                bmi = arithmetic.calculate_bmi(weight, height)
                print(f"BMI Anda: {bmi:.2f}")
                if bmi < 18.5:
                    print("Kategori: Underweight")
                elif bmi < 25:
                    print("Kategori: Normal")
                elif bmi < 30:
                    print("Kategori: Overweight")
                else:
                    print("Kategori: Obese")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            try:
                principal = float(input("Modal awal: "))
                rate = float(input("Tingkat bunga (desimal, misal 0.05): "))
                time = float(input("Waktu (tahun): "))
                result = arithmetic.calculate_compound_interest(principal, rate, time)
                print(f"Modal akhir: {result:.2f}")
                print(f"Keuntungan: {result - principal:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "6":
            arithmetic.arithmetic_demo()
        
        elif choice == "0":
            break
        
        press_enter_to_continue()

def number_theory_menu():
    """Menu teori bilangan"""
    while True:
        clear_screen()
        print("=== MENU TEORI BILANGAN ===")
        print("1. Cek Bilangan Prima")
        print("2. Faktor Prima")
        print("3. GCD & LCM")
        print("4. Faktorial")
        print("5. Fibonacci")
        print("6. Cek Perfect Number")
        print("7. Cek Armstrong Number")
        print("8. Demo Teori Bilangan")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            n = int(input("Masukkan bilangan: "))
            result = number_theory.is_prime(n)
            print(f"{n} {'adalah' if result else 'bukan'} bilangan prima")
        
        elif choice == "2":
            n = int(input("Masukkan bilangan: "))
            factors = number_theory.prime_factors(n)
            print(f"Faktor prima {n}: {factors}")
        
        elif choice == "3":
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            gcd_val = number_theory.gcd(a, b)
            lcm_val = number_theory.lcm(a, b)
            print(f"GCD({a}, {b}) = {gcd_val}")
            print(f"LCM({a}, {b}) = {lcm_val}")
        
        elif choice == "4":
            n = int(input("Masukkan bilangan: "))
            try:
                result = number_theory.factorial(n)
                print(f"{n}! = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            n = int(input("Berapa bilangan Fibonacci yang ingin ditampilkan? "))
            fib_seq = number_theory.fibonacci_sequence(n)
            print(f"{n} bilangan Fibonacci pertama: {fib_seq}")
        
        elif choice == "6":
            n = int(input("Masukkan bilangan: "))
            result = number_theory.perfect_number_check(n)
            print(f"{n} {'adalah' if result else 'bukan'} perfect number")
        
        elif choice == "7":
            n = int(input("Masukkan bilangan: "))
            result = number_theory.armstrong_number_check(n)
            print(f"{n} {'adalah' if result else 'bukan'} Armstrong number")
        
        elif choice == "8":
            number_theory.number_theory_demo()
        
        elif choice == "0":
            break
        
        press_enter_to_continue()

def geometry_menu():
    """Menu geometri"""
    while True:
        clear_screen()
        print("=== MENU GEOMETRI ===")
        print("1. Bangun Datar (2D)")
        print("2. Bangun Ruang (3D)")
        print("3. Jarak & Koordinat")
        print("4. Trigonometri")
        print("5. Demo Geometri")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-5): ")
        
        if choice == "1":
            print("\n--- Bangun Datar ---")
            print("1. Persegi  2. Persegi Panjang  3. Lingkaran  4. Segitiga")
            shape = input("Pilih bangun (1-4): ")
            
            if shape == "1":
                side = float(input("Masukkan panjang sisi: "))
                print(f"Luas: {geometry.square_area(side)}")
                print(f"Keliling: {geometry.square_perimeter(side)}")
            elif shape == "2":
                length = float(input("Masukkan panjang: "))
                width = float(input("Masukkan lebar: "))
                print(f"Luas: {geometry.rectangle_area(length, width)}")
                print(f"Keliling: {geometry.rectangle_perimeter(length, width)}")
            elif shape == "3":
                radius = float(input("Masukkan jari-jari: "))
                print(f"Luas: {geometry.circle_area(radius):.2f}")
                print(f"Keliling: {geometry.circle_circumference(radius):.2f}")
            elif shape == "4":
                base = float(input("Masukkan alas: "))
                height = float(input("Masukkan tinggi: "))
                print(f"Luas: {geometry.triangle_area(base, height)}")
        
        elif choice == "2":
            print("\n--- Bangun Ruang ---")
            print("1. Kubus  2. Balok  3. Bola  4. Silinder")
            shape = input("Pilih bangun (1-4): ")
            
            if shape == "1":
                side = float(input("Masukkan panjang sisi: "))
                print(f"Volume: {geometry.cube_volume(side)}")
                print(f"Luas permukaan: {geometry.cube_surface_area(side)}")
            elif shape == "2":
                length = float(input("Masukkan panjang: "))
                width = float(input("Masukkan lebar: "))
                height = float(input("Masukkan tinggi: "))
                print(f"Volume: {geometry.cuboid_volume(length, width, height)}")
                print(f"Luas permukaan: {geometry.cuboid_surface_area(length, width, height)}")
            elif shape == "3":
                radius = float(input("Masukkan jari-jari: "))
                print(f"Volume: {geometry.sphere_volume(radius):.2f}")
                print(f"Luas permukaan: {geometry.sphere_surface_area(radius):.2f}")
            elif shape == "4":
                radius = float(input("Masukkan jari-jari: "))
                height = float(input("Masukkan tinggi: "))
                print(f"Volume: {geometry.cylinder_volume(radius, height):.2f}")
                print(f"Luas permukaan: {geometry.cylinder_surface_area(radius, height):.2f}")
        
        elif choice == "3":
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            
            distance = geometry.distance_2d(x1, y1, x2, y2)
            midpoint = geometry.midpoint_2d(x1, y1, x2, y2)
            
            print(f"Jarak: {distance:.2f}")
            print(f"Titik tengah: {midpoint}")
            
            try:
                slope = geometry.slope_2d(x1, y1, x2, y2)
                print(f"Gradien: {slope:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            angle = float(input("Masukkan sudut (derajat): "))
            print(f"sin({angle}°) = {geometry.sin_degrees(angle):.4f}")
            print(f"cos({angle}°) = {geometry.cos_degrees(angle):.4f}")
            print(f"tan({angle}°) = {geometry.tan_degrees(angle):.4f}")
        
        elif choice == "5":
            geometry.geometry_demo()
        
        elif choice == "0":
            break
        
        press_enter_to_continue()

def statistics_menu():
    """Menu statistik"""
    while True:
        clear_screen()
        print("=== MENU STATISTIK ===")
        print("1. Input Data Manual")
        print("2. Statistik Deskriptif")
        print("3. Demo Statistik")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-3): ")
        
        if choice == "1" or choice == "2":
            # Input data
            data_input = input("Masukkan data (pisahkan dengan spasi): ")
            try:
                data = [float(x) for x in data_input.split()]
                
                if not data:
                    print("Data kosong!")
                    press_enter_to_continue()
                    continue
                
                print(f"\nData: {data}")
                print(f"Jumlah data: {len(data)}")
                print(f"Mean: {statistics.mean(data):.2f}")
                print(f"Median: {statistics.median(data)}")
                
                mode_result = statistics.mode(data)
                if mode_result:
                    print(f"Mode: {mode_result}")
                else:
                    print("Mode: Tidak ada")
                
                print(f"Range: {statistics.range_data(data)}")
                print(f"Standar deviasi: {statistics.standard_deviation(data):.2f}")
                print(f"Varians: {statistics.variance(data):.2f}")
                
                q1, q2, q3 = statistics.quartiles(data)
                print(f"Kuartil - Q1: {q1}, Q2: {q2}, Q3: {q3}")
                
                outliers = statistics.outliers_iqr_method(data)
                if outliers:
                    print(f"Outliers: {outliers}")
                else:
                    print("Tidak ada outliers")
                
            except ValueError:
                print("Error: Pastikan semua input adalah angka!")
        
        elif choice == "3":
            statistics.statistics_demo()
        
        elif choice == "0":
            break
        
        press_enter_to_continue()

def algebra_menu():
    """Menu aljabar"""
    while True:
        clear_screen()
        print("=== MENU ALJABAR ===")
        print("1. Persamaan Kuadrat")
        print("2. Sistem Persamaan Linear 2x2")
        print("3. Operasi Matriks")
        print("4. Barisan & Deret")
        print("5. Demo Aljabar")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-5): ")
        
        if choice == "1":
            print("Persamaan kuadrat: ax² + bx + c = 0")
            a = float(input("Masukkan koefisien a: "))
            b = float(input("Masukkan koefisien b: "))
            c = float(input("Masukkan koefisien c: "))
            
            try:
                solutions = algebra.quadratic_formula(a, b, c)
                if solutions:
                    print(f"Solusi: x₁ = {solutions[0]:.4f}, x₂ = {solutions[1]:.4f}")
                else:
                    print("Tidak ada solusi real")
                
                vertex = algebra.quadratic_vertex(a, b, c)
                print(f"Titik puncak: ({vertex[0]:.4f}, {vertex[1]:.4f})")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            print("Sistem persamaan:")
            print("a₁x + b₁y = c₁")
            print("a₂x + b₂y = c₂")
            
            a1 = float(input("a₁: "))
            b1 = float(input("b₁: "))
            c1 = float(input("c₁: "))
            a2 = float(input("a₂: "))
            b2 = float(input("b₂: "))
            c2 = float(input("c₂: "))
            
            solution = algebra.system_linear_2x2(a1, b1, c1, a2, b2, c2)
            if solution:
                print(f"Solusi: x = {solution[0]:.4f}, y = {solution[1]:.4f}")
            else:
                print("Tidak ada solusi unik")
        
        elif choice == "3":
            print("Matriks 2x2")
            print("Masukkan elemen matriks A:")
            a11 = float(input("A[0,0]: "))
            a12 = float(input("A[0,1]: "))
            a21 = float(input("A[1,0]: "))
            a22 = float(input("A[1,1]: "))
            
            matrix_a = [[a11, a12], [a21, a22]]
            print(f"Matriks A: {matrix_a}")
            print(f"Determinan: {algebra.matrix_determinant_2x2(matrix_a)}")
            print(f"Transpose: {algebra.matrix_transpose(matrix_a)}")
        
        elif choice == "4":
            print("1. Barisan Aritmatika  2. Barisan Geometri")
            seq_type = input("Pilih (1/2): ")
            
            if seq_type == "1":
                a = float(input("Suku pertama: "))
                d = float(input("Beda: "))
                n = int(input("Suku ke-: "))
                result = algebra.arithmetic_sequence(a, d, n)
                print(f"Suku ke-{n}: {result}")
            
            elif seq_type == "2":
                a = float(input("Suku pertama: "))
                r = float(input("Rasio: "))
                n = int(input("Suku ke-: "))
                result = algebra.geometric_sequence(a, r, n)
                print(f"Suku ke-{n}: {result}")
        
        elif choice == "5":
            algebra.algebra_demo()
        
        elif choice == "0":
            break
        
        press_enter_to_continue()

def calculator():
    """Kalkulator interaktif sederhana"""
    clear_screen()
    print("=== KALKULATOR INTERAKTIF ===")
    print("Masukkan 'quit' untuk keluar")
    
    while True:
        try:
            expression = input("\n>>> ")
            if expression.lower() == 'quit':
                break
            
            # Evaluasi expression (hati-hati dengan keamanan!)
            result = eval(expression)
            print(f"Hasil: {result}")
            
        except Exception as e:
            print(f"Error: {e}")

def demo_all():
    """Demo semua modul"""
    clear_screen()
    print("=== DEMO SEMUA MODUL ===\n")
    
    print("1. ARITMATIKA:")
    arithmetic.arithmetic_demo()
    press_enter_to_continue()
    
    print("\n2. TEORI BILANGAN:")
    number_theory.number_theory_demo()
    press_enter_to_continue()
    
    print("\n3. GEOMETRI:")
    geometry.geometry_demo()
    press_enter_to_continue()
    
    print("\n4. STATISTIK:")
    statistics.statistics_demo()
    press_enter_to_continue()
    
    print("\n5. ALJABAR:")
    algebra.algebra_demo()

# =====================
# TUTOR MODE FUNCTIONS
# =====================

def tutor_mode():
    """Mode tutor interaktif yang menjelaskan konsep langkah demi langkah."""
    while True:
        clear_screen()
        print("=== TUTOR MODE ===")
        print("Pilih kategori:")
        print("1. Aritmatika")
        print("2. Teori Bilangan")
        print("3. Geometri")
        print("4. Statistik")
        print("5. Aljabar")
        print("0. Kembali")
        cat = input("Pilih (0-5): ")
        if cat == '0':
            break
        if cat not in {'1','2','3','4','5'}:
            continue

        if cat == '1':
            _tutor_arithmetic()
        elif cat == '2':
            _tutor_number_theory()
        elif cat == '3':
            _tutor_geometry()
        elif cat == '4':
            _tutor_statistics()
        elif cat == '5':
            _tutor_algebra()

def _print_explanation_block(info):
    print("\n--- PENJELASAN ---")
    for i, step in enumerate(info.get('langkah', []), 1):
        print(f"{i}. {step}")
    if 'hasil' in info:
        print(f"\nHasil: {info['hasil']}")
    if 'kategori' in info:
        print(f"Kategori: {info['kategori']}")

def _tutor_arithmetic():
    while True:
        clear_screen()
        print("=== Tutor Aritmatika ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Modulus")
        print("6. Perpangkatan")
        print("7. Akar Kuadrat")
        print("8. BMI")
        print("9. Bunga Majemuk")
        print("0. Kembali")
        ch = input("Pilih: ")
        if ch == '0':
            break
        try:
            if ch in {'1','2','3','4','5','6'}:
                a = float(input("Masukkan a: "))
                b = float(input("Masukkan b: "))
                mapping = {
                    '1': 'add',
                    '2': 'subtract',
                    '3': 'multiply',
                    '4': 'divide',
                    '5': 'modulus',
                    '6': 'power'
                }
                info = arithmetic.explain(mapping[ch], a, b)
                _print_explanation_block(info)
            elif ch == '7':
                x = float(input("Bilangan: "))
                info = arithmetic.explain('sqrt', x)
                _print_explanation_block(info)
            elif ch == '8':
                w = float(input("Berat (kg): "))
                h = float(input("Tinggi (m): "))
                info = arithmetic.explain('bmi', w, h)
                _print_explanation_block(info)
            elif ch == '9':
                p = float(input("Modal awal: "))
                r = float(input("Bunga (desimal, misal 0.05): "))
                t = float(input("Waktu (tahun): "))
                n = int(input("Frekuensi per tahun (misal 12): "))
                info = arithmetic.explain('compound_interest', p, r, t, n=n)
                _print_explanation_block(info)
        except Exception as e:
            print(f"Error: {e}")
        press_enter_to_continue()

def _tutor_number_theory():
    while True:
        clear_screen()
        print("=== Tutor Teori Bilangan ===")
        print("1. Cek Prima")
        print("2. Faktor Prima")
        print("3. GCD")
        print("4. LCM")
        print("5. Faktorial")
        print("6. Fibonacci")
        print("0. Kembali")
        ch = input("Pilih: ")
        if ch == '0':
            break
        try:
            if ch == '1':
                n = int(input("Bilangan: "))
                info = number_theory.explain('is_prime', n)
            elif ch == '2':
                n = int(input("Bilangan: "))
                info = number_theory.explain('prime_factors', n)
            elif ch == '3':
                a = int(input("a: "))
                b = int(input("b: "))
                info = number_theory.explain('gcd', a, b)
            elif ch == '4':
                a = int(input("a: "))
                b = int(input("b: "))
                info = number_theory.explain('lcm', a, b)
            elif ch == '5':
                n = int(input("n: "))
                info = number_theory.explain('factorial', n)
            elif ch == '6':
                n = int(input("Jumlah suku: "))
                info = number_theory.explain('fibonacci', n)
            else:
                continue
            _print_explanation_block(info)
        except Exception as e:
            print(f"Error: {e}")
        press_enter_to_continue()

def _tutor_geometry():
    while True:
        clear_screen()
        print("=== Tutor Geometri ===")
        print("1. Luas Lingkaran")
        print("2. Luas Segitiga (alas-tinggi)")
        print("3. Pythagoras")
        print("0. Kembali")
        ch = input("Pilih: ")
        if ch == '0':
            break
        try:
            if ch == '1':
                r = float(input("Jari-jari: "))
                info = geometry.explain('circle_area', r)
            elif ch == '2':
                b = float(input("Alas: "))
                h = float(input("Tinggi: "))
                info = geometry.explain('triangle_area', b, h)
            elif ch == '3':
                a = float(input("Sisi a: "))
                b = float(input("Sisi b: "))
                info = geometry.explain('pythagoras', a, b)
            else:
                continue
            _print_explanation_block(info)
        except Exception as e:
            print(f"Error: {e}")
        press_enter_to_continue()

def _tutor_statistics():
    while True:
        clear_screen()
        print("=== Tutor Statistik ===")
        print("Masukkan data (dipisah spasi) atau kosong untuk kembali")
        data_in = input("Data: ")
        if not data_in.strip():
            break
        try:
            data = [float(x) for x in data_in.split()]
        except ValueError:
            print("Data tidak valid!")
            press_enter_to_continue()
            continue
        print("Pilihan konsep:")
        print("1. Mean  2. Median  3. Mode  4. Varians  5. Standar Deviasi")
        ch = input("Pilih: ")
        mapping = {'1':'mean','2':'median','3':'mode','4':'variance','5':'std'}
        if ch not in mapping:
            continue
        try:
            if mapping[ch] in {'variance','std'}:
                info = statistics.explain(mapping[ch], data, True)
            else:
                info = statistics.explain(mapping[ch], data)
            _print_explanation_block(info)
        except Exception as e:
            print(f"Error: {e}")
        press_enter_to_continue()

def _tutor_algebra():
    while True:
        clear_screen()
        print("=== Tutor Aljabar ===")
        print("1. Persamaan Kuadrat")
        print("2. Sistem Linear 2x2")
        print("3. Determinan 2x2")
        print("0. Kembali")
        ch = input("Pilih: ")
        if ch == '0':
            break
        try:
            if ch == '1':
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                info = algebra.explain('quadratic', a, b, c)
            elif ch == '2':
                a1 = float(input("a1: "))
                b1 = float(input("b1: "))
                c1 = float(input("c1: "))
                a2 = float(input("a2: "))
                b2 = float(input("b2: "))
                c2 = float(input("c2: "))
                info = algebra.explain('system2x2', a1, b1, c1, a2, b2, c2)
            elif ch == '3':
                print("Masukkan matriks 2x2:")
                a11 = float(input("[0,0]: "))
                a12 = float(input("[0,1]: "))
                a21 = float(input("[1,0]: "))
                a22 = float(input("[1,1]: "))
                info = algebra.explain('det2x2', [[a11,a12],[a21,a22]])
            else:
                continue
            _print_explanation_block(info)
        except Exception as e:
            print(f"Error: {e}")
        press_enter_to_continue()

def quiz_mode():
    """Menjalankan kuis adaptif (menggunakan rich jika tersedia)."""
    if not quiz:
        print("Modul kuis tidak tersedia.")
        press_enter_to_continue()
        return
    if not RICH_AVAILABLE:
        print("[INFO] Paket 'rich' tidak terdeteksi. Output akan tanpa warna. Install dengan: pip install rich colorama")
    try:
        rounds_raw = input("Berapa jumlah soal (default 5)? ").strip()
        rounds = int(rounds_raw) if rounds_raw else 5
    except ValueError:
        rounds = 5
    show_exp = input("Tampilkan pembahasan juga untuk jawaban benar? (y/N): ").strip().lower() == 'y'
    use_color = RICH_AVAILABLE
    quiz.run_quiz(rounds=rounds, use_color=use_color, show_explanation_when_correct=show_exp)
    press_enter_to_continue()

def ocr_demo_menu():
    """Demo OCR Matematika"""
    try:
        from modules import ocr_math
        clear_screen()
        print("=== OCR MATEMATIKA DEMO ===")
        print("Status: Conceptual Framework")
        print()
        ocr_math.ocr_demo()
        print()
        print("--- Installation Guide ---")
        guide = ocr_math.get_installation_guide()
        print("Requirements:")
        for req in guide["requirements"][:3]:  # Show first 3
            print(f"  • {req}")
        print("  • ... (dan lainnya)")
        print()
        print("Untuk implementasi penuh, butuh:")
        for dep in guide["system_dependencies"]:
            print(f"  • {dep}")
    except ImportError:
        print("Error: OCR module tidak tersedia")
    press_enter_to_continue()

def advanced_stats_dashboard():
    """Advanced Statistics Dashboard"""
    clear_screen()
    print("=== ADVANCED STATISTICS DASHBOARD ===")
    print()
    print("Fitur yang tersedia:")
    print("1. Kombinatorik & Permutasi")
    print("2. Distribusi Probabilitas")
    print("3. Uji Hipotesis")
    print("4. Regresi & Korelasi")
    print("5. Central Limit Theorem Demo")
    print("0. Kembali")
    
    while True:
        choice = input("\nPilih fitur (0-5): ")
        if choice == "0":
            break
        elif choice == "1":
            _demo_combinatorics()
        elif choice == "2":
            _demo_distributions()
        elif choice == "3":
            _demo_hypothesis_testing()
        elif choice == "4":
            _demo_regression()
        elif choice == "5":
            _demo_clt()
        press_enter_to_continue()

def _demo_combinatorics():
    """Demo kombinatorik"""
    from modules import statistics as stats
    print("\n--- KOMBINATORIK DEMO ---")
    n, r = 10, 3
    print(f"C({n},{r}) = {stats.combination(n, r)}")
    print(f"P({n},{r}) = {stats.permutation(n, r)}")
    print(f"{n}! = {stats.factorial(n)}")

def _demo_distributions():
    """Demo distribusi probabilitas"""
    from modules import statistics as stats
    print("\n--- DISTRIBUSI PROBABILITAS ---")
    print(f"Binomial P(X=3|n=10,p=0.3) = {stats.binomial_probability(10, 3, 0.3):.4f}")
    print(f"Normal PDF(x=0|μ=0,σ=1) = {stats.normal_pdf(0):.4f}")
    print(f"Poisson P(X=2|λ=3) = {stats.poisson_probability(2, 3):.4f}")

def _demo_hypothesis_testing():
    """Demo uji hipotesis"""
    from modules import statistics as stats
    print("\n--- UJI HIPOTESIS ---")
    sample_data = [2.1, 2.5, 2.3, 2.8, 2.4, 2.6, 2.2, 2.7]
    result = stats.t_test_one_sample(sample_data, 2.0)
    print(f"Sample mean: {stats.mean(sample_data):.3f}")
    print(f"t-statistic: {result['t_statistic']:.3f}")
    print(f"Conclusion: {result['conclusion']}")

def _demo_regression():
    """Demo regresi"""
    from modules import statistics as stats
    x_data = [1, 2, 3, 4, 5]
    y_data = [2.1, 4.2, 5.8, 8.1, 10.2]
    result = stats.linear_regression(x_data, y_data)
    print(f"\n--- REGRESI LINEAR ---")
    print(f"Equation: {result['equation']}")
    print(f"R-squared: {result['r_squared']:.4f}")
    print(f"Correlation: {result['correlation']:.4f}")

def _demo_clt():
    """Demo Central Limit Theorem"""
    from modules import statistics as stats
    population = list(range(1, 101))  # 1-100
    result = stats.sampling_distribution_demo(population, 10, 100)
    print(f"\n--- CENTRAL LIMIT THEOREM ---")
    print(f"Population mean: {result['population_mean']:.2f}")
    print(f"Sampling mean: {result['sampling_mean']:.2f}")
    print(f"Theoretical SE: {result['theoretical_se']:.2f}")
    print(f"CLT verified: {result['clt_verification']}")

def geometry_visualizer():
    """Geometry Advanced Features Demo"""
    clear_screen()
    print("=== GEOMETRY VISUALIZER ===")
    print()
    print("Advanced Features:")
    print("1. Law of Sines/Cosines")
    print("2. 3D Geometry")
    print("3. Transformasi Koordinat")
    print("4. Analisis Kurva (Parabola, Ellips)")
    print("0. Kembali")
    
    while True:
        choice = input("\nPilih (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            _demo_triangle_laws()
        elif choice == "2":
            _demo_3d_geometry()
        elif choice == "3":
            _demo_transformations()
        elif choice == "4":
            _demo_curves()
        press_enter_to_continue()

def _demo_triangle_laws():
    """Demo hukum sinus/cosinus"""
    from modules import geometry
    print("\n--- HUKUM SINUS/COSINUS ---")
    # Law of sines
    result_sin = geometry.law_of_sines(a=5, A=30, b=7)
    if "error" not in result_sin:
        print(f"Law of Sines: a={result_sin['a']}, A={result_sin['A']}°, b={result_sin['b']}, B={result_sin.get('B', 'N/A'):.1f}°")
    
    # Law of cosines
    result_cos = geometry.law_of_cosines(a=3, b=4, C=90)
    if "error" not in result_cos:
        print(f"Law of Cosines: c={result_cos['c']:.2f}")

def _demo_3d_geometry():
    """Demo geometri 3D"""
    from modules import geometry
    print("\n--- GEOMETRI 3D ---")
    print(f"Distance 3D (0,0,0) to (3,4,5): {geometry.distance_3d(0,0,0,3,4,5):.2f}")
    print(f"Midpoint 3D: {geometry.midpoint_3d(1,2,3,4,5,6)}")
    print(f"Sphere equation: {geometry.sphere_equation_center_radius((1,2,3), 5)}")

def _demo_transformations():
    """Demo transformasi"""
    from modules import geometry
    print("\n--- TRANSFORMASI ---")
    rotated = geometry.rotate_point_2d(1, 0, 90)
    scaled = geometry.scale_point_2d(2, 3, 2, 0.5)
    print(f"Rotate (1,0) by 90°: ({rotated[0]:.2f}, {rotated[1]:.2f})")
    print(f"Scale (2,3) by (2x, 0.5y): ({scaled[0]:.1f}, {scaled[1]:.1f})")

def _demo_curves():
    """Demo analisis kurva"""
    from modules import geometry
    print("\n--- ANALISIS KURVA ---")
    parabola = geometry.parabola_vertex_form(a=1, h=2, k=-3)
    print(f"Parabola vertex: {parabola['vertex']}")
    print(f"Opens: {parabola['opens']}")
    
    ellipse = geometry.ellipse_standard_form(5, 3)
    print(f"Ellipse area: {ellipse['area']:.2f}")
    print(f"Eccentricity: {ellipse['eccentricity']:.3f}")

def calculus_menu():
    """Menu kalkulus advanced"""
    if not UNIVERSITY_MODULES:
        print("X Calculus module not available. Install dependencies: pip install sympy matplotlib")
        press_enter_to_continue()
        return
        
    while True:
        clear_screen()
        print("=== KALKULUS ADVANCED ===")
        print("1. Turunan Simbolik (Derivatives)")
        print("2. Integral Simbolik (Integrals)")
        print("3. Limit Calculation")
        print("4. Taylor Series Expansion")
        print("5. Critical Points & Optimization")
        print("6. Interactive Derivative Calculator")
        print("7. Interactive Integral Calculator")
        print("8. Demo Calculus Complete")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            try:
                expr = input("Masukkan fungsi f(x): ")
                result = calculus.CalculusEngine().symbolic_derivative(expr)
                if result["success"]:
                    print(f"\nf(x) = {expr}")
                    print(f"f'(x) = {result['derivative']}")
                    print(f"LaTeX: {result['latex']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "2":
            try:
                expr = input("Masukkan fungsi f(x): ")
                result = calculus.CalculusEngine().symbolic_integral(expr)
                if result["success"]:
                    print(f"\nf(x) = {expr}")
                    print(f"∫f(x)dx = {result['integral']}")
                    print(f"LaTeX: {result['latex']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "3":
            try:
                expr = input("Masukkan fungsi f(x): ")
                point = float(input("Limit mendekati nilai: "))
                result = calculus.CalculusEngine().limit_calculation(expr, point)
                if result["success"]:
                    print(f"\nlim(x→{point}) {expr} = {result['limit']}")
                    print(f"Method: {result['method']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "4":
            try:
                expr = input("Masukkan fungsi f(x): ")
                point = float(input("Ekspansi di sekitar x = "))
                order = int(input("Orde ekspansi (default 5): ") or "5")
                result = calculus.CalculusEngine().taylor_series(expr, point, order)
                if result["success"]:
                    print(f"\nTaylor series untuk {expr} di x = {point}:")
                    print(f"T(x) = {result['series']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "5":
            try:
                expr = input("Masukkan fungsi f(x): ")
                result = calculus.CalculusEngine().critical_points(expr)
                if result["success"]:
                    print(f"\nAnalisis untuk f(x) = {expr}")
                    print(f"Critical points: {result['critical_points']}")
                    print(f"Classification: {result['classification']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "6":
            calculus.interactive_derivative()
            press_enter_to_continue()
            
        elif choice == "7":
            calculus.interactive_integral()
            press_enter_to_continue()
            
        elif choice == "8":
            calculus.calculus_demo()
            press_enter_to_continue()
            
        elif choice == "0":
            break

def differential_equations_menu():
    """Menu persamaan diferensial"""
    if not UNIVERSITY_MODULES:
        print("X Differential Equations module not available. Install dependencies: pip install sympy scipy")
        press_enter_to_continue()
        return
        
    while True:
        clear_screen()
        print("=== PERSAMAAN DIFERENSIAL ===")
        print("1. First-Order ODE Solver")
        print("2. Second-Order ODE Solver")
        print("3. Laplace Transform Solution")
        print("4. Numerical ODE Solution")
        print("5. System of ODEs")
        print("6. Basic PDE Solver")
        print("7. Interactive ODE Solver")
        print("8. Demo Differential Equations")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            try:
                eq = input("Masukkan persamaan dy/dx = f(x,y): ")
                var = input("Variable (default y): ") or "y"
                result = differential_equations.DifferentialEquationSolver().solve_first_order_ode(eq, var)
                if result["success"]:
                    print(f"\nSolution: {result['solution']}")
                    print(f"Method: {result['method']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "2":
            try:
                eq = input("Masukkan koefisien a, b, c untuk ay'' + by' + cy = 0")
                a = float(input("a = "))
                b = float(input("b = ")) 
                c = float(input("c = "))
                result = differential_equations.DifferentialEquationSolver().solve_second_order_ode(a, b, c)
                if result["success"]:
                    print(f"\nGeneral solution: {result['general_solution']}")
                    print(f"Characteristic equation: {result['characteristic_equation']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "7":
            differential_equations.interactive_ode_solver()
            press_enter_to_continue()
            
        elif choice == "8":
            differential_equations.differential_equations_demo()
            press_enter_to_continue()
            
        elif choice == "0":
            break

def visualization_3d_menu():
    """Menu visualisasi 3D"""
    if not UNIVERSITY_MODULES:
        print("X 3D Visualization module not available. Install dependencies: pip install matplotlib")
        press_enter_to_continue()
        return
        
    while True:
        clear_screen()
        print("=== VISUALISASI 3D & PLOTTING ===")
        print("1. 3D Function Plotting z = f(x,y)")
        print("2. Parametric Surface Plotting")
        print("3. Vector Field 3D")
        print("4. Contour Plots")
        print("5. Multiple Functions Comparison")
        print("6. Geometric Objects 3D")
        print("7. Interactive 3D Plotter")
        print("8. Demo 3D Visualization")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            try:
                expr = input("Masukkan fungsi z = f(x,y): ")
                viz = visualization_3d.Mathematical3DVisualizer()
                result = viz.plot_3d_function(expr)
                if result["success"]:
                    print(f"\nOK Plot generated for z = {expr}")
                    print(f"Z statistics: {result['z_statistics']}")
                    print("Use plt.show() in interactive environment to display")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "7":
            visualization_3d.interactive_3d_plotter()
            press_enter_to_continue()
            
        elif choice == "8":
            visualization_3d.visualization_demo()
            press_enter_to_continue()
            
        elif choice == "0":
            break

def latex_menu():
    """Menu LaTeX integration"""
    if not UNIVERSITY_MODULES:
        print("X LaTeX module not available. Install dependencies: pip install sympy matplotlib")
        press_enter_to_continue()
        return
        
    while True:
        clear_screen()
        print("=== LaTeX INTEGRATION ===")
        print("1. Expression to LaTeX")
        print("2. Matrix to LaTeX")
        print("3. Equation System to LaTeX")
        print("4. Step-by-Step Calculus LaTeX")
        print("5. Formula Library")
        print("6. LaTeX Document Generator")
        print("7. Interactive LaTeX Converter")
        print("8. Demo LaTeX Integration")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            try:
                expr = input("Masukkan ekspresi matematika: ")
                renderer = latex_renderer.LaTeXMathRenderer()
                result = renderer.expression_to_latex(expr)
                if result["success"]:
                    print(f"\nOriginal: {result['original_expression']}")
                    print(f"LaTeX: ${result['latex']}$")
                    print(f"Type: {result['expression_type']}")
                else:
                    print(f"Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "7":
            latex_renderer.interactive_latex_converter()
            press_enter_to_continue()
            
        elif choice == "8":
            latex_renderer.latex_demo()
            press_enter_to_continue()
            
        elif choice == "0":
            break

def word_problem_menu():
    """Menu word problem solver"""
    if not UNIVERSITY_MODULES:
        print("X Word Problem Solver not available. Install dependencies: pip install sympy")
        press_enter_to_continue()
        return
        
    while True:
        clear_screen()
        print("=== WORD PROBLEM SOLVER ===")
        print("1. Solve Linear Algebra Word Problem")
        print("2. Solve Calculus Optimization Problem")
        print("3. Solve Geometry Problem")
        print("4. Solve Physics Motion Problem")
        print("5. Solve General Math Problem")
        print("6. Interactive Word Problem Solver")
        print("7. Demo Word Problem Solver")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "5":
            try:
                problem_text = input("Describe your math problem in natural language:\n")
                solver = word_problem_solver.MathematicalWordSolver()
                result = solver.solve_word_problem(problem_text)
                
                if result["success"]:
                    print(f"\n✅ PROBLEM SOLVED!")
                    print(f"Type: {result['problem_type']}")
                    if result.get('solution'):
                        print(f"Solution: {result['solution']}")
                    print(f"Explanation: {result['explanation']}")
                    if result.get('steps'):
                        print("\nSteps:")
                        for i, step in enumerate(result['steps'], 1):
                            print(f"  {i}. {step}")
                else:
                    print(f"\nX Error: {result['error']}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
            
        elif choice == "6":
            word_problem_solver.interactive_word_solver()
            press_enter_to_continue()
            
        elif choice == "7":
            word_problem_solver.word_problem_demo()
            press_enter_to_continue()
            
        elif choice == "0":
            break

# EXPERT LEVEL MENU FUNCTIONS
def symbolic_analysis_menu():
    """Menu Symbolic Analysis Engine"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== SYMBOLIC ANALYSIS ENGINE ===")
        print("Advanced symbolic computation for researchers and academics")
        print()
        print("1. Advanced Equation Solving")
        print("2. Symbolic Matrix Operations")
        print("3. Expression Simplification")
        print("4. Series Analysis")
        print("5. Abstract Algebra Operations")
        print("6. Interactive Symbolic Solver")
        print("7. Symbolic Analysis Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Advanced Equation Solving
            print("\n=== ADVANCED EQUATION SOLVING ===")
            equation = input("Masukkan persamaan (contoh: x**2 + 5*x + 6 = 0): ")
            try:
                result = symbolic_analysis.solve_advanced_equation(equation)
                print(f"Solusi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Symbolic Matrix Operations
            print("\n=== SYMBOLIC MATRIX OPERATIONS ===")
            print("1. Matrix Determinant")
            print("2. Matrix Eigenvalues")
            print("3. Matrix Inversion")
            op_choice = input("Pilih operasi (1-3): ")
            try:
                result = symbolic_analysis.matrix_operations_interactive(op_choice)
                print(f"Hasil: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Expression Simplification
            print("\n=== EXPRESSION SIMPLIFICATION ===")
            expr = input("Masukkan ekspresi untuk disederhanakan: ")
            try:
                result = symbolic_analysis.simplify_expression_advanced(expr)
                print(f"Hasil simplifikasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Series Analysis
            print("\n=== SERIES ANALYSIS ===")
            func = input("Masukkan fungsi untuk analisis deret (contoh: sin(x)): ")
            var = input("Variabel (contoh: x): ")
            point = input("Titik ekspansi (contoh: 0): ")
            order = input("Orde deret (contoh: 5): ")
            try:
                result = symbolic_analysis.series_analysis_advanced(func, var, point, int(order))
                print(f"Deret Taylor: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Abstract Algebra Operations
            print("\n=== ABSTRACT ALGEBRA OPERATIONS ===")
            print("1. Group Theory")
            print("2. Ring Operations")
            print("3. Field Theory")
            alg_choice = input("Pilih area (1-3): ")
            try:
                result = symbolic_analysis.abstract_algebra_interactive(alg_choice)
                print(f"Hasil: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            symbolic_analysis.interactive_symbolic_solver()
            press_enter_to_continue()
        elif choice == "7":
            symbolic_analysis.symbolic_analysis_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def number_theory_crypto_menu():
    """Menu Number Theory & Cryptography"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== NUMBER THEORY & CRYPTOGRAPHY ===")
        print("Advanced cryptographic mathematics for researchers")
        print()
        print("1. Prime Generation & Testing")
        print("2. Integer Factorization")
        print("3. RSA Cryptosystem")
        print("4. Modular Arithmetic")
        print("5. Cryptographic Analysis")
        print("6. Interactive Crypto Tool")
        print("7. Number Theory Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Prime Number Analysis
            print("\n=== PRIME NUMBER ANALYSIS ===")
            n = int(input("Masukkan bilangan untuk dianalisis: "))
            try:
                result = number_theory_cryptography.prime_analysis(n)
                print(f"Hasil analisis: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # RSA Encryption
            print("\n=== RSA ENCRYPTION/DECRYPTION ===")
            message = input("Masukkan pesan untuk dienkripsi: ")
            try:
                result = number_theory_cryptography.rsa_demo(message)
                print(f"RSA Demo: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Modular Arithmetic
            print("\n=== MODULAR ARITHMETIC ===")
            a = int(input("Masukkan nilai a: "))
            b = int(input("Masukkan nilai b: "))
            m = int(input("Masukkan modulus m: "))
            try:
                result = number_theory_cryptography.modular_arithmetic_demo(a, b, m)
                print(f"Hasil: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Elliptic Curve Cryptography
            print("\n=== ELLIPTIC CURVE CRYPTOGRAPHY ===")
            try:
                result = number_theory_cryptography.ecc_demo()
                print(f"ECC Demo: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Factorization Methods
            print("\n=== FACTORIZATION METHODS ===")
            n = int(input("Masukkan bilangan untuk difaktorkan: "))
            try:
                result = number_theory_cryptography.factorization_demo(n)
                print(f"Faktorisasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            number_theory_cryptography.interactive_crypto_tool()
            press_enter_to_continue()
        elif choice == "7":
            number_theory_cryptography.number_theory_crypto_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def topology_geometry_menu():
    """Menu Topology & Differential Geometry"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== TOPOLOGY & DIFFERENTIAL GEOMETRY ===")
        print("Advanced geometric analysis for mathematical research")
        print()
        print("1. Manifold Creation & Analysis")
        print("2. Tensor Operations")
        print("3. Differential Forms")
        print("4. Topological Invariants")
        print("5. Curvature Analysis")
        print("6. Interactive Geometry Tool")
        print("7. Topology & Geometry Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Manifold Analysis
            print("\n=== MANIFOLD ANALYSIS ===")
            manifold_type = input("Tipe manifold (sphere, torus, klein): ")
            try:
                result = topology_differential_geometry.manifold_analysis(manifold_type)
                print(f"Analisis manifold: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Tensor Operations
            print("\n=== TENSOR OPERATIONS ===")
            operation = input("Operasi tensor (metric, riemann, einstein): ")
            try:
                result = topology_differential_geometry.tensor_operations(operation)
                print(f"Operasi tensor: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Differential Forms
            print("\n=== DIFFERENTIAL FORMS ===")
            form_degree = int(input("Derajat form (1, 2, 3): "))
            try:
                result = topology_differential_geometry.differential_forms_demo(form_degree)
                print(f"Differential forms: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Topological Invariants
            print("\n=== TOPOLOGICAL INVARIANTS ===")
            space_type = input("Tipe ruang topologi (circle, sphere, torus): ")
            try:
                result = topology_differential_geometry.topological_invariants(space_type)
                print(f"Invariant topologi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Curvature Analysis
            print("\n=== CURVATURE ANALYSIS ===")
            surface = input("Surface untuk analisis (sphere, saddle, cylinder): ")
            try:
                result = topology_differential_geometry.curvature_analysis(surface)
                print(f"Analisis kelengkungan: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            topology_differential_geometry.interactive_geometry_tool()
            press_enter_to_continue()
        elif choice == "7":
            topology_differential_geometry.topology_geometry_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def mathematical_logic_menu():
    """Menu Mathematical Logic & Proof System"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== MATHEMATICAL LOGIC & PROOF SYSTEM ===")
        print("Advanced logical reasoning and automated theorem proving")
        print()
        print("1. Formula Parsing & Analysis")
        print("2. Truth Table Generation")
        print("3. Automated Theorem Proving")
        print("4. Satisfiability Solving")
        print("5. Proof Verification")
        print("6. Interactive Logic Tool")
        print("7. Mathematical Logic Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Formula Parsing & Analysis
            print("\n=== FORMULA PARSING & ANALYSIS ===")
            formula = input("Masukkan formula logika (contoh: (p & q) | ~r): ")
            try:
                result = mathematical_logic_proof_system.parse_formula(formula)
                print(f"Analisis formula: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Truth Table Generation
            print("\n=== TRUTH TABLE GENERATION ===")
            formula = input("Masukkan formula untuk truth table: ")
            try:
                result = mathematical_logic_proof_system.generate_truth_table(formula)
                print(f"Truth table:\n{result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Automated Theorem Proving
            print("\n=== AUTOMATED THEOREM PROVING ===")
            premises = input("Masukkan premis (pisahkan dengan koma): ")
            conclusion = input("Masukkan kesimpulan: ")
            try:
                result = mathematical_logic_proof_system.theorem_proving(premises, conclusion)
                print(f"Hasil pembuktian: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Satisfiability Solving
            print("\n=== SATISFIABILITY SOLVING ===")
            formula = input("Masukkan formula CNF: ")
            try:
                result = mathematical_logic_proof_system.sat_solver(formula)
                print(f"SAT result: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Proof Verification
            print("\n=== PROOF VERIFICATION ===")
            proof_steps = input("Masukkan langkah-langkah proof: ")
            try:
                result = mathematical_logic_proof_system.verify_proof(proof_steps)
                print(f"Verifikasi proof: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            mathematical_logic_proof_system.interactive_logic_tool()
            press_enter_to_continue()
        elif choice == "7":
            mathematical_logic_proof_system.mathematical_logic_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def simulation_modeling_menu():
    """Menu Simulation & Mathematical Modeling"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== SIMULATION & MATHEMATICAL MODELING ===")
        print("Advanced mathematical simulation for complex systems")
        print()
        print("1. Monte Carlo Simulation")
        print("2. Stochastic Processes")
        print("3. Differential Equation Models")
        print("4. Agent-Based Modeling")
        print("5. System Dynamics")
        print("6. Interactive Simulation Tool")
        print("7. Simulation & Modeling Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Monte Carlo Simulation
            print("\n=== MONTE CARLO SIMULATION ===")
            simulation_type = input("Tipe simulasi (pi_estimation, integration, risk): ")
            n_samples = int(input("Jumlah sampel (10000): ") or "10000")
            try:
                result = simulation_mathematical_modeling.monte_carlo_simulation(simulation_type, n_samples)
                print(f"Hasil simulasi Monte Carlo: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Stochastic Processes
            print("\n=== STOCHASTIC PROCESSES ===")
            process = input("Tipe proses (brownian, poisson, markov): ")
            time_horizon = float(input("Horizon waktu (1.0): ") or "1.0")
            try:
                result = simulation_mathematical_modeling.stochastic_simulation(process, time_horizon)
                print(f"Simulasi stokastik: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Differential Equation Models
            print("\n=== DIFFERENTIAL EQUATION MODELS ===")
            model_type = input("Tipe model (predator_prey, sir, lorenz): ")
            try:
                result = simulation_mathematical_modeling.ode_simulation(model_type)
                print(f"Simulasi ODE: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Agent-Based Modeling
            print("\n=== AGENT-BASED MODELING ===")
            n_agents = int(input("Jumlah agen (100): ") or "100")
            n_steps = int(input("Jumlah langkah (1000): ") or "1000")
            try:
                result = simulation_mathematical_modeling.agent_based_simulation(n_agents, n_steps)
                print(f"Simulasi berbasis agen: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # System Dynamics
            print("\n=== SYSTEM DYNAMICS ===")
            system_type = input("Tipe sistem (population, economic, environmental): ")
            try:
                result = simulation_mathematical_modeling.system_dynamics_simulation(system_type)
                print(f"Simulasi dinamika sistem: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            simulation_mathematical_modeling.interactive_simulation_tool()
            press_enter_to_continue()
        elif choice == "7":
            simulation_mathematical_modeling.simulation_modeling_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def algorithm_analysis_menu():
    """Menu Algorithm Analysis & Integration"""
    if not EXPERT_MODULES:
        print("Expert modules not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== ALGORITHM ANALYSIS & INTEGRATION ===")
        print("Advanced computational complexity analysis and optimization")
        print()
        print("1. Complexity Analysis")
        print("2. Algorithm Benchmarking")
        print("3. Performance Optimization")
        print("4. Advanced Data Structures")
        print("5. Algorithm Comparison")
        print("6. Interactive Algorithm Tool")
        print("7. Algorithm Analysis Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Complexity Analysis
            print("\n=== COMPLEXITY ANALYSIS ===")
            algorithm_code = input("Masukkan algoritma untuk dianalisis (atau ketik 'bubble_sort'): ")
            try:
                result = algorithm_analysis_integration.complexity_analysis(algorithm_code)
                print(f"Analisis kompleksitas: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Algorithm Benchmarking
            print("\n=== ALGORITHM BENCHMARKING ===")
            algorithms = input("Algoritma untuk dibenchmark (pisahkan dengan koma): ")
            data_size = int(input("Ukuran data (1000): ") or "1000")
            try:
                result = algorithm_analysis_integration.benchmark_algorithms(algorithms, data_size)
                print(f"Hasil benchmark: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Performance Optimization
            print("\n=== PERFORMANCE OPTIMIZATION ===")
            code_snippet = input("Masukkan kode untuk dioptimasi: ")
            try:
                result = algorithm_analysis_integration.optimize_performance(code_snippet)
                print(f"Saran optimasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Advanced Data Structures
            print("\n=== ADVANCED DATA STRUCTURES ===")
            structure_type = input("Tipe struktur data (heap, trie, graph, btree): ")
            try:
                result = algorithm_analysis_integration.data_structure_demo(structure_type)
                print(f"Demo struktur data: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Algorithm Comparison
            print("\n=== ALGORITHM COMPARISON ===")
            algo1 = input("Algoritma 1: ")
            algo2 = input("Algoritma 2: ")
            try:
                result = algorithm_analysis_integration.compare_algorithms(algo1, algo2)
                print(f"Perbandingan algoritma: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            algorithm_analysis_integration.interactive_algorithm_tool()
            press_enter_to_continue()
        elif choice == "7":
            algorithm_analysis_integration.algorithm_analysis_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def automated_theorem_proving_menu():
    """Menu Automated Theorem Proving"""
    if not RESEARCHER_MODULES.get('automated_theorem_proving', False):
        print("Automated theorem proving module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== AUTOMATED THEOREM PROVING (RESEARCHER LEVEL) ===")
        print("Formal mathematical proof generation and verification")
        print()
        print("1. Automated Proof Generation")
        print("2. Interactive Proof Assistant")
        print("3. Natural Language to Formal Logic")
        print("4. Theorem Discovery Engine")
        print("5. Proof Verification System")
        print("6. Mathematical Logic Demo")
        print("7. Full Researcher Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Automated Proof Generation
            print("\n=== AUTOMATED PROOF GENERATION ===")
            theorem = input("Masukkan teorema untuk dibuktikan: ")
            try:
                result = automated_theorem_proving.generate_proof(theorem)
                print(f"Proof yang dihasilkan: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Interactive Proof Assistant
            print("\n=== INTERACTIVE PROOF ASSISTANT ===")
            try:
                result = automated_theorem_proving.proof_assistant_session()
                print(f"Sesi proof assistant: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Natural Language to Formal Logic
            print("\n=== NATURAL LANGUAGE TO FORMAL LOGIC ===")
            natural_statement = input("Masukkan pernyataan dalam bahasa natural: ")
            try:
                result = automated_theorem_proving.nl_to_formal_logic(natural_statement)
                print(f"Konversi ke logika formal: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Theorem Discovery Engine
            print("\n=== THEOREM DISCOVERY ENGINE ===")
            domain = input("Domain matematika (algebra, geometry, analysis): ")
            try:
                result = automated_theorem_proving.discover_theorems(domain)
                print(f"Teorema yang ditemukan: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Proof Verification System
            print("\n=== PROOF VERIFICATION SYSTEM ===")
            proof_text = input("Masukkan proof untuk diverifikasi: ")
            try:
                result = automated_theorem_proving.verify_proof_formal(proof_text)
                print(f"Hasil verifikasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            automated_theorem_proving.interactive_theorem_prover()
            press_enter_to_continue()
        elif choice == "7":
            automated_theorem_proving.automated_theorem_proving_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def advanced_mathematical_modeling_menu():
    """Menu Advanced Mathematical Modeling"""
    if not RESEARCHER_MODULES.get('advanced_mathematical_modeling', False):
        print("Advanced mathematical modeling module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== ADVANCED MATHEMATICAL MODELING (RESEARCHER LEVEL) ===")
        print("Complex systems simulation and theoretical physics modeling")
        print()
        print("1. Quantum System Simulation")
        print("2. Advanced PDE Solving")
        print("3. Stochastic Differential Equations")
        print("4. Multi-scale Modeling")
        print("5. Uncertainty Quantification")
        print("6. Interactive Modeling Tool")
        print("7. Full Researcher Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Complex System Modeling
            print("\n=== COMPLEX SYSTEM MODELING ===")
            print("1. Population Dynamics")
            print("2. Economic Models")
            print("3. Epidemiological Models")
            model_choice = input("Pilih model (1-3): ")
            try:
                result = advanced_mathematical_modeling.complex_system_modeling(model_choice)
                print(f"Model simulasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Optimization Theory
            print("\n=== OPTIMIZATION THEORY ===")
            objective = input("Masukkan fungsi objektif (contoh: x**2 + y**2): ")
            constraints = input("Masukkan kendala (pisahkan dengan koma): ")
            try:
                result = advanced_mathematical_modeling.optimization_solver(objective, constraints)
                print(f"Solusi optimal: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Stochastic Processes
            print("\n=== STOCHASTIC PROCESSES ===")
            print("1. Random Walk")
            print("2. Markov Chains")
            print("3. Brownian Motion")
            proc_choice = input("Pilih proses (1-3): ")
            steps = int(input("Jumlah langkah simulasi: "))
            try:
                result = advanced_mathematical_modeling.stochastic_process_simulation(proc_choice, steps)
                print(f"Hasil simulasi: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Partial Differential Equations
            print("\n=== PARTIAL DIFFERENTIAL EQUATIONS ===")
            equation_type = input("Tipe PDE (heat, wave, laplace): ")
            boundary = input("Kondisi batas: ")
            try:
                result = advanced_mathematical_modeling.pde_solver_advanced(equation_type, boundary)
                print(f"Solusi PDE: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Quantum Mechanics Simulation
            print("\n=== QUANTUM MECHANICS SIMULATION ===")
            try:
                result = advanced_mathematical_modeling.quantum_system_simulation()
                print(f"Simulasi kuantum berhasil: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            advanced_mathematical_modeling.interactive_advanced_modeling()
            press_enter_to_continue()
        elif choice == "7":
            advanced_mathematical_modeling.advanced_mathematical_modeling_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def mathematical_experimentation_menu():
    """Menu Mathematical Experimentation"""
    if not RESEARCHER_MODULES.get('mathematical_experimentation', False):
        print("Mathematical experimentation module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== MATHEMATICAL EXPERIMENTATION (RESEARCHER LEVEL) ===")
        print("AI-powered pattern discovery and automated conjecture generation")
        print()
        print("1. Large-scale Pattern Discovery")
        print("2. Automated Conjecture Generation")
        print("3. Sequence Analysis Engine")
        print("4. Number Theory Experiments")
        print("5. Statistical Hypothesis Testing")
        print("6. Interactive Experimentation")
        print("7. Full Researcher Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            # Large-scale Pattern Discovery
            print("\n=== LARGE-SCALE PATTERN DISCOVERY ===")
            data_type = input("Tipe data (sequence, matrix, graph): ")
            sample_size = int(input("Ukuran sampel (1000): ") or "1000")
            try:
                result = mathematical_experimentation.pattern_discovery(data_type, sample_size)
                print(f"Pola yang ditemukan: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Automated Conjecture Generation
            print("\n=== AUTOMATED CONJECTURE GENERATION ===")
            domain = input("Domain matematika (number_theory, algebra, geometry): ")
            try:
                result = mathematical_experimentation.generate_conjectures(domain)
                print(f"Konjektur yang dihasilkan: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Sequence Analysis Engine
            print("\n=== SEQUENCE ANALYSIS ENGINE ===")
            sequence = input("Masukkan sequence (pisahkan dengan koma): ")
            try:
                seq_list = [float(x.strip()) for x in sequence.split(',')]
                result = mathematical_experimentation.analyze_sequence(seq_list)
                print(f"Analisis sequence: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Number Theory Experiments
            print("\n=== NUMBER THEORY EXPERIMENTS ===")
            experiment_type = input("Tipe eksperimen (prime_gaps, divisibility, factorization): ")
            n_limit = int(input("Batas atas (10000): ") or "10000")
            try:
                result = mathematical_experimentation.number_theory_experiments(experiment_type, n_limit)
                print(f"Hasil eksperimen: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Statistical Hypothesis Testing
            print("\n=== STATISTICAL HYPOTHESIS TESTING ===")
            hypothesis = input("Masukkan hipotesis untuk diuji: ")
            try:
                result = mathematical_experimentation.statistical_testing(hypothesis)
                print(f"Hasil pengujian: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            # Interactive Experimentation
            print("\n=== INTERACTIVE EXPERIMENTATION ===")
            try:
                result = mathematical_experimentation.interactive_experimentation()
                print(f"Sesi eksperimen interaktif: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "7":
            mathematical_experimentation.mathematical_experimentation_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def researcher_symbolic_analysis_menu():
    """Menu Advanced Symbolic Analysis"""
    if not RESEARCHER_MODULES.get('researcher_symbolic_analysis', False):
        print("Advanced symbolic analysis module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== ADVANCED SYMBOLIC ANALYSIS (RESEARCHER LEVEL - ULTIMATE) ===")
        print("Abstract algebraic structures and categorical mathematics")
        print()
        print("1. Ultra Symbolic Computation")
        print("2. Algebraic Structure Analysis")
        print("3. Category Theory Mathematics")
        print("4. Quantum Algebraic Analysis")
        print("5. Infinite-dimensional Analysis")
        print("6. Automated Symbolic Reasoning")
        print("7. Interactive Symbolic Analysis")
        print("8. Full Researcher Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-8): ")
        
        if choice == "1":
            # Ultra Symbolic Computation
            print("\n=== ULTRA SYMBOLIC COMPUTATION ===")
            expression = input("Masukkan ekspresi simbolik ultra-kompleks: ")
            try:
                result = researcher_symbolic_analysis.ultra_symbolic_computation(expression)
                print(f"Komputasi ultra-simbolik: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            # Algebraic Structure Analysis
            print("\n=== ALGEBRAIC STRUCTURE ANALYSIS ===")
            structure_type = input("Tipe struktur (group, ring, field, module): ")
            try:
                result = researcher_symbolic_analysis.analyze_algebraic_structure(structure_type)
                print(f"Analisis struktur aljabar: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            # Category Theory Mathematics
            print("\n=== CATEGORY THEORY MATHEMATICS ===")
            category_concept = input("Konsep kategori (functor, natural_transformation, adjoint): ")
            try:
                result = researcher_symbolic_analysis.category_theory_analysis(category_concept)
                print(f"Analisis teori kategori: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "4":
            # Quantum Algebraic Analysis
            print("\n=== QUANTUM ALGEBRAIC ANALYSIS ===")
            quantum_system = input("Sistem kuantum (spin, oscillator, field): ")
            try:
                result = researcher_symbolic_analysis.quantum_algebraic_analysis(quantum_system)
                print(f"Analisis aljabar kuantum: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "5":
            # Infinite-dimensional Analysis
            print("\n=== INFINITE-DIMENSIONAL ANALYSIS ===")
            space_type = input("Tipe ruang (hilbert, banach, frechet): ")
            try:
                result = researcher_symbolic_analysis.infinite_dimensional_analysis(space_type)
                print(f"Analisis dimensi tak hingga: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "6":
            # Automated Symbolic Reasoning
            print("\n=== AUTOMATED SYMBOLIC REASONING ===")
            reasoning_problem = input("Masukkan problem untuk symbolic reasoning: ")
            try:
                result = researcher_symbolic_analysis.automated_symbolic_reasoning(reasoning_problem)
                print(f"Hasil reasoning simbolik: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "7":
            researcher_symbolic_analysis.interactive_researcher_symbolic_analysis()
            press_enter_to_continue()
        elif choice == "8":
            researcher_symbolic_analysis.researcher_symbolic_analysis_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def conjecture_generator_menu():
    """Menu Automated Conjecture Generator"""
    if not INNOVATOR_MODULES.get('conjecture_generator', False):
        print("Automated conjecture generator module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== AUTOMATED CONJECTURE GENERATOR (INNOVATOR LEVEL) ===")
        print("AI-powered mathematical conjecture generation and pattern discovery")
        print()
        print("1. Pattern-Based Conjecture Generation")
        print("2. Cross-Domain Pattern Analysis")
        print("3. Sequence Conjecture Discovery")
        print("4. Geometric Pattern Conjectures")
        print("5. Number Theory Conjecture Mining")
        print("6. Interactive Conjecture Workshop")
        print("7. AI Creativity Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            print("\n=== PATTERN-BASED CONJECTURE GENERATION ===")
            domain = input("Domain matematika (algebra, geometry, analysis): ")
            complexity = input("Tingkat kompleksitas (1-5): ")
            try:
                result = conjecture_generator.generate_pattern_conjectures(domain, int(complexity))
                print(f"Dugaan baru: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            print("\n=== CROSS-DOMAIN PATTERN ANALYSIS ===")
            domains = input("Domain gabungan (pisahkan dengan koma): ")
            try:
                result = conjecture_generator.cross_domain_analysis(domains.split(','))
                print(f"Pola lintas domain: {result}")
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "3":
            print("\n=== SEQUENCE CONJECTURE DISCOVERY ===")
            seq_type = input("Tipe urutan (fibonacci, prime, factorial, custom): ")
            from modules.conjecture_generator import discover_sequence_conjectures
            result = discover_sequence_conjectures(seq_type)
            print(result)
            press_enter_to_continue()
        elif choice == "4":
            print("\n=== GEOMETRIC PATTERN CONJECTURES ===")
            geo_type = input("Tipe geometri (triangle, circle, polygon, sphere, custom): ")
            from modules.conjecture_generator import generate_geometric_conjectures
            result = generate_geometric_conjectures(geo_type)
            print(result)
            press_enter_to_continue()
        elif choice == "5":
            print("\n=== NUMBER THEORY CONJECTURE MINING ===")
            nt_area = input("Area teori bilangan (prime, diophantine, modular, custom): ")
            from modules.conjecture_generator import mine_number_theory_conjectures
            result = mine_number_theory_conjectures(nt_area)
            print(result)
            press_enter_to_continue()
        elif choice == "6":
            print("\n=== INTERACTIVE CONJECTURE WORKSHOP ===")
            from modules.conjecture_generator import interactive_conjecture_workshop
            result = interactive_conjecture_workshop()
            print(result)
            press_enter_to_continue()
        elif choice == "7":
            conjecture_generator.conjecture_generator_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Menu tidak valid. Silakan pilih opsi yang tersedia.")
            press_enter_to_continue()

def theoretical_framework_builder_menu():
    """Menu Theoretical Framework Builder"""
    if not INNOVATOR_MODULES.get('theoretical_framework_builder', False):
        print("Theoretical framework builder module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== THEORETICAL FRAMEWORK BUILDER (INNOVATOR LEVEL) ===")
        print("AI-powered construction of new mathematical frameworks")
        print()
        print("1. Axiomatic System Generator")
        print("2. Category Theory Framework Builder")
        print("3. Algebraic Structure Designer") 
        print("4. Topological Space Constructor")
        print("5. Quantum Mathematical Framework")
        print("6. Interactive Framework Designer")
        print("7. Framework Builder Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            print("\n=== AXIOMATIC SYSTEM GENERATOR ===")
            concept = input("Konsep untuk diaksiomatisasi: ")
            try:
                from modules.theoretical_framework_builder import generate_axiomatic_system
                result = generate_axiomatic_system(concept)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            print("\n=== CATEGORY THEORY FRAMEWORK BUILDER ===")
            cat_type = input("Tipe kategori (sets, groups, topspaces, custom): ")
            from modules.theoretical_framework_builder import build_category_framework
            result = build_category_framework(cat_type)
            print(result)
            press_enter_to_continue()
        elif choice == "3":
            print("\n=== ALGEBRAIC STRUCTURE DESIGNER ===")
            struct_name = input("Nama struktur (misal: CommutativeMonoid): ")
            properties = input("Daftar properti (pisahkan dengan koma, misal: commutative, associative, identity): ")
            from modules.theoretical_framework_builder import design_algebraic_structure
            result = design_algebraic_structure(struct_name, properties)
            print(result)
            press_enter_to_continue()
        elif choice == "4":
            print("\n=== TOPOLOGICAL SPACE CONSTRUCTOR ===")
            space_type = input("Tipe ruang (metric, topological, manifold, custom): ")
            from modules.theoretical_framework_builder import construct_topological_space
            result = construct_topological_space(space_type)
            print(result)
            press_enter_to_continue()
        elif choice == "5":
            print("\n=== QUANTUM MATHEMATICAL FRAMEWORK ===")
            quantum_type = input("Tipe quantum (hilbert, operator, field, custom): ")
            from modules.theoretical_framework_builder import build_quantum_framework
            result = build_quantum_framework(quantum_type)
            print(result)
            press_enter_to_continue()
        elif choice == "6":
            print("\n=== INTERACTIVE FRAMEWORK DESIGNER ===")
            from modules.theoretical_framework_builder import interactive_framework_designer
            result = interactive_framework_designer()
            print(result)
            press_enter_to_continue()
        elif choice == "7":
            from modules.theoretical_framework_builder import framework_builder_demo
            framework_builder_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Menu tidak valid. Silakan pilih opsi yang tersedia.")
            press_enter_to_continue()

def interdisciplinary_integrator_menu():
    """Menu Interdisciplinary Integrator"""
    if not INNOVATOR_MODULES.get('interdisciplinary_integrator', False):
        print("Interdisciplinary integrator module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== INTERDISCIPLINARY INTEGRATOR (INNOVATOR LEVEL) ===")
        print("AI-powered integration across mathematical and scientific domains")
        print()
        print("1. Math-Physics Integration")
        print("2. Biology-Mathematics Synthesis")
        print("3. Computer Science-Math Fusion")
        print("4. Economics-Mathematics Bridge")
        print("5. Quantum-Classical Integration")
        print("6. Interactive Integration Workshop")
        print("7. Interdisciplinary Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            print("\n=== CROSS-DOMAIN PATTERN DISCOVERY ===")
            domain1 = input("Domain 1 (e.g., mathematics, physics, biology): ")
            domain2 = input("Domain 2 (e.g., physics, music, economics): ")
            try:
                from modules.interdisciplinary_integrator import discover_cross_domain_patterns
                result = discover_cross_domain_patterns(domain1, domain2)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            print("\n=== BIOLOGY-MATHEMATICS SYNTHESIS ===")
            bio_concept = input("Konsep biologi: ")
            math_concept = input("Konsep matematika: ")
            from modules.interdisciplinary_integrator import synthesize_biology_mathematics
            result = synthesize_biology_mathematics(bio_concept, math_concept)
            print(result)
            press_enter_to_continue()
        elif choice == "3":
            print("\n=== COMPUTER SCIENCE-MATH FUSION ===")
            cs_concept = input("Konsep komputer: ")
            math_concept = input("Konsep matematika: ")
            from modules.interdisciplinary_integrator import integrate_computer_science_math
            result = integrate_computer_science_math(cs_concept, math_concept)
            print(result)
            press_enter_to_continue()
        elif choice == "4":
            print("\n=== ECONOMICS-MATHEMATICS BRIDGE ===")
            econ_concept = input("Konsep ekonomi: ")
            math_concept = input("Konsep matematika: ")
            from modules.interdisciplinary_integrator import build_economics_bridge
            result = build_economics_bridge(econ_concept, math_concept)
            print(result)
            press_enter_to_continue()
        elif choice == "5":
            print("\n=== QUANTUM-CLASSICAL INTEGRATION ===")
            quantum_concept = input("Konsep quantum: ")
            classical_concept = input("Konsep klasik: ")
            from modules.interdisciplinary_integrator import integrate_quantum_classical
            result = integrate_quantum_classical(quantum_concept, classical_concept)
            print(result)
            press_enter_to_continue()
        elif choice == "6":
            print("\n=== INTERACTIVE INTEGRATION WORKSHOP ===")
            from modules.interdisciplinary_integrator import interactive_integration_workshop
            result = interactive_integration_workshop()
            print(result)
            press_enter_to_continue()
        elif choice == "7":
            from modules.interdisciplinary_integrator import interdisciplinary_integration_demo
            interdisciplinary_integration_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Menu tidak valid. Silakan pilih opsi yang tersedia.")
            press_enter_to_continue()

def ai_algorithm_designer_menu():
    """Menu AI Algorithm Designer"""
    if not INNOVATOR_MODULES.get('ai_algorithm_designer', False):
        print("AI algorithm designer module not available!")
        press_enter_to_continue()
        return
    
    while True:
        clear_screen()
        print("=== AI ALGORITHM DESIGNER (INNOVATOR LEVEL) ===")
        print("Self-improving AI algorithms for mathematical discovery")
        print()
        print("1. Meta-Algorithm Generator")
        print("2. Self-Optimizing Networks")
        print("3. Evolutionary Algorithm Designer")
        print("4. Quantum AI Algorithm Builder")
        print("5. Mathematical AI Architect")
        print("6. Interactive AI Designer")
        print("7. AI Designer Demo")
        print("0. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (0-7): ")
        
        if choice == "1":
            print("\n=== NEXT-GENERATION AI DESIGNER ===")
            task_description = input("Deskripsi task AI (e.g., meta learning, architecture search, optimization): ")
            try:
                from modules.ai_algorithm_designer import design_next_generation_ai
                result = design_next_generation_ai(task_description)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            press_enter_to_continue()
        elif choice == "2":
            print("\n=== SELF-OPTIMIZING NETWORKS ===")
            network_type = input("Tipe network (neural, transformer, cnn, custom): ")
            optimization_goal = input("Goal optimasi (accuracy, efficiency, generalization): ")
            from modules.ai_algorithm_designer import design_self_optimizing_networks
            result = design_self_optimizing_networks(network_type, optimization_goal)
            print(result)
            press_enter_to_continue()
        elif choice == "3":
            print("\n=== EVOLUTIONARY ALGORITHM DESIGNER ===")
            evolution_type = input("Tipe evolusi (genetic, particle, differential): ")
            target_domain = input("Domain target (neural, algorithm, mathematics): ")
            from modules.ai_algorithm_designer import create_evolutionary_algorithm_designer
            result = create_evolutionary_algorithm_designer(evolution_type, target_domain)
            print(result)
            press_enter_to_continue()
        elif choice == "4":
            print("\n=== QUANTUM AI ALGORITHM BUILDER ===")
            quantum_feature = input("Fitur quantum (superposition, entanglement, interference, tunneling): ")
            ai_application = input("Aplikasi AI (optimization, machine learning, cryptography, simulation): ")
            from modules.ai_algorithm_designer import build_quantum_ai_algorithm
            result = build_quantum_ai_algorithm(quantum_feature, ai_application)
            print(result)
            press_enter_to_continue()
        elif choice == "5":
            print("\n=== MATHEMATICAL AI ARCHITECT ===")
            math_domain = input("Domain matematika (algebra, analysis, geometry, number theory): ")
            ai_capability = input("Kemampuan AI (theorem proving, conjecture, reasoning, patterns, optimization, cryptography): ")
            from modules.ai_algorithm_designer import design_mathematical_ai_architect
            result = design_mathematical_ai_architect(math_domain, ai_capability)
            print(result)
            press_enter_to_continue()
        elif choice == "6":
            print("\n=== INTERACTIVE AI DESIGNER ===")
            from modules.ai_algorithm_designer import interactive_ai_designer_workshop
            result = interactive_ai_designer_workshop()
            print(result)
            press_enter_to_continue()
        elif choice == "7":
            from modules.ai_algorithm_designer import ai_algorithm_designer_demo
            ai_algorithm_designer_demo()
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Menu tidak valid. Silakan pilih opsi yang tersedia.")
            press_enter_to_continue()

def _visionary_run_pipeline(concept: str = "group", include_conjectures: bool = True) -> str:
    """Run the Visionary Level orchestration pipeline to build a mini-theory and LaTeX doc.

    Steps:
    - Axioms/framework: theoretical_framework_builder
    - Conjectures: conjecture_generator (optional)
    - Proof attempts: automated_theorem_proving (+ logic system optionally)
    - LaTeX artifact: latex_renderer
    """
    try:
        sections = []

        # 1) Generate axiomatic system (and an algebraic structure) using existing builder
        axioms_text = None
        structure_text = None
        if INNOVATOR_MODULES.get('theoretical_framework_builder', False):
            try:
                from modules.theoretical_framework_builder import generate_axiomatic_system, design_algebraic_structure
                axioms_text = generate_axiomatic_system(concept)
                # Also design a small algebraic structure if concept hints algebra
                if concept.lower() in {"group", "ring", "algebra", "monoid", "semigroup"}:
                    structure_text = design_algebraic_structure("CommutativeMonoid", "commutative, associative, identity")
            except Exception as e:
                axioms_text = f"[Axioms generation error: {e}]"
        else:
            axioms_text = "[Theoretical framework builder not available]"

        sections.append({
            "section": f"Axiomatic Basis for {concept.title()}",
            "content": (axioms_text or "") + ("\n\n" + structure_text if structure_text else ""),
            "math": ""
        })

        # 2) Generate a few conjectures (optional)
        conjectures_text = None
        if include_conjectures and INNOVATOR_MODULES.get('conjecture_generator', False):
            try:
                from modules.conjecture_generator import generate_pattern_conjectures
                conj_out = generate_pattern_conjectures("algebra" if concept.lower() != "number_theory" else "number_theory", 3)
                conjectures_text = str(conj_out)
            except Exception as e:
                conjectures_text = f"[Conjecture generation error: {e}]"
        elif include_conjectures:
            conjectures_text = "[Conjecture generator not available]"

        if conjectures_text:
            sections.append({
                "section": "Automated Conjectures", 
                "content": conjectures_text,
                "math": ""
            })

        # 3) Select 3–5 core theorems and attempt proofs
        theorem_statements = [
            # Ensure at least one fully-automated proof (special-cased in module):
            "Sum of two even integers is even",
            # A simple algebraic identity
            "For all x in R, x^2 - 1 = (x - 1)*(x + 1)",
            # Another basic property
            "If a and b are even, then a*b is even",
            # Optional number theory style
            "Odd plus odd equals even"
        ]

        proofs_text_lines = []
        latex_theorem_lines = []
        from datetime import datetime as _dt

        if RESEARCHER_MODULES.get('automated_theorem_proving', False):
            try:
                from modules.automated_theorem_proving import generate_proof
                for th in theorem_statements:
                    proof_result = generate_proof(th)
                    proofs_text_lines.append(proof_result)
            except Exception as e:
                proofs_text_lines.append(f"[Automated theorem proving error: {e}]")
        else:
            proofs_text_lines.append("[Automated theorem proving not available]")

        # Prepare a minimal LaTeX align block of formalized statements
        latex_theorem_lines = [
            r"\forall a,b \in \mathbb{Z}\, (\text{even}(a) \wedge \text{even}(b)) \Rightarrow \text{even}(a+b)",
            r"x^2 - 1 = (x-1)(x+1)",
            r"(\text{even}(a) \wedge \text{even}(b)) \Rightarrow \text{even}(ab)",
            r"(\text{odd}(a) \wedge \text{odd}(b)) \Rightarrow \text{even}(a+b)"
        ]

        sections.append({
            "section": "Core Theorems and Proof Attempts",
            "content": "\n\n".join(proofs_text_lines),
            "math": " \\\n".join(latex_theorem_lines)
        })

        # 4) Generate LaTeX document artifact
        output_file = os.path.join(os.path.dirname(__file__), "visionary_mini_theory.tex")
        if UNIVERSITY_MODULES:
            try:
                renderer = latex_renderer.LaTeXMathRenderer()
                doc = renderer.latex_document_generator(
                    title=f"Mini-Theory: {concept.title()} (Visionary Tracks)",
                    content_sections=sections,
                    output_file=output_file
                )
                doc_status = "✓ LaTeX document generated" if doc.get("success") else f"✗ LaTeX generation error: {doc.get('error')}"
            except Exception as e:
                doc_status = f"✗ LaTeX generation error: {e}"
        else:
            doc_status = "[LaTeX renderer not available — install university deps]"

        # Build a concise summary for console
        summary = []
        summary.append("=== VISIONARY TRACKS — End-to-end Pipeline ===")
        summary.append(f"Concept: {concept}")
        summary.append("")
        summary.append("Sections:")
        for i, s in enumerate(sections, 1):
            summary.append(f"  {i}. {s['section']}")
        summary.append("")
        summary.append(f"Artifact: {doc_status}")
        if "generated" in doc_status.lower():
            summary.append(f"Saved: {output_file}")
        summary.append("")
        summary.append("Theorems included (4):")
        for t in theorem_statements:
            summary.append(f"  • {t}")

        return "\n".join(summary)
    except Exception as e:
        return f"[Visionary pipeline error: {e}]"

def visionary_tracks_menu():
    """Menu for Visionary Level orchestration pipeline."""
    while True:
        clear_screen()
        print("=== LEVEL 6 — VISIONARY TRACKS ===")
        print("Orchestrate existing modules into an end-to-end mini-theory pipeline")
        print()
        print("1. Run Orchestration (custom concept)")
        print("2. Quick Demo (default concept: group)")
        print("0. Kembali ke Menu Utama")

        choice = input("\nPilih menu (0-2): ")
        if choice == "1":
            concept = input("Masukkan konsep utama (misal: group, ring, number_theory): ").strip() or "group"
            include_conj = input("Sertakan generasi konjektur? (Y/n): ").strip().lower()
            include = False if include_conj == 'n' else True
            result = _visionary_run_pipeline(concept, include)
            print(result)
            press_enter_to_continue()
        elif choice == "2":
            result = _visionary_run_pipeline("group", True)
            print(result)
            press_enter_to_continue()
        elif choice == "0":
            break
        else:
            print("Menu tidak valid. Silakan pilih opsi yang tersedia.")
            press_enter_to_continue()

def main():
    """Fungsi utama program"""
    while True:
        clear_screen()
        display_main_menu()
        choice = input("\nPilih menu (0-29, A-C): ").upper()
        
        if choice == "1":
            arithmetic_menu()
        elif choice == "2":
            number_theory_menu()
        elif choice == "3":
            geometry_menu()
        elif choice == "4":
            statistics_menu()
        elif choice == "5":
            algebra_menu()
        elif choice == "6":
            calculus_menu()
        elif choice == "7":
            differential_equations_menu()
        elif choice == "8":
            visualization_3d_menu()
        elif choice == "9":
            latex_menu()
        elif choice == "10":
            word_problem_menu()
        elif choice == "11":
            calculator()
        elif choice == "12":
            demo_all()
            press_enter_to_continue()
        elif choice == "13":
            tutor_mode()
        elif choice == "14":
            quiz_mode()
        elif choice == "15":
            if EXPERT_MODULES.get('symbolic_analysis', False):
                symbolic_analysis_menu()
            else:
                print("\n❌ Symbolic Analysis Engine tidak tersedia!")
                print("Install dependencies: pip install sympy scipy")
                press_enter_to_continue()
        elif choice == "16":
            if EXPERT_MODULES.get('number_theory_cryptography', False):
                number_theory_crypto_menu()
            else:
                print("\n❌ Number Theory & Cryptography tidak tersedia!")
                print("Install dependencies: pip install sympy")
                press_enter_to_continue()
        elif choice == "17":
            if EXPERT_MODULES.get('topology_differential_geometry', False):
                topology_geometry_menu()
            else:
                print("\n❌ Topology & Differential Geometry tidak tersedia!")
                print("Install dependencies: pip install sympy scipy matplotlib")
                press_enter_to_continue()
        elif choice == "18":
            if EXPERT_MODULES.get('mathematical_logic_proof_system', False):
                mathematical_logic_menu()
            else:
                print("\n❌ Mathematical Logic & Proof System tidak tersedia!")
                print("Install dependencies: pip install sympy")
                press_enter_to_continue()
        elif choice == "19":
            if EXPERT_MODULES.get('simulation_mathematical_modeling', False):
                simulation_modeling_menu()
            else:
                print("\n❌ Simulation & Mathematical Modeling tidak tersedia!")
                print("Install dependencies: pip install scipy numpy matplotlib pandas")
                press_enter_to_continue()
        elif choice == "20":
            if EXPERT_MODULES.get('algorithm_analysis_integration', False):
                algorithm_analysis_menu()
            else:
                print("\n❌ Algorithm Analysis & Integration tidak tersedia!")
                print("Install dependencies: pip install numpy matplotlib networkx")
                press_enter_to_continue()
        elif choice == "21":
            if RESEARCHER_MODULES.get('automated_theorem_proving', False):
                automated_theorem_proving_menu()
            else:
                print("\n❌ Automated Theorem Proving tidak tersedia!")
                print("Install dependencies: pip install sympy z3-solver")
                press_enter_to_continue()
        elif choice == "22":
            if RESEARCHER_MODULES.get('advanced_mathematical_modeling', False):
                advanced_mathematical_modeling_menu()
            else:
                print("\n❌ Advanced Mathematical Modeling tidak tersedia!")
                print("Install dependencies: pip install sympy scipy numpy matplotlib")
                press_enter_to_continue()
        elif choice == "23":
            if RESEARCHER_MODULES.get('mathematical_experimentation', False):
                mathematical_experimentation_menu()
            else:
                print("\n❌ Mathematical Experimentation tidak tersedia!")
                print("Install dependencies: pip install scikit-learn pandas numpy sympy")
                press_enter_to_continue()
        elif choice == "24":
            if RESEARCHER_MODULES.get('researcher_symbolic_analysis', False):
                researcher_symbolic_analysis_menu()
            else:
                print("\n❌ Advanced Symbolic Analysis tidak tersedia!")
                print("Install dependencies: pip install sympy scipy")
                press_enter_to_continue()
        elif choice == "25":
            if INNOVATOR_MODULES.get('conjecture_generator', False):
                conjecture_generator_menu()
            else:
                print("\n❌ Automated Conjecture Generator tidak tersedia!")
                print("Install dependencies: pip install tensorflow scikit-learn networkx pandas")
                press_enter_to_continue()
        elif choice == "26":
            if INNOVATOR_MODULES.get('theoretical_framework_builder', False):
                theoretical_framework_builder_menu()
            else:
                print("\n❌ Theoretical Framework Builder tidak tersedia!")
                print("Install dependencies: pip install tensorflow pytorch sympy networkx")
                press_enter_to_continue()
        elif choice == "27":
            if INNOVATOR_MODULES.get('interdisciplinary_integrator', False):
                interdisciplinary_integrator_menu()
            else:
                print("\n❌ Interdisciplinary Integrator tidak tersedia!")
                print("Install dependencies: pip install tensorflow scikit-learn scipy matplotlib")
                press_enter_to_continue()
        elif choice == "28":
            if INNOVATOR_MODULES.get('ai_algorithm_designer', False):
                ai_algorithm_designer_menu()
            else:
                print("\n❌ AI Algorithm Designer tidak tersedia!")
                print("Install dependencies: pip install tensorflow pytorch scikit-learn")
                press_enter_to_continue()
        elif choice == "29":
            visionary_tracks_menu()
        elif choice == "A":
            ocr_demo_menu()
        elif choice == "B":
            advanced_stats_dashboard()
        elif choice == "C":
            geometry_visualizer()
        elif choice == "0":
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid! Gunakan 0-29 atau A-C")
            press_enter_to_continue()

if __name__ == "__main__":
    main()