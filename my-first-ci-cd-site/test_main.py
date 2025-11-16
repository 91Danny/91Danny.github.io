import main
import pytest

def test_add():
    """Test the add function with various inputs"""
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0
    assert main.add(0, 0) == 0

def test_add_negative_numbers():
    """Test adding negative numbers"""
    assert main.add(-5, -3) == -8

def test_main_output(capsys):
    """Test the main function output"""
    main.main()
    captured = capsys.readouterr()
    assert "Hello from my CI/CD app!" in captured.out
    assert "2 + 3 is 5" in captured.out
