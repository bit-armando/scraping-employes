import re


title_regex = re.compile(r'(cien(cia|t[íi]fic[oa]) (en |de )?datos)|(data scien(ce|tist))', re.IGNORECASE)
english_regex = re.compile(r'ingl[ée]s\:?\s\(?(requisito|nivel)?[\s\W]?(\d+\s?(\%\s?)?)?(b[áa]sico|intermedio|avanzado|conversacional|deseable|opcional|t[ée]cnico)?\)?', re.IGNORECASE)

skills_regex = [
    r'ph?yth?on', r'html5',  r'css3', r'javascript', r'typescript',
    r'angular', r'react', r'mern', r'node', r'npm',  r'express', r'bootstrap',
    r'php', r'lumen', r'laravel',
    r'mongodb', r'dynamodb',  r'mysql',  r'postgresql', r'nosql', r'er model',
    r'mvc', r'unit[\- ]testing',
    r'redis', r'memcache', r'amctivemq', r'rabbitmq', r'solr',
    r'git', r'github',  r'agile', r'scrum',
    r'unix', r'linux',
    r'rest-api', r'aws',  r'apache hadoop', r'hadoop', r'spark', r'azure',
    r'tableau'
]

# TODO: Mover esta celda a un módulo separado
estados_mex = {
    'agu': 'Aguascalientes', 'bc': 'Baja California', 'bcs': 'baja California Sur',
    'cam': 'Campeche', 'chp': 'Chiapas', 'chih': 'Chihuahua',
    'cdmx': 'Ciudad de México', 'coa': 'Coahuila', 'col': 'Colima',
    'dur': 'Durango', 'gua': 'Guanajuato', 'gro': 'Guerrero',
    'hid': 'Hidalgo', 'jal': 'Jalisco', 'mex': 'México',
    'mic': 'Michoacán', 'mor': 'Morelos', 'nay': 'Nayarit',
    'n l': 'Nuevo León', 'oax': 'Oaxaca', 'pue': 'Puebla',
    'que': 'Querétaro', 'roo': 'Quintana Roo', 'slp': 'San Luis Potosí',
    'sin': 'Sinaloa', 'son': 'Sonora', 'tab': 'Tabasco',
    'tam': 'Tamaulipas', 'tla': 'Tlaxcala', 'ver': 'Veracruz',
    'yuc': 'Yucatán', 'zac': 'Zacatecas',
}

estados_usa = {
    'al': 'Alabama', 'ak': 'Alaska', 'az': 'Arizona', 'as': 'Samoa Americana',
    'ar': 'Arkansas', 'ca': 'California', 'co': 'Colorado', 'ct': 'Connecticut',
    'de': 'Delaware', 'dc': 'Distrito de Columbia', 'fl': 'Florida', 'ga': 'Georgia',
    'gu': 'Guam', 'hi': 'Hawái', 'id': 'Idaho', 'il': 'Illinois',
    'in': 'Indiana', 'ia': 'Iowa', 'ks': 'Kansas', 'ky': 'Kentucky',
    'la': 'Louisiana', 'me': 'Maine', 'md': 'Maryland', 'ma': 'Massachusetts',
    'mi': 'Michigan', 'mn': 'Minnesota', 'ms': 'Misisipi', 'mo': 'Misouri',
    'mt': 'Montana', 'ne': 'Nebraska', 'nv': 'Nevada', 'nh': 'New Hampshire',
    'nj': 'New Jersey', 'nm': 'New Mexico', 'ny': 'New York', 'nc': 'North Carolina',
    'nd': 'South Carolina', 'mp': 'Islas Marianas del Norte', 'oh': 'Ohio',
    'ok': 'Oklahoma', 'or': 'Oregon', 'pw': 'Palaos', 'pa': 'Pensilvania',
    'pr': 'Puerto Rico', 'ri': 'Rhode Island', 'sc': 'South Carolina',
    'sd': 'South Dakota', 'tn': 'Tennessee', 'tx': 'Texas', 'ut': 'Utah',
    'vt': 'Vermont', 'vi': 'Islas Vírgenes', 'va': 'Virginia', 'wa': 'Washington',
    'wv': 'Virginia Occidental', 'wi': 'Wisconsin', 'wy': 'Wyoming',
}

estados_all = {**estados_mex, **estados_usa} # Unir todos los diccionarios

def get_estado(abr: str) -> str:
    """\
    Recibe una abreviatura y devuelve su estado correspondiente.
    En caso de fallar devuelve la abreviatura.
    """
    return estados_all.get(abr.lower(), abr)
