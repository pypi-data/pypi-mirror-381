"""Unit tests for volume units."""

from conftest import isclose

from wamu.volume import FluidOunceUS, Gallon, Liter, Milliliter, Pint, Quart


def test_one_liter():
    """Confirm simple Liter conversions."""
    liter = Liter(1)

    assert liter == 1.0

    assert float(liter) == 1.0
    assert int(liter) == 1

    assert liter.liters == 1.0
    assert liter.milliliters == 1000.0

    assert isclose(liter.gallons, 0.2641720524)
    assert isclose(liter.pints, 2.1133764189)
    assert isclose(liter.quarts, 1.0566882094)
    assert isclose(liter.fl_ounces_us, 33.814022702)

    assert str(liter) == "1 L"
    assert repr(liter) == "Liter(1)"


def test_one_ml():
    """Confirm simple Milliliter conversions."""
    ml = Milliliter(1)

    assert ml == 1.0

    assert float(ml) == 1.0
    assert int(ml) == 1

    assert ml.milliliters == 1.0
    assert ml.liters == 0.001

    assert isclose(ml.fl_ounces_us, 0.0338140227)

    assert str(ml) == "1 mL"
    assert repr(ml) == "Milliliter(1)"


def test_one_gal():
    """Confirm simple Gallon conversions."""
    gal = Gallon(1)

    assert gal == 1.0

    assert float(gal) == 1.0
    assert int(gal) == 1

    assert gal.gallons == 1.0
    assert gal.pints == 8.0
    assert gal.quarts == 4.0
    assert gal.fl_ounces_us == 128.0

    assert isclose(gal.liters, 3.78541178)
    assert isclose(gal.milliliters, 3785.41178)

    assert str(gal) == "1 gal"
    assert repr(gal) == "Gallon(1)"


def test_one_pint():
    """Confirm simple Pint conversions."""
    pint = Pint(1)

    assert pint == 1.0

    assert float(pint) == 1.0
    assert int(pint) == 1

    assert pint.pints == 1.0
    assert pint.quarts == 0.5
    assert pint.fl_ounces_us == 16.0

    assert isclose(pint.liters, 0.473176473)
    assert isclose(pint.milliliters, 473.176473)

    assert str(pint) == "1 pt"
    assert repr(pint) == "Pint(1)"


def test_one_quart():
    """Confirm simple Quart conversions."""
    quart = Quart(1)

    assert quart == 1.0

    assert float(quart) == 1.0
    assert int(quart) == 1

    assert quart.quarts == 1.0
    assert quart.fl_ounces_us == 32.0

    assert isclose(quart.liters, 0.946352946)
    assert isclose(quart.milliliters, 946.352946)

    assert str(quart) == "1 qt"
    assert repr(quart) == "Quart(1)"


def test_one_us_oz():
    """Confirm simple US fluid ounce conversions."""
    fl_oz = FluidOunceUS(1)

    assert fl_oz == 1.0

    assert float(fl_oz) == 1.0
    assert int(fl_oz) == 1

    assert fl_oz.pints == 0.0625
    assert fl_oz.quarts == 0.03125
    assert fl_oz.gallons == 0.0078125

    assert isclose(fl_oz.liters, 0.0295735296)
    assert isclose(fl_oz.milliliters, 29.5735295625)

    assert str(fl_oz) == "1 fl oz"
    assert repr(fl_oz) == "FluidOunceUS(1)"
