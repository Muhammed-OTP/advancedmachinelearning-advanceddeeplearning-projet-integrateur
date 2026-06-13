# PHASES DU PROJET — AML & ADL Paire 1

**Groupe :** Mohamed Salem (C34613), Fatimata (C21304), Oussama (C34603)  
**Délai :** Mercredi 10 juin → Samedi 13 juin 2026

---

## Phase 1 : Configuration (Jour 1 — Matin)
- [x] Créer le dépôt GitHub `aml-adl-paire1`
- [x] Initialiser la structure des dossiers (presentation/, notebooks/, rapports/, data/, images/)
- [x] Configurer l'environnement Python (`pip install -r requirements.txt`)
- [ ] Vérifier que `presentation/index.html` s'ouvre correctement dans le navigateur

## Phase 2 : Présentation HTML ✅
- [x] Créer `index.html` avec 52+ slides (structure complète)
- [x] Navigation (flèches, menu latéral, raccourcis clavier)
- [x] Page de garde avec noms, matricules, encadreur Dr. Rivea Sadegh
- [x] Plan (table des matières cliquable)
- [x] Couleurs université UN-FST (#3A8E5B, #E8B608, #FEEFEE, #D1F2F7)
- [x] KaTeX pour les équations LaTeX
- [x] Chart.js pour les graphiques interactifs
- [x] Responsive (mobile/desktop)

## Phase 3 : Slides ML ✅
- [x] ML-1 à ML-16 (Condorcet, Bagging, RF, AdaBoost, XGBoost, Stacking, code NumPy, résultats Digits, Dropout=Bagging)

## Phase 4 : Slides DL ✅
- [x] DL-1 à DL-17 (Perceptron, MLP, backprop, Adam, Dropout, Fashion-MNIST, pont ML↔DL)

## Phase 5 : Slides Projet ✅
- [x] P-1 à P-12 (pipeline HAM10000, résultats, SHAP, MC-Bootstrap, démo, conclusion)
- [x] Conclusion + Bibliographie + Remerciements

## Phase 6 : Notebooks
- [x] `01_notebook_ML.ipynb` : Condorcet Monte Carlo, Bagging from scratch, comparaisons sklearn
- [x] `02_notebook_DL.ipynb` : MLP NumPy from scratch, PyTorch, Dropout, Fashion-MNIST
- [x] `03_notebook_projet_integrateur.ipynb` : exécuté, figures dans `images/`, SHAP corrigé

## Phase 7 : Rapports et Finalisation
- [x] `rapports/rapport_ML_DL.pdf` (5 pages : théorie ML/DL + Outils IA)
- [x] `rapports/rapport_projet_integrateur.pdf` (6 pages : pipeline HAM10000 + Outils IA)
- [x] `rapports/generate_rapports.py` (regénération ReportLab)
- [x] `README.md` mis à jour (HAM10000, métriques correctes)
- [ ] Push GitHub : commit + push livrables finaux
- [ ] Test final : parcourir tous les slides dans le navigateur
- [ ] Préparer la démo en direct (Jupyter ouvert sur slide P-11)

---

## Phase 8 : Ajouts soutenance — 13 juin 2026

### Phase 8A : Outils IA ✅
- [x] Slide Outils IA dans `index.html` (slide 51)
- [x] Page Outils IA dans `rapport_ML_DL.pdf`
- [x] Page Outils IA dans `rapport_projet_integrateur.pdf`

### Phase 8B : HAM10000 dans la présentation
- [x] Slides Projet (P-1 à P-12) : HAM10000, 7 classes, résultats 75.8 %
- [ ] (Optionnel) Renommer labels menu ML-12 / DL-15 si jury exige zéro mention MNIST

### Phase 8C : HAM10000 dans les rapports ✅
- [x] `rapport_projet_integrateur.pdf` : dataset, pipeline, résultats HAM10000
- [x] Bibliographie corrigée (refs 2024–2025 vérifiées, fausses refs supprimées)
- [x] `rapport_ML_DL.pdf` : équations et tableaux corrigés

### Phase 8D : Notebook projet intégrateur
- [x] Pipeline MLP→PCA→XGBoost, 42 features, SHAP, MC-Bootstrap, commentaires FR
- [x] Fallback données synthétiques si CSV absent
- [x] Exécuter le notebook et vérifier cohérence des métriques avec rapport/slides (voir note features simulées)

---

## Raccourcis utiles pendant la soutenance

| Touche | Action |
|--------|--------|
| ← / → | Slide précédent / suivant |
| Home | Premier slide (page de garde) |
| End | Dernier slide |
| Cliquer sur Plan | Aller directement à une section |
| Boutons du header | Sauter à ML / DL / Projet / Conclusion |
