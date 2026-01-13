# Dataset for Aqualyx AI

## sample_water_usage.csv

Columns:

| timestamp | usage_liters | leak |
|-----------|--------------|------|
| 2026-01-01 00:00 | 0.5 | 0 |
| 2026-01-01 01:00 | 0.6 | 0 |

- **leak** column: 0 = normal, 1 = simulated leak  
- Dataset is **public water consumption data** + simulated leaks  
- Can be used to train and evaluate the Random Forest model
