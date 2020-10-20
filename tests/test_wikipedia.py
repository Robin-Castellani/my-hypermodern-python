"""
Test for the Wikipedia API
"""

from my_hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(lang='de')
    args, _ = mock_requests_get.call_args
    assert 'de.wikipedia.org' in args[0]