Additional Django template tags and filters

# ?: or IIF
The ?: ternary operator, conditional operator, inline if (iif) or ternary if for Django

## How to use
	{% load alx.iif %}

	{% ?: exp1 exp2 exp3 %}
	{% ?: exp1 exp2 %}
Each expression may be one of the following types:
* int, float, string
* None, True, False
* template variable

## Examples
	{% ?: article.is_published "Published" "Draft" %}
	She's got {% ?: number_of_apples "no" %} apples.
