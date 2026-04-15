# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational course materials for NCSU GIS 714: Geospatial Computation and Simulations (GeoForAll Lab, NC State University). Contains Jupyter Notebook assignments using GRASS GIS for geospatial analysis and simulation, plus platform-specific setup tutorials.

Course website: [https://ncsu-geoforall-lab.github.io/geospatial-simulations-course/](https://ncsu-geoforall-lab.github.io/geospatial-simulations-course/)

## Running Notebooks

- **Cloud (Binder):** Click the Binder button in README.md — builds GRASS GIS 8.2 from source via `binder/postBuild`
- **Local:** Follow platform tutorials in `GRASS_GIS_Foundations/` (Windows: OSGeo4W or standalone; Mac: separate tutorial)
- Notebooks depend on GRASS GIS Python APIs (`grass.script`, `grass.jupyter`) and packages in `binder/requirements.txt` (folium, matplotlib, numpy, Pillow, rpy2, etc.)
- All notebooks assume GRASS GIS datasets in `data/` are available (North Carolina sample dataset, temporal workshop data, etc.)

## Repository Structure

- `GRASS_GIS_Foundations/` — Setup tutorials and introductory GRASS GIS notebooks
- `Data_Simulation/` — Fractal surfaces, random points, deterministic/stochastic surface generation
- `Surface_Water_Simulations/` — SIMWE water/sediment modeling, flow accumulation, geostatistics
- `Spread_Simulations/` — PoPS disease/pest spread modeling
- `Temporal_Analyses/` — Climate, solar radiation, and visualization time-series analysis
- `Tangible_Landscape/` — Interactive landscape modeling assignment
- `AI_Coding/` — AI-assisted coding materials (placeholder)
- `Intro_To_Git/` — Git/GitHub learning resources and slides
- `data/` — GRASS GIS location databases (nc_spm_08_grass7, NC_spm_temporal_workshop, dix_park, baranjahill)
- `binder/` — Binder config (apt.txt, requirements.txt, runtime.txt, postBuild)

## Tangible Landscape Assignment

Students submit Python + JSON files to a separate repository: https://github.com/ncsu-geoforall-lab/gis714-2026-tangible-landscape/

Submissions must pass GitHub checks:
- **Black** formatting compliant
- **Flake8** lint compliant
- Python file must have `def run_*:` function and `if __name__==__main__` test case
- JSON file must have activity title and display commands

Format Python files with: `black your_activity.py`

## Key Conventions

- Notebooks use `grass.jupyter` for interactive map rendering and `grass.script` for GRASS module execution
- GRASS GIS sessions are initialized within notebooks pointing to datasets in `data/`
- When updating for a new course year, update links in README.md, Tangible_Landscape/README.md, and notebook markdown cells to reflect the current year
