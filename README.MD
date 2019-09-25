This project use Monte Carlo simulation to generate daily sales prediction according to the sample mean and deviation of exist data. It's different from mathematic model and just use past sales series data. 

W**hat is Monte Carlo methods, its origin, use case**

Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle([See Wikipedia for more information](https://en.wikipedia.org/wiki/Monte_Carlo_method?wprov=sfti1)). Optimization, numerical integration and generating draws from a probability distribution are main use cases. Any problem that follows a distribution can be solved by this methods.

W**hy choose Monte Carlo methods**

The sales outcome is determined by multiple factors which cannot easily detect. The terms like demand in Economics, the movement of market don't have a steam of data support the model to predict especially in business reality. Even if the data is provided, the sales can still not follow the models and yield predictions that is far away from the final result(Due to the complex nature of this problem). Therefore, it's hard to solve the problem by this way of modeling.

Utilizing the computer ability to simulate the possible outcome of some part of the problem, Monte Carlo shines at with limited dimensions of data but provide a much simple solution to real world problems.

H**ow we design the program**

The prediction variable is monthly sale. The data we have is only several daily sales in a month. We simply assume that the daily sale in a month follows normal distribution.

1. Calculate the mean and std of the given sample
2. Generate random number that follows the sample mean and std for the remaining days of the month
3. Repeat 100000+ times of the simulation results and store it 
4. Calculate mean, median, best and worst case of results and compare it to the goal, additionally a chance of complete that goal.

**How to use the code**

Download the code by using `git clone`.

    git clone ...
    cd project_directory
    virtualenv ENV_NAME
    pip install -r requirements.txt

    from MCPredictor import MonteCarloPredictor
    
    sale_prediction = MonteCarloPredictor(MEAN, STD, DAYS_LEFT)
    sale_predict.predict_mean_achievement()
    sale_predict.report_chance_of_achieve_KPI(CURRENT_SALE,TARGET_SALE)