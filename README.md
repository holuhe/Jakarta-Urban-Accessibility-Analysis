# Jakarta Urban Accessibility Analysis

> A kecamatan-level analysis of how easily Jakarta residents can reach essential services such as hospitals, schools, shopping malls, and public transport.

## Overview

Jakarta is one of the most densely populated and congested metropolitan areas in the world, and access to essential services varies widely across the city. This project measures that variation by calculating an **accessibility score** for every kecamatan (district) in Jakarta, based on the travel time needed to reach key infrastructure.

The analysis covers four categories of destinations:

- Hospitals
- Schools
- Shopping malls
- Public transport (stations and stops)

## Methodology

1. **Study area:** Each kecamatan in DKI Jakarta is represented by its centroid (or population-weighted centroid) as the origin point.
2. **Travel time estimation:** Travel times from each kecamatan to the nearest destination in each category are calculated over the road and transit network.
3. **Accessibility score:** The travel times for each destination type are normalized and combined into a single score per kecamatan. Lower travel time means higher accessibility.
4. **Cumulative opportunities analysis:** For each kecamatan, we count how many facilities can be reached within set travel time thresholds (e.g., 15, 30, 45, and 60 minutes). This shows not only how close the nearest facility is, but how many options residents actually have.

## Deliverables

The main output of this project is a collection of final maps, including:

- Accessibility score by kecamatan, per destination type and overall
- Travel time to the nearest hospital, school, mall, and public transport stop
- Cumulative opportunities maps at each time threshold
- Comparison maps highlighting the best and least served kecamatan

All maps are saved in the `outputs/maps/` folder.

## Tech Stack *(draft, to be confirmed)*

- **Language:** Python 3.11+
- **Spatial analysis:** GeoPandas, Shapely, OSMnx, NetworkX (or r5py for multimodal routing)
- **Data handling:** pandas, NumPy
- **Visualization:** Matplotlib, contextily, (optionally QGIS for final map layout)
- **Environment:** Jupyter Notebook

## Data Sources *(draft, to be confirmed)*

| Data | Source |
|------|--------|
| Kecamatan boundaries | BPS / Jakarta Satu |
| Hospitals, schools, malls | OpenStreetMap |
| Road network | OpenStreetMap |
| Public transport | TransJakarta, MRT, LRT, KRL GTFS or OSM data |

## Project Structure *(draft, to be confirmed)*

```
jakarta-urban-accessibility/
├── data/
│   ├── raw/               # Original downloaded datasets
│   └── processed/         # Cleaned and analysis-ready data
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_travel_time_analysis.ipynb
│   ├── 03_accessibility_score.ipynb
│   └── 04_cumulative_opportunities.ipynb
├── src/                   # Reusable helper functions
├── outputs/
│   └── maps/              # Final maps
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or newer
- Git

### Installation

```bash
git clone https://github.com/your-username/jakarta-urban-accessibility.git
cd jakarta-urban-accessibility
pip install -r requirements.txt
```

### Usage

Run the notebooks in order, from `01_data_preparation.ipynb` to `04_cumulative_opportunities.ipynb`. Final maps will be written to `outputs/maps/`.

## Results

*Add preview images of your key maps here once they are finished.*

## Limitations

- Travel times are estimates and may not reflect real-world traffic conditions.
- Kecamatan centroids simplify the movement of people within each district.
- Facility data from OpenStreetMap may be incomplete in some areas.

## Contributing

Suggestions and improvements are welcome. Please open an issue to discuss changes before submitting a pull request.

## License

Distributed under the MIT License. See `LICENSE` for details.
