import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite(
    extension_profiles=('collective.transform.creole:default',)
)

import collective.transform.creole

class TestCase(ptc.PloneTestCase):
    
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.transform.creole)
            fiveconfigure.debug_mode = False
        
        @classmethod
        def tearDown(cls):
            pass
    
    def performTransform(self, orig, targetMimetype='text/html', mimetype='text/wiki+creole'):
         return self.portal.portal_transforms.convertTo(targetMimetype, orig, context=self.portal, mimetype=mimetype).getData()


def test_suite():
    return unittest.TestSuite([
        
        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='collective.transform.creole',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='collective.transform.creole.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.transform.creole',
            test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='collective.transform.creole',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='CreoleTestCase')
