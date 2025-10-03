"""Unit tests for pressure units."""

from conftest import isclose

from wamu.pressure import (
    Atmosphere,
    Bar,
    Hectopascal,
    InchesMercury,
    Pascal,
    PoundsPerSquareInch,
)


def test_one_pascal():
    """Confirm simple Pascal conversions."""
    pa = Pascal(1)

    assert pa == 1.0

    assert float(pa) == 1.0
    assert int(pa) == 1

    assert pa.bar == 1e-5
    assert isclose(pa.pounds_per_sq_in, 0.0001450377)

    assert str(pa) == "1 Pa"
    assert repr(pa) == "Pascal(1)"


def test_one_hectopascal():
    """Confirm simple Hectopascal conversions."""
    hPa = Hectopascal(1)

    assert hPa == 1.0

    assert float(hPa) == 1.0
    assert int(hPa) == 1

    assert hPa.bar == 1e-3

    assert isclose(hPa.inches_mercury, 0.02953)

    assert str(hPa) == "1 hPa"
    assert repr(hPa) == "Hectopascal(1)"


def test_one_inch_mercury():
    """Confirm simple InchesMercury conversions."""
    inHg = InchesMercury(1)

    assert inHg == 1.0

    assert float(inHg) == 1.0
    assert int(inHg) == 1

    assert isclose(inHg.bar, 0.033864)
    assert isclose(inHg.pounds_per_sq_in, 0.4911542)

    assert str(inHg) == "1 inHg"
    assert repr(inHg) == "InchesMercury(1)"


def test_one_bar():
    """Confirm simple Bar conversions."""
    bar = Bar(1)

    assert bar == 1.0

    assert float(bar) == 1.0
    assert int(bar) == 1

    assert bar.hectopascals == 1000.0
    assert isclose(bar.pounds_per_sq_in, 14.50377)

    assert str(bar) == "1 bar"
    assert repr(bar) == "Bar(1)"


def test_one_atmosphere():
    """Confirm simple Atmosphere conversions."""
    atm = Atmosphere(1)

    assert atm == 1.0

    assert float(atm) == 1.0
    assert int(atm) == 1

    assert isclose(atm.bar, 1.01325)
    assert isclose(atm.pounds_per_sq_in, 14.69595)

    assert str(atm) == "1 atm"
    assert repr(atm) == "Atmosphere(1)"


def test_one_psi():
    """Confirm simple PSI conversions."""
    psi = PoundsPerSquareInch(1)

    assert psi == 1.0

    assert float(psi) == 1.0
    assert int(psi) == 1

    assert isclose(psi.bar, 0.0689476)
    assert isclose(psi.inches_mercury, 2.036020461087)

    assert str(psi) == "1 psi"
    assert repr(psi) == "PoundsPerSquareInch(1)"
