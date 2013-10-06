import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['static'])

class Main:
  def index(self):
    tmpl = lookup.get_template("index.txt")
    return tmpl.render()
  
  def analyze(self, sentenceReceived=None):
    print sentenceReceived

  index.exposed = True
  analyze.exposed=True

cherrypy.quickstart(Main())
