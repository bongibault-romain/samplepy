# Sample Python Project

Projet Python de démonstration avec tests pour SonarQube.

## Installation

```bash
pip install -r requirements.txt
```

## Exécution des tests

```bash
# Tests avec couverture et rapport XML pour SonarQube
pytest --cov=src --cov-report=xml --cov-report=term --junitxml=test-results.xml
```

## Structure du projet

- `src/` : Code source
- `tests/` : Tests unitaires
- `test-results.xml` : Rapport de tests pour SonarQube
- `coverage.xml` : Rapport de couverture pour SonarQube
