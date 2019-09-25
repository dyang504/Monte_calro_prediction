import numpy as np
import statistics


class MonteCarloPredictor:
    """
    Simulate sales and make prediction(Mean, Max, Min)
    
    Arguments to init:
    mean -- The mean value of past sales
    std -- Standard diviation of past sales
    days_left -- How many days remain in the month
    """
    def __init__(self, mean: float, std: float, days_left: int):
        self.sale_simulation = self._generate_simulation(mean, std, days_left)

    def predict_mean_achievement(self):
        return self._cal_total_mean(self.sale_simulation)

    def predict_max_achievement(self):
        return max(self.sale_simulation)

    def predicxt_min_achievement(self):
        return min(self.sale_simulation)

    def report_chance_of_achieve_KPI(self, current_sale: float, target: int):
        """
        Calculate the chance of achieve KPI target
        
        Keyword arguments:
        current_sale -- How much sale by now
        target -- How much sale this month targeted
        """
        return self._achieve_report(current_sale, target, self.sale_simulation)
    
    def _generate_simulation(self,mean: float, std: float, days_left: int, simulation_times=100000):
        """
        Simulate the following days sales
        
        Keyword arguments:
        mean -- The mean value of past sales
        std -- Standard diviation of past sales
        days_left -- How many days remain in the month
        simulation_times -- How many times the simulation should repeat(default: 100000)
        """
        sale_list = []
        for i in range(simulation_times):
            sale = np.random.normal(mean, std, days_left).round(0)
            sale_list.append(sale)
        return sale_list
    
    def _cal_total_mean(self,sale_list: list):
        """
        Calculate mean of total simulation results
        
        Keyword arguments:
        sale_list -- The sale simulations list
        """
        sale_sum = []
        for sale in sale_list:
            sale_sum.append(sum(sale))
        return statistics.mean(sale_sum)
    
    def _chance_of_achieve_target(self, sale_list: list, current_sale: float, target: int):
        """
        Calculate the rate of achieve target KPI
        
        Keyword arguments:
        sale_list -- The sale simulations list
        current_sale -- How much sale by now
        target -- How much sale this month targeted
        """
        chance_list = []
        for sale in sale_list:
            complete_rate = (sale.sum() + current_sale) / target
            chance_list.append(complete_rate)
        return chance_list
    
    def _achieve_report(self, current_sale: float, target: int, sale_simulation: list):
        result = {}
        result["predict_month_sale"] = self._cal_total_mean(sale_simulation) + current_sale
        completion_rate_simulation = self._chance_of_achieve_target(sale_simulation, current_sale, target)
        result['max_complete_rate'] = max(completion_rate_simulation)
        result['min_complete_rate'] = min(completion_rate_simulation)
        result['mean_complete_rate'] = statistics.mean(completion_rate_simulation)
        number_of_completion = len(
            [item for item in completion_rate_simulation if item >= 1])
        result['chance_of_completion'] = number_of_completion / len(sale_simulation)
        return result


if __name__ == "__main__":
    sale_prediction = MonteCarloPredictor(2934572.804, 364027.7298, 8)
    print(sale_predict.predict_mean_achievement())
    print(sale_predict.report_chance_of_achieve_KPI(64560601.68,100820000))
