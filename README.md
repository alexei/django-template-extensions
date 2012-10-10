Additional Django template tags and filters

# ?: or IIF
The ?: ternary operator, conditional operator, inline if (iif) or ternary if for Django
## How to use:
	{% load alx.iif %}

	{% ?: True True False %} -> True
	{% ?: True False %} -> True
