## SPARQL endpoint

At [https://nubbekg.aksw.org/sparql](https://nubbekg.aksw.org/sparql) you will find the SPARQL endpoint for nubbekg.
The backend is provided by [OpenLink Virtuoso](https://virtuoso.openlinksw.com/), while the frontend is provided by [YASGUI](https://yasgui.triply.cc/).

### Rates and limitations

You can make a limited number of connections. The settings can be seen below:

            ResultSetMaxRows           = 25000
            MaxQueryExecutionTime      =   600  (seconds)
            MaxQueryCostEstimationTime =   400  (seconds)
            Connection limit           =    10  (parallel connections per IP address

**ATTENTION**: *The result size is currently limited to 25000 rows. This way partial results are displayed as complete ones and there won't be a HTTP error.*

## SPARQL example queries
The following query gives you formula, name, weight and smile of a compound:
```
PREFIX nubbe:  <http://nubbekg.aksw.org/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?formula ?name ?smiles ?weight WHERE {

?compound a nubbe:Compound .
?compound nubbe:molecularFormula ?formula .
?compound nubbe:commonName ?name .
?compound nubbe:smiles ?smiles .

?compound nubbe:hasDescriptors ?descr .
?molecdescr rdfs:subClassOf ?descr .
?molecdescr nubbe:molecularWeight ?weight .}

LIMIT 100
```
The following query gives you formula and weight of a compound where the weight is between 320.00 and 320.20:
```
PREFIX nubbe:  <http://nubbekg.aksw.org/ontology#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?formula ?name ?smiles ?weight WHERE {

?compound a nubbe:Compound .
?compound nubbe:molecularFormula ?formula .

?compound nubbe:hasDescriptors ?descr .
?molecdescr rdfs:subClassOf ?descr .
?molecdescr nubbe:molecularWeight ?weight .

FILTER (?weight > 320.00 && ?weight < 340.00) .
}
LIMIT 100
```

It is also possible to query without YASGUI, but with a self written script that connects to our endpoint. Below is a example in python with SPARQLWrapper:
```
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "https://nubbekg.aksw.org/sparql"
)
sparql.setReturnFormat(JSON)

sparql.setQuery(
    """
    PREFIX nubbe:  <http://nubbekg.aksw.org/ontology#>
    PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl:  <http://www.w3.org/2002/07/owl#>
    PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

    SELECT DISTINCT ?formula ?name ?smiles ?species ?city ?exinfo WHERE {

    ?compound a nubbe:Compound .
    ?compound nubbe:molecularFormula ?formula .
    ?compound nubbe:commonName ?name .
    ?compound nubbe:smiles ?smiles .

    ?compound nubbe:hasIsolationData ?isolation .
    ?isolation nubbe:obtentionMethod ?exinfo .
    ?isolation nubbe:city ?city .

    ?compound nubbe:isClassifiedBy ?taxa .
    ?taxa nubbe:species ?species .}

    LIMIT 10
    """
)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
```
You can check out a real simple tutorial for SPARQL [here](https://www.w3.org/TR/sparql11-query/):
