"""Fixture pytest pour corriger automatiquement coverage.xml"""
import xml.etree.ElementTree as ET
import pytest


def pytest_sessionfinish(session, exitstatus):
    print("Correction de coverage.xml pour SonarQube...")
    """Hook exécuté après les tests pour corriger coverage.xml"""
    try:
        tree = ET.parse('coverage.xml')
        root = tree.getroot()
        
        # Corriger tous les filename
        for cls in root.findall('.//class'):
            filename = cls.get('filename')
            if filename and not filename.startswith('src/'):
                cls.set('filename', f'src/{filename}')
        
        # Sauvegarder
        tree.write('coverage.xml', encoding='utf-8', xml_declaration=True)
    except FileNotFoundError:
        pass
    except Exception:
        pass
