# Assuming that for each factor, we have a scale from 0 to 100
# Weights assigned based on importance (can be dynamic or adjustable by the user)

WEIGHTS = {
    'price': 0.4,
    'location': 0.3,
    'property': 0.2,
    'external': 0.1,
    'appreciation': 0.0  # If not used directly in total score
}


class Property:
    def __init__(self, price, area_m2, price_per_m2, avg_price_per_m2, location_score, school_rating,
                 size, bedrooms, bathrooms, condition_score=None, renovation_cost=None, appreciation_rate=None,
                 crime_rate=None):
        self.price = price
        self.area_m2 = area_m2  # Now in square meters (m²)
        self.price_per_m2 = price_per_m2  # Price per square meter
        self.avg_price_per_m2 = avg_price_per_m2  # Average price per m² in the area
        self.location_score = location_score  # Assumed from 0 to 100 (crime, public transport, etc.)
        self.school_rating = school_rating  # From 0 to 10
        self.size = size
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

        # Optional values with defaults
        self.condition_score = condition_score if condition_score is not None else 80  # Default 80/100 if not provided
        self.renovation_cost = renovation_cost if renovation_cost is not None else 0  # Assume no renovation cost if not provided
        self.appreciation_rate = appreciation_rate if appreciation_rate is not None else 3  # Assume 3% annual appreciation
        self.crime_rate = crime_rate if crime_rate is not None else 50  # Default crime rate of 50/100

    # Method to calculate price score
    def price_score(self):
        price_diff = self.avg_price_per_m2 - self.price_per_m2
        price_ratio = self.price_per_m2 / self.avg_price_per_m2
        price_score = 100 - (price_ratio * 100)  # Higher price per m² gets lower score

        # Clamp between 0 and 100
        return max(0, min(price_score, 100))

    # Method to calculate location score
    def location_score_method(self):
        crime_penalty = (100 - self.crime_rate) * 0.5  # Assume crime lowers score by 50%
        school_bonus = (self.school_rating / 10) * 100 * 0.3  # Better schools get a bonus
        location_score = self.location_score + crime_penalty + school_bonus

        return max(0, min(location_score, 100))

    # Method to calculate property-specific score (condition, size, etc.)
    def property_score(self):
        # Assuming 185 m² (approximately 2000 sqft) is an average home size
        size_score = (self.area_m2 / 185) * 100
        condition_penalty = 100 - self.condition_score  # Condition impacts the score
        renovation_penalty = (self.renovation_cost / 100000) * 100  # Major renovations reduce score

        property_score = size_score - condition_penalty - renovation_penalty

        return max(0, min(property_score, 100))

    # Method to calculate external factors (appreciation potential, future trends)
    def external_score(self):
        appreciation_bonus = self.appreciation_rate * 5  # High appreciation gets higher score
        external_score = appreciation_bonus

        return max(0, min(external_score, 100))

    # Combine all the factors to calculate total value-for-money score
    def total_score(self):
        price_score = self.price_score()
        location_score = self.location_score_method()
        property_score = self.property_score()
        external_score = self.external_score()

        # Weighted total score
        total_score = (
                price_score * WEIGHTS['price'] +
                location_score * WEIGHTS['location'] +
                property_score * WEIGHTS['property'] +
                external_score * WEIGHTS['external'] +
                self.appreciation_rate * WEIGHTS['appreciation']
        )

        return total_score


# Create a property using square meters
# property_1 = Property(
#     price=500000,
#     area_m2=150,  # In square meters
#     price_per_m2=3300,  # Price per square meter
#     avg_price_per_m2=3500,  # Avg price in the area
#     location_score=80,  # Good location score out of 100
#     school_rating=9,  # Good schools nearby
#     size=150,  # House size in m²
#     bedrooms=4,
#     bathrooms=3
# )

# # Calculate and display the value-for-money score
# print(f"Total Value-for-Money Score (Property 1): {property_1.total_score():.2f}")
