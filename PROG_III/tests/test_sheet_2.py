import sys
import runpy
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

SHEET_2_DIR = ROOT_DIR / "sheet_2"


def test_ex1(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX1.py"))
    captured = capsys.readouterr()

    assert "'Ten': 10" in captured.out
    assert "'Twenty': 20" in captured.out
    assert "'Thirty': 30" in captured.out


def test_ex2(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX2.py"))
    captured = capsys.readouterr()

    # Valida todos os elementos da união
    for elemento in ["'Ten': 10", "'Twenty': 20", "'Thirty': 30", "'Fourty': 40", "'Fifty': 50"]:
        assert elemento in captured.out


def test_ex3(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX3.py"))
    captured = capsys.readouterr()

    assert "Alice's age is: 30" in captured.out


def test_ex4(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX4.py"))
    captured = capsys.readouterr()

    assert "Value from key 'history' is: 80" in captured.out
    assert "Updated Name: Mark" in captured.out


def test_ex5(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX5.py"))
    captured = capsys.readouterr()

    assert "Lowest subject is: Math" in captured.out


def test_ex6(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_2_DIR / "EX6.py"))
    captured = capsys.readouterr()

    assert "Inverted dictionary:" in captured.out
    for par in ["1: 'a'", "2: 'b'", "3: 'c'"]:
        assert par in captured.out