from src.load_data import load_csv
from src.clean_data import clean_data
from src.evaluate import WaterQualityEvaluator

def main():
    file_path = "data/sensor_data.csv"
    df = load_csv(file_path)
    
    if df.empty:
        print("No data to process.")
        return
    
    df = clean_data(df)
    evaluator = WaterQualityEvaluator()
    
    for _, row in df.iterrows():
        result = evaluator.check_safety(row)
        print(f"Sensor {row['sensor_id']} at {row['location']}: {result}")

if __name__ == "__main__":
    main()
