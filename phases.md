# PHASES DU PROJET — AML & ADL Paire 1

**Groupe :** Mohamed Salem (C34613), Fatimata (C21304), Oussama (C34603)
**Délai :** Mercredi 10 juin → Samedi 13 juin 2026

---

## Phase 1 : Configuration (Jour 1 — Matin)
- [ ] Créer le dépôt GitHub `aml-adl-paire1`
- [ ] Initialiser la structure des dossiers (presentation/, notebooks/, rapports/, data/, images/)
- [ ] Configurer l'environnement Python (`pip install -r requirements.txt`)
- [ ] Vérifier que `presentation/index.html` s'ouvre correctement dans le navigateur

## Phase 2 : Présentation HTML ✅ (Jour 1 — Après-midi)
- [x] Créer `index.html` avec 51 slides (structure complète)
- [x] Navigation (flèches, menu latéral, raccourcis clavier)
- [x] Page de garde avec noms, matricules, encadreur Dr. Rivea Sadegh
- [x] Plan (table des matières cliquable)
- [x] Couleurs université UN-FST (#3A8E5B, #E8B608, #FEEFEE, #D1F2F7)
- [x] KaTeX pour les équations LaTeX
- [x] Chart.js pour les graphiques interactifs
- [x] Responsive (mobile/desktop)

## Phase 3 : Slides ML (Jour 1 — Soir) ✅
- [x] ML-1 : Motivation (Mauritanie, rétinopathie)
- [x] ML-2 : Biais-variance + bullseye SVG
- [x] ML-3/4 : Condorcet (intuition + preuve + graphique)
- [x] ML-5 : Tableau comparatif Bagging/Boosting/Stacking
- [x] ML-6/7 : Bagging + Random Forest (schéma SVG)
- [x] ML-8/9 : AdaBoost + XGBoost/LightGBM
- [x] ML-10 : Stacking (schéma SVG + OOF)
- [x] ML-11 : Code NumPy from scratch
- [x] ML-12/13 : Résultats MNIST + heatmap importances
- [x] ML-14 : Lien DL (Dropout = Bagging) ⭐
- [x] ML-15/16 : Limites + Conclusion ML

## Phase 4 : Slides DL (Jour 2 — Matin) ✅
- [x] DL-1/2 : Perceptron → XOR problem
- [x] DL-3/4 : MLP + Forward propagation
- [x] DL-5/6 : Activations + Fonctions de coût
- [x] DL-7/8/9 : Backpropagation (intuition + équations + code)
- [x] DL-10/11 : SGD + Momentum/Adam
- [x] DL-12/13 : Vanishing gradient + Dropout
- [x] DL-14 : Dropout = Bagging (LE PONT) ⭐
- [x] DL-15/16/17 : Fashion-MNIST + courbes + conclusion

## Phase 5 : Slides Projet (Jour 2 — Midi) ✅
- [x] P-1 : Architecture pipeline hybride (flow diagram)
- [x] P-2 : Pourquoi hybride ?
- [x] P-3/4/5 : Blocs DL + PCA + XGBoost (code)
- [x] P-6/7 : Résultats comparatifs (tableaux + graphiques)
- [x] P-8/9 : SHAP + MC-Dropout
- [x] P-10/11/12 : Équité par classe + Démo + Conclusion projet
- [x] C-1/2/3/4 : Conclusion + Bibliographie + Remerciements

## Phase 6 : Notebooks (Jour 2 — Après-midi)
- [ ] `01_notebook_ML.ipynb` : Condorcet Monte Carlo, Bagging from scratch, comparaisons sklearn
- [ ] `02_notebook_DL.ipynb` : MLP NumPy from scratch, PyTorch, Dropout, Fashion-MNIST
- [ ] `03_notebook_projet_integrateur.ipynb` : Pipeline complet MLP→PCA→XGBoost, SHAP, MC-Dropout

## Phase 7 : Rapports et Finalisation (Jour 2 — Soir)
- [ ] `rapports/rapport_ML_DL.pdf` (4-6 pages : contexte, théorie, expériences)
- [ ] `rapports/rapport_projet_integrateur.pdf` (10-15 pages : pipeline, résultats, discussion)
- [ ] Finaliser `README.md`
- [ ] Push GitHub : `git add . && git commit -m "livraison finale" && git push`
- [ ] Test final : ouvrir `index.html` dans Chrome/Firefox, vérifier tous les slides
- [ ] Préparer la démo en direct (Jupyter ouvert sur slide P-11)

---

## Raccourcis utiles pendant la soutenance

| Touche | Action |
|--------|--------|
| ← / → | Slide précédent / suivant |
| Home | Premier slide (page de garde) |
| End | Dernier slide |
| Cliquer sur Plan | Aller directement à une section |
| Boutons du header | Sauter à ML / DL / Projet / Conclusion |
