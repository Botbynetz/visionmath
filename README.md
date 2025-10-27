# 🎓 Matematika UNIVERSITY LEVEL untuk Programmer

**Comprehensive University-Level Mathematical Computing Suite**

Program interaktif komprehensif yang mengcover matematika dari dasar hingga UNIVERSITY LEVEL. Dilengkapi dengan symbolic computation, 3D visualization, LaTeX integration, dan NLP-powered word problem solver. Dirancang untuk mahasiswa, engineer, dan programmer dengan pendekatan academic rigor dan practical applications.

## 🎯 Philosophy & Features

**CORE MATHEMATICS:**
- 📚 **From Basic to University Level** - Complete mathematical progression
- 🔧 **Algorithm Implementation** - Mathematical algorithms with explanations
- 🎓 **Interactive Learning** - Step-by-step guided problem solving
- 🧩 **Adaptive Assessment** - Smart quiz system with level adjustment

**UNIVERSITY-LEVEL MATHEMATICS:**
- ∫ **Advanced Calculus** - Symbolic derivatives, integrals, limits, Taylor series
- 📊 **Linear Algebra** - Eigenvalues, matrix decompositions, vector spaces
- ∂ **Differential Equations** - ODE/PDE solving, Laplace transforms, numerical methods
- 📈 **3D Visualization** - Function plotting, parametric surfaces, vector fields
- TeX **LaTeX Integration** - Mathematical expression rendering and document generation
- 🤖 **NLP Problem Solver** - Natural language mathematical word problem solving

**ADVANCED FEATURES:**
- � **Symbolic Computation** - SymPy integration for exact mathematical operations
- 📐 **Interactive Visualization** - Matplotlib-based 3D plotting and analysis
- 📝 **Academic Documentation** - LaTeX formula rendering and document export
- 🧠 **Pattern Recognition** - Intelligent problem classification and solving

## 📁 Struktur Proyek

```
├── main.py                       # 🚀 Main application - University Level Menu System
├── quiz_progress.json           # 📊 Progress tracking untuk adaptive quiz
├── requirements.txt            # 📦 Dependencies (sympy, matplotlib, scipy, etc.)
└── modules/                   # 🧮 Mathematical Computation Modules
    ├── arithmetic.py         # ➕ Basic arithmetic + advanced explanations
    ├── number_theory.py      # 🔢 Number theory (primes, factorization, modular)
    ├── geometry.py           # 📐 Geometry & advanced trigonometry  
    ├── statistics.py         # 📈 Statistics & probability theory
    ├── algebra.py            # 🔀 Linear algebra + matrix operations
    ├── calculus.py          # ∫ University calculus (symbolic computation)
    ├── differential_equations.py  # ∂ ODE/PDE solver with Laplace transforms
    ├── visualization_3d.py   # 📈 3D mathematical visualization engine
    ├── latex_renderer.py     # TeX LaTeX integration & rendering
    ├── word_problem_solver.py # 🤖 NLP-powered mathematical problem solver
    ├── quiz.py              # 🎯 Adaptive learning assessment system
    └── ocr_math.py          # 👁️ OCR framework (conceptual demo)
```

## 🚀 Cara Menjalankan

### Prerequisites - University Level Dependencies
```bash
# Core dependencies untuk symbolic computation
pip install sympy numpy scipy matplotlib

# Optional untuk enhanced display
pip install rich colorama pillow
```

### Setup & Run
```powershell
# Method 1: Virtual Environment (Recommended)
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python.exe main.py

# Method 2: Direct Installation
pip install -r requirements.txt
python main.py
```

### Quick Test
```python
# Test university modules installation
python -c "from modules.calculus import CalculusEngine; print('University modules ready!')"
```

## 🌟 Fitur Lengkap

## 📊 MATHEMATICAL MODULES

### **CORE FOUNDATION (High School Level)**

#### 1. ➕ Aritmatika Dasar
- Basic operations (+, -, ×, ÷, mod, power) dengan step explanations
- Temperature conversion, BMI calculator, compound interest
- **Algorithm Focus**: Understanding computational foundations

#### 2. 🔢 Teori Bilangan Advanced
- **Prime Operations**: Sieve of Eratosthenes, primality testing
- **GCD/LCM**: Euclidean algorithm with step visualization  
- **Special Numbers**: Perfect, Armstrong, Fibonacci sequence analysis
- **Cryptography Ready**: Prime factorization, modular arithmetic

#### 3. 📐 Geometri & Trigonometri Advanced
- **2D/3D Geometry**: Complex shapes, ellipsoid volume, frustum calculations
- **Trigonometry**: Law of sines/cosines, trigonometric identities
- **Transformations**: Rotation matrices, scaling, coordinate translation
- **Analytical Geometry**: Parabola, ellipse, hyperbola with complete parameterization

#### 4. 📈 Statistik & Probabilitas Advanced  
- **Descriptive Statistics**: Comprehensive central tendency and dispersion
- **Probability Distributions**: Binomial, Normal, Poisson with PDF/CDF
- **Inferential Statistics**: T-tests, chi-square, regression analysis
- **Advanced Topics**: Correlation analysis, confidence intervals, CLT

#### 5. 🔀 Aljabar Advanced
- **Linear Systems**: 2×2 determinant method, 3×3 Gauss-Jordan elimination
- **Polynomial Operations**: Factorization, binomial expansion, root finding
- **Matrix Operations**: Addition, multiplication, determinants, inverses
- **Advanced Linear Algebra**: Eigenvalues, eigenvectors, matrix decompositions

### **UNIVERSITY LEVEL MATHEMATICS**

#### 6. ∫ Kalkulus Advanced (SymPy-Powered)
- **Symbolic Differentiation**: Chain rule, product rule, quotient rule dengan step explanations
- **Symbolic Integration**: Integration by parts, substitution, partial fractions
- **Limits & Continuity**: L'Hôpital's rule, epsilon-delta definitions  
- **Series Expansion**: Taylor series, Maclaurin series, convergence analysis
- **Multivariable Calculus**: Partial derivatives, gradient, optimization
- **Applications**: Related rates, optimization problems, area/volume calculations

#### 7. ∂ Persamaan Diferensial (Comprehensive ODE/PDE)
- **First-Order ODEs**: Separable, linear, Bernoulli equations
- **Second-Order ODEs**: Characteristic equations, undetermined coefficients
- **Laplace Transforms**: Transform solutions, initial value problems
- **Numerical Methods**: Euler's method, Runge-Kutta, finite differences
- **Systems of ODEs**: Linear systems, eigenvalue methods
- **Partial Differential Equations**: Heat equation, wave equation, Laplace equation
- **Applications**: Population models, physics simulations, engineering problems

#### 8. 📈 Visualisasi 3D & Mathematical Plotting
- **3D Function Plotting**: Surface plots untuk z = f(x,y) dengan custom ranges
- **Parametric Surfaces**: Spheres, cylinders, torus, custom parametric equations  
- **Vector Field Visualization**: 3D vector fields dengan arrow plots
- **Contour Plots**: Level curves, gradient visualization
- **Multiple Function Comparison**: Side-by-side surface plotting
- **Geometric Objects**: Mathematical object rendering (spheres, helixes, etc.)
- **Interactive Features**: Real-time parameter adjustment, zoom, rotation

#### 9. TeX LaTeX Integration & Mathematical Rendering
- **Expression Conversion**: Automatic SymPy to LaTeX conversion
- **Formula Rendering**: Mathematical expression visualization dengan matplotlib
- **Matrix LaTeX**: Professional matrix typesetting (pmatrix, bmatrix, etc.)
- **Equation Systems**: Multi-equation LaTeX formatting
- **Step-by-Step LaTeX**: Calculus operations dengan detailed LaTeX steps
- **Formula Library**: Pre-built LaTeX templates untuk common formulas
- **Document Generation**: Complete LaTeX documents dengan mathematical content
- **Academic Formatting**: Publication-ready mathematical documentation

#### 10. 🤖 Word Problem Solver (NLP-Powered)
- **Natural Language Processing**: Mathematical problem text parsing
- **Problem Classification**: Automatic identification of problem types (algebra, calculus, geometry, physics)
- **Variable Extraction**: Smart variable identification and constraint extraction
- **Equation Generation**: Automatic mathematical model construction
- **Multi-Step Solving**: Integration dengan calculus, algebra, dan differential equation solvers
- **Solution Explanation**: Human-readable step-by-step solutions
- **Problem Types Supported**: Linear algebra, optimization, geometry, physics motion, differential equations
- **Pattern Recognition**: Common problem pattern identification dan template matching

### 🎓 LEARNING FEATURES

#### 8. 👨‍🏫 Tutor Mode Advanced
Mode interaktif untuk belajar konsep matematika secara bertahap:

Kategori yang tersedia:
- Aritmatika (penjumlahan, pembagian, modulus, pangkat, akar, BMI, bunga majemuk)
- Teori Bilangan (prima, faktor prima, GCD, LCM, faktorial, Fibonacci)
- Geometri (luas lingkaran, luas segitiga, Pythagoras)
- Statistik (mean, median, mode, varians, standar deviasi)
- Aljabar (persamaan kuadrat, sistem 2x2, determinan 2x2)

Contoh sesi Tutor Mode (Aritmatika – Penjumlahan):
```
=== Tutor Aritmatika ===
1. Penjumlahan ...
Pilih: 1
Masukkan a: 12
Masukkan b: 7

--- PENJELASAN ---
1. Kita ingin menghitung 12 + 7
2. Penjumlahan menggabungkan dua kuantitas menjadi satu total
3. Hasilnya adalah 19

Hasil: 19
```

Contoh sesi Tutor Mode (Teori Bilangan – GCD):
```
Hitung GCD(48, 18)
GCD(48, 18) → sisa 12
GCD(18, 12) → sisa 6
GCD(12, 6) → sisa 0
Sisa nol → GCD = 6
```

#### 9. 🎯 Kuis Adaptif Enhanced
Fitur evaluasi interaktif dengan level dinamis (1–5). Level naik jika performa konsisten baik (streak ≥ 3 & akurasi ≥ 80%), turun jika banyak salah (2 salah dari 3 terakhir atau akurasi < 40%).

Kategori soal saat ini:
- Aritmatika (operasi dasar, pembagian hasil bulat, pangkat)
- Teori Bilangan (prima, GCD, faktorial)
- Geometri (luas persegi, luas lingkaran, Pythagoras)

Contoh sesi (dipersingkat):
```
=== KUIS ADAPTIF === Level saat ini: 1
Soal 1/5 (aritmatika) : Hitung 7 + 9
Jawaban: 16
Benar!
Level sekarang: 1 | Akurasi: 1/1

Soal 2/5 (teori_bilangan) : Apakah 21 bilangan prima? (ya/tidak)
Jawaban: tidak
Benar!
...
```

Progres disimpan otomatis ke `quiz_progress.json`.

## 🎓 UNIVERSITY-LEVEL EXAMPLES

### Calculus Examples
```python
from modules.calculus import CalculusEngine
calc = CalculusEngine()

# Symbolic differentiation with steps
result = calc.symbolic_derivative("x**3 + sin(x)*cos(x)")
print(f"f'(x) = {result['derivative']}")
print(f"LaTeX: {result['latex']}")

# Integration with techniques
integral = calc.symbolic_integral("x*exp(-x**2)", definite=True, lower_bound=0, upper_bound=1)
print(f"∫₀¹ x·e^(-x²) dx = {integral['numerical_value']}")

# Taylor series expansion
taylor = calc.taylor_series("sin(x)", point=0, order=5)
print(f"sin(x) ≈ {taylor['series']}")
```

### Differential Equations Examples
```python
from modules.differential_equations import DifferentialEquationSolver
de_solver = DifferentialEquationSolver()

# First-order ODE
solution = de_solver.solve_first_order_ode("x + y", "y")
print(f"dy/dx = x + y → y = {solution['solution']}")

# Second-order with characteristic equation
second_order = de_solver.solve_second_order_ode(1, -3, 2)  # y'' - 3y' + 2y = 0
print(f"General solution: {second_order['general_solution']}")
```

### 3D Visualization Examples  
```python
from modules.visualization_3d import Mathematical3DVisualizer
viz = Mathematical3DVisualizer()

# 3D surface plot
surface = viz.plot_3d_function("x**2 + y**2 - 2*x*y", x_range=(-3,3), y_range=(-3,3))

# Vector field visualization
vector_field = viz.vector_field_3d("y", "-x", "z", density=8)

# Parametric surface (sphere)
sphere = viz.parametric_surface("cos(u)*sin(v)", "sin(u)*sin(v)", "cos(v)")
```

### LaTeX Integration Examples
```python
from modules.latex_renderer import LaTeXMathRenderer
latex = LaTeXMathRenderer()

# Expression to LaTeX
expr_latex = latex.expression_to_latex("integrate(sin(x)**2, x)")
print(f"LaTeX: ${expr_latex['latex']}$")

# Matrix to LaTeX  
matrix_latex = latex.matrix_to_latex([[1, 2, 3], [4, 5, 6]], 'bmatrix')
print(f"Matrix: ${matrix_latex['latex']}$")

# Step-by-step calculus
steps = latex.calculus_step_by_step_latex("x**3 + x**2", 'derivative')
for step in steps['steps']:
    print(f"Step: {step['step']}")
    print(f"LaTeX: ${step['latex']}$")
```

### Word Problem Solver Examples
```python
from modules.word_problem_solver import MathematicalWordSolver
solver = MathematicalWordSolver()

# Linear algebra problem
problem1 = "Two numbers have a sum of 15 and difference of 3. Find the numbers."
result1 = solver.solve_word_problem(problem1)
print(f"Problem type: {result1['problem_type']}")
print(f"Solution: {result1['solution']}")

# Calculus optimization
problem2 = "Find the maximum value of f(x) = -x^2 + 4x + 1"
result2 = solver.solve_word_problem(problem2)
print(f"Optimization result: {result2['solution']}")

# Physics motion
problem3 = "A car travels at 60 mph for 2.5 hours. How far does it travel?"
result3 = solver.solve_word_problem(problem3)
print(f"Distance: {result3['solution']['distance']} miles")
```

## 🔧 API Reference

### Direct Module Usage
```python
# Core modules can be used independently
from modules.calculus import CalculusEngine
from modules.differential_equations import DifferentialEquationSolver  
from modules.visualization_3d import Mathematical3DVisualizer
from modules.latex_renderer import LaTeXMathRenderer
from modules.word_problem_solver import MathematicalWordSolver

# Initialize engines
calc = CalculusEngine()
de_solver = DifferentialEquationSolver()
viz = Mathematical3DVisualizer()
latex = LaTeXMathRenderer()
solver = MathematicalWordSolver()

# Use individual methods
derivative = calc.symbolic_derivative("x**3 + 2*x")
ode_solution = de_solver.solve_first_order_ode("x*y", "y")
surface_plot = viz.plot_3d_function("sin(x)*cos(y)")
latex_formula = latex.expression_to_latex("sqrt(x**2 + y**2)")
word_solution = solver.solve_word_problem("Find the area of a circle with radius 5")
```

## 🚀 Advanced Features

- **Symbolic Computation**: Exact mathematical operations using SymPy
- **Numerical Methods**: High-precision floating-point calculations with SciPy
- **3D Visualization**: Interactive mathematical plots with Matplotlib
- **LaTeX Integration**: Publication-ready mathematical documentation
- **NLP Processing**: Natural language mathematical problem understanding
- **Educational Framework**: Step-by-step learning with adaptive assessment
- **Modular Architecture**: Independent mathematical engines for custom integration

## 📈 Performance & Scalability

- **Memory Efficient**: Lazy evaluation for large symbolic expressions
- **Computation Optimization**: Cached results for repeated calculations  
- **Visualization Performance**: Adaptive resolution based on complexity
- **Cross-Platform**: Windows, macOS, Linux compatibility
- **Python 3.8+**: Modern Python features with type hints
 - Penjelasan otomatis untuk setiap soal benar (saat ini hanya salah)

## Dependencies
Tambahkan sebelum menjalankan (jika belum terpasang):
```
pip install -r requirements.txt
```

## Lisensi
Bebas digunakan untuk tujuan edukasi.