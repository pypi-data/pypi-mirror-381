"""Unit tests for temperature units."""

from wamu.temperature import Celsius, Fahrenheit, Kelvin, Temperature


def assert_is_freezing(temp: Temperature):
    """Assert all values match expected levels for freezing."""
    assert temp.celcius == 0.0
    assert temp.fahrenheit == 32.0
    assert temp.kelvin == 273.15


def test_convert_none():
    """Make sure that conversions with None are also None."""
    tempC = Celsius(None)

    assert tempC.celcius is None
    assert tempC.fahrenheit is None
    assert tempC.kelvin is None


def test_degC_freezing():
    """Confirm Celsius conversions for freezing."""
    tempC = Celsius(0)

    assert tempC == 0.0

    assert int(tempC) == 0
    assert float(tempC) == 0.0

    assert str(tempC) == "0 °C"
    assert repr(tempC) == "Celsius(0)"

    assert_is_freezing(tempC)

    # remove when deprecated property is removed
    assert tempC.degrees_celcius == tempC.celcius


def test_degF_freezing():
    """Confirm Fahrenheit conversions for freezing."""
    tempF = Fahrenheit(32)

    assert tempF == 32.0

    assert int(tempF) == 32
    assert float(tempF) == 32.0

    assert str(tempF) == "32 °F"
    assert repr(tempF) == "Fahrenheit(32)"

    assert_is_freezing(tempF)

    # remove when deprecated property is removed
    assert tempF.degrees_fahrenheit == tempF.fahrenheit


def test_degK_freezing():
    """Confirm Kelvin conversions for freezing."""
    tempK = Kelvin(273.15)

    assert tempK == 273.15

    assert int(tempK) == 273
    assert float(tempK) == 273.15

    assert str(tempK) == "273.15 K"
    assert repr(tempK) == "Kelvin(273.15)"

    assert_is_freezing(tempK)

    # remove when deprecated property is removed
    assert tempK.degrees_kelvin == tempK.kelvin


def test_boiling_temps():
    """Confirm conversions for boiling temperatures."""
    tempF = Fahrenheit(212.0)
    assert tempF.celcius == 100.0
    assert tempF.kelvin == 373.15

    tempC = Celsius(100.0)
    assert tempC.fahrenheit == 212.0
    assert tempF.kelvin == 373.15

    tempK = Kelvin(373.15)
    assert tempK.celcius == 100.0
    assert tempK.fahrenheit == 212.0


def test_mixed_temp_math():
    """Confirm math works with different temperature types."""
    tempC = Celsius(0)
    tempC += Fahrenheit(212)

    assert tempC.celcius == 100.0
    assert tempC.fahrenheit == 212.0

    tempK = Kelvin(0)
    tempK += Celsius(100)

    assert tempK.kelvin == 373.15
    assert tempK.celcius == 100.0


def test_mixed_temp_compare():
    """Confirm comparison works with different temperature types."""
    assert Celsius(0) == Fahrenheit(32)
    assert Celsius(100) > Kelvin(100)

    # make sure numbers can appear on either side of the comparison
    assert 100 >= Kelvin(100)
    assert Kelvin(100) >= 100
