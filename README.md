# AML & ADL — Paire 1 — Groupe Paire 1

**Université de Nouakchott — Faculté des Sciences et Techniques**
Master 1 Intelligence Artificielle — 2025/2026

---

## 👥 Groupe

| Nom | Matricule |
|-----|-----------|
| Mohamed Salem Ebnou Echvagha Oubeid | C34613 |
| Fatimata Issa Saw | C21304 |
| Oussama Sid'Ahmed Hedy | C34603 |

**Encadreur :** Dr. Rivea Sadegh

---

## 📚 Modules

| Module | Code | Chapitre |
|--------|------|----------|
| Advanced Machine Learning | C25M1221 | Méthodes d'ensemble (Bagging, Boosting, Stacking) |
| Advanced Deep Learning | C25M1222 | Fondements des réseaux profonds (MLP, Backprop, Dropout) |

---

## 🔑 Fil conducteur

> **Dropout dans les réseaux de neurones = Bagging implicite**
> (Gal & Ghahramani, ICML 2016)

---

## 📁 Structure du dépôt

```
aml-adl-paire1/
├── presentation/
│   └── index.html          # Présentation HTML unique (51 slides)
├── notebooks/
│   ├── 01_notebook_ML.ipynb
│   ├── 02_notebook_DL.ipynb
│   └── 03_notebook_projet_integrateur.ipynb
├── rapports/
│   ├── rapport_ML_DL.pdf
│   └── rapport_projet_integrateur.pdf
├── data/
│   └── .gitkeep
├── images/
│   └── logo_un_fst.png
├── phases.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Utilisation

### Présentation
Ouvrir `presentation/index.html` dans un navigateur moderne (Chrome, Firefox, Edge).

**Navigation :**
- Flèches `←` `→` ou boutons Précédent/Suivant
- Touches `Home` (premier slide) et `End` (dernier slide)
- Menu latéral et onglets de section dans le header

### Notebooks
```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

---

## 🔬 Projet Intégrateur — Pipeline Hybride

```
[Images MNIST 28×28]
       ↓
[MLP Extracteur (PyTorch) — 784→256→128→64]
       ↓
[PCA — 64→50 composantes (85% variance)]
       ↓
[XGBoost — 500 arbres, lr=0.05]
       ↓
[Prédiction + Incertitude MC-Dropout]
```

**Résultats :**
| Modèle | Accuracy |
|--------|----------|
| RF sur pixels bruts | 85.8% |
| XGBoost sur pixels bruts | 90.1% |
| MLP seul | 97.8% |
| **Pipeline hybride** | **98.2%** |

---

## 📖 Références clés

1. Géron (2023) — Hands-On Machine Learning, O'Reilly
2. Goodfellow et al. (2016) — Deep Learning, MIT Press
3. Gal & Ghahramani (2016) — Dropout as Bayesian Approximation, ICML
4. Chen & Guestrin (2016) — XGBoost, KDD
5. Lundberg & Lee (2017) — SHAP, NeurIPS
