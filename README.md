# Time Series Analysis of Riverside Transportation Agency

## Analysis Question

We wanted to answer a simple but important question: **“Will Riverside's public transportation ridership ever get back to its pre-COVID levels?”**  

To investigate, we used data from the Department of Transportation, focusing on the **Riverside Transit Agency (RTA)**. Specifically, we looked at **“Unlinked Passenger Trips”** for **Motorbus (MB)** service, since this is the main way people get around.  

We set our benchmark as the **pre-COVID level**, calculated as the monthly average for 2019: **651,742 trips**.  

All models were trained on **post-COVID data starting January 2021**, since our focus was on the recovery period after COVID.

---

## Our Forecasting Tool: SARIMA

We used **SARIMA** (Seasonal AutoRegressive Integrated Moving Average) to build our forecast. Here’s what each part does:

* **AR (AutoRegressive):** Captures how this month’s ridership depends on last month’s.  
* **I (Integrated):** Tracks the overall trend—whether ridership is generally going up, down, or flat.  
* **MA (Moving Average):** Helps correct past forecast errors.  
* **S (Seasonal):** Detects repeating patterns throughout the year (like summer dips or fall rises).

---

## Finding the Right Model

Finding a good SARIMA model wasn’t easy. A forecast isn’t useful if it’s unstable or doesn’t make sense.  

Our first attempts (both complex manual models and a wide `auto_arima` search) **overfit the data**. That means the model clung too closely to recent data points, producing unrealistic trends.  

![An unstable, overfit forecast showing a sharp nosedive.](![img.png](img.png))

Other problems included **huge confidence intervals**, which made predictions almost meaningless. Narrowing them for a more reliable forecast was a priority.

---

## The Final Model

To fix overfitting, we restricted the `auto_arima` search to find a **stable, linear trend** (`d=1`) and checked whether the trend was actually increasing (`with_intercept=True`).  

This worked. The final model was simple, stable, and statistically sound:  

**`SARIMAX(1, 1, 0)x(1, 0, 0, 12)`**  

Diagnostic tests confirmed it captured real patterns, leaving only random noise:  

* `Prob(Q) = 0.95`  
* `Prob(JB) = 0.93`  

Looking at the coefficients helps interpret the trend:

| Term | Coefficient | p-value | Meaning |
|:---|---:|---:|:---|
| **`intercept`** | -2399.78 | **0.677** | Not significant (no growth) |
| `ar.L1` | -0.2979 | 0.020 | Significant |
| `ar.S.L12` | 0.3703 | 0.012 | Significant |

The **intercept** represents the average monthly growth. With a **p-value of 0.677**, it’s not statistically significant. In other words, **there’s no evidence of real growth**—the recovery seen in 2021–2023 has stalled.

---

## The Answer: Will Ridership Recover?

**Short answer: no.**  

Since the model detected no upward trend, it forecasts a **flat ridership level** into the future, with only seasonal fluctuations.  

![The final, stable forecast, showing a flat trend that does not reach the pre-COVID baseline.](![img_1.png](img_1.png))

The red forecast line stays flat and never reaches the green **pre-COVID baseline**. According to this model, Riverside’s public transit ridership **does not seem likely to recover anytime soon**.
