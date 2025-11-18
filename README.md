# AOV_Archive
AOV Archive is a structured archival release of the Arctic Observing Viewer (AOV) application and its supporting data ecosystem.
The repository includes:

The Main AOV Web Application – A React/HTML/CSS/JS map-driven interface.

Scripts – Python utilities for normalizing and preparing AOV datasets.

Related Tables – CSV tables linking AOV institutions and funding agencies to authoritative ROR (Research Organization Registry) identifiers.

Unique Indexes – Curated CSV files listing all unique Agencies, Institutions, and Principal Investigators (PIs), including normalized names, alias lists, and ROR associations.

This README provides a comprehensive overview of the project, including structure, development processes, data standards, and containerization/testing workflows.

Table of Contents

Project Overview

Repository Structure

Main AOV Application

Scripts (Python Utilities)

Related Tables (CSV ROR Mappings)

Unique Indexes

Licensing

Project Overview

The AOV Archive repository preserves the full environment needed to run, test, and understand the AOV visualization ecosystem.
It includes:

A React-based mapping application

Automated testing through Cypress

Dockerized build & test environments

Python data-curation pipelines

Comprehensive mapping of institutions and agencies to ROR identifiers

Normalized indexes for core contributors (PIs, Agencies, Institutions)

Repository Structure
AOV-Archived/
│
├── aov-app/                # Main AOV React/HTML/CSS/JS application
│   ├── client/
│   ├── cypress/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── Makefile
│
├── scripts/                # Python scripts for data normalization & curation
│   ├── find_unique_values.py
│   ├── normalize_Fields.py
│   ├── sort_by_alph.py
│
├── related_tables/         # ROR mapping tables for institutions/agencies
│   ├── institution_ROR.csv
│   ├── agency_ROR.csv
│
├── unique_Tables/         # Unique normalized lists of names w/ ROR + aliases
│   ├── agency_Unique.csv
│   ├── institution_Unique.csv
│   ├── ORCID_Unique.csv
│
└── README.md

Main AOV Application


The AOV client application is a modern React-based mapping tool, tested with Cypress and containerized via Docker.
Make commands are used to streamline everything from installation to testing to deployment.

Prerequisites

You will need:

Docker

Docker Compose

Node.js

npm

Install the application dependencies:

make install-app

Setup

Clone and install:

git clone <repository-url>
cd <repository-directory>
make install-app

Pre-Commit Checks

Before committing, run:

make test-app


This runs:

Code formatting

License header checks

Lint & type checks

Client tests

Cypress E2E tests (Dockerized)

Snapshot cleanup

Client Commands
make develop
make build
make install-client
make test-lint
make test-types

Cypress E2E Commands
make open-test
make install-e2e-cypress
make test-e2e-cypress
make clean-snapshots

Docker Commands
make docker-build
make test-e2e
make test-e2e-image-snapshots-update


The complete E2E cycle with snapshot updates:

make test-e2e-image-snapshots-update

Scripts (Python Utilities)

The scripts/ folder contains Python utilities used for data preparation before ingestion into the AOV application.

Typical operations include:

Normalizing field names

Cleaning inconsistent or malformed entries

Standardizing institution & agency names

Validating and fixing geometry data

Mapping entries to ROR identifiers

Preparing final datasets for production use

Related Tables (CSV ROR Mappings)

These tables map institutions and funding agencies found in the AOV dataset to their authoritative entries in the Research Organization Registry (ROR).

Each table typically includes:

Normalized name

Site_ID (to form the link between site and agency/institution)

ROR ID

These mappings ensure consistency across the full visualization ecosystem.

Unique Indexes

The unique-indexes/ folder contains comprehensive lists of all unique Institutions, Funding Agencies, and Principal Investigators found across the AOV dataset.

Each CSV includes:

✔ Canonical (normalized) name
✔ All known aliases (as used across datasets)
✔ ROR ID, when applicable
✔ Boolean flag indicating whether a ROR exists

This index is used to:

De-duplicate inconsistent naming conventions

Support automated ROR matching

Maintain stable referential keys across the dataset

Improve search, filtering, and visualization accuracy


Licensing
This software is Copyright ©️ 2020 
The University of Texas at El Paso. 
All Rights Reserved.
