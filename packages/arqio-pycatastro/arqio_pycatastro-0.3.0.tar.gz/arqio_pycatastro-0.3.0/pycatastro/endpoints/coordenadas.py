"""
Coordinates endpoints for JSON-based Catastro API.
Based on COVCCoordenadas.go from alejndr0/go-catastro
"""
from ..http_client import CatastroHttpClient
from ..models import (
    ConsultaRCCOORRequest, ConsultaRCCOORDistanciaRequest, ConsultaCPMRCRequest
)
from typing import Dict, Any


def consulta_rccoor(request: ConsultaRCCOORRequest) -> Dict[str, Any]:
    """
    Query cadastral reference by coordinates.
    
    Args:
        request: Request with coordinates and SRS
        
    Returns:
        JSON response with cadastral reference data
    """
    client = CatastroHttpClient()
    params = {
        "CoorX": request.coor_x,
        "CoorY": request.coor_y,
        "SRS": request.srs
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR", params)


def consulta_rccoor_distancia(request: ConsultaRCCOORDistanciaRequest) -> Dict[str, Any]:
    """
    Query list of cadastral references by distance to coordinates.
    
    Args:
        request: Request with coordinates and SRS
        
    Returns:
        JSON response with cadastral references sorted by distance
    """
    client = CatastroHttpClient()
    params = {
        "CoorX": request.coor_x,
        "CoorY": request.coor_y,
        "SRS": request.srs
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR_Distancia", params)


def consulta_cpmrc(request: ConsultaCPMRCRequest) -> Dict[str, Any]:
    """
    Query coordinates by province, municipality and cadastral reference.
    
    Args:
        request: Request with provincia, municipio, SRS and parcela or referencia_catastral
        
    Returns:
        JSON response with coordinate data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "SRS": request.srs,
        "Parcela": request.parcela,
        "RefCat": request.referencia_catastral
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_CPMRC", params)