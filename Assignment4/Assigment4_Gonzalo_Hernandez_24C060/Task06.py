##Task 06: Modifying RDF(s)
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

##Import RDFLib main methods
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from validation import Report
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

##Create a new class named Researcher
ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

##Task 6.0: Create new prefixes for "ontology" and "person" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.
# this task is validated in the next step
ont = Namespace("http://oeg.fi.upm.es/def/ontology#")
per = Namespace("http://oeg.fi.upm.es/def/people#")

##TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under "Vocabulario", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate
# TO DO
#Persona
g.add((per.Person, RDF.type, RDFS.Class))
g.add((per.Person, RDFS.label, Literal("Person", datatype=XSD.string)))
#Profesor
g.add((per.Professor, RDF.type, RDFS.Class))
g.add((per.Professor, RDFS.subClassOf, per.Person))
g.add((per.Professor, RDFS.label, Literal("Professor", datatype=XSD.string)))
#Professor COmpleto
g.add((per.FullProfessor, RDF.type, RDFS.Class))
g.add((per.FullProfessor, RDFS.subClassOf, per.Professor))
g.add((per.FullProfessor, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))
#Profesor Asociado
g.add((per.AssociateProfessor, RDF.type, RDFS.Class))
g.add((per.AssociateProfessor, RDFS.subClassOf, per.Professor))
g.add((per.AssociateProfessor, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))
#Profesor INterino
g.add((per.InterimAssociateProfessor, RDF.type, RDFS.Class))
g.add((per.InterimAssociateProfessor, RDFS.subClassOf, per.AssociateProfessor))
g.add((per.InterimAssociateProfessor, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)
# Validation. Do not remove
r.validate_task_06_01(g)

##TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)
# TO DO
#Propiedad hasName
g.add((per.hasName, RDF.type, RDF.Property))
g.add((per.hasName, RDFS.domain, per.Person))
g.add((per.hasName, RDFS.range, RDFS.Literal))
g.add((per.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
#Propiedad hasColleague
g.add((per.hasColleague, RDF.type, RDF.Property))
g.add((per.hasColleague, RDFS.domain, per.Person))
g.add((per.hasColleague, RDFS.range, per.Person))
g.add((per.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))
#Propiedad hasHomePage
g.add((per.hasHomePage, RDF.type, RDF.Property))
g.add((per.hasHomePage, RDFS.domain, per.FullProfessor))
g.add((per.hasHomePage, RDFS.range, RDFS.Literal))
g.add((per.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation. Do not remove
r.validate_task_06_02(g)

##TASK 6.3: Create the individuals shown in slide 36 under "Datos". Link them with the same relationships shown in the diagram."
# TO DO
#Namespace
data = Namespace("http://oeg.fi.upm.es/resource/person/")
#Oscar
g.add((data.Oscar, RDF.type, per.AssociateProfessor))
g.add((data.Oscar, per.hasColleague, data.Asun))
g.add((data.Oscar, per.hasName, Literal("Oscar Corcho García", datatype=XSD.string)))
g.add((data.Oscar, RDFS.label, Literal("Oscar", datatype=XSD.string)))
#Asun
g.add((data.Asun, RDF.type, per.FullProfessor))
g.add((data.Asun, per.hasColleague, data.Raul))
g.add((data.Asun, per.hasHomePage, Literal("http://www.oeg-upm.net/", datatype=XSD.string)))
g.add((data.Asun, RDFS.label, Literal("Asun", datatype=XSD.string)))
#Raul
g.add((data.Raul, RDF.type, per.InterimAssociateProfessor))
g.add((data.Raul, RDFS.label, Literal("Raul", datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

##TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually
# TO DO
#Namespace
foaf = Namespace("http://xmlns.com/foaf/0.1/")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
#Nuevas relaciones
g.add((vcard.Family, RDF.type, RDF.Property))
g.add((vcard.Family, RDFS.range, XSD.string))
g.add((vcard.Given, RDF.type, RDF.Property))
g.add((vcard.Given, RDFS.range, XSD.string))
g.add((foaf.email, RDF.type, RDFS.Datatype))
g.add((foaf.eamil, RDFS.range, XSD.string))
#Más info de Oscar
g.add((data.Oscar, vcard.Given, Literal("Oscar", datatype=XSD.string)))
g.add((data.Oscar, vcard.Family, Literal("Corcho García", datatype=XSD.string)))
g.add((data.Oscar, foaf.email, Literal("ocorcho@fi.upm.es", datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation. Do not remove
r.validate_task_06_04(g)
r.save_report("_Task_06")