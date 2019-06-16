#!/usr/bin/env python
# coding: utf-8
import numpy as np
import statistics


def generate_simulation(mean,std,days_left,simulation_times= 100000):
    sale_list = []
    for i in range(simulation_times):
        sale = np.random.normal(mean,std,days_left).round(0)
        sale_list.append(sale)
    return sale_list


def cal_total_mean(sale_list):
    sale_sum = []
    for sale in sale_list:
        sale_sum.append(sale.sum())
    return statistics.mean(sale_sum)

def chance_of_achieve_target(sale_list,total_now,target):
    chance_list = []
    for sale in sale_list:
        complete_rate = (sale.sum() + total_now) / target
        chance_list.append(complete_rate)
    return chance_list


sale_list = generate_simulation(2934572.804,364027.7298,8,1000000)
cal_total_mean(sale_list) + 64560601.68


rate_list = chance_of_achieve_target(sale_list,64560601.68,100820000)


sale_list = generate_simulation(2557926.804,268773.4431,8)
cal_total_mean(sale_list) + 2557926.804*23


def predict_mean_sale(current_sale:float,current_mean:float,std:float,days_remian:int,target,simulate_times=1000000):
    result = {}
    sale_simulation = generate_simulation(current_mean,std,days_remian,simulate_times)
    result["predict_month_sale"] =  cal_total_mean(sale_simulation) + current_sale
    completion_rate_simulation = chance_of_achieve_target(sale_simulation,current_sale,target)
    result['max_complete_rate'] = max(completion_rate_simulation)
    result['min_complete_rate'] = min(completion_rate_simulation)
    result['mean_complete_rate'] = statistics.mean(completion_rate_simulation)
    number_of_completion = len([item for item in completion_rate_simulation if item >= 1])
    result['chance_of_completion'] = number_of_completion / simulate_times
    return result


predict_mean_sale(current_sale=41651951.19,current_mean=2975139,std=983765,days_remian=17,target=90800000)

predict_mean_sale(current_sale=19820245,current_mean=2477500,std=203895,days_remian=22,target=86280000)
