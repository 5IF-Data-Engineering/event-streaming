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

<table>
   <tr>
    <th>Endpoint</th>
    <th>Full path</th>
    <th>Method</th>
    <th>Description</th>
    <th>Parameters</th>
  </tr>

  <tr>
    <td rowspan="6">ingestion_weather/</td>
    <td rowspan="6"><code>ingestion_weather/?lat=%s&lon=%s&start_date=%s&end_date=%s&city=%s&daily=%s</code></td>
    <td rowspan="6">GET</td>
    <td rowspan="6">Ingest weather data from the source to the staging area</td>
    <td>lat</td>
  </tr>
    <tr>
        <td>lon</td>
    </tr>
    <tr>
        <td>start_date</td>
    </tr>
    <tr>
        <td>end_date</td>
    </tr>
    <tr>
        <td>city</td>
    </tr>
    <tr>
        <td>daily</td>
    </tr>

  <tr>
    <td rowspan="2">ingestion_bus_delay/</td>
    <td rowspan="2"><code>ingestion_bus_delay/?year=%s&city=%s</code></td>
    <td rowspan="2">GET</td>
    <td rowspan="2">Ingest bus data from the source to the staging area</td>
    <td>year</td>
  </tr>
    <tr>
      <td>city</td>
    </tr>
</table>

## Staging
The staging API is used to process data from the staging area to the production area.

<table>
   <tr>
    <th>Endpoint</th>
    <th>Full path</th>
    <th>Method</th>
    <th>Description</th>
    <th>Parameters</th>
  </tr>

  <tr>
    <td>staging_full_weather/</td>
    <td><code>staging_full_weather/</code></td>
    <td>GET</td>
    <td>Process weather data from the staging area to the production area</td>
    <td></td>
  </tr>

  <tr>
    <td>staging_full_bus_delay/</td>
    <td><code>staging_full_bus_delay/</code></td>
    <td>GET</td>
    <td>Process bus data from the staging area to the production area</td>
    <td></td>
  </tr>
</table>

## Enrichment
The enrichment API is used to enrich data from the production area.

<table>
   <tr>
    <th>Endpoint</th>
    <th>Full path</th>
    <th>Method</th>
    <th>Description</th>
    <th>Parameters</th>
  </tr>

  <tr>
    <td>join_bus_weather/</td>
    <td><code>join_bus_weather/</code></td>
    <td>GET</td>
    <td>Enrich weather data from the production area</td>
    <td></td>  
  </tr>
</table>
