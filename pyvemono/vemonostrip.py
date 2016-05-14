''' Python Code for Communication with the Visible Energy Monostrip '''
import requests
import os
import urllib2
from xml.dom.minidom import parseString

class VeMonoStripErr(Exception):
    pass

class VeMonoStrip:
    def __init__(self, server, plug):
        self.urlbase="http://%s" % '/'.join([server, str(plug)])

    @classmethod
    def _GetText(cls, nodelist):
      rc = []
      for node in nodelist:
          if node.nodeType == node.TEXT_NODE:
              rc.append(node.data)
      return ''.join(rc)

    def Get(self, key):       
        url = self.urlbase + "/status.xml"
        try:
          request = urllib2.urlopen(url,timeout=2)
        except urllib2.URLError as e:
          raise VeMonoStripErr("Unable to access %s: %s" % (url, e))
        dom = parseString(request.read())
        state = dom.getElementsByTagName(key)[0]
        return self._GetText(state.childNodes)

    def Set(self, pwr):
        url = self.urlbase + "/set.xml?value=" + pwr
        try:
          request = urllib2.urlopen(url,timeout=2)
        except urllib2.URLError as e:
          raise VeMonoStripErr("Unable to access %s: %s" % (url, e))




