import pytest
from brownie import Wei, accounts

@pytest.fixture
def peek(Peek):
    peek_contract = Peek.deploy({"from": accounts[0]})
    return peek_contract

def test_allow_me_to_peek(peek):
    tx = peek.allowMeToPeek({"from": accounts[0]})
    tx.wait(1)

    assert peek.isAllowedToPeek(accounts[0]) == True

def test_allow_disallow_me_form_peeking(peek):
    tx = peek.allowMeToPeek({"from": accounts[0]})
    tx.wait(1)
    expected_bool = peek.amIAllowedToPeek(accounts[0].address, {"from": accounts[0]})
    tx = peek.disallowMeFromPeeking({"from": accounts[0]})
    tx.wait(1)

    assert peek.isAllowedToPeek(accounts[0]) == False

def test_am_i_allowed_to_peek(peek):
    tx = peek.allowMeToPeek({"from": accounts[0]})
    tx.wait(1)
    expected_bool = peek.amIAllowedToPeek(accounts[0].address, {"from": accounts[0]})

    assert peek.isAllowedToPeek(accounts[0]) == True

