# AOV_Archive

_AOV Archive is a structured archival release of the Arctic Observing Viewer (AOV) application and its supporting data ecosystem._

---

## 📦 Overview

This repository provides **everything needed to run, test, and understand the AOV visualization ecosystem**:

- **Main AOV Web Application** — React/HTML/CSS/JS map-driven interface.
- **Python Scripts** — Utilities for normalizing and preparing AOV datasets.
- **CSV Mapping Tables** — Authoritative ROR (Research Organization Registry) links for agencies & institutions.
- **Unique Indexes** — Curated CSV files listing all unique Agencies, Institutions, and Principal Investigators, including normalized names and ROR associations.

---

## 🗂️ Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Main AOV Application](#main-aov-application)
- [Scripts (Python Utilities)](#scripts-python-utilities)
- [Related Tables (CSV ROR Mappings)](#related-tables-csv-ror-mappings)
- [Unique Indexes](#unique-indexes)
- [Licensing](#licensing)

---

## Project Overview

The AOV Archive repository preserves the full environment for the AOV visualization ecosystem.

- ⚛️ **React-based mapping application**
- 🧪 **Automated testing** via Cypress
- 🐳 **Dockerized build & test environments**
- 🐍 **Python data-curation pipelines**
- 📄 **Authoritative ROR mappings**
- 🏷️ **Normalized indexes for core contributors** (PIs, Agencies, Institutions)

---

## Repository Structure

```
AOV-Archived/
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
├── unique_Tables/          # Unique normalized lists of names w/ ROR + aliases
│   ├── agency_Unique.csv
│   ├── institution_Unique.csv
│   ├── ORCID_Unique.csv
│
└── README.md
```

---

## Main AOV Application

The AOV client is a modern React-based mapping tool:

- **Tested with Cypress**
- **Containerized via Docker**
- **Makefile-managed commands for install, test, deploy**

### ⚙️ Prerequisites

- Docker
- Docker Compose
- Node.js
- npm

#### Install dependencies:

```sh
make install-app
```

#### Clone & set up:

```sh
git clone <repository-url>
cd <repository-directory>
make install-app
```

### 🧑‍💻 Pre-Commit Checks

Before committing, run:

```sh
make test-app
```

Runs:  
• Code formatting  
• License header checks  
• Lint & type checks  
• Unit/client tests  
• Cypress E2E tests (Docker)  
• Snapshot cleanup

---

### Main Commands

| Description               | Command                       |
|---------------------------|-------------------------------|
| Develop app               | `make develop`                |
| Build client              | `make build`                  |
| Install client deps       | `make install-client`         |
| Linting                   | `make test-lint`              |
| Type checking             | `make test-types`             |

### Cypress E2E

| Description              | Command                        |
|--------------------------|--------------------------------|
| Open test UI             | `make open-test`               |
| Install Cypress deps     | `make install-e2e-cypress`     |
| Run e2e tests            | `make test-e2e-cypress`        |
| Clean snapshots          | `make clean-snapshots`         |

### Docker Commands

| Description          | Command                        |
|----------------------|-------------------------------|
| Build image          | `make docker-build`           |
| Run all e2e tests    | `make test-e2e`               |
| Update snapshots     | `make test-e2e-image-snapshots-update` |

---

## Scripts (Python Utilities)

Located in the `scripts/` folder.

Typical operations:

- Normalize field names
- Clean inconsistent/malformed entries
- Standardize institution/agency names
- Validate/fix geometry
- Map ROR identifiers
- Prepare final datasets

---

## Related Tables (CSV ROR Mappings)

Maps institutions & agencies in the AOV dataset to their authoritative ROR entries.

Each table includes:

- **Normalized name**
- **Site_ID** (links site → agency/institution)
- **ROR ID**

Ensures consistency across the full ecosystem.

---

## Unique Indexes

The `unique_Tables/` folder includes comprehensive lists of unique Institutions, Agencies, and Principal Investigators.

Each CSV contains:

- ✔ Canonical (normalized) name
- ✔ All known aliases
- ✔ ROR ID (if available)
- ✔ Boolean flag (ROR exists)

Used to:

- De-duplicate naming conventions
- Automate ROR matching
- Maintain stable referential keys
- Improve search/filter/visualization accuracy

---

## 📜 Licensing

_This software is Copyright ©️ 2020  
The University of Texas at El Paso.  
All Rights Reserved._
