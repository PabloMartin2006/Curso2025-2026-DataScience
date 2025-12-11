# Self-Assessment — Hands-on 5

**Criterios cumplidos**
- [x] CSV actualizado con enlaces (`estacionesbicimad-with-links.csv`) ubicado en `/csv`.
- [x] Archivo JSON con las operaciones de OpenRefine (`estacionesbicimad-with-links.json`) en `/openrefine`.
- [x] Mapping actualizado (`mapping-with-links.rml`) en `/mappings`, incluyendo `owl:sameAs`.
- [x] RDF generado (`estacionesbicimad-with-links.ttl`) con al menos un enlace válido a Wikidata.
- [x] Archivo SPARQL (`queries-with-links.sparql`) en `/rdf`, con consultas que usan la ontología y `owl:sameAs`.

**Data Linking**
- [x] Reconciliación realizada en OpenRefine utilizando dirección, nombre y coordenadas.
- [x] Creación de la columna `same_as_wikidata_address` con URIs completas de Wikidata.
- [x] Al menos una estación enlazada correctamente con un recurso externo.
- [x] Uso de OpenRefine para mejorar calidad del matching (columnas auxiliares).

**RML Transformation**
- [x] El mapping se modificó para añadir `owl:sameAs` en el TriplesMap de `bm:Station`.
- [x] Uso correcto de `rr:predicateObjectMap` y `rml:reference`.
- [x] RDF final contiene los triples de enlace y mantiene la estructura del assignment anterior.

**SPARQL Queries**
- [x] Todas las consultas hacen uso de la ontología (`bm:Station`, `bm:name`, `bm:totalBases`, etc.).
- [x] Todas devuelven resultados no vacíos gracias a la existencia de enlaces.
- [x] Todas emplean explícitamente `owl:sameAs ?wikidata`.
- [x] Consultas relevantes para la aplicación, recuperando estaciones enlazadas con datos externos.

**Resumen**
- El dataset fue enriquecido incorporando enlaces a Wikidata.
- La reconciliación, transformación y validación cumplen los requisitos del assignment.
- Los enlaces permiten consultas más completas y demuestran integración de datos.
- Todos los criterios del self-assessment oficial han sido satisfechos.