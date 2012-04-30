# Create your handlers here
from airy.core.web import *

class SampleHandler(AiryHandler):
    def get(self):
       #some logic here
       variable = 'assign data'
       self.render('#content', 'sample/index.html', variable=variable)     
