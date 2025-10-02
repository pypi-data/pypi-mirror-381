"""
Detailed property information endpoint for Spanish Catastro.
Handles unit selection and extended property details.
"""
from typing import Dict, Any, List, Optional
from ..models import ConsultaDetalladaRequest, PropertyUnit, DetailedPropertyInfo


def extract_unit_options(dnprc_response: Dict[str, Any]) -> List[PropertyUnit]:
    """
    Extract available unit options from a DNPRC response.
    
    Args:
        dnprc_response: Response from consulta_dnprc API call
        
    Returns:
        List of PropertyUnit objects representing available units
    """
    units = []
    
    rcdnp_list = dnprc_response.get('consulta_dnprcResult', {}).get('lrcdnp', {}).get('rcdnp', [])
    
    for i, record in enumerate(rcdnp_list):
        rc = record.get('rc', {})
        cadastral_ref = f"{rc.get('pc1', '')}{rc.get('pc2', '')}"
        
        debi = record.get('debi', {})
        usage = debi.get('luso', 'N/A')
        surface = float(debi.get('sfc', 0)) if debi.get('sfc') != 'N/A' else 0.0
        built_year = int(debi.get('ant', 0)) if debi.get('ant') != 'N/A' else 0
        
        loint = record.get('dt', {}).get('locs', {}).get('lous', {}).get('lourb', {}).get('loint', {})
        floor = loint.get('pt', 'N/A')
        door = loint.get('pu', 'N/A')
        
        # Try to construct extended reference
        # The extended reference appears to follow a pattern like 1945320DF3814F0026AL
        # where the original reference is extended with unit-specific identifiers
        unit_suffix = f"{i+1:04d}AL"  # This is a guess at the pattern
        extended_ref = f"{cadastral_ref}{unit_suffix}"
        
        unit = PropertyUnit(
            unit_id=str(i+1),
            floor=floor,
            door=door,
            usage=usage,
            surface=surface,
            built_year=built_year,
            extended_reference=extended_ref
        )
        
        units.append(unit)
    
    return units


def get_property_unit_options(provincia: str, municipio: str, 
                            referencia_catastral: str) -> List[PropertyUnit]:
    """
    Get available unit options for a building/property.
    
    Args:
        provincia: Province name
        municipio: Municipality name  
        referencia_catastral: Basic cadastral reference
        
    Returns:
        List of available units in the property
    """
    # Import here to avoid circular imports
    from . import callejero
    
    # First get the basic property information
    from ..models import ConsultaDNPRCRequest
    request = ConsultaDNPRCRequest(
        provincia=provincia,
        municipio=municipio,
        referencia_catastral=referencia_catastral
    )
    
    response = callejero.consulta_dnprc(request)
    return extract_unit_options(response)


def get_detailed_property_info_web(provincia: str, municipio: str,
                                  referencia_catastral: str,
                                  extended_reference: str = "") -> Optional[DetailedPropertyInfo]:
    """
    Attempt to get detailed property information using web scraping approach.
    This is a fallback when API doesn't provide sufficient detail.
    
    Note: This is a proof-of-concept. A production implementation would need
    proper web scraping with respect for robots.txt and rate limiting.
    
    Args:
        provincia: Province name
        municipio: Municipality name
        referencia_catastral: Basic cadastral reference
        extended_reference: Extended reference for specific unit
        
    Returns:
        Detailed property information or None if not available
    """
    # For now, return None as web scraping would require careful implementation
    # to respect the website's terms of service
    return None


def consulta_detallada(request: ConsultaDetalladaRequest) -> Dict[str, Any]:
    """
    Get detailed property information.
    
    Currently this returns enhanced information based on existing API calls
    plus unit selection capabilities.
    
    Args:
        request: Request with property details
        
    Returns:
        Enhanced property information dictionary
    """
    # Get unit options
    units = get_property_unit_options(
        request.provincia,
        request.municipio, 
        request.referencia_catastral
    )
    
    # Get coordinates for the property
    from . import coordenadas
    from ..models import ConsultaCPMRCRequest
    
    coord_request = ConsultaCPMRCRequest(
        provincia=request.provincia,
        municipio=request.municipio,
        srs="EPSG:4326",
        referencia_catastral=request.referencia_catastral
    )
    
    try:
        coord_response = coordenadas.consulta_cpmrc(coord_request)
        coordinates = coord_response.get('Consulta_CPMRCResult', {}).get('coordenadas', {}).get('coord', [])
    except:
        coordinates = []
    
    # Build enhanced response
    result = {
        'consulta_detalladaResult': {
            'referencia_catastral': request.referencia_catastral,
            'extended_reference': request.extended_reference,
            'units': [
                {
                    'unit_id': unit.unit_id,
                    'floor': unit.floor,
                    'door': unit.door,
                    'usage': unit.usage,
                    'surface': unit.surface,
                    'built_year': unit.built_year,
                    'extended_reference': unit.extended_reference
                }
                for unit in units
            ],
            'coordinates': coordinates,
            'total_units': len(units)
        }
    }
    
    return result