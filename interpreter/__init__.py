#coding=utf8
__author__ = 'markel'


from pprint import pprint
from xml_parse import ConvertXmlToDict


pprint(ConvertXmlToDict('spr_prod.gfd', nameDirect='layout'))