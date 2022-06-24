from brownie import accounts, Peek

def allow_me_to_peek(acct):
    tx = Peek[-1].allowMeToPeek({"from": acct})
    tx.wait(1)

def deploy(account):
    peek_contract = Peek.deploy({"from": account}, publish_source=True)
    tx = peek_contract.allowMeToPeek({"from": account})
    tx.wait(1)

def verify(contractAddress):
    peek_contract = Peek.at(contractAddress)
    Peek.publish_source(peek_contract)

def main():
    account = accounts.load("your-id")
    deploy(account)
    # verify("0x6FcD37eCDdb8B7B6A10B8174FfBcaD0f1332A78f")
    