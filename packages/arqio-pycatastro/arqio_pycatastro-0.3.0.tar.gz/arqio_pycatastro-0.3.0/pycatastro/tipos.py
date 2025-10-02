"""
Street type constants for Spanish Catastro API.
Based on tipos.go from alejndr0/go-catastro
"""

# Street type constants
ACCESO = "AC"
AGREGADO = "AG" 
ALDEA = "AL"
ALAMEDA = "AL"
ANDADOR = "AN"
AREA = "AR"
ARRABAL = "AR"
AUTOPISTA = "AU"
AVENIDA = "AV"
ARROYO = "AY"
BAJADA = "BJ"
BLOQUE = "BL"
BARRIO = "BO"
BARRANQUIL = "BQ"
BARRANCO = "BR"
CANADA = "CA"
COLEGIO = "CG"
CIGARRAL = "CG"
CHALET = "CH"
CINTURON = "CI"
CALLEJA = "CJ"
CALLEJON = "CJ"
CALLE = "CL"
CAMINOS = "CM"
CARMEN = "CM"
COLONIA = "CN"
CONCEJO = "CO"
COLEGIO_CO = "CO"
CAMPA = "CP"
CAMPO = "CP"
CARRETERA = "CR"
CARRERA = "CR"
CASERIO = "CS"
CUESTA = "CT"
COSTANILLA = "CT"
CONJUNTO = "CU"
CALEYA = "CY"
CALLIZO = "CZ"
DETRAS = "DE"
DIPUTACION = "DP"
DISEMINADOS = "DS"
EDIFICIOS = "ED"
EXTRAMUROS = "EM"
ENTRADA = "EN"
ESPALDA = "EP"
EXTRARADIO = "ER"
ESCALINATA = "ES"
EXPLANADA = "EX"
FERROCARRIL = "FC"
FINCA = "FN"
GLORIETA = "GL"
GRUPO = "GR"
GRAN_VIA = "GV"
HUERTA = "HT"
JARDINES = "JR"
LAGO = "LA"
LADO = "LD"
LADERA = "LD"
LUGAR = "LG"
MALECON = "MA"
MERCADO = "MC"
MUELLE = "ML"
MUNICIPIO = "MN"
MASIAS = "MS"
MONTE = "MT"
MANZANA = "MZ"
POBLADO = "PB"
PLACETAS = "PC"
PARTIDA = "PD"
PARTICULAR = "PI"
PASAJE = "PJ"
PASADIZO = "PJ"
POLIGONO = "PL"
PARAMO = "PM"
PARROQUIA = "PQ"
PARQUE = "PQ"
PROLONGACION = "PR"
CONTINUACION = "PR"
PASEO = "PS"
PUENTE = "PT"
PASADIZO_PJ = "PU"
PLAZA = "PZ"
QUINTA = "QT"
RACONADA = "RA"
RAMBLA = "RB"
RINCON = "RC"
RINCONA = "RC"
RONDA = "RD"
RAMAL = "RM"
RAMPA = "RP"
RIERA = "RR"
RUA = "RU"
SALIDA = "SA"
SECTOR = "SC"
SENDA = "SD"
SOLAR = "SL"
SALON = "SN"
SUBIDA = "SU"
TERRENOS = "TN"
TORRENTE = "TO"
TRAVESIA = "TR"
URBANIZACION = "UR"
VALLE = "VA"
VIADUCTO = "VD"
VIA = "VI"
VIAL = "VL"
VEREDA = "VR"


def get_all_street_types():
    """
    Get all street types with their codes, constants, and descriptions.
    
    Returns:
        List of tuples: (code, constant_name, description)
    """
    return [
        ("AC", "ACCESO", "Access"),
        ("AG", "AGREGADO", "Aggregate"),
        ("AL", "ALDEA/ALAMEDA", "Village/Avenue"),
        ("AN", "ANDADOR", "Walkway"),
        ("AR", "AREA/ARRABAL", "Area/Suburb"),
        ("AU", "AUTOPISTA", "Highway"),
        ("AV", "AVENIDA", "Avenue"),
        ("AY", "ARROYO", "Stream"),
        ("BJ", "BAJADA", "Descent"),
        ("BL", "BLOQUE", "Block"),
        ("BO", "BARRIO", "Neighborhood"),
        ("BQ", "BARRANQUIL", "Small ravine"),
        ("BR", "BARRANCO", "Ravine"),
        ("CA", "CANADA", "Cattle path"),
        ("CG", "COLEGIO/CIGARRAL", "School/Country house"),
        ("CH", "CHALET", "Chalet"),
        ("CI", "CINTURON", "Belt"),
        ("CJ", "CALLEJA/CALLEJON", "Lane/Alley"),
        ("CL", "CALLE", "Street"),
        ("CM", "CAMINOS/CARMEN", "Roads/Carmen"),
        ("CN", "COLONIA", "Colony"),
        ("CO", "CONCEJO/COLEGIO", "Council/School"),
        ("CP", "CAMPA/CAMPO", "Field"),
        ("CR", "CARRETERA/CARRERA", "Road/Career"),
        ("CS", "CASERIO", "Hamlet"),
        ("CT", "CUESTA/COSTANILLA", "Slope/Small slope"),
        ("CU", "CONJUNTO", "Complex"),
        ("CY", "CALEYA", "Lane (Asturian)"),
        ("CZ", "CALLIZO", "Narrow street"),
        ("DE", "DETRAS", "Behind"),
        ("DP", "DIPUTACION", "Provincial council"),
        ("DS", "DISEMINADOS", "Scattered"),
        ("ED", "EDIFICIOS", "Buildings"),
        ("EM", "EXTRAMUROS", "Outside walls"),
        ("EN", "ENTRADA", "Entrance"),
        ("EP", "ESPALDA", "Back"),
        ("ER", "EXTRARADIO", "Outskirts"),
        ("ES", "ESCALINATA", "Steps"),
        ("EX", "EXPLANADA", "Esplanade"),
        ("FC", "FERROCARRIL", "Railway"),
        ("FN", "FINCA", "Estate"),
        ("GL", "GLORIETA", "Roundabout"),
        ("GR", "GRUPO", "Group"),
        ("GV", "GRAN_VIA", "Main avenue"),
        ("HT", "HUERTA", "Orchard"),
        ("JR", "JARDINES", "Gardens"),
        ("LA", "LAGO", "Lake"),
        ("LD", "LADO/LADERA", "Side/Hillside"),
        ("LG", "LUGAR", "Place"),
        ("MA", "MALECON", "Embankment"),
        ("MC", "MERCADO", "Market"),
        ("ML", "MUELLE", "Dock"),
        ("MN", "MUNICIPIO", "Municipality"),
        ("MS", "MASIAS", "Farmhouses"),
        ("MT", "MONTE", "Mountain"),
        ("MZ", "MANZANA", "Block"),
        ("PB", "POBLADO", "Settlement"),
        ("PC", "PLACETAS", "Small squares"),
        ("PD", "PARTIDA", "District"),
        ("PI", "PARTICULAR", "Private"),
        ("PJ", "PASAJE/PASADIZO", "Passage"),
        ("PL", "POLIGONO", "Polygon"),
        ("PM", "PARAMO", "Moor"),
        ("PQ", "PARROQUIA/PARQUE", "Parish/Park"),
        ("PR", "PROLONGACION/CONTINUACION", "Extension/Continuation"),
        ("PS", "PASEO", "Boulevard"),
        ("PT", "PUENTE", "Bridge"),
        ("PU", "PASADIZO", "Passageway"),
        ("PZ", "PLAZA", "Square"),
        ("QT", "QUINTA", "Villa"),
        ("RA", "RACONADA", "Corner"),
        ("RB", "RAMBLA", "Rambla"),
        ("RC", "RINCON/RINCONA", "Corner"),
        ("RD", "RONDA", "Ring road"),
        ("RM", "RAMAL", "Branch"),
        ("RP", "RAMPA", "Ramp"),
        ("RR", "RIERA", "Stream (Catalan)"),
        ("RU", "RUA", "Street (Galician)"),
        ("SA", "SALIDA", "Exit"),
        ("SC", "SECTOR", "Sector"),
        ("SD", "SENDA", "Path"),
        ("SL", "SOLAR", "Plot"),
        ("SN", "SALON", "Hall"),
        ("SU", "SUBIDA", "Ascent"),
        ("TN", "TERRENOS", "Grounds"),
        ("TO", "TORRENTE", "Torrent"),
        ("TR", "TRAVESIA", "Cross street"),
        ("UR", "URBANIZACION", "Development"),
        ("VA", "VALLE", "Valley"),
        ("VD", "VIADUCTO", "Viaduct"),
        ("VI", "VIA", "Way"),
        ("VL", "VIAL", "Road"),
        ("VR", "VEREDA", "Path")
    ]