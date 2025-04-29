###############
#
# This is your favorite file!
# Write your tests here
#
###############

from student import from_same_nest
from dog import *

def test_from_same_nest():
    assert from_same_nest(buddy,rocky)
    assert not from_same_nest(rex,bella)
    assert not from_same_nest(buster,rosie)
    assert not from_same_nest(thor,elsa)
    assert not from_same_nest(charlie,molly)
    assert not from_same_nest(cooper,sophie)
    assert not from_same_nest(pepper,pepper)

def test_different_father_same_mother():
    assert not from_same_nest(nala,bailey)
    assert not from_same_nest(nala,shadow)
    assert not from_same_nest(bailey,shadow)

def test_different_mother_same_father():
    assert not from_same_nest(bailey,ruby)

def test_different_parents():
    assert not from_same_nest(penny,leo)
    assert not from_same_nest(maggie,zeus)

def test_same_parents_different_year():
    assert not from_same_nest(max,luna)
    assert not from_same_nest(daisy,milo)