"""
Data models for Catastro API requests and responses.
Based on struct.go from alejndr0/go-catastro
"""
from dataclasses import dataclass
from typing import List, Optional, Dict, Any


# JSON-based models for all endpoints

# Common structures
@dataclass
class ErrorList:
    cod: str
    des: str  # "des" in some responses, "desc" in others


# Callejero endpoints

@dataclass
class ObtenerProvinciasRequest:
    """Request for ObtenerProvincias - does not need parameters."""
    pass


@dataclass
class ObtenerMunicipiosRequest:
    provincia: str
    municipio: str = ""


@dataclass
class ObtenerMunicipiosCodigosRequest:
    codigo_municipio: str = ""
    codigo_municipio_ine: str = ""
    codigo_provincia: str = ""


@dataclass 
class ObtenerCallejeroRequest:
    provincia: str
    municipio: str
    tipo_via: str = ""
    nombre_via: str = ""


@dataclass
class ObtenerCallejeroCodigosRequest:
    codigo_provincia: str
    codigo_municipio: str = ""
    codigo_municipio_nie: str = ""
    codigo_via: str = ""


@dataclass
class ObtenerNumereroRequest:
    provincia: str
    municipio: str
    tipo_via: str
    nombre_via: str
    numero: str = ""


@dataclass
class ObtenerNumereroCodigosRequest:
    codigo_provincia: str
    codigo_municipio_ine: str = ""
    codigo_municipio: str = ""
    codigo_via: str = ""
    numero: str = ""


# Consulta DNP endpoints

@dataclass
class ConsultaDNPLOCRequest:
    provincia: str
    municipio: str
    sigla: str = ""
    calle: str = ""
    numero: str = ""
    bloque: str = ""
    escalera: str = ""
    planta: str = ""
    puerta: str = ""


@dataclass
class ConsultaDNPLOCCodigosRequest:
    codigo_provincia: str
    codigo_municipio: str = ""
    codigo_municipio_nie: str = ""
    codigo_via: str = ""
    numero: str = ""
    bloque: str = ""
    escalera: str = ""
    planta: str = ""
    puerta: str = ""


@dataclass
class ConsultaDNPRCRequest:
    provincia: str
    municipio: str
    referencia_catastral: str


@dataclass
class ConsultaDNPRCCodigosRequest:
    codigo_provincia: str
    codigo_municipio: str = ""
    codigo_municipio_nie: str = ""
    referencia_catastral: str = ""


@dataclass
class ConsultaDNPPPRequest:
    provincia: str
    municipio: str
    poligono: str
    parcela: str


@dataclass
class ConsultaDNPPPCodigosRequest:
    codigo_provincia: str
    codigo_municipio: str = ""
    codigo_municipio_ine: str = ""
    poligono: str = ""
    parcela: str = ""


# Coordinates endpoints

@dataclass
class ConsultaRCCOORRequest:
    coor_x: str
    coor_y: str
    srs: str


@dataclass
class ConsultaRCCOORDistanciaRequest:
    coor_x: str
    coor_y: str
    srs: str


@dataclass
class ConsultaCPMRCRequest:
    provincia: str
    municipio: str
    srs: str
    parcela: str = ""
    referencia_catastral: str = ""


# Extended property information models

@dataclass
class PropertyUnit:
    """Represents a single unit within a building."""
    unit_id: str
    floor: str
    door: str
    usage: str
    surface: float
    built_year: int
    extended_reference: str = ""


@dataclass
class DetailedPropertyInfo:
    """Detailed property information from Catastro web interface."""
    cadastral_reference: str
    extended_reference: str
    location: str
    postal_code: str
    property_class: str
    main_use: str
    built_surface: float
    construction_year: int
    parcel_surface: float
    participation: float
    units: List[PropertyUnit]
    
    
@dataclass
class ConsultaDetalladaRequest:
    """Request for detailed property information."""
    provincia: str
    municipio: str
    referencia_catastral: str
    extended_reference: str = ""


# Response models are complex nested structures
# For now, we'll use generic dict responses and let users access the data directly
# In the future, these could be expanded to full dataclass hierarchies

@dataclass
class CatastroResponse:
    """Generic response wrapper for all Catastro API responses."""
    data: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        return self.data