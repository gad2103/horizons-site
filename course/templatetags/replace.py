import re 

from django import template
register = template.Library()

@register.filter
def replace ( string, args ): 
    search  = args.split(",")[0]
    replace = args.split(",")[1]

    return re.sub( search, replace, str(string) )
