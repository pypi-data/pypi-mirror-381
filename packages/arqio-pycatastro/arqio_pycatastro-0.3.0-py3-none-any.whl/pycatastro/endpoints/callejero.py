"""
Callejero endpoints for JSON-based Catastro API.
Based on COVCCallejero.go from alejndr0/go-catastro
"""
from ..http_client import CatastroHttpClient
from ..models import (
    ObtenerProvinciasRequest, ObtenerMunicipiosRequest, ObtenerCallejeroRequest,
    ObtenerNumereroRequest, ConsultaDNPLOCRequest, ConsultaDNPRCRequest, 
    ConsultaDNPPPRequest, CatastroResponse
)
from typing import Dict, Any


def obtener_provincias() -> Dict[str, Any]:
    """
    Get list of Spanish provinces.
    
    Returns:
        JSON response with province data
    """
    client = CatastroHttpClient()
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerProvincias")


def obtener_municipios(request: ObtenerMunicipiosRequest) -> Dict[str, Any]:
    """
    Get list of municipalities for a province.
    
    Args:
        request: Request with provincia and optionally municipio
        
    Returns:
        JSON response with municipality data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios", params)


def obtener_callejero(request: ObtenerCallejeroRequest) -> Dict[str, Any]:
    """
    Get list of streets for a municipality.
    
    Args:
        request: Request with provincia, municipio, and optionally tipo_via, nombre_via
        
    Returns:
        JSON response with street data
    """
    client = CatastroHttpClient()  
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "TipoVia": request.tipo_via,
        "NomVia": request.nombre_via
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerCallejero", params)


def obtener_numerero(request: ObtenerNumereroRequest) -> Dict[str, Any]:
    """
    Get list of street numbers for a street.
    
    Args:
        request: Request with provincia, municipio, tipo_via, nombre_via and optionally numero
        
    Returns:
        JSON response with number data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "TipoVia": request.tipo_via,
        "NomVia": request.nombre_via,
        "Numero": request.numero
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerNumerero", params)


def consulta_dnploc(request: ConsultaDNPLOCRequest) -> Dict[str, Any]:
    """
    Query non-protected cadastral data by location.
    
    Args:
        request: Request with location details
        
    Returns:
        JSON response with cadastral data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "Sigla": request.sigla,
        "Calle": request.calle, 
        "Numero": request.numero,
        "Bloque": request.bloque,
        "Escalera": request.escalera,
        "Planta": request.planta,
        "Puerta": request.puerta
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPLOC", params)


def consulta_dnprc(request: ConsultaDNPRCRequest) -> Dict[str, Any]:
    """
    Query non-protected cadastral data by cadastral reference.
    
    Args:
        request: Request with cadastral reference
        
    Returns:
        JSON response with cadastral data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "RefCat": request.referencia_catastral
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC", params)


def consulta_dnppp(request: ConsultaDNPPPRequest) -> Dict[str, Any]:
    """
    Query non-protected cadastral data by polygon-parcel.
    
    Args:
        request: Request with polygon and parcel
        
    Returns:
        JSON response with cadastral data
    """
    client = CatastroHttpClient()
    params = {
        "Provincia": request.provincia,
        "Municipio": request.municipio,
        "Poligono": request.poligono,
        "Parcela": request.parcela
    }
    return client.get_json("OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPPP", params)