import pandas as pd
from topsisx import topsis

def test_ranking_simple():
    df = pd.DataFrame({"C1":[250,200,300],"C2":[6,7,5],"C3":[2,3,4],"C4":[5,9,6]})
    scores, ranks = topsis(df, weights=[1,1,1,2], impacts=['+','+','-','+'])
    assert scores.shape == (3,)
    assert ranks.shape == (3,)
    assert set(ranks.tolist()) == {1,2,3}
