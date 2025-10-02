#!/usr/bin/env python3
"""
CLI interface for pycatastro - Spanish Catastro API client.
Provides command-line access to all Catastro API endpoints.
"""
import argparse
import json
import sys
from typing import Dict, Any, Optional

from . import CatastroClient, CatastroApiError, tipos


def print_json(data: Dict[str, Any], compact: bool = False) -> None:
    """Pretty print JSON data."""
    if compact:
        print(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def format_output(data: Dict[str, Any], format_type: str, compact: bool = False) -> None:
    """Format and print output based on format type."""
    if format_type == 'json':
        print_json(data, compact)
    elif format_type == 'table':
        print_table(data)
    else:
        print_json(data, compact)


def print_table(data: Dict[str, Any]) -> None:
    """Print data in table format (simplified)."""
    # This is a basic table formatter - could be enhanced
    print_json(data)


def cmd_provincias(args: argparse.Namespace) -> None:
    """Get list of Spanish provinces."""
    client = CatastroClient()
    try:
        result = client.obtener_provincias()
        
        if args.format == 'table' and not args.raw:
            # Extract and format province data nicely
            prov_list = result.get('consulta_provincieroResult', {}).get('provinciero', {}).get('prov', [])
            print(f"Found {len(prov_list)} Spanish provinces:\n")
            print(f"{'Code':<6} {'Name':<30}")
            print("-" * 38)
            for prov in prov_list:
                print(f"{prov.get('cpine', ''):<6} {prov.get('np', ''):<30}")
        else:
            format_output(result, args.format, args.compact)
            
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_municipios(args: argparse.Namespace) -> None:
    """Get municipalities for a province."""
    client = CatastroClient()
    try:
        result = client.obtener_municipios(args.provincia, args.municipio or "")
        
        if args.format == 'table' and not args.raw:
            # Extract and format municipality data nicely
            muni_list = result.get('consulta_municipieroResult', {}).get('municipiero', {}).get('muni', [])
            print(f"Found {len(muni_list)} municipalities in {args.provincia}:\n")
            print(f"{'Code':<10} {'Name':<40}")
            print("-" * 52)
            for muni in muni_list:
                print(f"{muni.get('cm', ''):<10} {muni.get('nm', ''):<40}")
        else:
            format_output(result, args.format, args.compact)
            
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_callejero(args: argparse.Namespace) -> None:
    """Get streets for a municipality."""
    client = CatastroClient()
    try:
        result = client.obtener_callejero(
            args.provincia, 
            args.municipio, 
            args.tipo_via or "", 
            args.nombre_via or ""
        )
        
        if args.format == 'table' and not args.raw:
            # Extract and format street data nicely
            calle_list = result.get('consulta_callejeroResult', {}).get('callejero', {}).get('calle', [])
            print(f"Found {len(calle_list)} streets:\n")
            print(f"{'Type':<4} {'Code':<6} {'Name':<50}")
            print("-" * 62)
            for calle in calle_list:
                direccion = calle.get('dir', {})
                print(f"{direccion.get('tv', ''):<4} {direccion.get('cv', ''):<6} {direccion.get('nv', ''):<50}")
        else:
            format_output(result, args.format, args.compact)
            
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_numerero(args: argparse.Namespace) -> None:
    """Get street numbers for a street."""
    client = CatastroClient()
    try:
        result = client.obtener_numerero(
            args.provincia, 
            args.municipio, 
            args.tipo_via, 
            args.nombre_via, 
            args.numero or ""
        )
        
        if args.format == 'table' and not args.raw:
            # Extract and format number data nicely
            num_list = result.get('consulta_numereroResult', {}).get('nump', [])
            print(f"Found {len(num_list)} numbers:\n")
            print(f"{'Number':<10} {'Cadastral Ref':<20}")
            print("-" * 32)
            for num in num_list:
                number = num.get('num', {}).get('pnp', '')
                pc = num.get('pc', {})
                ref = f"{pc.get('pc1', '')}{pc.get('pc2', '')}"
                print(f"{number:<10} {ref:<20}")
        else:
            format_output(result, args.format, args.compact)
            
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_dnploc(args: argparse.Namespace) -> None:
    """Query cadastral data by location."""
    client = CatastroClient()
    try:
        result = client.consulta_dnploc(
            args.provincia,
            args.municipio,
            args.sigla or "",
            args.calle or "",
            args.numero or "",
            args.bloque or "",
            args.escalera or "",
            args.planta or "",
            args.puerta or ""
        )
        
        if args.format == 'table' and not args.raw:
            # Extract and format cadastral location data nicely
            rcdnp_list = result.get('consulta_dnplocResult', {}).get('lrcdnp', {}).get('rcdnp', [])
            if rcdnp_list:
                print(f"Found {len(rcdnp_list)} cadastral records for the address:\\n")
                print(f"{'Cadastral Ref':<20} {'Usage':<12} {'Surface (m²)':<12} {'Floor':<6} {'Door':<6}")
                print("-" * 62)
                for record in rcdnp_list:
                    rc = record.get('rc', {})
                    cadastral_ref = f"{rc.get('pc1', '')}{rc.get('pc2', '')}"
                    
                    debi = record.get('debi', {})
                    usage = debi.get('luso', 'N/A')[:11]  # Truncate long usage descriptions
                    surface = debi.get('sfc', 'N/A')
                    
                    loint = record.get('dt', {}).get('locs', {}).get('lous', {}).get('lourb', {}).get('loint', {})
                    floor = loint.get('pt', 'N/A')
                    door = loint.get('pu', 'N/A')
                    
                    print(f"{cadastral_ref:<20} {usage:<12} {surface:<12} {floor:<6} {door:<6}")
            else:
                print("No cadastral records found.")
        else:
            format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        error_msg = str(e)
        print(f"API Error: {error_msg}", file=sys.stderr)
        
        if "NO EXISTE NINGÚN INMUEBLE" in error_msg:
            print("\nSuggestions:", file=sys.stderr)
            print("- Try including the street type with --sigla (e.g., --sigla CL for CALLE)", file=sys.stderr)
            print("- Check the exact street name and type using 'callejero' command first:", file=sys.stderr)
            print(f"  pycatastro callejero {args.provincia} {args.municipio} --nombre-via {args.calle or 'STREET_NAME'}", file=sys.stderr)
            print("- Try a different street number or add specific unit details (--bloque, --planta, --puerta)", file=sys.stderr)
            print("- Some addresses may not be registered in the cadastral database", file=sys.stderr)
            print("- Alternative: use coordinates instead: pycatastro rccoor --coor-x X --coor-y Y --srs EPSG:25830", file=sys.stderr)
        
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_dnprc(args: argparse.Namespace) -> None:
    """Query cadastral data by cadastral reference."""
    client = CatastroClient()
    try:
        result = client.consulta_dnprc(
            args.provincia,
            args.municipio,
            args.referencia_catastral
        )
        
        if args.format == 'table' and not args.raw:
            # Extract and format cadastral reference data nicely
            rcdnp_list = result.get('consulta_dnprcResult', {}).get('lrcdnp', {}).get('rcdnp', [])
            if rcdnp_list:
                print(f"Found {len(rcdnp_list)} records for cadastral reference {args.referencia_catastral}:\\n")
                print(f"{'Unit':<6} {'Usage':<12} {'Surface (m²)':<12} {'Floor':<6} {'Door':<6} {'Built':<6}")
                print("-" * 68)
                for i, record in enumerate(rcdnp_list, 1):
                    debi = record.get('debi', {})
                    usage = debi.get('luso', 'N/A')[:11]  # Truncate long usage descriptions
                    surface = debi.get('sfc', 'N/A')
                    built_year = debi.get('ant', 'N/A')
                    
                    loint = record.get('dt', {}).get('locs', {}).get('lous', {}).get('lourb', {}).get('loint', {})
                    floor = loint.get('pt', 'N/A')
                    door = loint.get('pu', 'N/A')
                    
                    print(f"{i:<6} {usage:<12} {surface:<12} {floor:<6} {door:<6} {built_year:<6}")
                    
                # Show address information
                if rcdnp_list:
                    first_record = rcdnp_list[0]
                    dt = first_record.get('dt', {})
                    location = dt.get('locs', {}).get('lous', {}).get('lourb', {})
                    if location:
                        dir_info = location.get('dir', {})
                        address = f"{dir_info.get('tv', '')} {dir_info.get('nv', '')} {dir_info.get('pnp', '')}"
                        municipality = f"{dt.get('nm', '')}, {dt.get('np', '')}"
                        print(f"\\nAddress: {address.strip()}")
                        print(f"Location: {municipality}")
            else:
                print("No cadastral records found for this reference.")
        else:
            format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_dnppp(args: argparse.Namespace) -> None:
    """Query cadastral data by polygon-parcel."""
    client = CatastroClient()
    try:
        result = client.consulta_dnppp(
            args.provincia,
            args.municipio,
            args.poligono,
            args.parcela
        )
        format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_rccoor(args: argparse.Namespace) -> None:
    """Query cadastral reference by coordinates."""
    client = CatastroClient()
    try:
        result = client.consulta_rccoor(
            args.coor_x,
            args.coor_y,
            args.srs
        )
        
        if args.format == 'table' and not args.raw:
            # Extract and format coordinate data nicely
            coord_list = result.get('Consulta_RCCOORResult', {}).get('coordenadas', {}).get('coord', [])
            print(f"Found {len(coord_list)} cadastral references:\n")
            print(f"{'Cadastral Ref':<20} {'X':<12} {'Y':<12}")
            print("-" * 46)
            for coord in coord_list:
                pc = coord.get('pc', {})
                geo = coord.get('geo', {})
                ref = f"{pc.get('pc1', '')}{pc.get('pc2', '')}"
                print(f"{ref:<20} {geo.get('xcen', ''):<12} {geo.get('ycen', ''):<12}")
        else:
            format_output(result, args.format, args.compact)
            
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_rccoor_distancia(args: argparse.Namespace) -> None:
    """Query cadastral references by distance to coordinates."""
    client = CatastroClient()
    try:
        result = client.consulta_rccoor_distancia(
            args.coor_x,
            args.coor_y,
            args.srs
        )
        format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_cpmrc(args: argparse.Namespace) -> None:
    """Query coordinates by cadastral reference."""
    client = CatastroClient()
    try:
        result = client.consulta_cpmrc(
            args.provincia,
            args.municipio,
            args.srs,
            args.parcela or "",
            args.referencia_catastral or ""
        )
        format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_download_image(args: argparse.Namespace) -> None:
    """Download cadastral plot image using WMS service."""
    client = CatastroClient()
    try:
        filename = client.save_cadastral_image(
            bbox=args.bbox,
            filename=args.output,
            width=args.width or 800,
            height=args.height or 600,
            format_img=args.format_img or 'image/png',
            srs=args.srs or 'EPSG:4326',
            time=args.time
        )
        
        # Get file info for display
        file_info = client.get_file_info(filename)
        print(f"Image saved as: {file_info['filename']} ({file_info['size_formatted']})")
        
    except Exception as e:
        print(f"Error downloading image: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_download_parcel_wfs(args: argparse.Namespace) -> None:
    """Download parcel data using WFS INSPIRE service."""
    client = CatastroClient()
    try:
        filename = client.save_parcel_data(
            referencia_catastral=args.referencia_catastral,
            filename=args.output,
            srs=args.srs or 'EPSG:4326'
        )
        
        # Get file info for display
        file_info = client.get_file_info(filename)
        print(f"Parcel data saved as: {file_info['filename']} ({file_info['size_formatted']})")
        print(f"Format: GML (Geographic Markup Language)")
        
    except Exception as e:
        print(f"Error downloading parcel data: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_get_coordinates_by_ref(args: argparse.Namespace) -> None:
    """Get coordinates for a cadastral reference using the API client."""
    client = CatastroClient()
    try:
        # Extract province and municipality from cadastral reference if possible
        # For now, we'll need them as parameters - let's improve this command
        result = client.consulta_cpmrc(
            args.provincia,
            args.municipio,
            args.srs or 'EPSG:4326',
            "",  # parcela
            args.referencia_catastral
        )
        
        if args.format == 'table' and not getattr(args, 'raw', False):
            # Extract and format coordinate data nicely
            coord_list = result.get('Consulta_CPMRCResult', {}).get('coordenadas', {}).get('coord', [])
            if coord_list:
                print(f"Coordinates for cadastral reference {args.referencia_catastral}:\n")
                print(f"{'X (Longitude)':<17} {'Y (Latitude)':<17} {'SRS':<12} {'Address':<40}")
                print("-" * 88)
                for coord in coord_list:
                    geo = coord.get('geo', {})
                    srs = geo.get('srs', args.srs or 'EPSG:4326')
                    x_coord = geo.get('xcen', '')
                    y_coord = geo.get('ycen', '')
                    address = coord.get('ldt', 'N/A')
                    print(f"{x_coord:<17} {y_coord:<17} {srs:<12} {address:<40}")
            else:
                print("No coordinates found for the given cadastral reference.")
        else:
            format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_list_property_units(args: argparse.Namespace) -> None:
    """List available units/floors/doors for a property."""
    client = CatastroClient()
    try:
        result = client.get_property_units(
            args.provincia,
            args.municipio,
            args.referencia_catastral
        )
        
        if args.format == 'table' and not getattr(args, 'raw', False):
            # Extract and format unit data nicely
            unit_data = result.get('property_units_result', {})
            units = unit_data.get('units', [])
            total = unit_data.get('total_units', 0)
            
            print(f"Found {total} units for cadastral reference {args.referencia_catastral}:\n")
            print(f"{'Unit':<6} {'Floor':<8} {'Door':<8} {'Usage':<15} {'Surface (m²)':<12} {'Built':<6} {'Extended Reference':<20}")
            print("-" * 95)
            
            for unit in units:
                print(f"{unit.get('unit_id', ''):<6} {unit.get('floor', ''):<8} {unit.get('door', ''):<8} "
                      f"{unit.get('usage', '')[:14]:<15} {unit.get('surface', ''):<12} "
                      f"{unit.get('built_year', ''):<6} {unit.get('extended_reference', ''):<20}")
        else:
            format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_detailed_property_info(args: argparse.Namespace) -> None:
    """Get detailed property information with unit selection."""
    client = CatastroClient()
    try:
        result = client.get_detailed_property_info(
            args.provincia,
            args.municipio,
            args.referencia_catastral,
            args.extended_reference or ""
        )
        
        if args.format == 'table' and not getattr(args, 'raw', False):
            # Extract and format detailed data nicely
            detailed_data = result.get('consulta_detalladaResult', {})
            units = detailed_data.get('units', [])
            coordinates = detailed_data.get('coordinates', [])
            
            print(f"Detailed information for cadastral reference {args.referencia_catastral}:\n")
            
            # Show coordinates if available
            if coordinates:
                coord = coordinates[0]
                geo = coord.get('geo', {})
                print(f"Location: {coord.get('ldt', 'N/A')}")
                print(f"Coordinates: {geo.get('xcen', 'N/A')}, {geo.get('ycen', 'N/A')} ({geo.get('srs', 'N/A')})")
                print()
            
            # Show units
            print(f"Units ({len(units)} total):\n")
            print(f"{'Unit':<6} {'Floor':<8} {'Door':<8} {'Usage':<15} {'Surface (m²)':<12} {'Built':<6}")
            print("-" * 67)
            
            for unit in units:
                print(f"{unit.get('unit_id', ''):<6} {unit.get('floor', ''):<8} {unit.get('door', ''):<8} "
                      f"{unit.get('usage', '')[:14]:<15} {unit.get('surface', ''):<12} "
                      f"{unit.get('built_year', ''):<6}")
        else:
            format_output(result, args.format, args.compact)
        
    except CatastroApiError as e:
        print(f"API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_download_descriptive_report(args: argparse.Namespace) -> None:
    """Download descriptive and graphic report PDF for a property."""
    client = CatastroClient()
    try:
        filename = client.save_descriptive_report(
            referencia_catastral=args.referencia_catastral,
            filename=args.output,
            extended_reference=getattr(args, 'extended_reference', '') or ''
        )
        
        # Get file info for display
        file_info = client.get_file_info(filename)
        print(f"Descriptive report saved as: {file_info['filename']} ({file_info['size_formatted']})")
        print(f"Format: PDF (Consulta descriptiva y gráfica)")
        
    except Exception as e:
        print(f"Error downloading descriptive report: {e}", file=sys.stderr)
        if "No descriptive report available" in str(e):
            print("\nSuggestions:", file=sys.stderr)
            print("- Try using an extended reference for a specific unit:", file=sys.stderr)
            print(f"  pycatastro list-units [provincia] [municipio] {args.referencia_catastral}", file=sys.stderr)
            print("- Then use the extended reference from the unit list:", file=sys.stderr)
            print(f"  pycatastro download-report {args.referencia_catastral} --extended-reference [extended_ref]", file=sys.stderr)
        sys.exit(1)


def cmd_list_street_types(args: argparse.Namespace) -> None:
    """List all available street types."""
    print("Available street types:\n")
    print(f"{'Code':<4} {'Constant':<25} {'Description':<30}")
    print("-" * 61)
    
    street_types = tipos.get_all_street_types()
    for code, constant, desc in street_types:
        print(f"{code:<4} {constant:<25} {desc:<30}")


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser with all commands."""
    parser = argparse.ArgumentParser(
        description='CLI interface for pycatastro - Spanish Catastro API client',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get all provinces
  pycatastro provincias
  
  # Get municipalities in Valencia
  pycatastro municipios VALENCIA
  
  # Get streets named "MAYOR" in Valencia city
  pycatastro callejero VALENCIA VALENCIA --tipo-via CL --nombre-via MAYOR
  
  # Query by coordinates
  pycatastro rccoor --coor-x 728015.00 --coor-y 4372193.00 --srs EPSG:25830
  
  # Query by location (include street type for better results)
  pycatastro dnploc BARCELONA BARCELONA --sigla CL --calle ENAMORATS --numero 121
  
  # Query by cadastral reference
  pycatastro dnprc BARCELONA BARCELONA 1945320DF3814F
  
  # Download cadastral plot image
  pycatastro download-image --bbox "-8.6,-8.5,42.2,42.3" --width 1024 --height 768
  
  # Download parcel data (GML format)
  pycatastro download-parcel 36050A01000100
  
  # Download descriptive report (PDF format)
  pycatastro download-report 1945320DF3814F --extended-reference 1945320DF3814F0025AL
  
  # Get coordinates for cadastral reference
  pycatastro get-coordinates BARCELONA BARCELONA 1945320DF3814F
  
  # List available units in a building
  pycatastro list-units BARCELONA BARCELONA 1945320DF3814F
  
  # Get detailed property information
  pycatastro detailed-info BARCELONA BARCELONA 1945320DF3814F
  
  # List all street types
  pycatastro list-street-types
        """
    )
    
    # Global options
    parser.add_argument('--format', choices=['json', 'table'], default='table',
                       help='Output format (default: table)')
    parser.add_argument('--compact', action='store_true',
                       help='Compact JSON output (no indentation)')
    parser.add_argument('--raw', action='store_true',
                       help='Show raw API response without formatting')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Provincias command
    parser_prov = subparsers.add_parser('provincias', help='Get list of Spanish provinces')
    parser_prov.set_defaults(func=cmd_provincias)
    
    # Municipios command
    parser_muni = subparsers.add_parser('municipios', help='Get municipalities for a province')
    parser_muni.add_argument('provincia', help='Province name (e.g., VALENCIA)')
    parser_muni.add_argument('municipio', nargs='?', default='', help='Municipality filter (optional)')
    parser_muni.set_defaults(func=cmd_municipios)
    
    # Callejero command
    parser_call = subparsers.add_parser('callejero', help='Get streets for a municipality')
    parser_call.add_argument('provincia', help='Province name')
    parser_call.add_argument('municipio', help='Municipality name')
    parser_call.add_argument('--tipo-via', help='Street type (e.g., CL, AV, PZ)')
    parser_call.add_argument('--nombre-via', help='Street name filter')
    parser_call.set_defaults(func=cmd_callejero)
    
    # Numerero command
    parser_num = subparsers.add_parser('numerero', help='Get street numbers for a street')
    parser_num.add_argument('provincia', help='Province name')
    parser_num.add_argument('municipio', help='Municipality name')
    parser_num.add_argument('tipo_via', help='Street type (e.g., CL, AV, PZ)')
    parser_num.add_argument('nombre_via', help='Street name')
    parser_num.add_argument('--numero', help='Specific number filter (optional)')
    parser_num.set_defaults(func=cmd_numerero)
    
    # DNP Location command
    parser_dnploc = subparsers.add_parser('dnploc', help='Query cadastral data by location')
    parser_dnploc.add_argument('provincia', help='Province name (e.g., BARCELONA, VALENCIA)')
    parser_dnploc.add_argument('municipio', help='Municipality name (e.g., BARCELONA, VALENCIA)')
    parser_dnploc.add_argument('--sigla', help='Street type abbreviation (e.g., CL, AV, PZ)')
    parser_dnploc.add_argument('--calle', help='Street name (e.g., MAYOR, COLON, ENAMORATS)')
    parser_dnploc.add_argument('--numero', help='Street number (e.g., 1, 25, 121)')
    parser_dnploc.add_argument('--bloque', help='Block identifier')
    parser_dnploc.add_argument('--escalera', help='Staircase identifier')
    parser_dnploc.add_argument('--planta', help='Floor number')
    parser_dnploc.add_argument('--puerta', help='Door identifier')
    parser_dnploc.set_defaults(func=cmd_dnploc)
    
    # DNP Reference command
    parser_dnprc = subparsers.add_parser('dnprc', help='Query cadastral data by reference')
    parser_dnprc.add_argument('provincia', help='Province name')
    parser_dnprc.add_argument('municipio', help='Municipality name')
    parser_dnprc.add_argument('referencia_catastral', help='Cadastral reference')
    parser_dnprc.set_defaults(func=cmd_dnprc)
    
    # DNP Polygon-Parcel command
    parser_dnppp = subparsers.add_parser('dnppp', help='Query cadastral data by polygon-parcel')
    parser_dnppp.add_argument('provincia', help='Province name')
    parser_dnppp.add_argument('municipio', help='Municipality name')
    parser_dnppp.add_argument('poligono', help='Polygon')
    parser_dnppp.add_argument('parcela', help='Parcel')
    parser_dnppp.set_defaults(func=cmd_dnppp)
    
    # Coordinates to Reference command
    parser_rccoor = subparsers.add_parser('rccoor', help='Query cadastral reference by coordinates')
    parser_rccoor.add_argument('--coor-x', required=True, help='X coordinate')
    parser_rccoor.add_argument('--coor-y', required=True, help='Y coordinate')
    parser_rccoor.add_argument('--srs', required=True, help='Spatial reference system (e.g., EPSG:25830)')
    parser_rccoor.set_defaults(func=cmd_rccoor)
    
    # Coordinates with Distance command
    parser_rccoor_dist = subparsers.add_parser('rccoor-distancia', help='Query references by distance to coordinates')
    parser_rccoor_dist.add_argument('--coor-x', required=True, help='X coordinate')
    parser_rccoor_dist.add_argument('--coor-y', required=True, help='Y coordinate')
    parser_rccoor_dist.add_argument('--srs', required=True, help='Spatial reference system')
    parser_rccoor_dist.set_defaults(func=cmd_rccoor_distancia)
    
    # Reference to Coordinates command
    parser_cpmrc = subparsers.add_parser('cpmrc', help='Query coordinates by cadastral reference')
    parser_cpmrc.add_argument('provincia', help='Province name')
    parser_cpmrc.add_argument('municipio', help='Municipality name')
    parser_cpmrc.add_argument('srs', help='Spatial reference system')
    parser_cpmrc.add_argument('--parcela', help='Parcel')
    parser_cpmrc.add_argument('--referencia-catastral', help='Cadastral reference')
    parser_cpmrc.set_defaults(func=cmd_cpmrc)
    
    # List street types command
    parser_types = subparsers.add_parser('list-street-types', help='List all available street types')
    parser_types.set_defaults(func=cmd_list_street_types)
    
    # Download image command (WMS)
    parser_img = subparsers.add_parser('download-image', help='Download cadastral plot image using WMS')
    parser_img.add_argument('--bbox', required=True, help='Bounding box: minx,miny,maxx,maxy')
    parser_img.add_argument('--width', type=int, help='Image width in pixels (default: 800)')
    parser_img.add_argument('--height', type=int, help='Image height in pixels (default: 600)')
    parser_img.add_argument('--format-img', choices=['image/png', 'image/jpeg', 'image/gif', 'image/bmp', 'image/tif'], 
                           help='Image format (default: image/png)')
    parser_img.add_argument('--srs', help='Spatial reference system (default: EPSG:4326)')
    parser_img.add_argument('--time', help='Historical date in YYYY-MM-DD format')
    parser_img.add_argument('--output', help='Output filename')
    parser_img.set_defaults(func=cmd_download_image)
    
    # Download parcel WFS command
    parser_wfs = subparsers.add_parser('download-parcel', help='Download parcel data using WFS INSPIRE service')
    parser_wfs.add_argument('referencia_catastral', help='Cadastral reference (14 characters)')
    parser_wfs.add_argument('--srs', help='Spatial reference system (default: EPSG:4326)')
    parser_wfs.add_argument('--output', help='Output filename')
    parser_wfs.set_defaults(func=cmd_download_parcel_wfs)
    
    # Download descriptive report command
    parser_report = subparsers.add_parser('download-report', help='Download descriptive and graphic report (PDF)')
    parser_report.add_argument('referencia_catastral', help='Cadastral reference (14 characters)')
    parser_report.add_argument('--extended-reference', help='Extended reference for specific unit')
    parser_report.add_argument('--output', help='Output filename')
    parser_report.set_defaults(func=cmd_download_descriptive_report)
    
    # Get coordinates by reference command
    parser_coords = subparsers.add_parser('get-coordinates', help='Get coordinates for cadastral reference')
    parser_coords.add_argument('provincia', help='Province name')
    parser_coords.add_argument('municipio', help='Municipality name')
    parser_coords.add_argument('referencia_catastral', help='Cadastral reference')
    parser_coords.add_argument('--srs', help='Spatial reference system (default: EPSG:4326)')
    parser_coords.set_defaults(func=cmd_get_coordinates_by_ref)
    
    # List property units command
    parser_units = subparsers.add_parser('list-units', help='List available units/floors/doors in a property')
    parser_units.add_argument('provincia', help='Province name')
    parser_units.add_argument('municipio', help='Municipality name')
    parser_units.add_argument('referencia_catastral', help='Cadastral reference')
    parser_units.set_defaults(func=cmd_list_property_units)
    
    # Detailed property info command
    parser_detailed = subparsers.add_parser('detailed-info', help='Get detailed property information with unit selection')
    parser_detailed.add_argument('provincia', help='Province name')
    parser_detailed.add_argument('municipio', help='Municipality name')
    parser_detailed.add_argument('referencia_catastral', help='Cadastral reference')
    parser_detailed.add_argument('--extended-reference', help='Extended reference for specific unit')
    parser_detailed.set_defaults(func=cmd_detailed_property_info)
    
    return parser


def main() -> None:
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not hasattr(args, 'func'):
        parser.print_help()
        return
    
    # Execute the command
    args.func(args)


if __name__ == '__main__':
    main()