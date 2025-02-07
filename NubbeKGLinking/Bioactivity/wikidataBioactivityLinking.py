import requests
import json
import re
import time

# SPARQL-Abfrage für NubbeKG
nubbe_sparql_query = """
PREFIX nubbe:  <http://nubbekg.aksw.org/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?bioactivity ?bioactivityLabel
WHERE {
  ?bioactivity a nubbe:Bioactivity .
  ?bioactivity rdfs:label ?bioactivityLabel .
}
"""

# URLs der SPARQL-Endpunkte
wikidata_url = "https://query.wikidata.org/sparql"
nubbe_url = "https://nubbekg.aksw.org/sparql"

# Funktion, um Daten von einem SPARQL-Endpunkt abzurufen
# Funktion, um Daten von einem SPARQL-Endpunkt abzurufen
def fetch_sparql_data(query, endpoint, retries=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    for attempt in range(retries):
        response = requests.get(endpoint, params={'query': query, 'format': 'json'}, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            print(f"Fehler 403 bei Anfrage an {endpoint}. Versuche es erneut (Versuch {attempt + 1} von {retries})...")
            time.sleep(5)  # Warte 5 Sekunden, bevor der nächste Versuch gestartet wird
        else:
            print(f"Fehler bei der Anfrage an {endpoint}: {response.status_code}")
            break
    return None
# Abrufen von Nubbe-Daten
def fetch_nubbe_data():
    nubbe_data = fetch_sparql_data(nubbe_sparql_query, nubbe_url)
    return nubbe_data

# Prüfen, ob ein Label in Wikidata existiert und die URI finden
def check_label_in_wikidata(label):
    query = f"""
    SELECT ?bioactivity ?bioactivityLabel WHERE {{
        ?bioactivity rdfs:label "{label}"@en .
        ?bioactivity rdfs:label ?bioactivityLabel .
        FILTER(LANG(?bioactivityLabel) = "en") .
    }}
    """
    data = fetch_sparql_data(query, wikidata_url)
    return data['results']['bindings'] if data and 'results' in data else None

# Funktion zur Anpassung der Label-Bezeichnung
def adjust_label(label):
    match = re.match(r'(?i)^Inhibition of (.+)', label)
    if match:
        print (f"{match.group(1)} inhibitor")
        return f"{match.group(1)} inhibitor"
    return label

# Abrufen der Nubbe-Daten
nubbe_data = fetch_nubbe_data()

# Verarbeite die Nubbe-Daten
if nubbe_data:
    result = []
    count = 1
    nubbe_dict = {}

    # Fasse alle Labels unter einer URI zusammen
    for item in nubbe_data['results']['bindings']:
        bioactivity_uri = item['bioactivity']['value']
        bioactivity_label = item['bioactivityLabel']['value']
        
        # Ignoriere Labels mit "N/A"
        if bioactivity_label == "N/A":
            continue

        # Füge das ursprüngliche Label zur URI hinzu
        if bioactivity_uri not in nubbe_dict:
            nubbe_dict[bioactivity_uri] = bioactivity_label

    # Durchlaufe die Ursprünge und prüfe auf Übereinstimmungen in Wikidata
    for nubbe_uri, nubbe_label in nubbe_dict.items():
        adjusted_label = adjust_label(nubbe_label).lower()
        print(f"Überprüfe Match {count} für URI: {nubbe_uri} mit Label: {adjusted_label}")

        wikidata_matches = check_label_in_wikidata(adjusted_label)

        # Wenn Übereinstimmungen in Wikidata gefunden wurden
        if wikidata_matches:
            for match in wikidata_matches:
                wikidata_uri = match['bioactivity']['value']
                wikidata_label = match['bioactivityLabel']['value']
                result.append({
                    'nubbe_uri': nubbe_uri,
                    'original_label': nubbe_label,
                    'wikidata_uri': wikidata_uri,
                    'wikidata_label': wikidata_label
                })
                print(f"Match gefunden: {wikidata_label} (Wikidata URI: {wikidata_uri})")

        count += 1
        time.sleep(2)

    # Speichern in einer JSON-Datei
    with open('NubbeKGLinking/Bioactivity/merged_bioactivity_uris_wikidata.json', 'w') as f:
        json.dump(result, f, indent=4)

    # Ausgabe der Anzahl der Ergebnisse
    print(f"Es wurden {len(result)} Übereinstimmungen gefunden und gespeichert.")
else:
    print("Es gab ein Problem beim Abrufen der Nubbe-Daten.")
