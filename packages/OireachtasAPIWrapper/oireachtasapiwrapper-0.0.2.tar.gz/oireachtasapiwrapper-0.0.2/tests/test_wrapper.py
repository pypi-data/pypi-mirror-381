import pytest
from unittest.mock import Mock

from OireachtasAPI import wrapper


@pytest.mark.parametrize(
    ("endpoint_name", "expected_url"),
    [
        ("legislation", "https://api.oireachtas.ie/v1/legislation"),
        ("debates", "https://api.oireachtas.ie/v1/debates"),
        ("constituencies", "https://api.oireachtas.ie/v1/constituencies"),
        ("parties", "https://api.oireachtas.ie/v1/parties"),
        ("divisions", "https://api.oireachtas.ie/v1/divisions"),
        ("questions", "https://api.oireachtas.ie/v1/questions"),
        ("houses", "https://api.oireachtas.ie/v1/houses"),
        ("members", "https://api.oireachtas.ie/v1/members"),
    ],
)
def test_fetch_endpoint_returns_expected_url(endpoint_name, expected_url):
    assert wrapper.Wrapper()._fetch_endpoint(endpoint_name=endpoint_name) == expected_url


def test_wrapper_make_request_uses_api_client(monkeypatch, response_factory):
    payload = {"head": {"counts": {"billCount": 1}}}
    mock_response = response_factory(status_code=200, json_data=payload)
    mock_make_request = Mock(return_value=mock_response)
    monkeypatch.setattr(wrapper.Wrapper, "make_request", mock_make_request)

    response = wrapper.Wrapper().wrapper_make_request(endpoint_name="legislation", params={"limit": 1})

    assert response.json()["head"]["counts"]["billCount"] == 1
    mock_make_request.assert_called_once_with(
        endpoint="https://api.oireachtas.ie/v1/legislation", params={"limit": 1}
    )
