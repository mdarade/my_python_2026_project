import pytest

from my_python_2026_project.main import greet, main


def test_greet_default() -> None:
    assert greet() == "Hello, world!"


def test_greet_name() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert "Hello, world!" in capsys.readouterr().out
