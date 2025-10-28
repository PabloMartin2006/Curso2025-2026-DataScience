# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
#!pip install rdflib
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

# %%
from validation import Report

# %% [markdown]
# First let's read the RDF file

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data06.ttl", format="TTL")
report = Report()

# %% [markdown]
# **TASK 7.1a: For all classes, list each classURI. If the class belogs to another class, then list its superclass.**
# **Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called "result". If a class does not have a super class, then return None as the superclass**

# %%
# TO DO
# Visualize the results
result = [] #list of tuples
for s in g.subjects(RDF.type, RDFS.Class):
    superclass = g.value(s, RDFS.subClassOf)
    result.append((s, superclass))
for r in result:
  print(r)

# %%
## Validation: Do not remove
report.validate_07_1a(result)

# %% [markdown]
# **TASK 7.1b: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)**

# %%
query =  """SELECT DISTINCT ?c ?sc WHERE{
?c a rdfs:Class.
OPTIONAL{?c rdfs:subClassOf ?sc}.
}"""

for r in g.query(query):
  print(r.c, r.sc)

# %%
## Validation: Do not remove
report.validate_07_1b(query,g)

# %% [markdown]
# **TASK 7.2a: List all individuals of "Person" with RDFLib (remember the subClasses). Return the individual URIs in a list called "individuals"**
# 

# %%
ns = Namespace("http://oeg.fi.upm.es/def/people#")

# variable to return
individuals = []


revisar = [ns.Person]
revisado = set()

while revisar:
    actual = revisar.pop()
    revisado.add(actual)
    for sc in g.subjects(RDFS.subClassOf, actual):
        if sc not in revisado:
            revisar.append(sc)


for cl in revisado:
    for individuo in g.subjects(RDF.type, cl):
        individuals.append(individuo)

# %%
# validation. Do not remove
report.validate_07_02a(individuals)

# %% [markdown]
# **TASK 7.2b: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind**

# %%
query =  """SELECT DISTINCT ?ind WHERE{
?ind a ?class .
?class rdfs:subClassOf* <http://oeg.fi.upm.es/def/people#Person>.
}"""

for r in g.query(query):
  print(r.ind)

# %%
## Validation: Do not remove
report.validate_07_02b(g, query)

# %% [markdown]
# **TASK 7.3:  List the name and type of those who know Rocky (in SPARQL only). Use name and type as variables in the query**

# %%
query =  """SELECT ?name ?type WHERE{
    ?name <http://oeg.fi.upm.es/def/people#knows> <http://oeg.fi.upm.es/def/people#Rocky>.
    ?name a ?type
  }"""
# Visualize the results
for r in g.query(query):
  print(r.name, r.type)


# %%
## Validation: Do not remove
report.validate_07_03(g, query)

# %% [markdown]
# **Task 7.4: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name**

# %%
query =  """SELECT ?name WHERE {
  ?p1 <http://oeg.fi.upm.es/def/people#ownsPet> ?pet.
  {?name <http://oeg.fi.upm.es/def/people#hasColleague> ?p1}
  UNION
  {?p2 <http://oeg.fi.upm.es/def/people#hasColleague> ?p1. ?name <http://oeg.fi.upm.es/def/people#hasColleague> ?p2.}
}
"""
# TO DO
# Visualize the results

# %%
## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")


