from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_button(text, button_type="button", color="purple", additional_classes=""):
    """
    Template tag para generar un botón con estilos.

    Args:
        text (str): Texto del botón.
        button_type (str): Tipo del botón (submit, reset, button).
        color (str): Color principal del botón.
        additional_classes (str): Clases adicionales para personalización.

    Returns:
        str: HTML del botón con estilos aplicados.
    """

    button_html = f"""
    <button
        class="
            text-white
            bg-gradient-to-br from-{color}-600 to-{color}-800 hover:bg-gradient-to-bl
            focus:ring-4 focus:outline-none focus:ring-{color}-300 dark:focus:ring-{color}-800
            font-medium text-sm rounded-lg
            px-5 py-2.5
            {additional_classes}"
        type="{button_type}">
        {text}
    </button>
    """
    return mark_safe(button_html)




@register.simple_tag
def render_url_button(text, url=None, color="blue", additional_classes="", **kwargs):
    from django.urls import reverse, NoReverseMatch

    # Filtrar solo los argumentos necesarios para reverse
    url_kwargs = {k: v for k, v in kwargs.items() if not k in ["color", "additional_classes"]}

    try:
        if not url:
            raise ValueError("El parámetro 'url' es obligatorio y no puede ser vacío.")
        href = reverse(url, kwargs=url_kwargs)
    except (NoReverseMatch, ValueError) as e:
        print(f"Error en render_url_button: {e}")
        href = "#"

    button_html = f"""
    <a href="{href}"
       class="text-white bg-gradient-to-br from-{color}-600 to-{color}-800 hover:bg-gradient-to-bl
              focus:ring-4 focus:outline-none focus:ring-{color}-300 dark:focus:ring-{color}-800
              font-medium rounded-lg text-sm px-5 py-2.5 {additional_classes}">
        {text}
    </a>
    """
    return mark_safe(button_html)

