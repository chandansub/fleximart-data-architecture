import pandas as pd

# -------- EXTRACT --------
def extract_customers():
    return pd.read_csv("data/customers_raw.csv")

def extract_products():
    return pd.read_csv("data/products_raw.csv")

def extract_sales():
    return pd.read_csv("data/sales_raw.csv")


# -------- TRANSFORM --------
def transform_customers(df):
    df = df.drop_duplicates()
    df["email"] = df["email"].fillna("unknown@email.com")
    df["phone"] = df["phone"].astype(str).str.replace(" ", "")
    df["registration_date"] = pd.to_datetime(df["registration_date"], errors="coerce")
    return df

def transform_products(df):
    df["category"] = df["category"].str.capitalize()
    df["price"] = df["price"].fillna(df["price"].mean())
    df["stock_quantity"] = df["stock_quantity"].fillna(0)
    return df

def transform_sales(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=["customer_id", "product_id"])
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
    return df


# -------- MAIN --------
if __name__ == "__main__":
    customers_df = transform_customers(extract_customers())
    products_df = transform_products(extract_products())
    sales_df = transform_sales(extract_sales())

    print(customers_df.head())
    print(products_df.head())
    print(sales_df.head())
