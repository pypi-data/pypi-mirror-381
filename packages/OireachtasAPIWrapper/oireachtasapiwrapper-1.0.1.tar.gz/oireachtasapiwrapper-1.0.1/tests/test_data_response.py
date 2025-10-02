import pytest
from unittest.mock import Mock

from OireachtasAPI import api


@pytest.mark.parametrize(
    ("endpoint", "count_key"),
    [
        ("https://api.oireachtas.ie/v1/legislation", "billCount"),
        ("https://api.oireachtas.ie/v1/questions", "questionCount"),
        ("https://api.oireachtas.ie/v1/debates", "debateCount"),
        ("https://api.oireachtas.ie/v1/constituencies", "constituencyCount"),
        ("https://api.oireachtas.ie/v1/parties", "partyCount"),
    ],
)
def test_fetch_data_response_contains_expected_counts(monkeypatch, response_factory, endpoint, count_key):
    payload = {"head": {"counts": {count_key: 1}}}
    mock_response = response_factory(status_code=200, json_data=payload)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

    response = api.API().make_request(endpoint=endpoint, params={"limit": 1})

    assert count_key in response.json()["head"]["counts"]
    mock_get.assert_called_once_with(url=endpoint, params={"limit": 1})
