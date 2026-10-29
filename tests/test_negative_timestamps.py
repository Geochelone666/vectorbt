from datetime import datetime, timezone
import pytest
from vectorbt.utils.datetime_ import to_tzaware_datetime


@pytest.mark.parametrize('power',[0,3,6,9])
@pytest.mark.parametrize('seconds',[1_000_000_000,1_700_000_000])
def test_negative_integer_units_ignore_sign_when_measuring_magnitude(power,seconds):
    raw=seconds*10**power
    assert to_tzaware_datetime(raw,naive_tz='UTC')==datetime.fromtimestamp(seconds,timezone.utc)
    assert to_tzaware_datetime(-raw,naive_tz='UTC')==datetime.fromtimestamp(-seconds,timezone.utc)


@pytest.mark.parametrize('raw',[-1,-999_999_999,-1_000_000_000])
def test_negative_seconds_match_float_timestamp(raw):
    assert to_tzaware_datetime(raw,naive_tz='UTC')==to_tzaware_datetime(float(raw),naive_tz='UTC')
