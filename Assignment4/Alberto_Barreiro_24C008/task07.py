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
result = []
for cls in g.subjects(RDF.type, RDFS.Class):
    superclasses = list(g.objects(cls, RDFS.subClassOf))
    if superclasses:
        for sup in superclasses:
            result.append((str(cls), str(sup)))
    else:
        result.append((str(cls), None))
for r in result:
  print(r)

# %%
## Validation: Do not remove
report.validate_07_1a(result)

# %% [markdown]
# **TASK 7.1b: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)**

# %%
query = """
SELECT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""

for r in g.query(query):
  print(r.c, r.sc)


# %%
## Validation: Do not remove
report.validate_07_1b(query,g)

# %% [markdown]
# **TASK 7.2a: List all individuals of "Person" with RDFLib (remember the subClasses). Return the individual URIs in a list called "individuals"**
# 

# %%
people = Namespace("http://oeg.fi.upm.es/def/people#")

def is_subclass_of_person(c):
    if c == people.Person:
        return True
    for _, _, sup in g.triples((c, RDFS.subClassOf, None)):
        if is_subclass_of_person(sup):
            return True
    return False

individuals = []
vistos = set()

for s, p, o in g.triples((None, RDF.type, None)):
    if o == people.Person or is_subclass_of_person(o):
        if s not in vistos:
            vistos.add(s)
            individuals.append(s)

for i in individuals:
    print(i)

# %%
# validation. Do not remove
report.validate_07_02a(individuals)

# %% [markdown]
# **TASK 7.2b: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind**

# %%

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?ind
WHERE {
  ?ind rdf:type ?c .
  ?c rdfs:subClassOf* people:Person .
}
"""
for r in g.query(query):
  print(r.ind)
# Visualize the results

# %%
## Validation: Do not remove
report.validate_07_02b(g, query)

# %% [markdown]
# **TASK 7.3:  List the name and type of those who know Rocky (in SPARQL only). Use name and type as variables in the query**

# %%

query =  """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT ?name ?type
where{
?x people:knows people:Rocky .
?x rdfs:label ?name .
?x a ?type .
}
"""
# Visualize the results
for r in g.query(query):
  print(r.name, r.type)

# %%
## Validation: Do not remove
report.validate_07_03(g, query)

# %% [markdown]
# **Task 7.4: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name**

# %%
query =  """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name WHERE {
    ?x rdfs:label ?name .
    {
        ?x people:hasColleague ?colleague .
        ?z people:ownsPet ?pet .
    } UNION {
        ?x people:hasColleague ?colleague1 .
        ?y people:hasColleague ?colleague2 .
        ?z people:ownsPet ?pet .
    }
}
"""

for r in g.query(query):
  print(r.name)

# TO DO
# Visualize the results

# %%
## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")


