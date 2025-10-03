"""Unit tests for velocity units."""

from conftest import isclose

from wamu.rate import CentimetersPerHour, InchesPerHour, MillimetersPerHour


def test_one_cm_per_hour():
    """Confirm simple CentimeterPerHour conversions."""
    cm_per_hr = CentimetersPerHour(1)

    assert cm_per_hr == 1.0

    assert float(cm_per_hr) == 1.0
    assert int(cm_per_hr) == 1

    assert cm_per_hr.millimeters_per_hr == 10.0
    assert isclose(cm_per_hr.inches_per_hour, 0.3937)

    assert str(cm_per_hr) == "1 cm/h"
    assert repr(cm_per_hr) == "CentimetersPerHour(1)"


def test_one_mm_per_hr():
    """Confirm simple MillimeterPerHour conversions."""
    mm_per_hr = MillimetersPerHour(1)

    assert mm_per_hr == 1.0

    assert float(mm_per_hr) == 1.0
    assert int(mm_per_hr) == 1

    assert mm_per_hr.centimeters_per_hr == 0.1
    assert isclose(mm_per_hr.inches_per_hour, 0.03937)

    assert str(mm_per_hr) == "1 mm/h"
    assert repr(mm_per_hr) == "MillimetersPerHour(1)"


def test_one_inch_per_hr():
    """Confirm simple InchPerHour conversions."""
    in_per_hr = InchesPerHour(1)

    assert in_per_hr == 1.0

    assert float(in_per_hr) == 1.0
    assert int(in_per_hr) == 1

    assert in_per_hr.centimeters_per_hr == 2.54
    assert in_per_hr.millimeters_per_hr == 25.4

    assert str(in_per_hr) == "1 in/h"
    assert repr(in_per_hr) == "InchesPerHour(1)"
