import pytest

from OireachtasAPI import urls


@pytest.mark.parametrize(
    ("method_name", "expected"),
    [
        ("_legislation_url", "https://api.oireachtas.ie/v1/legislation"),
        ("_debates_url", "https://api.oireachtas.ie/v1/debates"),
        ("_constituencies_url", "https://api.oireachtas.ie/v1/constituencies"),
        ("_parties_url", "https://api.oireachtas.ie/v1/parties"),
        ("_divisions_url", "https://api.oireachtas.ie/v1/divisions"),
        ("_questions_url", "https://api.oireachtas.ie/v1/questions"),
        ("_houses_url", "https://api.oireachtas.ie/v1/houses"),
        ("_members_url", "https://api.oireachtas.ie/v1/members"),
    ],
)
def test_url_builders_return_expected_values(method_name, expected):
    url_builder = urls.URLs()
    method = getattr(url_builder, method_name)
    assert method() == expected
