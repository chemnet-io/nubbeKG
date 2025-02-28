import json
import urllib.parse

# Mapping from state abbreviation to the full state name (as used by DBpedia)
state_mapping = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AM": "Amazonas",
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
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
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
    
    # URL-encode the full name appropriately.
    # Allow some characters like parentheses and underscores that might appear in DBpedia URIs.
    encoded_name = urllib.parse.quote(full_name, safe="()_")
    
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
