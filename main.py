# Sawron Mahian Jalil
# 213350

import proplog

print("p     not(p)")
print("------------")
for p in [True, False]:
    notp = proplog.negation(p)
    print(p,notp)
print()

print("p     q     p∧q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pNq = proplog.conjunction(p, q)
        print(p,q,pNq)
print()

# (disjunction)

print("p     q     p∨q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pVq = proplog.disjunction(p, q)
        print(p, q, pVq)
print()

# (conditional)
print("p     q     p→q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pImpq = proplog.implication(p, q)
        print(p, q, pImpq)
print()

# (biconditional)
print("p     q     p↔️q")
print("---------------")
for p in [True, False]:
    for q in [True, False]:
        pBiq = proplog.bi_implication(p, q)
        print(p, q, pBiq)
print()