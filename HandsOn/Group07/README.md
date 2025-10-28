# Hands-On 1 – Dataset Selection  
### Group 07

**Course:** Data Science (2025–2026)  
**Subject:** Linked Data and Knowledge Graphs  

---

## Group Members
- Carlos Cumbrado (@CarlosCumbrado)

---

## Objective
The goal of this hands-on is to **select an open dataset** that will be used in future assignments to:
- Transform the data into RDF format.  
- Link it with other open datasets.  
- Publish it as Linked Open Data.  
- Build a small application based on it.

---

## Selected Dataset
**Title:** *Calidad del aire. Datos diarios desde 2001 (versión 2024)*  
**Publisher:** Ayuntamiento de Madrid  
**Source:** [Portal de Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/sites/v/index.jsp?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD)  
**Format:** CSV  
**License:** Open Data License (Ayuntamiento de Madrid)  
**Documentation:** *Intérprete de ficheros de datos horarios, diarios y tiempo real – Calidad del Aire* (Ayuntamiento de Madrid, 2024) (https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/Aire/Ficheros/Interprete_ficheros_%20calidad_%20del_%20aire_global.pdf)

---

## Description
This dataset contains **daily air quality measurements** collected from official monitoring stations across Madrid.  
It includes concentrations of key pollutants such as:
- Nitrogen Dioxide (NO₂)  
- Ozone (O₃)  
- Particulate Matter (PM₁₀, PM₂.₅)  
- Sulfur Dioxide (SO₂)  
- Carbon Monoxide (CO)  

Each record includes:
- Station identifiers (`PROVINCIA`, `MUNICIPIO`, `ESTACION`, `PUNTO_MUESTREO`)  
- Pollutant type (`MAGNITUD`)  
- Date (year, month, day)  
- 24 hourly concentration values with validation flags (`D01–D24`, `V01–V24`)
