import importlib, sys

print("Python:", sys.version[:6])
print("-" * 35)

pkgs = [
    ("numpy",       "numpy"),
    ("sklearn",     "scikit-learn"),
    ("torch",       "torch"),
    ("torchvision", "torchvision"),
    ("xgboost",     "xgboost"),
    ("lightgbm",    "lightgbm"),
    ("shap",        "shap"),
    ("matplotlib",  "matplotlib"),
    ("seaborn",     "seaborn"),
    ("jupyter_core","jupyter"),
    ("ipywidgets",  "ipywidgets"),
    ("gradio",      "gradio"),
]

all_ok = True
for imp, name in pkgs:
    try:
        m = importlib.import_module(imp)
        ver = getattr(m, "__version__", "?")
        print("  OK      " + name.ljust(14) + ver)
    except ImportError:
        print("  MISSING " + name)
        all_ok = False

print("-" * 35)
print("All packages OK!" if all_ok else "Some packages are MISSING — see above.")
