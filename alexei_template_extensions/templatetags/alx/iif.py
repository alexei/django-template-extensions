'''
The ?: ternary operator, conditional operator, inline if (iif) or ternary if for Django

Copyright (c) Alexandru Marasteanu <hello [at) alexei (dot] ro>
All rights reserved.

Distributed under the 3-Clause BSD license
'''

from django import template

register = template.Library()

class IifNode(template.Node):
    def __init__(self, exp1 = None, exp2 = None, exp3 = None):
        if not exp3:
            exp3 = exp2
            exp2 = exp1
        self.exp1 = self.fix_type(exp1)
        self.exp2 = self.fix_type(exp2)
        self.exp3 = self.fix_type(exp3)

    def render(self, context):
        try:
            if isinstance(self.exp1, template.Variable):
                self.exp1 = self.exp1.resolve(context)
            if isinstance(self.exp2, template.Variable):
                self.exp2 = self.exp2.resolve(context)
            if isinstance(self.exp3, template.Variable):
                self.exp3 = self.exp3.resolve(context)
            return self.exp2 if bool(self.exp1) else self.exp3
        except template.VariableDoesNotExist:
            return ""

    def fix_type(self, v):
        try:
            i = int(v)
            if str(i) == v:
                v = i
            else:
                raise ValueError()
        except ValueError:
            try:
                f = float(v)
                v = f
            except ValueError:
                if v[0] == v[-1] and v[0] in ('"', "'"):
                    v = v[1:-1]
                elif v == "None":
                    v = None
                elif v in ("True", "False"):
                    v = bool(v)
                else:
                    v = template.Variable(v)

        return v

@register.tag("?:")
@register.tag("iif")
def iif(parser, token):
    try:
        tag, exp1, exp2, exp3 = token.split_contents()
    except ValueError:
        try:
            tag, exp1, exp2 = token.split_contents()
            exp3 = None
        except ValueError:
            raise template.TemplateSyntaxError, "%r tag requires two or three arguments" % token.contents.split()[0]

    return IifNode(exp1 = exp1, exp2 = exp2, exp3 = exp3)
