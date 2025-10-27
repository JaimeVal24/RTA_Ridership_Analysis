# Time Series Analysis of Riverside Transportation Agency

## The Big Question

The main goal of this project is to answer "Will Riverside's public transportation ridership ever get back to its pre-COVID levels?"

To find out, we looked at data from the Department of Transportation, focusing on the **Riverside Transit Agency (RTA)**. We zoomed in on **"Unlinked Passenger Trips"** for the **Motorbus (MB)** service, since that's how most people get around.

First, we set our target: the "pre-COVID level," which we calculated as the monthly average from 2019. That number is **651,742 trips**.

All our models were trained on post-COVID data, starting from January 2021, to aim specifically for the recovery period after covid.

## Our Forecasting Tool: The SARIMA Model

**SARIMA** (Seasonal AutoRegressive Integrated Moving Average) was used to make the model to make our forecast. 

* **AR (AutoRegressive):** How this month's ridership is related to last month's.
* **I (Integrated):** This part handles the overall trend. Is ridership generally going up, down, or staying flat?
* **MA (Moving Average):** This helps the model learn from its own past forecast mistakes.
* **S (Seasonal):** This is key for ridership. It looks for patterns that repeat every year (like a dip in summer or a rise in the fall).

## The (Difficult) Hunt for a Good Model

Finding the *right* SARIMA model was a journey. It's not enough to just make a forecast; the forecast needs to be statistically stable and make common sense.

The first fittings of the ARIMA model presented some difficulties. A very complex manual model and a wide-open `auto_arima` search were implemented. Both gave us models that were **unstable and overfit**.

The plot below demonstrates one of these models, where the model seems to deeply attach itself to the last few data points, and continues to dive lower in its predicted trend.

![An unstable, overfit forecast showing a sharp nosedive.](![img.png](img.png))

Apart from this model, some other struggles included large confidence interval, which essentially made the model useless, as they spanned nearly the entireity of the range of values. 
Attempting to narrow down this confidence interval to create a more reliable forecast was also a priority.

## The Final Model

To fix this, the `autoarima` function was given some restircitions in order to avoid overfitting; Forcing it to look for a **stable, linear trend** (`d=1`) and to check if that trend was *actually* growing (`with_intercept=True`).

This time, it worked. The search found a simple, stable, and statistically model: **`SARIMAX(1, 1, 0)x(1, 0, 0, 12)`**.

This model's diagnostic tests were good (`Prob(Q) = 0.95`, `Prob(JB) = 0.93`), which means it successfully captured all the real patterns in the data, leaving behind only random noise.

Looking at the intercept and its stastical signifcance gives some incite to the overal trend of the prediction.

| Term | Coefficient | p-value | What it Means |
|:---|---:|---:|:---|
| **`intercept`** | -2399.78 | **0.677** | **NOT Significant** |
| `ar.L1` | -0.2979 | 0.020 | Significant |
| `ar.S.L12` | 0.3703 | 0.012 | Significant |

The **`intercept`** is the term that represents the "drift," or the average monthly **growth**. Its p-value was **0.677**.

 The model signifies that there is no evidence of any real growth. The recovery trend we saw from 2021-2023 has stalled, as opposed to what one might assume if you were to look at the collected data from the past few years.

## The Answer: So, Will We Recover?

**Based on the data, the model's forecast is NO.**

Because the model found no statistical evidence of an upward trend, it cannot project one into the future. Instead, it projects a **flat forecast**. It just takes the current ridership level and projects it forward, adding the normal seasonal ups and downs.

The plot below shows this final, stable forecast. As you can see, the red forecast line isn't trending up. It stays flat, never getting close to the green "Pre-COVID" line.

![The final, stable forecast, showing a flat trend that does not reach the pre-COVID baseline.](![img_1.png](img_1.png))

According to this model, it does not seem like we will be recovering any time soon.