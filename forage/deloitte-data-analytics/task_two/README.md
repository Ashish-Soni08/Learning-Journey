# Background Information

We have processed all data on employee compensation and generated an Excel file (Equality Table.xlsx) containing 3 columns:

1. Factory
2. Job Role
3. Equality Score (integer; ranging between -100 and +100; 0 is ideal)

Here is your task:

- Create a 4th column (Equality class), classifying the equality score into 3 types:

  - Fair (+-10)
  - Unfair (<-10 AND >10)
  - Highly Discriminative (<-20 AND >20)

Examples:

- 6 → Fair
- -9 → Unfair
- -30 → Highly Discriminative
