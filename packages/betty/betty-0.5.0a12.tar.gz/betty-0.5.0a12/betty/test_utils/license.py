"""
Test utilities for :py:mod:`betty.license`.
"""

from __future__ import annotations

from typing_extensions import override

from betty.license import License
from betty.locale.localizable import Localizable, Plain
from betty.locale.localizer import DEFAULT_LOCALIZER
from betty.test_utils.plugin import DummyPluginBase, PluginInstanceTestBase


class LicenseTestBase(PluginInstanceTestBase[License]):
    """
    A base class for testing :py:class:`betty.license.License` implementations.
    """

    def test_summary(self) -> None:
        """
        Tests :py:meth:`betty.license.License.summary` implementations.
        """
        for sut in self.get_sut_instances():
            assert sut.summary.localize(DEFAULT_LOCALIZER)

    def test_text(self) -> None:
        """
        Tests :py:meth:`betty.license.License.text` implementations.
        """
        for sut in self.get_sut_instances():
            assert sut.text.localize(DEFAULT_LOCALIZER)

    def test_url(self) -> None:
        """
        Tests :py:meth:`betty.license.License.url` implementations.
        """
        for sut in self.get_sut_instances():
            url = sut.url
            if url is not None:
                assert url.localize(DEFAULT_LOCALIZER)


class DummyLicense(DummyPluginBase, License):
    """
    A dummy license implementation.
    """

    @override
    @property
    def summary(self) -> Localizable:
        return Plain("")  # pragma: nocover

    @override
    @property
    def text(self) -> Localizable:
        return Plain("")  # pragma: nocover
