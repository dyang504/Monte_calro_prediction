from MCPredictor import MonteCarloPredictor

def test_generate_simulation():
    test_case = [[2],[4],[6]]
    # predict = MonteCarloPredictor(2934572.804, 364027.7298, 8)
    assert MonteCarloPredictor(2934572.804, 364027.7298, 8)._cal_total_mean(test_case) == 4
    
