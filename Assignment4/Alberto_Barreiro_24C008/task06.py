#%% [markdown] 
# **Task 06: Modifying RDF(s)**

# %%


# %%
#%pip install rdflib
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

# %% [markdown]
# Import RDFLib main methods

# %%
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from validation import Report
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

# %% [markdown]
# Create a new class named Researcher

# %%
ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **Task 6.0: Create new prefixes for "ontology" and "person" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.**

# %%
person = Namespace("http://oeg-upm.net/people#") 
ontology = Namespace("http://oeg-upm.net/ontology#")

g.bind('person', person)
g.bind('ontology', ontology)

# %% [markdown]
# **TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under "Vocabulario", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate**
# 

# %%
people = Namespace("http://oeg.fi.upm.es/def/people#")
g.bind("people", people)


person = people.Person
professor = people.Professor
associate = people.AssociateProfessor
interim = people.InterimAssociateProfessor
full = people.FullProfessor

g.add((person, RDF.type, RDFS.Class))
g.add((person, RDFS.label, Literal("Person", datatype=XSD.string)))

g.add((professor, RDF.type, RDFS.Class))
g.add((professor, RDFS.label, Literal("Professor", datatype=XSD.string)))
g.add((professor, RDFS.subClassOf, person))

g.add((associate, RDF.type, RDFS.Class))
g.add((associate, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))
g.add((associate, RDFS.subClassOf, professor))

g.add((interim, RDF.type, RDFS.Class))
g.add((interim, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))
g.add((interim, RDFS.subClassOf, associate))

g.add((full, RDF.type, RDFS.Class))
g.add((full, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))
g.add((full, RDFS.subClassOf, professor))


# Visualize the results
for s, p, o in g:
  print(s,p,o)

# %%
# Validation. Do not remove
r.validate_task_06_01(g)

# %% [markdown]
# **TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)**

# %%
hasName = people.hasName
hasColleague = people.hasColleague
hasHomePage = people.hasHomePage

g.add((hasName, RDF.type, RDF.Property))
g.add((hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
g.add((hasName, RDFS.domain, person))
g.add((hasName, RDFS.range, RDFS.Literal))

g.add((hasColleague, RDF.type, RDFS.subPropertyOf))
g.add((hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))
g.add((hasColleague, RDFS.domain, person))
g.add((hasColleague, RDFS.range, person))

g.add((hasHomePage, RDF.type, RDFS.subPropertyOf))
g.add((hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
g.add((hasHomePage, RDFS.domain, full))
g.add((hasHomePage, RDFS.range, RDFS.Literal))

for s, p, o in g:
  print(s,p,o)

# %%
# Validation. Do not remove
r.validate_task_06_02(g)

# %% [markdown]
# **TASK 6.3: Create the individuals shown in slide 36 under "Datos". Link them with the same relationships shown in the diagram."**

# %%
indiv = Namespace("http://oeg.fi.upm.es/resource/person/")

oscar = indiv.Oscar
asun = indiv.Asun
raul = indiv.Raul
g.add((oscar, RDF.type, full))
g.add((oscar, RDFS.label, Literal("Oscar", datatype=XSD.string)))
g.add((oscar, hasColleague, indiv.Asun))
g.add((oscar, hasName, Literal("Oscar García", datatype=XSD.string)))

g.add((asun, RDF.type, full))
g.add((asun, RDFS.label, Literal("Asun", datatype=XSD.string)))
g.add((asun, hasColleague, oscar))
g.add((asun, hasHomePage, Literal("https://www.oeg-upm.net/", datatype=XSD.string)))

g.add((raul, RDFS.label, Literal("Raul", datatype=XSD.string)))
g.add((raul, RDF.type, interim))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

# %%
r.validate_task_06_03(g)

# %% [markdown]
# **TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually**
# 

# %%
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
foaf = Namespace("http://xmlns.com/foaf/0.1/")

g.add((oscar, vcard.Given, Literal("Oscar", datatype=XSD.string)))
g.add((oscar, vcard.Family, Literal("García", datatype=XSD.string)))
g.add((oscar, foaf.email, Literal("ocorcho@fi.upm.es", datatype=XSD.string)))
for s, p, o in g:
  print(s,p,o)

# %%
# Validation. Do not remove
r.validate_task_06_04(g)
r.save_report("_Task_06")


