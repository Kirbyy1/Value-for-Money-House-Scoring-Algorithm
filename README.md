# Value-for-Money House Scoring Algorithm

This project calculates the "value-for-money" score for real estate properties based on various criteria such as price, location, condition, and potential for appreciation. The algorithm helps users identify which properties offer the best value based on their needs.

## Features

- **Price Scoring**: Evaluates the property price against the average price per square meter in the area.
- **Location Scoring**: Factors in location attributes, such as crime rate and proximity to good schools.
- **Property-Specific Scoring**: Evaluates the property’s size, number of bedrooms, bathrooms, and overall condition.
- **External Scoring**: Accounts for future appreciation potential and other external factors.
- **Customizable**: Users can adjust weights for different scoring factors to suit their priorities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/value-for-money-house.git
    cd value-for-money-house
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open `main.py` and configure the property details such as price, size, location score, etc.

2. Run the script:

    ```bash
    python main.py
    ```

3. The script will calculate and print the **Value-for-Money** score for each property.

### Example

```python
# main.py
from property import Property

# Example property
property_1 = Property(
    price=500000,
    area_m2=150,  # In square meters
    price_per_m2=3300,  # Price per square meter
    avg_price_per_m2=3500,   # Avg price in the area
    location_score=80,        # Good location score out of 100
    school_rating=9,          # Good schools nearby
    size=150,                 # House size in m²
    bedrooms=4,
    bathrooms=3
)

# Calculate and display the value-for-money score
print(f"Total Value-for-Money Score: {property_1.total_score():.2f}")
