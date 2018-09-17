# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rescuearea.theme.testing import RESCUEAREA_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that rescuearea.theme is properly installed."""

    layer = RESCUEAREA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rescuearea.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rescuearea.theme'))

    def test_browserlayer(self):
        """Test that IRescueareaThemeLayer is registered."""
        from rescuearea.theme.interfaces import (
            IRescueareaThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IRescueareaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RESCUEAREA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['rescuearea.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rescuearea.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rescuearea.theme'))

    def test_browserlayer_removed(self):
        """Test that IRescueareaThemeLayer is removed."""
        from rescuearea.theme.interfaces import \
            IRescueareaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRescueareaThemeLayer,
            utils.registered_layers(),
        )
