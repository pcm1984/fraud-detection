import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for realistic data generation
fake = Faker()

# Constants
NUM_TRANSACTIONS = 10000
FRAUD_PERCENTAGE = 0.05  # 5% of transactions will be fraudulent

# Generate synthetic data
def generate_transaction_data(num_transactions):
    transaction_ids = [fake.uuid4() for _ in range(num_transactions)]
    amounts = np.round(np.random.uniform(1, 20000, num_transactions), 2)  # Random amounts
    payment_methods = np.random.choice(["CreditCard", "DebitCard", "PayPal", "Crypto"], num_transactions)
    locations = np.random.choice(["US", "Canada", "India", "Germany", "Australia"], num_transactions)
    timestamps = [fake.date_time_this_year() for _ in range(num_transactions)]
    user_histories = np.random.randint(0, 11, num_transactions)  # Past fraudulent transactions
    is_fraud = np.random.rand(num_transactions) < FRAUD_PERCENTAGE

    # Apply additional fraud rules
    is_fraud = np.logical_or(is_fraud, (amounts > 15000) & (np.random.rand(num_transactions) < 0.5))
    is_fraud = np.logical_or(is_fraud, (payment_methods == "Crypto") & (np.random.rand(num_transactions) < 0.3))
    is_fraud = np.logical_or(is_fraud, (user_histories > 5) & (np.random.rand(num_transactions) < 0.7))

    # Create a DataFrame
    data = pd.DataFrame({
        "TransactionID": transaction_ids,
        "Amount": amounts,
        "PaymentMethod": payment_methods,
        "Location": locations,
        "Timestamp": timestamps,
        "UserHistory": user_histories,
        "IsFraud": is_fraud.astype(bool)
    })
    return data

# Generate and save the dataset
df = generate_transaction_data(NUM_TRANSACTIONS)
df.to_csv("synthetic_fraud_data.csv", index=False)
print("Synthetic fraud data generated and saved as 'synthetic_fraud_data.csv'")

