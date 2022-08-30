from demo_ci_fastapi import __version__


def test_version():
    """Default test."""
    assert __version__ == '0.1.0'
