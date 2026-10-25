import sys
import runpy
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

SHEET_1_DIR = ROOT_DIR / "sheet_1"


def test_ex1(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX1.py"))
    captured = capsys.readouterr()

    assert "The maximum value in the list is: 8" in captured.out


def test_ex2(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX2.py"))
    captured = capsys.readouterr()

    assert "Even numbers: 2, Uneven numbers: 3" in captured.out


def test_ex3(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX3.py"))
    captured = capsys.readouterr()

    assert "List without duplicates: [1, 2, 3, 4, 5]" in captured.out


def test_ex4_tabuada(monkeypatch, capsys):
    # Simula a inserção do número '1' no terminal
    monkeypatch.setattr("builtins.input", lambda _: "1")

    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX4.py"))
    captured = capsys.readouterr()

    assert "--- Multiplication Table of 1 ---" in captured.out
    assert "1 x 1 = 1" in captured.out
    assert "1 x 10 = 10" in captured.out


def test_ex5(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX5.py"))
    captured = capsys.readouterr()

    assert "Rotated list: [3, 4, 5, 1, 2]" in captured.out


def test_ex6(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX6.py"))
    captured = capsys.readouterr()

    assert "Índice do 40: 3" in captured.out
    assert "Índice do 25: None" in captured.out


def test_ex7_binary_gap(capsys):
    capsys.readouterr()
    runpy.run_path(str(SHEET_1_DIR / "EX7.py"))
    captured = capsys.readouterr()

    assert "N = 1041 (10000010001_2): 5" in captured.out
    assert "N = 529 (1000010001_2): 4" in captured.out
    assert "N = 20 (10100_2): 1" in captured.out
    assert "N = 15 (1111_2): 0" in captured.out
    assert "N = 32 (100000_2): 0" in captured.out