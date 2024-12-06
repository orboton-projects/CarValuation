
# Car Valuation Automation Suite

This project automates validation of car valuations using **Python** and **Playwright** with modular components for maintainability.

---

## Features
- Reads input from `car_input.txt`.
- Automates website interactions for valuation retrieval.
- Compares website output with `car_output.txt`.
- Logs mismatches or passes to the console.

---

## Project Structure
```plaintext
.

├── pages/                   # Reusable web interaction methods based on page
├── utils/                   # Utils or helpers methods
├── tests/                   # Test scripts
├── actions/                 # User Actions 
├── data/                    # Test data      
├── requirements.txt         # Dependencies
├── README.md                # Documentation
```

---

## Prerequisites
1. Install **Python 3.8+**.
2. Install dependencies:
   ```bash
   pip install pytest playwright pandas
   playwright install
   ```

---

## How to Use
1. Update `car_input.txt` with vehicle details:
   ```plaintext
   VARIANT_REG,MAKE,MODEL,YEAR
   RA04DWC,Ford,Fusion2,2004
   ```
2. Add expected valuations to `car_output.txt`:
   ```plaintext
   RA04DWC,£670
   ```
3. Run the test script:
   ```bash
   pytest src/tests/test_car_valuation.py --headed
   ```

---

## Sample Output
```plaintext
Test passed for RA04DWC: Valuation matched.
Test failed for RA05XYZ: Mismatch for RA05XYZ: Expected £2400, Got £1,165
```
## Test Execution Demo
[DemoTestExecution.mp4](DemoTestExecution.mp4)
