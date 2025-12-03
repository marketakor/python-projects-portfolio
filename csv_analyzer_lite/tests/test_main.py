from main import load_csv, calculate_stats  
import pandas as pd

def test_calculate_stats(tmp_path):
    # vytvoření dočasného CSV souboru pro test
    csv_content = """product,price,quantity
apple,10,3
banana,5,6
orange,7,2
"""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(csv_content)

    # načtení CSV a výpočet statistik
    df = load_csv(csv_file)
    stats = calculate_stats(df)

    # ověření výsledků
    assert stats["avg_price"] == (10+5+7)/3
    assert stats["min_price"] == 5
    assert stats["max_price"] == 10
    assert stats["total_quantity"] == 3+6+2
