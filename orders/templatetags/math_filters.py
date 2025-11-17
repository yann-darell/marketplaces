from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply two numbers in templates: {{ value|mul:arg }}.

    Uses Decimal for safer arithmetic, falls back to float on error.
    Returns empty string on unrecoverable error.
    """
    try:
        # Coerce to Decimal via string to avoid float precision issues
        v = Decimal(str(value))
        a = Decimal(str(arg))
        res = v * a
        # If result is an integer-valued Decimal, return int to avoid trailing .0
        if res == res.quantize(1):
            return int(res)
        return res
    except (InvalidOperation, TypeError, ValueError):
        try:
            return float(value) * float(arg)
        except Exception:
            return ''
