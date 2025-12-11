##Task 07: Querying RDF(s)
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"
from validation import Report

##First let's read the RDF file
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data06.ttl", format="TTL")
report = Report()

##TASK 7.1a: For all classes, list each classURI. If the class belogs to another class, then list its superclass. Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called "result". If a class does not have a super class, then return None as the superclass
# TO DO
#Lista classUri
result=[]
for sb in g.subjects(RDF.type, RDFS.Class):
  sc=None
  for Sc in g.objects(sb,RDFS.subClassOf):
    sc=Sc
  result.append((sb,sc))
for cl, sc in result:
   short_c = g.namespace_manager.normalizeUri(cl)
   short_sc = g.namespace_manager.normalizeUri(sc) if sc else None
for r in result:
  print(r)

## Validation: Do not remove
report.validate_07_1a(result)

##TASK 7.1b: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)
query =  "Select ?c ?sc WHERE {?c rdf:type rdfs:Class. OPTIONAL {?c rdfs:subClassOf ?sc.}}"

for r in g.query(query):
  print(r.c, r.sc)

## Validation: Do not remove
report.validate_07_1b(query,g)

##TASK 7.2a: List all individuals of "Person" with RDFLib (remember the subClasses). Return the individual URIs in a list called "individuals"
ns = Namespace("http://oeg.fi.upm.es/def/people#")

# variable to return
individuals = []
def subclases(cl):
  sb=[]
  for s,p,o in g.triples((None,RDFS.subClassOf,cl)):
    sb.append(s)
    sb += subclases(s)
  return sb
clases= subclases(ns.Person)
clases.append(ns.Person)
for cl in clases:
  for s,p,o in g.triples((None,RDF.type,cl)):
    individuals.append(s)
# visualize results
for i in individuals:
  print(i)

# validation. Do not remove
report.validate_07_02a(individuals)

##TASK 7.2b: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind
query =  "SELECT ?ind WHERE{?c rdfs:subClassOf* <http://oeg.fi.upm.es/def/people#Person>. ?ind a ?c}"

for r in g.query(query):
  print(r.ind)
# Visualize the results

## Validation: Do not remove
report.validate_07_02b(g, query)

##TASK 7.3: List the name and type of those who know Rocky (in SPARQL only). Use name and type as variables in the query
query =  """SELECT ?name ?type WHERE{
  ?name <http://oeg.fi.upm.es/def/people#knows> <http://oeg.fi.upm.es/def/people#Rocky>.
  ?name rdf:type ?type.}"""
# TO DO
# Visualize the results
for r in g.query(query):
  print(r.name, r.type)

## Validation: Do not remove
report.validate_07_03(g, query)

##Task 7.4: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name
query =  """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
Select ?name WHERE{
  { ?name people:hasColleague ?c1.
    ?c1 people:ownsPet ?dog.}
    UNION{
    ?name people:hasColleague ?c2.
    ?c2 people:hasColleague ?c3.
    ?c3 people:ownsPet ?dog.}
  }
"""

for r in g.query(query):
  print(r.name)

# TO DO
# Visualize the results

## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")