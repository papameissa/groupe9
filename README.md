# 📊 Mon Journal d'Humeur - Mini Projet Flask

## 🎯 Description

Une application web interactive pour suivre votre humeur au quotidien ! Enregistrez comment vous vous sentez avec des émojis, ajoutez des notes personnelles et visualisez vos tendances émotionnelles avec des graphiques dynamiques.

## ✨ Fonctionnalités

- ✅ Enregistrement de l'humeur quotidienne avec 6 émojis différents
- 📝 Ajout de notes personnelles optionnelles
- 📅 Historique complet de toutes vos humeurs
- 📈 Statistiques visuelles avec graphiques (camembert et ligne)
- 🗑️ Suppression d'entrées
- 📱 Design responsive et moderne
- 💾 Stockage en JSON (pas besoin de base de données)

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Naviguez dans le dossier du projet**
   ```bash
   cd miniflask
   ```

2. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancez l'application**
   ```bash
   python app.py
   ```

4. **Ouvrez votre navigateur**
   Allez sur : `http://localhost:5000`

## 📖 Comment utiliser l'application

### Page d'accueil
1. Sélectionnez votre humeur du jour en cliquant sur un émoji
2. Ajoutez une note si vous le souhaitez (optionnel)
3. Cliquez sur "Enregistrer mon humeur"
4. Votre humeur apparaît dans l'historique ci-dessous

### Page Statistiques
- Visualisez la répartition de vos humeurs avec un graphique en camembert
- Suivez l'évolution de vos entrées dans le temps
- Consultez le nombre total d'entrées enregistrées

## 📂 Structure du projet

```
miniflask/
│
├── app.py                      # Application Flask principale
├── requirements.txt            # Dépendances Python
├── mood_data.json             # Fichier de données (créé automatiquement)
│
├── templates/
│   ├── index.html             # Page d'accueil
│   └── stats.html             # Page statistiques
│
└── static/
    └── css/
        └── style.css          # Styles CSS
```

## 🎨 Technologies utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, JavaScript
- **Graphiques** : Chart.js
- **Stockage** : JSON

## 🔧 Personnalisation

### Ajouter de nouveaux émojis
Dans `templates/index.html`, section `.mood-selector`, ajoutez :
```html
<input type="radio" name="mood" value="🎉" id="party">
<label for="party" class="mood-option">🎉<span>Festif</span></label>
```

### Modifier les couleurs
Dans `static/css/style.css`, cherchez les valeurs de couleurs (ex: `#667eea`) et modifiez-les selon vos préférences.

## 💡 Idées d'amélioration

Pour aller plus loin avec ce projet, vous pouvez :

1. **Ajouter une authentification** pour avoir plusieurs utilisateurs
2. **Exporter les données** en CSV ou PDF
3. **Ajouter des rappels** pour enregistrer son humeur quotidiennement
4. **Créer une API REST** pour une application mobile
5. **Analyser les patterns** avec du machine learning
6. **Ajouter des catégories** (travail, famille, santé, etc.)
7. **Créer des objectifs** de bien-être
8. **Intégrer la météo** pour voir les corrélations

## 📝 Concepts Flask appris

Ce projet vous apprend :
- ✅ Routing et gestion des URLs
- ✅ Templating avec Jinja2
- ✅ Gestion des formulaires (GET/POST)
- ✅ Fichiers statiques (CSS, JS)
- ✅ JSON pour le stockage de données
- ✅ API REST basique
- ✅ Structure d'un projet Flask

## 🐛 Résolution de problèmes

**L'application ne démarre pas ?**
- Vérifiez que Flask est installé : `pip list | grep Flask`
- Assurez-vous d'être dans le bon dossier

**Le style ne s'affiche pas ?**
- Videz le cache du navigateur (Ctrl + F5)
- Vérifiez que le dossier `static/css` existe

**Les données ne se sauvegardent pas ?**
- Vérifiez les permissions d'écriture dans le dossier
- Le fichier `mood_data.json` devrait se créer automatiquement

## 📚 Ressources pour apprendre

- [Documentation Flask officielle](https://flask.palletsprojects.com/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 🎓 Pour les débutants

Ce projet est parfait pour débuter avec Flask car :
- ✅ Code simple et bien commenté
- ✅ Pas de base de données complexe
- ✅ Interface utilisateur intuitive
- ✅ Concepts Flask essentiels couverts
- ✅ Possibilité d'évolution progressive

---

**Créé avec ❤️ pour apprendre Flask**

Amusez-vous bien avec votre journal d'humeur ! 🎉
