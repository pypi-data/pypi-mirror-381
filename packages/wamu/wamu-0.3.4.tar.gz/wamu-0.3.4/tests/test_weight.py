"""Unit tests for weight units."""

from conftest import isclose

from wamu.weight import Gram, Kilogram, Milligram, Ounce, Pound


def test_one_kg():
    """Confirm simple Kilogram conversions."""
    kg = Kilogram(1)

    assert kg == 1.0

    assert float(kg) == 1.0
    assert int(kg) == 1

    assert kg.kilograms == 1.0
    assert kg.grams == 1000.0
    assert kg.milligrams == 1000000.0

    assert isclose(kg.pounds, 2.204622)
    assert isclose(kg.ounces, 35.274)


def test_one_g():
    """Confirm simple Gram conversions."""
    g = Gram(1)

    assert g == 1.0

    assert float(g) == 1.0
    assert int(g) == 1

    assert g.kilograms == 0.001
    assert g.grams == 1.0
    assert g.milligrams == 1000.0

    assert isclose(g.pounds, 0.002204622)
    assert isclose(g.ounces, 0.035274)


def test_one_mg():
    """Confirm simple Milligram conversions."""
    mg = Milligram(1)

    assert mg == 1.0

    assert float(mg) == 1.0
    assert int(mg) == 1

    assert mg.kilograms == 0.000001
    assert mg.grams == 0.001
    assert mg.milligrams == 1.0

    assert isclose(mg.pounds, 0.000002204622)
    assert isclose(mg.ounces, 0.000035274)


def test_one_lb():
    """Confirm simple Pound conversions."""
    lb = Pound(1)

    assert lb == 1.0

    assert float(lb) == 1.0
    assert int(lb) == 1

    assert lb.pounds == 1.0
    assert lb.ounces == 16.0
    assert lb.tons == 0.0005

    assert isclose(lb.kilograms, 0.45359237)


def test_one_oz():
    """Confirm simple Ounce conversions."""
    oz = Ounce(1)

    assert oz == 1.0

    assert float(oz) == 1.0
    assert int(oz) == 1

    assert oz.ounces == 1.0
    assert oz.pounds == 0.0625
    assert oz.tons == 0.00003125

    assert isclose(oz.kilograms, 0.02834952)
