import json
import re

# 1. Update data/new_source.json
source_file = '/Users/umidgasimzade/Documents/GitHub/VoteSDA!/data/new_source.json'
with open(source_file, 'r', encoding='utf-8') as f:
    source = json.load(f)

source['name-gov-henrik'] = 'Henrik Vasmer <img alt="Independent Logo" src="assets/images/independent.png" style="height: 32px; width: auto;" title="Independent"/>'
source['role-gov-henrik'] = "Governor Candidate"
source['const-gov-henrik'] = "Cambria"
source['bio-gov-henrik'] = "Independent Candidate for the Governorship of Cambria. He is SDA's endorsed choice."

with open(source_file, 'w', encoding='utf-8') as f:
    json.dump(source, f, indent=2, ensure_ascii=False)

# 2. Update scripts/manual_translations.py
manual_file = '/Users/umidgasimzade/Documents/GitHub/VoteSDA!/scripts/manual_translations.py'
with open(manual_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add new keys before the end of each dictionary block.
# Finding "}" followed by the next section header.

fr_add = '''    "role-gov-henrik": "Candidat au poste de Gouverneur",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Candidat indépendant pour le poste de Gouverneur de Cambria. Il est le choix soutenu par la SDA.",
}'''
content = content.replace("}\n\n# SPANISH", fr_add + "\n\n# SPANISH")

es_add = '''    "role-gov-henrik": "Candidato a Gobernador",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Candidato independiente para la Gobernación de Cambria. Es la elección respaldada por la SDA.",
}'''
content = content.replace("}\n\n# DANISH", es_add + "\n\n# DANISH")

da_add = '''    "role-gov-henrik": "Guvernørkandidat",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Uafhængig kandidat til guvernørposten i Cambria. Han er SDA's støttede valg.",
}'''
content = content.replace("}\n\n# WELSH", da_add + "\n\n# WELSH")

cy_add = '''    "role-gov-henrik": "Ymgeisydd Llywodraethwr",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Ymgeisydd Annibynnol ar gyfer Llywodraethwr Cambria. Ef yw dewis a gefnogir gan yr SDA.",
}'''
content = content.replace("}\n\n# LATVIAN", cy_add + "\n\n# LATVIAN")

lv_add = '''    "role-gov-henrik": "Gubernatora Kandidāts",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Neatkarīgais kandidāts uz Kambrijas gubernatora amatu. Viņš ir SDA atbalstītā izvēle.",
}'''
content = content.replace("}\n\n# GERMAN", lv_add + "\n\n# GERMAN")

de_add = '''    "role-gov-henrik": "Gouverneurskandidat",
    "const-gov-henrik": "Cambria",
    "bio-gov-henrik": "Unabhängiger Kandidat für das Gouverneursamt von Cambria. Er ist die unterstützte Wahl der SDA.",
}'''
content = content.replace("}\n\n# ===== BUILD FINAL DATA", de_add + "\n\n# ===== BUILD FINAL DATA")

with open(manual_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Henrik translations added.")
