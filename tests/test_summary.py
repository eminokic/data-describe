import pytest

from ._test_data import DATA
import mwdata as mw
from mwdata.core.summary import cardinality


@pytest.fixture
def data():
    return DATA


@pytest.fixture
def load_summary(data):
    return mw.data_summary(data), data


def test_shape(load_summary):
    summary, data = load_summary
    assert summary.shape == (9, data.shape[1])


def test_cardinality(data):
    assert cardinality(data.d) == 2
    assert cardinality(data.e) == 2


def test_pandas_series(data):
    assert mw.data_summary(data.iloc[:, 0]).shape == (9, 1)
