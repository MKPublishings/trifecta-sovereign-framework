from omni_ai import omni_synthesis
from qfstds import qfstds_transit
from boc_genesis import boc_genesis

def run_trifecta():
    omni_score = omni_synthesis()
    qfstds_eff = qfstds_transit()
    boc_rate = boc_genesis()
    overall = (omni_score + qfstds_eff + boc_rate) / 3
    print(f"Unified Trifecta Score: {overall:.4f}")

if __name__ == "__main__":
    run_trifecta()