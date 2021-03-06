"""Test for the Wikipedia API."""

from unittest.mock import Mock

import click
import pytest

from my_hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    """The language passed is results in a call to that Wikipedia lang."""
    wikipedia.random_page(lang="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    """It return a Page instance."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """A void JSON response raises a Click exception."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
