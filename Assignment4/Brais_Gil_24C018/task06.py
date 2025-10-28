
# coding: utf-8

# **Task 06: Modifying RDF(s)**

# In[222]:

#!pip install rdflib
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"


# Import RDFLib main methods

# In[223]:

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from validation import Report
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()


# Create a new class named Researcher

# In[224]:

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **Task 6.0: Create new prefixes for "ontology" and "person" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.**

# In[225]:

# this task is validated in the next step
ontology = Namespace("http://www.oeg-upm.net/Ontology#")
person = Namespace("http://oeg.fi.upm.es/def/people#")
g.namespace_manager.bind('ontology', ontology)
g.namespace_manager.bind('person', person)


# **TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under "Vocabulario", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate**
# 

# In[226]:

# TO DO
#Clases
g.add((person.Person , RDF.type, RDFS.Class))
g.add((person.Professor , RDF.type, RDFS.Class))
g.add((person.FullProfessor , RDF.type, RDFS.Class))
g.add((person.AssociateProfessor , RDF.type, RDFS.Class))
g.add((person.InterimAssociateProfessor , RDF.type, RDFS.Class))

#Etiquetas
g.add((person.Person, RDFS.label, Literal("Person", datatype=XSD.string)))
g.add((person.Professor, RDFS.label, Literal("Professor", datatype=XSD.string)))
g.add((person.FullProfessor, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))
g.add((person.AssociateProfessor, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))
g.add((person.InterimAssociateProfessor, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))

#Subclases
g.add((person.Professor, RDFS.subClassOf, person.Person))
g.add((person.FullProfessor, RDFS.subClassOf, person.Professor))
g.add((person.AssociateProfessor, RDFS.subClassOf, person.Professor))
g.add((person.InterimAssociateProfessor, RDFS.subClassOf, person.AssociateProfessor))



# Visualize the results
for s, p, o in g:
  print(s,p,o)


# In[227]:

# Validation. Do not remove
r.validate_task_06_01(g)


# **TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)**

# In[228]:

# TO DO
#Propiedades
g.add((person.hasName , RDF.type, RDF.Property))
g.add((person.hasHomePage , RDF.type, RDF.Property))
g.add((person.hasColleague , RDF.type, RDF.Property))

#Etiquetas
g.add((person.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
g.add((person.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
g.add((person.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))

#Dominios
g.add((person.hasName, RDFS.domain, person.Person))
g.add((person.hasHomePage, RDFS.domain, person.FullProfessor))
g.add((person.hasColleague, RDFS.domain, person.Person))

#Rangos
g.add((person.hasName, RDFS.range, RDFS.Literal))
g.add((person.hasColleague, RDFS.range, person.Person))
g.add((person.hasHomePage, RDFS.range, RDFS.Literal))

# Visualize the results
for s, p, o in g:
  print(s,p,o)


# In[229]:

# Validation. Do not remove
r.validate_task_06_02(g)


# **TASK 6.3: Create the individuals shown in slide 36 under "Datos". Link them with the same relationships shown in the diagram."**

# In[230]:

# TO DO
data=Namespace("http://oeg.fi.upm.es/resource/person/")

#Instancias
g.add((data.Oscar, RDF.type, person.AssociateProfessor))
g.add((data.Asun, RDF.type, person.FullProfessor))
g.add((data.Raul, RDF.type, person.InterimAssociateProfessor))

#Etiquetas
g.add((data.Oscar, RDFS.label, Literal("Oscar", datatype=XSD.string)))
g.add((data.Asun, RDFS.label, Literal("Asun", datatype=XSD.string)))
g.add((data.Raul, RDFS.label, Literal("Raul", datatype=XSD.string)))

#Propiedades de las instancias
g.add((data.Oscar, person.hasName, Literal("Oscar Corcho García", datatype=RDFS.Literal)))
g.add((data.Oscar, person.hasColleague, data.Asun))
g.add((data.Asun, person.hasColleague, data.Raul))
g.add((data.Asun, person.hasHomePage, Literal("http://www.oeg-upm.net/", datatype=RDFS.Literal)))


# Visualize the results
for s, p, o in g:
  print(s,p,o)


# In[231]:

r.validate_task_06_03(g)


# **TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually**
# 

# In[232]:

# TO DO
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
foaf = Namespace("http://xmlns.com/foaf/0.1/")

#Tipos
g.add((foaf.email , RDF.type, RDFS.Datatype))
g.add((vcard.Family , RDF.type, RDF.Property))
g.add((vcard.Given , RDF.type, RDFS.Datatype))

#Rangos
g.add((foaf.email , RDFS.range, XSD.string))
g.add((vcard.Family , RDFS.range, XSD.string))
g.add((vcard.Given , RDFS.range, XSD.string))

g.add((data.Oscar, foaf.email, Literal("ocorcho@fi.upm.es")))
g.add((data.Oscar, vcard.Family, Literal("Corcho García")))
g.add((data.Oscar, vcard.Given, Literal("Oscar")))


# Visualize the results
for s, p, o in g:
  print(s,p,o)


# In[233]:

# Validation. Do not remove
r.validate_task_06_04(g)
r.save_report("_Task_06")

