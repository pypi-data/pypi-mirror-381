import pytest
from unittest.mock import Mock

from OireachtasAPI import api, errors


@pytest.mark.parametrize(
    "endpoint",
    [
        "https://api.oireachtas.ie/v1/legislation",
        "https://api.oireachtas.ie/v1/debates",
        "https://api.oireachtas.ie/v1/constituencies",
        "https://api.oireachtas.ie/v1/parties",
        "https://api.oireachtas.ie/v1/divisions",
        "https://api.oireachtas.ie/v1/questions",
        "https://api.oireachtas.ie/v1/houses",
        "https://api.oireachtas.ie/v1/members",
    ],
)
def test_make_request_success(monkeypatch, response_factory, endpoint):
    mock_response = response_factory(status_code=200)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

    response = api.API().make_request(endpoint=endpoint)

    assert response.status_code == 200
    mock_get.assert_called_once_with(url=endpoint, params={})


@pytest.mark.parametrize(
    ("status_code", "expected_exception"),
    [
        (400, errors.BadRequest),
        (401, errors.Unauthorised),
        (403, errors.Forbidden),
        (404, errors.NotFound),
        (429, errors.TooManyRequests),
    ],
)
def test_make_request_raises_for_error_status(monkeypatch, response_factory, status_code, expected_exception):
    mock_response = response_factory(status_code=status_code)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

    with pytest.raises(expected_exception):
        api.API().make_request(endpoint="https://api.oireachtas.ie/v1/legislation")

    mock_get.assert_called_once()
