# Pipeline API
## Table of Contents
- [Introduction](#introduction)
- [API Documentation](#api-documentation)
  - [Ingestion](#ingestion)
  - [Staging](#staging)
  - [Enrichment](#enrichment)

# Introduction
Pipeline API is a Restful API that is built using [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/). The API is used to trigger the data pipeline and to get the status of the data pipeline.

# API Documentation
The API documentation is available at `http://localhost:8000/doc/` after running the API.
Based on the architecture, the API is divided into three parts:
- Ingestion
- Staging
- Enrichment

Base API URL: `http://localhost:8000/`
## Ingestion
The ingestion API is used to ingest data from the source to the staging area.

| Endpoint | Full path                                                                     | Method | Description | Parameters |
| --- |-------------------------------------------------------------------------------|  | --- | --- | --- |
| ingestion_weather/ | `ingestion_weather/?lat=%s&lon=%s&start_date=%s&end_date=%s&city=%s&daily=%s` | GET | Ingest weather data from the source to the staging area | - lat |
| | | | | - lon |
| | | | | - start_date |
| | | | | - end_date |
| | | | | - city |
| | | | | - daily (optional) |
| ingestion_bus_delay/ | `ingestion_bus_delay/?year=%s&city=%s` | GET | Ingest bus data from the source to the staging area | - year |
| | | | | - city |

## Staging
The staging API is used to process data from the staging area to the production area.

| Endpoint | Full path                                                                     | Method | Description | Parameters |
| --- |-------------------------------------------------------------------------------|  | --- | --- | --- |
| staging_full_weather/ | `staging_weather/` | GET | Process weather data from the staging area to the production area |  |
| staging_full_bus_delay/ | `staging_bus_delay/` | GET | Process bus data from the staging area to the production area |  |

## Enrichment
The enrichment API is used to enrich data from the production area.

| Endpoint | Full path                                                                     | Method | Description | Parameters |
| --- |-------------------------------------------------------------------------------|  | --- | --- | --- |
| join_bus_weather/ | `join_bus_weather/` | GET | Enrich weather data from the production area |  |
