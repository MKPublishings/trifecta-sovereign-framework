import numpy as np

def boc_genesis(nodes=5, txns=100):
    """Simulate genesis consensus deployment."""
    votes = np.random.binomial(1, 0.8, (nodes, txns))  # Probabilistic voting (80% approval)
    consensus = np.mean(votes, axis=0) > 0.5  # Majority rule
    success_rate = np.mean(consensus)
    print(f"B.O.C. Consensus Success Rate: {success_rate:.4f}")
    return success_rate
