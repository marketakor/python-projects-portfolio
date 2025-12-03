import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def calculate_stats(df):
    stats = {
        "avg_price": df['price'].mean(),
        "min_price": df['price'].min(),
        "max_price": df['price'].max(),
        "total_quantity": df['quantity'].sum()
    }
    return stats

if __name__ == "__main__":
    df = load_csv("data/sample.csv")
    stats = calculate_stats(df)
    print("Průměrná cena:", stats['avg_price'])
    print("Minimální cena:", stats['min_price'])
    print("Maximální cena:", stats['max_price'])
    print("Celkové množství:", stats['total_quantity'])
