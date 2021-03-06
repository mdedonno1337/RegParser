#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import re

from MDmisc.RecursiveDefaultDict import defDict
from MDmisc.string import split_no_empty

class RegParser( object ):
    def __init__( self, reg = None ):
        self.reg = reg
        self.d = []
        
        self.load( self.reg )
        
        self.ret = defDict()
        
    def load( self, reg ):
        for exp in split_no_empty( reg, '\n' ):
            exp = re.sub( '\s+', '[\s\t]+', exp )
            exp = re.compile( exp )
            self.d.append( exp )
    
    def process( self, data ):
        i = 0
        j = 0
        
        for line in split_no_empty( data, "\n" ):
            m = re.match( self.d[i], line )
            
            j += 1
            
            if m == None:
                i += 1
                j = 0
                
                m = re.match( self.d[i], line )
                if m == None:
                    continue
                
            for key, value in m.groupdict().iteritems():
                self.ret[ i ][ j ][ key ] = value
        
    def get_json( self ):
        return json.dumps( self.ret, sort_keys = True, indent = 4, separators = ( ',', ': ' ) )
    
    def get_dict( self ):
        return self.ret
    
