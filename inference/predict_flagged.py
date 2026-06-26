import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "..", "invoice_flagging", "models", "predict_flag_invoice.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "invoice_flagging", "models", "scaler.pkl")
FEATURE_COLUMNS = [
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_quantity",
    "total_item_dollars",
]

def load_model(model_path: str = MODEL_PATH):
    return joblib.load(model_path)


def load_scaler(scaler_path: str = SCALER_PATH):
    return joblib.load(scaler_path)


def predict_invoice_flag(input_data):
    model = load_model()
    scaler = load_scaler()

    input_df = pd.DataFrame(input_data)
    missing_columns = set(FEATURE_COLUMNS) - set(input_df.columns)
    if missing_columns:
        raise ValueError(f"Missing required feature columns: {sorted(missing_columns)}")

    input_df = input_df[FEATURE_COLUMNS].copy()
    input_scaled = scaler.transform(input_df)
    input_df["Predicted_flag"] = model.predict(input_scaled).round()
    return input_df

if __name__ == "__main__":
    sample_data = {
        "invoice_quantity": [10, 5, 2, 8],
        "invoice_dollars": [18500, 9000, 3000, 200],
        "Freight": [150, 75, 20, 10],
        "total_item_quantity": [10, 5, 2, 8],
        "total_item_dollars": [18495, 9005, 2995, 190],
    }

    prediction = predict_invoice_flag(sample_data)
    print(prediction)