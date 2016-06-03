import unittest

import second as bas2
import third as bk2
class Region2Test (unittest.TestCase):
    def setUp(self):
        self.tab15=[[0.0035,300, 0.394913866E+02, 0.254991145E+04, 0.241169160E+04, 0.852238967E+01, 0.191300162E+01, 0.427920172E+03],
                    [0.0035,700, 0.923015898E+02, 0.333568375E+04, 0.301262819E+04, 0.101749996E+02, 0.208141274E+01, 0.644289068E+03],
                    [30,    700, 0.542946619E-02, 0.263149474E+04, 0.246861076E+04, 0.517540298E+01, 0.103505092E+02, 0.480386523E+03]]
        self.tab24=[[0.001, 3000, 0.534433241E+03],
                    [3,     3000, 0.575373370E+03],
                    [3,     4000, 0.101077577E+04]]
        self.tab29=[[0.1, 7.5, 0.399517097E+03],
                    [0.1, 8,   0.514127081E+03],
                    [2.5, 8,   0.103984917E+04]]

def testSpecificEnthalpy_PT(self):
           places = 6
           for item in self.tab15:
               self.assertAlmostEqual(bas2.enthalpyreg2(item[0], item[1]),item[2],places)
def testSpecificVolume_PT(self):
           places = 6
           for item in self.tab15:
               self.assertAlmostEqual(bas2.volreg2(item[0], item[1]),item[3], places)
def testSpecificinternalEnergy_PT(self):
           places = 6
           for item in self.tab15:
               self.assertAlmostEqual(bas2.energyreg2(item[0], item[1]),item[4],places) 
               
def testSpecificEntropy_PT(self):
           places = 6
           for item in self.tab15:
               self.assertAlmostEqual(bas2.entropyreg2(item[0], item[1]),item[5],places)                

def testSpecificisobaricheatcapacity_PT(self):
           places = 6
           for item in self.tab15:
               self.assertAlmostEqual(bas2.cpreg2(item[0], item[1]),item[6],places)  
 
def testSpeedofsound_PT(self):
           places = 5
           for item in self.tab15:
               self.assertAlmostEqual(bas2.spsoundreg2(item[0], item[1]),item[7],places)                  

def testTemperature_ph(self):
           places = 6
           for item in self.tab24:
               self.assertAlmostEqual(bk2.phtoTreg2(item[0], item[1]),item[2],places)
               
def testTemperature_ps(self):
           places = 6
           for item in self.tab29:
               self.assertAlmostEqual(bk2.pstoTreg2(item[0], item[1]),item[2],places)
             
def suite_use_make_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Region2Test))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite_use_make_suite')

