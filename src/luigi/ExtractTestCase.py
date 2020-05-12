import os
import datetime
import json
import marbles.core
import pandas as pd
#directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
#os.chdir(directorio)
#file = 'afluencia-diaria-del-metro-cdmx.json'
#json_file = open(file, 'rb')
#class ExtractTestCase(marbles.core.TestCase):
#    def __init__(self):
#        pass
#    def featurize(self, X):
 
class ExtractTestCase(marbles.core.TestCase):
        def setUp(self):
                self.json_file = json_file   # ... #json_file

        #def __init__(self):
        #        self.json_file
        
        def tearDown(self):
                delattr(self, 'json_file')
        
        def test_extract(self):
                self.assertTrue(self.json_file.read(2) != '[]', note = 'json file is empty')
                now = datetime.datetime.now()
                passfail=self.json_file.read(2) != '[]'
                nombreprueba='test load datos raw'
                print (now.strftime("%Y-%m-%d %H:%M:%S"))
                df1 = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
                return df1

if __name__ == '__main__':
    marbles.core.main()