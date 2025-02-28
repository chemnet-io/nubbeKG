import json
import urllib.parse

# Mapping from state abbreviation to the full state name (as used by DBpedia)
state_mapping = {
    "AC": "Acre_(state)",
    "AL": "Alagoas",
    "AM": "Amazonas_(Brazilian_state)",
    "AP": "Amapá",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal (Brazil)",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MG": "Minas Gerais",
    "MS": "Mato Grosso do Sul",
    "MT": "Mato Grosso",
    "PA": "Pará",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "PR": "Paraná",
    "RJ": "Rio_de_Janeiro_(state)",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "SC": "Santa_Catarina_(state)",
    "SP": "São_Paulo_(state)",
    "TO": "Tocantins"
}

# File names
input_file = "NubbeKGLinking/State/merged_state_uris_wikidata.json"
output_file = "NubbeKGLinking/State/merged_state_uris_dbpedia.json"

# Load the JSON data from the file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Process each entry in the JSON list
for entry in data:
    # Use the abbreviation as key to get the full state name.
    abbr = entry.get("original_label")
    full_name = state_mapping.get(abbr, abbr)  # fallback to abbreviation if not found

    # Replace every space with an underscore
    dbpedia_name = full_name.replace(" ", "_")
    
    # Optionally, encode the name to handle special characters (while preserving underscores)
    encoded_name = urllib.parse.quote(dbpedia_name, safe="()_")
    
    # Construct the DBpedia URI.
    dbpedia_uri = f"http://dbpedia.org/resource/{encoded_name}"
    
    # Update the entry: add DBpedia URI and label, and optionally remove Wikidata fields.
    entry["dbpedia_uri"] = dbpedia_uri
    entry["dbpedia_label"] = full_name
    entry.pop("wikidata_uri", None)
    entry.pop("wikidata_label", None)

# Write the updated JSON to the output file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated JSON with DBpedia URIs has been written to {output_file}")
