"""
Main Catastro API client providing a unified interface to all endpoints.
"""
from .endpoints import callejero, coordenadas
from .models import (
    ObtenerProvinciasRequest, ObtenerMunicipiosRequest, ObtenerCallejeroRequest,
    ObtenerNumereroRequest, ConsultaDNPLOCRequest, ConsultaDNPRCRequest,
    ConsultaDNPPPRequest, ConsultaRCCOORRequest, ConsultaRCCOORDistanciaRequest,
    ConsultaCPMRCRequest, CatastroResponse
)
from typing import Dict, Any, Optional
import requests
from urllib.parse import urlencode


class CatastroClient:
    """
    Main client for interacting with Spanish Catastro APIs.
    
    Provides JSON-based access to all Catastro endpoints.
    """
    
    # Callejero endpoints
    def obtener_provincias(self) -> Dict[str, Any]:
        """Get list of Spanish provinces."""
        return callejero.obtener_provincias()
    
    def obtener_municipios(self, provincia: str, municipio: str = "") -> Dict[str, Any]:
        """Get list of municipalities for a province."""
        request = ObtenerMunicipiosRequest(provincia=provincia, municipio=municipio)
        return callejero.obtener_municipios(request)
    
    def obtener_callejero(self, provincia: str, municipio: str, 
                         tipo_via: str = "", nombre_via: str = "") -> Dict[str, Any]:
        """Get list of streets for a municipality."""
        request = ObtenerCallejeroRequest(
            provincia=provincia, municipio=municipio,
            tipo_via=tipo_via, nombre_via=nombre_via
        )
        return callejero.obtener_callejero(request)
    
    def obtener_numerero(self, provincia: str, municipio: str, tipo_via: str,
                        nombre_via: str, numero: str = "") -> Dict[str, Any]:
        """Get list of street numbers for a street."""
        request = ObtenerNumereroRequest(
            provincia=provincia, municipio=municipio,
            tipo_via=tipo_via, nombre_via=nombre_via, numero=numero
        )
        return callejero.obtener_numerero(request)
    
    def consulta_dnploc(self, provincia: str, municipio: str,
                       sigla: str = "", calle: str = "", numero: str = "",
                       bloque: str = "", escalera: str = "", planta: str = "",
                       puerta: str = "") -> Dict[str, Any]:
        """Query non-protected cadastral data by location."""
        request = ConsultaDNPLOCRequest(
            provincia=provincia, municipio=municipio, sigla=sigla,
            calle=calle, numero=numero, bloque=bloque,
            escalera=escalera, planta=planta, puerta=puerta
        )
        return callejero.consulta_dnploc(request)
    
    def consulta_dnprc(self, provincia: str, municipio: str,
                      referencia_catastral: str) -> Dict[str, Any]:
        """Query non-protected cadastral data by cadastral reference."""
        request = ConsultaDNPRCRequest(
            provincia=provincia, municipio=municipio,
            referencia_catastral=referencia_catastral
        )
        return callejero.consulta_dnprc(request)
    
    def consulta_dnppp(self, provincia: str, municipio: str,
                      poligono: str, parcela: str) -> Dict[str, Any]:
        """Query non-protected cadastral data by polygon-parcel."""
        request = ConsultaDNPPPRequest(
            provincia=provincia, municipio=municipio,
            poligono=poligono, parcela=parcela
        )
        return callejero.consulta_dnppp(request)
    
    # Coordinates endpoints
    def consulta_rccoor(self, coor_x: str, coor_y: str, srs: str) -> Dict[str, Any]:
        """Query cadastral reference by coordinates."""
        request = ConsultaRCCOORRequest(coor_x=coor_x, coor_y=coor_y, srs=srs)
        return coordenadas.consulta_rccoor(request)
    
    def consulta_rccoor_distancia(self, coor_x: str, coor_y: str, srs: str) -> Dict[str, Any]:
        """Query list of cadastral references by distance to coordinates."""
        request = ConsultaRCCOORDistanciaRequest(coor_x=coor_x, coor_y=coor_y, srs=srs)
        return coordenadas.consulta_rccoor_distancia(request)
    
    def consulta_cpmrc(self, provincia: str, municipio: str, srs: str,
                      parcela: str = "", referencia_catastral: str = "") -> Dict[str, Any]:
        """Query coordinates by province, municipality and cadastral reference."""
        request = ConsultaCPMRCRequest(
            provincia=provincia, municipio=municipio, srs=srs,
            parcela=parcela, referencia_catastral=referencia_catastral
        )
        return coordenadas.consulta_cpmrc(request)
    
    # Detailed property information
    def get_property_units(self, provincia: str, municipio: str,
                          referencia_catastral: str) -> Dict[str, Any]:
        """
        Get available units/floors/doors for a property.
        
        Args:
            provincia: Province name
            municipio: Municipality name
            referencia_catastral: Basic cadastral reference
            
        Returns:
            Dictionary with unit information and selection options
        """
        from .endpoints import detallada
        
        units = detallada.get_property_unit_options(provincia, municipio, referencia_catastral)
        
        return {
            'property_units_result': {
                'referencia_catastral': referencia_catastral,
                'total_units': len(units),
                'units': [
                    {
                        'unit_id': unit.unit_id,
                        'floor': unit.floor,
                        'door': unit.door,
                        'usage': unit.usage,
                        'surface': unit.surface,
                        'built_year': unit.built_year,
                        'extended_reference': unit.extended_reference,
                        'description': f"Floor {unit.floor}, Door {unit.door} - {unit.usage} ({unit.surface}m²)"
                    }
                    for unit in units
                ]
            }
        }
    
    def get_detailed_property_info(self, provincia: str, municipio: str,
                                  referencia_catastral: str,
                                  extended_reference: str = "") -> Dict[str, Any]:
        """
        Get detailed property information with unit selection.
        
        Args:
            provincia: Province name
            municipio: Municipality name
            referencia_catastral: Basic cadastral reference
            extended_reference: Extended reference for specific unit
            
        Returns:
            Detailed property information dictionary
        """
        from .endpoints import detallada
        from .models import ConsultaDetalladaRequest
        
        request = ConsultaDetalladaRequest(
            provincia=provincia,
            municipio=municipio,
            referencia_catastral=referencia_catastral,
            extended_reference=extended_reference
        )
        
        return detallada.consulta_detallada(request)
    
    # WMS and WFS services
    def download_cadastral_image(self, bbox: str, width: int = 800, height: int = 600,
                                format_img: str = 'image/png', srs: str = 'EPSG:4326',
                                time: Optional[str] = None, timeout: int = 30) -> bytes:
        """
        Download cadastral plot image using WMS service.
        
        Args:
            bbox: Bounding box as 'minx,miny,maxx,maxy'
            width: Image width in pixels
            height: Image height in pixels  
            format_img: Image format (image/png, image/jpeg, etc.)
            srs: Spatial reference system
            time: Optional historical date in YYYY-MM-DD format
            timeout: Request timeout in seconds
            
        Returns:
            Image data as bytes
            
        Raises:
            requests.RequestException: If the request fails
        """
        params = {
            'SERVICE': 'WMS',
            'VERSION': '1.1.1',
            'REQUEST': 'GetMap',
            'LAYERS': 'Catastro',
            'STYLES': '',
            'FORMAT': format_img,
            'BBOX': bbox,
            'WIDTH': width,
            'HEIGHT': height,
            'SRS': srs
        }
        
        if time:
            params['TIME'] = time
            
        url = f"http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?{urlencode(params)}"
        
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        return response.content
    
    def download_parcel_data(self, referencia_catastral: str, srs: str = 'EPSG:4326',
                            timeout: int = 30) -> str:
        """
        Download parcel data using WFS INSPIRE service.
        
        Args:
            referencia_catastral: Cadastral reference (14 characters)
            srs: Spatial reference system
            timeout: Request timeout in seconds
            
        Returns:
            GML data as string
            
        Raises:
            requests.RequestException: If the request fails
        """
        params = {
            'service': 'wfs',
            'version': '2',
            'request': 'getfeature',
            'STOREDQUERIE_ID': 'GetParcel',
            'srsname': srs,
            'REFCAT': referencia_catastral
        }
        
        url = f"http://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?{urlencode(params)}"
        
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        return response.text
    
    # Convenience methods for file operations
    def save_cadastral_image(self, bbox: str, filename: Optional[str] = None,
                            width: int = 800, height: int = 600,
                            format_img: str = 'image/png', srs: str = 'EPSG:4326',
                            time: Optional[str] = None, timeout: int = 30) -> str:
        """
        Download and save cadastral plot image to file.
        
        Args:
            bbox: Bounding box as 'minx,miny,maxx,maxy'
            filename: Output filename (auto-generated if None)
            width: Image width in pixels
            height: Image height in pixels
            format_img: Image format
            srs: Spatial reference system
            time: Optional historical date
            timeout: Request timeout in seconds
            
        Returns:
            Path to saved file
        """
        image_data = self.download_cadastral_image(
            bbox=bbox, width=width, height=height,
            format_img=format_img, srs=srs, time=time, timeout=timeout
        )
        
        # Determine file extension from format
        format_map = {
            'image/png': '.png',
            'image/jpeg': '.jpg', 
            'image/gif': '.gif',
            'image/bmp': '.bmp',
            'image/tif': '.tif'
        }
        
        ext = format_map.get(format_img, '.png')
        if filename is None:
            filename = f"catastro_plot{ext}"
        
        with open(filename, 'wb') as f:
            f.write(image_data)
        
        return filename
    
    def get_file_info(self, filename: str) -> Dict[str, Any]:
        """
        Get file information for display purposes.
        
        Args:
            filename: Path to file
            
        Returns:
            Dictionary with file information
        """
        import os
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            return {
                'filename': filename,
                'size_bytes': file_size,
                'size_formatted': f"{file_size:,} bytes"
            }
        return {'filename': filename, 'size_bytes': 0, 'size_formatted': '0 bytes'}
    
    def save_parcel_data(self, referencia_catastral: str, filename: Optional[str] = None,
                        srs: str = 'EPSG:4326', timeout: int = 30) -> str:
        """
        Download and save parcel data to file.
        
        Args:
            referencia_catastral: Cadastral reference
            filename: Output filename (auto-generated if None)
            srs: Spatial reference system
            timeout: Request timeout in seconds
            
        Returns:
            Path to saved file
        """
        gml_data = self.download_parcel_data(
            referencia_catastral=referencia_catastral,
            srs=srs, timeout=timeout
        )
        
        if filename is None:
            filename = f"parcel_{referencia_catastral}.gml"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(gml_data)
        
        return filename
    
    def download_descriptive_report(self, referencia_catastral: str, extended_reference: str = "", 
                                   timeout: int = 30) -> bytes:
        """
        Download descriptive and graphic report (PDF) for a property.
        
        This downloads the "Consulta descriptiva y gráfica" PDF document
        that contains comprehensive property information including maps,
        construction details, and cadastral data.
        
        Args:
            referencia_catastral: Basic cadastral reference (14 characters)
            extended_reference: Extended reference for specific unit (if available)
            timeout: Request timeout in seconds
            
        Returns:
            PDF data as bytes
            
        Raises:
            requests.RequestException: If the request fails
            ValueError: If no valid PDF is available for the reference
        """
        # Use extended reference if provided, otherwise try basic reference
        ref_to_use = extended_reference if extended_reference else referencia_catastral
        url = f"https://www1.sedecatastro.gob.es/CYCBienInmueble/SECImprimirCroquisyDatos.aspx?refcat={ref_to_use}"
        
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        # Check if we got HTML instead of PDF (indicates no report available)
        content_type = response.headers.get('content-type', '').lower()
        if 'text/html' in content_type or response.content.startswith(b'<!DOCTYPE') or response.content.startswith(b'<html'):
            raise ValueError(f"No descriptive report available for reference {ref_to_use}. "
                           "This property may not have a detailed report, or you may need to "
                           "use a more specific unit reference.")
        
        # Verify it's actually a PDF
        if not response.content.startswith(b'%PDF'):
            raise ValueError(f"Invalid PDF data received for reference {ref_to_use}")
        
        return response.content
    
    def save_descriptive_report(self, referencia_catastral: str, filename: Optional[str] = None,
                               extended_reference: str = "", timeout: int = 30) -> str:
        """
        Download and save descriptive report PDF to file.
        
        Args:
            referencia_catastral: Basic cadastral reference
            filename: Output filename (auto-generated if None)
            extended_reference: Extended reference for specific unit
            timeout: Request timeout in seconds
            
        Returns:
            Path to saved file
        """
        pdf_data = self.download_descriptive_report(
            referencia_catastral=referencia_catastral,
            extended_reference=extended_reference,
            timeout=timeout
        )
        
        ref_for_filename = extended_reference if extended_reference else referencia_catastral
        if filename is None:
            filename = f"report_{ref_for_filename}.pdf"
        
        with open(filename, 'wb') as f:
            f.write(pdf_data)
        
        return filename