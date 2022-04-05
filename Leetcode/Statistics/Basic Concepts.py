======== Mean =============================================
It is a measure of central tendency of a probability distribution along median and mode.
It is also referred to as an expected value.

======== Mean vs Median and Mode =============================================

If the mean is greater than the median, the distribution is positively skewed (has long right tail)
If the mean is less than the median, the distribution is negatively skewed. (has logn left tail)
In skewed data, the tail region may act as an outlier for the statistical model
and it will affect the model's performance especailly regression based models.
Mean更容易受outlier影响。 举例： 湾区工资巨富问题拉大mean
Mode: most common number

========= standard deviation =============================================
is a measure of how dispersed the data is in relation to the mean.
Low standard deviation means data are clustered around the mean,
and high standard deviation indicates data are more spread out

========= variance =============================================
measures how far a random sample can differ from the true mean (average), square of std.

========= variation =============================================
When happens: when two groups have same mean, median and mode.
example: team A height (72,73,76,76,78), team B height (67,72,76,76,84)
we can check by the
(1) range = max(value) - min(value), tell us how spread out the data is

(2) we can calculate the sample std = sqrt((x - x bar<mean>)^2/n-1),
sample std can tell us how far each data points to the sample mean, another indicator how spread out the data is.

========= Confidence Interval =============================================
A confidence interval gives us a range of values that is likely to contain the unknown population parameter.
95% is a commonly used confidence level which means that
in repeated sampling 95% of the confidence intervals include the parameter.

For example: we want to know the average height for men in the US. Randomly select certain men
and measure their heights. we can say 95% Confidence interval is between 168-185cm. It's likely
to cover the true average height for men in the US.

========= Confidence Level =============================================
The confidence level in hypothesis testing is the probability of not rejecting the
null hypothesis when the null hypothesis is true. P(Not Rejecting H0|H0 is True) = 1 -
P(Rejecting H0|H0 is True)

========== Significance Level (type I error) =============================================
The confidence level in hypothesis testing is the probability of rejecting the
null hypothesis when the null hypothesis is true.
Significance level = 1 - confidence level, exp: 1 - 95% = 0.05

========= P value =======================================================
P-value is the probability of getting the observed data as least as extreme given
the null hypothesis is true.
A smaller p-value means a higher chance of rejecting the null hypothesis.
It's widely used in A/B testing when testing a metric in treatment and control group.
举例：
For example, we would like to check the pizza delivery times in USA, we do a
hypothesis (null hypothesis) that the pizza delivery time is 30 minutes and we've
collected some sampled delivery times (randomly and large), then perform the
calculation (one-sample t-test) and find that the mean delivery time is 40 minutes
with a p-value of 0.02. What this means is that the average pizza delivery time is
not 30 minutes, the delivery time is 30 minutes in 2% of cases due to random
sampling error, and we reject the null hypothesis.

========= Hypothesis Testing =======================================================
1. Type I Error: ~~ 1 - confidence level ~~ significance level
Also know as false positive. It's used to categorize errors in a binary hypothesis test.
It occurs when mistakenly reject true null hypothesis
Used in A/B testing, observe difference but there's no difference.
举例：A person is not infected but the test result shows positive. That is Type I error.
That's super bad because that person may take medical treatment that actually completely unnecessary.

2. Type II Error: ~~ 1 - statistical power
Also know as false negative. It's used to categorize errors in a binary hypothesis test.
It occurs when we fail to reject the null hypothesis which is in fact false.
Meaning we want to minimize the type 2 error of the test.
Used in A/B testing, we don't observe difference but there's a difference.
举例: A person is infected but the test result shows negative. It's bad because the person may miss
best timing to get treatment he really needs.

========= statistic power calculation =======================================================
statistic power is used in a binary hypothesis test.
statistic power = 1 - beta, the probability of correctly reject the null hypothesis.
statistic power is likelihood that a test will detect an effect when the effect is present.
The higher the statistical power is, the better the test is.

A power analysis can be used to estimate the minimum sample size required for an experiment, given
a desired significance level(5%), effect size((mean1-mean2)/pooled std), and statistical power.
举个例子：
A person is infected covid, and the test shows positive. That's the power of a test.

========= Z-test VS T-test ===============================================================
Z-test is a hypothesis test with a normal distribution that uses a z-statistic.
Z-test is used when you know the population variance or if you don't know the population
variance but have a large sample size.
For large sample sizes, the t-test gives almost identical p-values as the z-test.

T-test is a hypothesis test with a t-distribution that uses a t-statistic.
T- test is used when you don't know the population variance and have a small sample size.


=========== Probability Distributions ==============================================================================
* Bernoulli: mean: p, variance: 1-p
* Binomial:  mean: np, variance: np(1-p)
The Bernoulli distribution represents the success or failure of a single Bernoulli trial.
The Binomial Distribution represents the number of successes and failures
in n independent Bernoulli trials for some given value of n.

* Poisson: mean: lambda,  variance: lambda
is a discrete probability distribution of the number of events occurring in a given time period,
given the average number of times the event occurs over that time period.

举例：# of cars passing in a drive thru in a hour

* Exponential distribution:  mean: 1/lambda  variance: 1/lambda^2
is a continuous probability distribution of the time between events in a Poisson point process
举例：# of minutes between car arrivals in drive thru

泊松分布和指数分布的联系是there's no single event happened over a specified period.

* Normal Distribution: mean: miu, variance: theta^2
cumulative standard normal distributions
cumulative binomial probabilities

========= Margin of Error ==============================================================================
A margin of error tells you how many percentage points your results will differ from the real population value.
The margin of error is added to and subtracted from the mean to determine the confidence interval.

For example, a 95% confidenc interval with a 4% margin of error means that
your statistic will be within 4% percentage points of the real population value 95% of the time.
formula part: sample std / sqrt(sample size)

========= Effect Size =================================================================================
an effect size is a value measuring the strength of the relationship between two variables in a population,
or a sample-based estimate of that quantity.
  cohen's d is the most commonly used measure of effect size for t tests. cohen d: d = abs(mean1 - mean2)/((std1 + std2)/2)
  A commonly used interpretation is to refer to effect sizes as small (d = 0.2), medium (d = 0.5), and large (d = 0.8)
  If effective size is too small, then larger sample size will be required.
需要一定的effective size才能比较control和treatment. 需要多大sample size才能detect区别

========= Sample Size =================================================================================
Continous case => formula: 2* (Z alpha/2 + Z 1-beta)^2 * pooled std^2 / (mean 1 - mean 2)
proportion case => formula: 2 * (Z beta + Z -alpha)^2 * p * (1 - p) / p2 - p1, where p = (p1 + p2)/2

========= Pooled Std =================================================================================
The Pooled Standard Deviation is a weighted average of standard deviations for two or more groups
formula: sqrt((n1-1)*std1^2 + (n2-1)*std^2))/(n1+n2-2))
special case if two groups have same sample size: formula = sqrt((std1 + std2 +...)/k)

========= Central Limit Theorem ========================================================================
No matter what is the population’s original distribution, when taking random sample from the population,
the distribution of the means or sums from the random samples approaches a normal distribution as the random sample size gets larger.
The mean will be very close or equal to the population mean, and the standard deviation will decrease as the sample size gets larger.

========= Degrees of freedom ========================================================================
Refers to the maximum number of logically independent values, which are values that have the freedom to vary, sample size-1
