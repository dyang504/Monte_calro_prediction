import numpy as np
import statistics


def generate_simulation(mean, std, days_left, simulation_times=100000):
    sale_list = []
    for i in range(simulation_times):
        sale = np.random.normal(mean, std, days_left).round(0)
        sale_list.append(sale)
    return sale_list


def cal_total_mean(sale_list):
    sale_sum = []
    for sale in sale_list:
        sale_sum.append(sale.sum())
    return statistics.mean(sale_sum)


def chance_of_achieve_target(sale_list, total_now, target):
    chance_list = []
    for sale in sale_list:
        complete_rate = (sale.sum() + total_now) / target
        chance_list.append(complete_rate)
    return chance_list


def achieve_report(current_sale: float, target, sale_simulation):
    result = {}
    result["predict_month_sale"] = cal_total_mean(
        sale_simulation) + current_sale
    completion_rate_simulation = chance_of_achieve_target(
        sale_simulation, current_sale, target)
    result['max_complete_rate'] = max(completion_rate_simulation)
    result['min_complete_rate'] = min(completion_rate_simulation)
    result['mean_complete_rate'] = statistics.mean(completion_rate_simulation)
    number_of_completion = len(
        [item for item in completion_rate_simulation if item >= 1])
    result['chance_of_completion'] = number_of_completion / len(sale_simulation)
    return result


class MCPredictor:
    def __init__(self, mean, std, days_left):
        self.sale_simulation = generate_simulation(mean, std, days_left)

    def predict_mean_achievement(self):
        return cal_total_mean(self.sale_simulation)

    def predict_max_achievement(self):
        pass

    def predicxt_min_achievement(self):
        pass

    def report_chance_of_achieve_KPI(self, current_sale, target):
        return achieve_report(current_sale, target, self.sale_simulation)


if __name__ == "__main__":
    sale_predict = MCPredictor(2934572.804, 364027.7298, 8)
    print(sale_predict.predict_mean_achievement())
    print(sale_predict.report_chance_of_achieve_KPI(64560601.68,100820000))
