# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from matem.chartkick.testing import IntegrationTestCase
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class TestsInstall(IntegrationTestCase):
    """Test installation of matem.chartkick into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_product_installed(self):
        """Test if matem.chartkick is installed in portal_quickinstaller."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('matem.chartkick'))


def test_suite():
    """This """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
