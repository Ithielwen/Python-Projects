from Adventure import playagain, barkeep_patron_outside, barkeep, wait, brawl, patron, message, perform, outside, sounds, stay
import pytest

def test_playagain(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Y")

    i = input("Play again? Y or N")
    assert i == "Y"
    
    monkeypatch.setattr('builtins.input', lambda _: "N")
    
    i = input("Play again? Y or N?")
    assert i == "N"

    monkeypatch.setattr('builtins.input', lambda _: "ghrnft")
    
    i = input("Play again? Y or N?")
    return "error"

def test_barkeep_patron_outside(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "BARKEEP")

    i = input("BARKEEP, PATRON, OUTSIDE?")
    assert i == "BARKEEP"

    monkeypatch.setattr('builtins.input', lambda _: "PATRON")

    i = input("BARKEEP, PATRON, OUTSIDE?")
    assert i == "PATRON"

    monkeypatch.setattr('builtins.input', lambda _: "OUTSIDE")

    i = input("BARKEEP, PATRON, OUTSIDE")
    assert i == "OUTSIDE"
    
    monkeypatch.setattr('builtins.input', lambda _: "ghfrhf")

    i = input("BARKEEP, PATRON, OUTSIDE?")
    return "error"

def test_barkeep(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "WAIT")

    i = input("Do you WAIT your turn or do you start a BRAWL with the Orc?")
    assert i == "WAIT"

    monkeypatch.setattr('builtins.input', lambda _: "BRAWL")

    i = input("Do you want to WAIT your turn or do you start a BRAWL with the Orc?")
    assert i == "BRAWL"

    monkeypatch.setattr('builtins.input', lambda _: "ghjourhgr")

    i = input("Do you want to WAIT your turn or do you start a BRAWL with the Orc?")
    return "error"

def test_wait(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "NECKLACE")

    i = input("Do you look for the lost NECKLACE or defeat the MIMICS?")
    assert i == "NECKLACE"

    monkeypatch.setattr('builtins.input', lambda _: "MIMICS")

    i = input("Do you look for the lost NECKLACE or defeat the MIMICS?")
    assert i == "MIMICS"

    monkeypatch.setattr('builtins.input', lambda _: "ihvghef")

    i = input("Do you look for the lost NECKLACE or defeat the MIMICS?")
    return "error"

def test_brawl(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "FIREBALL")

    i = input("Do you cast FIREBALL at the Orc or do you draw your SWORDS?")
    assert i == "FIREBALL"

    monkeypatch.setattr('builtins.input', lambda _: "SWORDS")

    i = input("Do you cast FIREBALL at the Orc or do you draw your SWORDS?")
    assert i == "SWORDS"

    monkeypatch.setattr('builtins.input', lambda _: "Fhefefha;w")

    i = input("Do you cast FIREBALL at the Orc or do you draw your SWORDS?")
    return "error"

def test_patron(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "MESSAGE")

    i = input("MESSAGE or PERFORM")
    assert i == "MESSAGE"

    monkeypatch.setattr('builtins.input', lambda _: "PERFORM")

    i = input("MESSAGE or PERFORM")
    assert i == "PERFORM"

    monkeypatch.setattr('builtins.input', lambda _: "fghherfe")

    i = input("MESSAGE or PERFORM")
    return "error"

def test_message(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "LEFT")

    i = input("LEFT or RIGHT")
    assert i == "LEFT"

    monkeypatch.setattr('builtins.input', lambda _: "RIGHT")

    i = input("LEFT or RIGHT")
    assert i == "RIGHT"

    monkeypatch.setattr('builtins.input', lambda _: "jfrhgwe")

    i = input("LEFT or RIGHT")
    return "error"

def test_perform(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "HIGHER")

    i = input("HIGHER or LOWER")
    assert i == "HIGHER"

    monkeypatch.setattr('builtins.input', lambda _: "LOWER")

    i = input("HIGHER or LOWER")
    assert i == "LOWER"

    monkeypatch.setattr('builtins.input', lambda _: "hfgrhger")

    i = input("HIGHER or LOWER")
    return "error"

def test_outside(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "SOUNDS")

    i = input("SOUNDS or STAY")
    assert i == "SOUNDS"

    monkeypatch.setattr('builtins.input', lambda _: "STAY")

    i = input("SOUNDS or STAY")
    assert i == "STAY"

    monkeypatch.setattr('builtins.input', lambda _: "hfeufe")

    i = input("SOUNDS or STAY")
    return "error"

def test_sounds(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "HIGHER")

    i = input("HIGHER or LOWER")
    assert i == "HIGHER"

    monkeypatch.setattr('builtins.input', lambda _: "LOWER")

    i = input("HIGHER or LOWER")
    assert i == "LOWER"

    monkeypatch.setattr('builtins.input', lambda _: "hfeehgeh")
    
    i = input("HIGHER or LOWER")
    return "error"

def test_stay(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "INVESTIGATE")

    i = input("INVESTIGATE or NOTHING")
    assert i == "INVESTIGATE"

    monkeypatch.setattr('builtins.input', lambda _: "NOTHING")

    i = input("INVESTIGATE or NOTHING")
    assert i == "NOTHING"

    monkeypatch.setattr('builtins.input', lambda _: "hgoueg")

    i = input("INVESTIGATE or NOTHING")
    return "error"

pytest.main(["-v", "--tb=line", "-rN", __file__])
