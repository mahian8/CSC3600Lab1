# Hello world Python
import matplotlib

def negation(p):
    # returns the opposite truth value for p (i.e. not(p))
    return not(p)

def conjunction(p, q):
    # return the AND value i.e. p∧q
    return (p and q)

def disjunction(p, q):
    # Returns p OR q
    return p or q

def implication(p, q):
    # Returns p -> q (if p then q)
    return (not p) or q

def bi_implication(p, q):
    # Returns p <-> q (p if and only if q)
    return p == q