# pycatastro

Python client for the SedeCatastro (Spanish Cadastre) API.

- Complete interface to SedeCatastro JSON APIs
- Clean Pythonic API that accepts and returns JSON
- Based on the comprehensive [go-catastro](https://github.com/alejndr0/go-catastro) Go library
- Extensible and well-documented

## Features

- **JSON-first**: All APIs use JSON/dict for clean Python integration
- **Comprehensive**: Covers all major Catastro API endpoints
- **Type-safe**: Uses dataclasses for request/response models
- **Error handling**: Proper exception handling for API errors
- **Street types**: Includes all Spanish street type constants

## Installation

```bash
pip install pycatastro
```

## Quick Start

```python
from pycatastro import CatastroClient, tipos

client = CatastroClient()

# Get all Spanish provinces
provinces = client.obtener_provincias()

# Get municipalities in Valencia province  
municipalities = client.obtener_municipios("VALENCIA")

# Get streets named "MAYOR" in Valencia
streets = client.obtener_callejero(
    provincia="VALENCIA",
    municipio="VALENCIA", 
    tipo_via=tipos.CALLE,
    nombre_via="MAYOR"
)

# Query cadastral data by location
cadastral_data = client.consulta_dnploc(
    provincia="VALENCIA",
    municipio="VALENCIA",
    calle="MAYOR",
    numero="1"
)

# Query by coordinates
coords_data = client.consulta_rccoor(
    coor_x="728015.00",
    coor_y="4372193.00", 
    srs="EPSG:25830"
)

# Download cadastral image
image_data = client.download_cadastral_image(
    bbox="2.183,41.407,2.185,41.408",
    width=1024,
    height=768
)

# Download parcel data
gml_data = client.download_parcel_data("1945320DF3814F")

# Download comprehensive PDF report (may need extended reference)
pdf_data = client.download_descriptive_report("1945320DF3814F", extended_reference="1945320DF3814F0025AL")

# Get available units in a building
units_info = client.get_property_units("BARCELONA", "BARCELONA", "1945320DF3814F")

# Get detailed property information
detailed_info = client.get_detailed_property_info("BARCELONA", "BARCELONA", "1945320DF3814F")

print(cadastral_data)
```

## API Endpoints

### Callejero (Street Directory)

- ✅ `obtener_provincias()` - Get list of provinces
- ✅ `obtener_municipios(provincia, municipio="")` - Get municipalities  
- ✅ `obtener_callejero(provincia, municipio, tipo_via="", nombre_via="")` - Get streets
- ✅ `obtener_numerero(provincia, municipio, tipo_via, nombre_via, numero="")` - Get street numbers

### Consulta DNP (Non-Protected Data Query)

- ✅ `consulta_dnploc(provincia, municipio, ...)` - Query by location
- ✅ `consulta_dnprc(provincia, municipio, referencia_catastral)` - Query by cadastral reference  
- ✅ `consulta_dnppp(provincia, municipio, poligono, parcela)` - Query by polygon-parcel

### Coordinates

- ✅ `consulta_rccoor(coor_x, coor_y, srs)` - Get cadastral reference by coordinates
- ✅ `consulta_rccoor_distancia(coor_x, coor_y, srs)` - Get references by distance to coordinates
- ✅ `consulta_cpmrc(provincia, municipio, srs, ...)` - Get coordinates by cadastral reference

### Downloads (WMS/WFS Services)

- ✅ `download_cadastral_image(bbox, width, height, ...)` - Download cadastral plot images
- ✅ `download_parcel_data(referencia_catastral, srs)` - Download parcel geometry data
- ✅ `download_descriptive_report(referencia_catastral)` - Download comprehensive PDF reports

### Detailed Property Information

- ✅ `get_property_units(provincia, municipio, referencia_catastral)` - List available units/floors/doors
- ✅ `get_detailed_property_info(provincia, municipio, referencia_catastral, ...)` - Enhanced property details

## Street Types

The `tipos` module provides constants for all Spanish street types:

```python
from pycatastro import tipos

# Common street types
tipos.CALLE        # "CL" - Street
tipos.AVENIDA      # "AV" - Avenue  
tipos.PLAZA        # "PZ" - Square
tipos.PASEO        # "PS" - Boulevard
tipos.CARRETERA    # "CR" - Road
tipos.CAMINO       # "CM" - Path
# ... and many more
```

## Error Handling

```python
from pycatastro import CatastroClient, CatastroApiError

client = CatastroClient()

try:
    result = client.obtener_provincias()
except CatastroApiError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Network/other error: {e}")
```

## Command Line Interface

pycatastro includes a comprehensive CLI for all API endpoints:

```bash
# Get all provinces
pycatastro provincias

# Get municipalities in Valencia
pycatastro municipios VALENCIA

# Get streets named "MAYOR" in Valencia city
pycatastro callejero VALENCIA VALENCIA --tipo-via CL --nombre-via MAYOR

# Query by coordinates
pycatastro rccoor --coor-x 728015.00 --coor-y 4372193.00 --srs EPSG:25830

# Query by location
pycatastro dnploc VALENCIA VALENCIA --calle COLON --numero 1

# Download cadastral image
pycatastro download-image --bbox "2.183,41.407,2.185,41.408" --width 1024 --height 768

# Download parcel data
pycatastro download-parcel 1945320DF3814F

# Download descriptive report (comprehensive PDF) - may require extended reference
pycatastro download-report 1945320DF3814F --extended-reference 1945320DF3814F0025AL

# Get coordinates for cadastral reference
pycatastro get-coordinates BARCELONA BARCELONA 1945320DF3814F

# List available units in a building (floors, doors, etc.)
pycatastro list-units BARCELONA BARCELONA 1945320DF3814F

# Get detailed property information with unit breakdown
pycatastro detailed-info BARCELONA BARCELONA 1945320DF3814F

# List all street types
pycatastro list-street-types
```

See `CLI.md` for complete CLI documentation.

## Examples

See `examples/demo.py` for a comprehensive demonstration of all features.

```bash
python examples/demo.py
```

## Development

Requirements:
- Python 3.9+
- requests
- xmltodict (for legacy XML endpoints)

```bash
# Install development dependencies
pip install -e .
pip install pytest

# Run tests
pytest

# Run specific tests
pytest tests/test_json_endpoints.py -v
```

## Architecture

- **Client Layer**: `CatastroClient` - Main user interface
- **Endpoint Layer**: `endpoints/` - Organized by API category  
- **HTTP Layer**: `http_client.py` - Handles JSON API communication
- **Models Layer**: `models.py` - Request/response data structures

## Relationship to go-catastro

This library is inspired by and follows the structure of [alejndr0/go-catastro](https://github.com/alejndr0/go-catastro), providing the same comprehensive API coverage but in Python with a JSON-first approach.

## Contributing

Contributions welcome! Please read the `CODING_AGENT.md` for guidelines on adding new endpoints.

## License

MIT License - see LICENSE file for details.