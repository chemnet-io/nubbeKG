import requests
import json

# SPARQL-Abfrage für DBpedia
dbpedia_sparql_query = """
SELECT ?species ?speciesLabel WHERE {
  ?species rdfs:label ?speciesLabel.
  FILTER(LANG(?speciesLabel) = "en")
}
"""

# SPARQL-Abfrage für NubbeKG
nubbe_sparql_query = """
PREFIX nubbe:  <http://nubbekg.aksw.org/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?species ?speciesLabel
WHERE {
  ?species a nubbe:Species .
  ?species rdfs:label ?speciesLabel .
}
"""

# URLs der SPARQL-Endpunkte
dbpedia_url = "https://dbpedia.org/sparql"
nubbe_url = "https://nubbekg.aksw.org/sparql"

# Funktion, um Daten von einem SPARQL-Endpunkt abzurufen
def fetch_sparql_data(query, endpoint):
    response = requests.get(endpoint, params={'query': query, 'format': 'json'})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler bei der Anfrage an {endpoint}: {response.status_code}")
        return None

# Abrufen von Nubbe-Daten
def fetch_nubbe_data():
    nubbe_data = fetch_sparql_data(nubbe_sparql_query, nubbe_url)
    return nubbe_data

# Prüfen, ob ein Label in DBpedia existiert und die URI finden
def check_label_in_dbpedia(label):
    query = f"""
    SELECT ?species ?speciesLabel WHERE {{
        ?species rdfs:label "{label}"@en .
        ?species rdfs:label ?speciesLabel .
        FILTER(LANG(?speciesLabel) = "en")
    }}
    """
    data = fetch_sparql_data(query, dbpedia_url)
    return data['results']['bindings'] if data and 'results' in data else None

# Abrufen der Nubbe-Daten
nubbe_data = fetch_nubbe_data()

# Verarbeite die Nubbe-Daten
if nubbe_data:
    result = []
    count = 1
    nubbe_dict = {}

    # Fasse alle Labels unter einer URI zusammen
    for item in nubbe_data['results']['bindings']:
        species_uri = item['species']['value']
        species_label = item['speciesLabel']['value']

        # Füge das Label zur URI hinzu
        if species_uri not in nubbe_dict:
            nubbe_dict[species_uri] = []
        nubbe_dict[species_uri].append(species_label)

    # Durchlaufe die Ursprünge und prüfe auf Übereinstimmungen in DBpedia
    for nubbe_uri, nubbe_labels in nubbe_dict.items():
        nubbe_labels_combined = " ".join(nubbe_labels)  # Kombiniere alle Labels der gleichen URI
        print(f"Überprüfe Match {count} für URI: {nubbe_uri} mit Label: {nubbe_labels_combined}")

        dbpedia_matches = check_label_in_dbpedia(nubbe_labels_combined)

        # Wenn Übereinstimmungen in DBpedia gefunden wurden
        if dbpedia_matches:
            for match in dbpedia_matches:
                dbpedia_uri = match['species']['value']
                dbpedia_label = match['speciesLabel']['value']
                result.append({
                    'nubbe_uri': nubbe_uri,
                    'dbpedia_uri': dbpedia_uri,
                    'dbpedia_label': dbpedia_label
                })
                print(f"Match gefunden: {dbpedia_label} (DBpedia URI: {dbpedia_uri})")

        count += 1

    # Speichern in einer JSON-Datei
    with open('NubbeKGLinking/Species/merged_species_uris_dbpedia.json', 'w') as f:
        json.dump(result, f, indent=4)

    # Ausgabe der Anzahl der Ergebnisse
    print(f"Es wurden {len(result)} Übereinstimmungen gefunden und gespeichert.")
else:
    print("Es gab ein Problem beim Abrufen der Nubbe-Daten.")
