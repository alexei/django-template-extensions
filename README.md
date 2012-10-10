Additional Django template tags and filters

# ?: or IIF
The ?: ternary operator, conditional operator, inline if (iif) or ternary if for Django

## How to use
	{% ?: exp1 exp2 exp3 %}
	{% ?: exp1 exp2 %}
Which are equivalent to:
	{% if exp1 %}
		{{ exp2 }}
	{% else %}
		{{ exp3 }}
	{% endif %}
	{% if exp1 %}
		{{ exp1 }}
	{% else %}
		{{ exp2 }}
	{% endif %}
Each expression may be one of the following types:
* int, float, string
* None, True, False
* template variable

## Examples
	{% ?: article.is_published "Published" "Draft" %}
	She's got {% ?: number_of_apples "no" %} apples.
