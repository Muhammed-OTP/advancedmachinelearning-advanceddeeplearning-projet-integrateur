# AML & ADL — Paire 1 — Groupe Échvagha

**Université de Nouakchott — Faculté des Sciences et Techniques**  
Master 1 Intelligence Artificielle — 2025/2026

---

## Groupe

| Nom | Matricule |
|-----|-----------|
| Mohamed Salem Ebnou Oubeid | C34613 |
| Fatimata Issa Saw | C21304 |
| Oussama Sid'Ahmed Hedy | C34603 |

**Encadreur :** Dr. Rivea Sadegh  
**Soutenance :** 13 juin 2026

---

## Modules

| Module | Code | Contenu |
|--------|------|---------|
| Advanced Machine Learning | C25M1221 | Bagging, Boosting, Stacking, Condorcet |
| Advanced Deep Learning | C25M1222 | MLP, Backprop, Dropout, Adam |

---

## Fil conducteur

> **Dropout (Deep Learning) = Bagging implicite** — Gal & Ghahramani, ICML 2016

Le projet intégrateur applique ce pont via un pipeline **MLP → PCA → XGBoost** sur **HAM10000** (classification de lésions cutanées, 7 classes).

---

## Structure du dépôt

```
aml-adl-paire1-groupe-echvagha/
├── presentation/
│   └── index.html              # Présentation HTML (52+ slides, KaTeX, Chart.js)
├── notebooks/
│   ├── 01_notebook_ML.ipynb    # Condorcet, Bagging, RF, XGBoost (Digits)
│   ├── 02_notebook_DL.ipynb    # MLP NumPy/PyTorch, Dropout (Fashion-MNIST)
│   └── 03_notebook_projet_integrateur.ipynb  # Pipeline HAM10000
├── rapports/
│   ├── generate_rapports.py    # Génération PDF (ReportLab)
│   ├── rapport_ML_DL.pdf
│   └── rapport_projet_integrateur.pdf
├── data/                       # HAM10000_metadata.csv (optionnel)
├── images/                     # Figures générées par les notebooks
├── phases.md
├── requirements.txt
├── verify_env.py
└── README.md
```

---

## Installation

```bash
# Environnement recommandé (Windows, chemin court)
python -m venv C:\ml_venv
C:\ml_venv\Scripts\activate
pip install -r requirements.txt
python verify_env.py
```

---

## Utilisation

### Présentation

Ouvrir `presentation/index.html` dans Chrome, Firefox ou Edge.

| Touche | Action |
|--------|--------|
| ← / → | Slide précédent / suivant |
| Home / End | Premier / dernier slide |
| Menu latéral | Saut direct à une section |

### Notebooks

```bash
jupyter notebook notebooks/
```

Le notebook `03_notebook_projet_integrateur.ipynb` fonctionne **sans fichiers HAM10000** : il génère des métadonnées et histogrammes de couleur synthétiques calibrés sur la distribution réelle du dataset.

### Rapports PDF

```bash
python rapports/generate_rapports.py
```

---

## Projet intégrateur — HAM10000

```
[HAM10000 : métadonnées + 42 features (6 meta + 36 hist. couleur)]
       ↓
[MLP extracteur sklearn — 42 → 128 → 64]
       ↓
[PCA — 64 → 30 composantes (~85 % variance)]
       ↓
[XGBoost — 300 arbres, lr=0.05]
       ↓
[Prédiction + SHAP + Incertitude MC-Bootstrap]
```

**Résultats (validation, features simulées / rapport) :**

| Modèle | Accuracy |
|--------|----------|
| Random Forest (features brutes) | 54.1 % |
| XGBoost (features brutes) | 62.8 % |
| MLP seul | 73.2 % |
| **Pipeline hybride (MLP+PCA+XGB)** | **75.8 %** |

Classes : MEL, NV, BCC, AKIEC, BKL, DF, VASC

---

## Références clés

1. Tschandl et al. (2018) — HAM10000, *Scientific Data*
2. Gal & Ghahramani (2016) — Dropout as Bayesian Approximation, ICML
3. Chen & Guestrin (2016) — XGBoost, KDD
4. Lundberg & Lee (2017) — SHAP, NeurIPS
5. Thwin & Park (2024) — Deep ensemble on HAM10000, *Appl. Sci.*
6. Fiaz et al. (2025) — Hybrid explainable framework, *Frontiers in Medicine*
