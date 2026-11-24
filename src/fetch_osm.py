import osmnx as ox
import geopandas as gpd
from .config import RAW_DIR

# jakarta_boundary = PROCESSED_DIR / "jakarta_boundary.gpkg"

# raw_hospitals = ox.features_from_polygon(
#     jakarta_boundary.geometry.union_all(),
#     tags={
#         "amenity": ["hospital"]
#     }
# )

# raw_hospitals.to_file(
#     PROCESSED_DIR / "hospital_OSM.geojson",
#     driver="GeoJSON"
# )

def fetch_osm_objects(boundary, name, tags, refresh=False):
    output_path = RAW_DIR / f"{name}_OSM.gpkg"

    if output_path.exists() and not refresh:
        print(f"Datasets exist: {name}_OSM.gpkg")
        return gpd.read_file(output_path)

    print(f"Fetching {name} from OSM...")

    polygon = boundary.geometry.union_all()

    gdf = ox.features_from_polygon(
        polygon,
        tags=tags
    )

    gdf.to_file(output_path, driver="GPKG")

    print(f"Saved: {output_path}")

    return gdf