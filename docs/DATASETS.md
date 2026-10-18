# Dataset setup

No CSV datasets, dataset archives, tracking databases, or trained model files are included. Dataset contents were not inspected during repository preparation. CSV files remain local and are ignored by Git.

For the original author, copy the following existing course files into the matching notebook/script directory. For other readers, a verified public source and license are still needed; filenames alone are not sufficient to identify the correct dataset.

| Destination folder | Required filename | Original course folder |
| --- | --- | --- |
| `days/day-09` | `customers_tiny.csv` | `day 9` |
| `days/day-12` | `advertising.csv` | `day 12` |
| `days/day-13` | `advertising.csv` | `day 13` |
| `days/day-13` | `womens_clothing_ecommerce_reviews.csv` | `day 13` |
| `days/day-16` | `retail_customers - retail_customers.csv` | `day 16` |
| `assignments/assignment-01` | `customers_messy_500.csv` | `Assignment 1` |
| `practice/ml-quiz` | `house_prices.csv` | `quize2` |
| `practice/ml-quiz` | `customer_churn.csv` | `quize2` |

The sentiment notebook expects both `Review Text` and `sentiment` columns. Do not substitute a similarly named dataset without checking its schema and how its target labels were created.

Day 15 loads scikit-learn's bundled breast-cancer dataset. Day 18 generates synthetic data in code. Their notebooks do not require an external CSV.

For each externally sourced dataset, add: original source URL, author, license, expected columns, target definition, and preparation instructions. Do not invent download links or claim permission where the source is unknown.
