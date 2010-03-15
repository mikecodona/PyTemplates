__metaclass__ = type

class html_element():
    def __init__(self, *children):
        if len(children) >= 1 and isinstance(children[0], dict):
            self._attrs = children[0] 
            self._children = children[1:]
        else:
            self._children = children

    def __str__(self):
        params = dict()
        params['name'] =  self.__class__.__name__
        params['content']  = ''.join([str(child) for child in self._children])
        
        if hasattr(self, "_attrs"):
            params['attrs'] = ' '.join(["%s=\"%s\"" % (k, v) for k, v in self._attrs.iteritems()])

        if "attrs" in params:        
            return "<%(name)s %(attrs)s>%(content)s</%(name)s>" % params
        else:
            return "<%(name)s>%(content)s</%(name)s>" % params
        
class br(html_element):
    def __str__(self):
        return "<br />"

class html(html_element):
    def __init__(self, *children):
        super(html, self).__init__(*children)
        self._doctype = """"<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">"""

    def __str__(self):
        return self._doctype + super(html, self).__str__()

html_elements = ["h1", "h2", "h3", "p", "div", "span"]
for he in html_elements:
    globals()[he] = type(he, (html_element,), {})

if __name__ == "__main__":

    html_str = html(div({"class": "boring_class"}, h1("Hello"), p("Welcome to my html templating library")))

    print html_str
