from django import template
import re

register = template.Library()

@register.filter(name="truncate_words_html")
def truncate_words_html(value, arg):
    """
    Trunca el texto HTML a un número específico de palabras.
    Preserva las etiquetas HTML.
    
    Uso: {{ texto|truncate_words_html:50 }}
    """
    try:
        length = int(arg)
    except ValueError:
        return value
    
    if not value:
        return ""
    
    # Contar palabras mientras se preservan las etiquetas HTML
    words_to_return = length
    
    # Separar por espacios pero preservando las etiquetas HTML
    tag_pattern = r'(<[^>]+>|[^<>\s]+)'
    splitted = re.findall(tag_pattern, value)
    
    # Recorrer y contar
    result = []
    word_count = 0
    
    for part in splitted:
        if not part.startswith('<'):
            word_count += 1
            if word_count > words_to_return:
                result.append('...')
                break
        result.append(part)
    
    return ''.join(result)

@register.filter(name="reading_time")
def reading_time(value):
    """
    Estima el tiempo de lectura de un artículo.
    
    Uso: {{ articulo.contenido|reading_time }}
    """
    if not value:
        return "0 min de lectura"
    
    # Contar las palabras (aproximadamente)
    word_count = len(value.split())
    
    # Velocidad promedio de lectura: 200 palabras por minuto
    minutes = max(1, word_count // 200)
    
    if minutes == 1:
        return "1 min de lectura"
    else:
        return f"{minutes} min de lectura"
