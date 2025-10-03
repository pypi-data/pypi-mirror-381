"""Unit tests for velocity units."""

from conftest import isclose

from wamu.velocity import (
    FeetPerSecond,
    KilometersPerHour,
    Knots,
    Mach,
    MetersPerSecond,
    MilesPerHour,
)


def test_one_mps():
    """Confirm simple MetersPerSecond conversions."""
    mps = MetersPerSecond(1)

    assert mps == 1.0

    assert float(mps) == 1.0
    assert int(mps) == 1

    assert mps.kilometers_per_hr == 3.6

    assert isclose(mps.miles_per_hr, 2.23694)
    assert isclose(mps.feet_per_sec, 3.28084)
    assert isclose(mps.knots, 1.94384449)

    assert str(mps) == "1 m/s"
    assert repr(mps) == "MetersPerSecond(1)"


def test_one_kph():
    """Confirm simple KilometersPerHour conversions."""
    kph = KilometersPerHour(1)

    assert kph == 1.0

    assert float(kph) == 1.0
    assert int(kph) == 1

    assert isclose(kph.meters_per_sec, 0.27777778)
    assert isclose(kph.miles_per_hr, 0.62137119)
    assert isclose(kph.feet_per_sec, 0.91134442)
    assert isclose(kph.knots, 0.5399568)
    assert isclose(kph.mach, 0.00080985)

    assert str(kph) == "1 km/h"
    assert repr(kph) == "KilometersPerHour(1)"


def test_one_mph():
    """Confirm simple MilesPerHour conversions."""
    mph = MilesPerHour(1)

    assert mph == 1.0

    assert float(mph) == 1.0
    assert int(mph) == 1

    assert isclose(mph.feet_per_sec, 1.46666667)
    assert isclose(mph.meters_per_sec, 0.44704)
    assert isclose(mph.kilometers_per_hr, 1.609344)
    assert isclose(mph.knots, 0.8689762419)
    assert isclose(mph.mach, 0.00130332)

    assert str(mph) == "1 mph"
    assert repr(mph) == "MilesPerHour(1)"


def test_one_fps():
    """Confirm simple FeetPerSecond conversions."""
    fps = FeetPerSecond(1)

    assert fps == 1.0

    assert float(fps) == 1.0
    assert int(fps) == 1

    assert isclose(fps.meters_per_sec, 0.3048)
    assert isclose(fps.kilometers_per_hr, 1.09728)
    assert isclose(fps.miles_per_hr, 0.68181818)
    assert isclose(fps.knots, 0.5924838)

    assert str(fps) == "1 fps"
    assert repr(fps) == "FeetPerSecond(1)"


def test_one_knot():
    """Confirm simple Knot conversions."""
    knot = Knots(1)

    assert knot == 1.0

    assert float(knot) == 1.0
    assert int(knot) == 1

    assert knot.kilometers_per_hr == 1.852
    assert isclose(knot.meters_per_sec, 0.514444)
    assert isclose(knot.miles_per_hr, 1.1507794)
    assert isclose(knot.feet_per_sec, 1.6878099)
    assert isclose(knot.mach, 0.00149984)

    assert str(knot) == "1 kt"
    assert repr(knot) == "Knots(1)"


def test_one_mach():
    """Confirm simple Mach conversions."""
    mach = Mach(1)

    assert mach == 1.0

    assert float(mach) == 1.0
    assert int(mach) == 1

    assert mach.meters_per_sec == 343.0
    assert mach.kilometers_per_hr == 1234.8

    assert isclose(mach.miles_per_hr, 767.269148)
    assert isclose(mach.feet_per_sec, 1125.328084)
    assert isclose(mach.knots, 666.738661)

    assert str(mach) == "1 M"
    assert repr(mach) == "Mach(1)"
