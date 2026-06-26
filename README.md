# Vendor Invoice Intelligence System

An AI-powered analytics portal that leverages machine learning to predict freight costs and detect risky vendor invoices, reducing financial leakage and manual workload.

## 🎯 Features

- **Freight Cost Prediction**: Predict freight costs using invoice dollar amounts to support budgeting and vendor negotiations
- **Invoice Risk Flagging**: Detect abnormal vendor invoices that require manual approval based on cost, freight, and delivery patterns
- **Interactive Web Interface**: Built with Streamlit for easy-to-use predictions
- **ML-Driven Insights**: Trained Random Forest and Linear Regression models with proper feature scaling

## 📁 Project Structure

```
Vendor_invoice_intelligence_system/
├── README.md                          # Project documentation
├── app.py                             # Main Streamlit application
├── data/                              # Data files and database
│   └── inventory.db                   # SQLite database
├── invoice_flagging/                  # Invoice flagging module
│   ├── train.py                       # Training script
│   ├── data_preprocessing.py          # Data preprocessing utilities
│   ├── model_evaluation.py            # Model evaluation functions
│   └── models/                        # Trained models
│       ├── predict_flag_invoice.pkl   # Random Forest classifier
│       └── scaler.pkl                 # Feature scaler
├── freight_cost_prediction/           # Freight cost prediction module
│   ├── models/
│   │   └── predict_freight_model.pkl  # Linear Regression model
│   └── [training scripts]
├── inference/                         # Inference modules
│   ├── predict_flagged.py             # Invoice flagging inference
│   └── predict_freight.py             # Freight cost inference
└── notebooks/                         # Jupyter notebooks (exploration, analysis)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository** (after pushing to GitHub):
```bash
git clone https://github.com/[your-username]/Vendor_invoice_intelligence_system.git
cd Vendor_invoice_intelligence_system
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install streamlit pandas numpy scikit-learn joblib plotly
```

## 💻 Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Two Prediction Modules

#### 1. **Freight Cost Prediction** 🚚
- Input: Invoice Dollar Amount
- Output: Predicted Freight Cost
- Use case: Budget forecasting and vendor cost negotiation

**Example:**
- Invoice Dollars: $18,500
- Predicted Freight: ~$150-200

#### 2. **Invoice Manual Approval Flag** 📋
- Inputs:
  - Invoice Quantity
  - Invoice Dollars
  - Freight Cost
  - Total Item Quantity
  - Total Item Dollars
- Output: Flag status (Manual Approval Required / Safe for Auto-Approval)
- Use case: Identify suspicious or abnormal invoices

**Sample Values:**

**Safe Invoice (Auto-Approval):**
```
Invoice Quantity: 100
Invoice Dollars: $5,000
Freight: $150
Total Item Quantity: 100
Total Item Dollars: $4,950
→ Result: ✓ SAFE for Auto-Approval
```

**Flagged Invoice (Manual Review):**
```
Invoice Quantity: 50
Invoice Dollars: $8,000
Freight: $500
Total Item Quantity: 50
Total Item Dollars: $1,200
→ Result: 🚨 Requires MANUAL APPROVAL
```

## 🤖 Models

### Invoice Flagging Model
- **Algorithm**: Random Forest Classifier
- **Features**: 5 invoice and purchase metrics
- **Training Data**: Historical vendor invoices
- **Output**: Binary classification (Flag/No Flag)
- **Scaling**: StandardScaler for feature normalization

**Flagging Logic:**
- Flags invoices if: `|invoice_dollars - total_item_dollars| > $5`
- Flags invoices if: average receiving delay > 10 days

### Freight Cost Prediction Model
- **Algorithm**: Linear Regression
- **Feature**: Invoice Dollar Amount
- **Output**: Predicted Freight Cost
- **Use**: Quick cost estimation from invoice value

## 📊 Training Models

### Train Invoice Flagging Model
```bash
cd invoice_flagging
python train.py
```

This will:
- Load data from `data/inventory.db`
- Apply feature scaling
- Train Random Forest with grid search
- Save model to `models/predict_flag_invoice.pkl`
- Save scaler to `models/scaler.pkl`

## 📋 Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application interface |
| `inference/predict_flagged.py` | Invoice flagging prediction logic |
| `inference/predict_freight.py` | Freight cost prediction logic |
| `invoice_flagging/data_preprocessing.py` | Data loading and preprocessing |
| `invoice_flagging/model_evaluation.py` | Model training and evaluation |
| `invoice_flagging/train.py` | Training orchestration |

## 🔧 Technical Details

### Data Pipeline
1. Load invoice and purchase data from SQLite database
2. Aggregate purchase data by PO number
3. Join with vendor invoice data
4. Engineer features from date differences and totals
5. Scale features using StandardScaler
6. Make predictions

### Feature Engineering
- `days_po_to_invoice`: Days between PO date and invoice date
- `days_to_pay`: Days between invoice date and payment date
- `total_brands`: Count of unique brands in purchase
- `avg_receiving_delay`: Average delay in receiving items
- Cost variance metrics

## 📦 Dependencies

```
streamlit>=1.0.0
pandas>=1.0.0
numpy>=1.0.0
scikit-learn>=1.0.0
joblib>=1.0.0
plotly>=5.0.0
```

See `requirements.txt` for complete list.

## 🔐 Security & Best Practices

- Models are serialized with joblib and validated before use
- Feature validation prevents unexpected inputs
- Error handling for missing columns and data mismatches
- Database queries use parameterized statements

## 📈 Future Improvements

- [ ] Add API endpoint for batch predictions
- [ ] Implement model monitoring and drift detection
- [ ] Add explainability features (SHAP values)
- [ ] Support for multiple vendor categories
- [ ] Real-time invoice stream processing
- [ ] Dashboard for prediction analytics
- [ ] Model retraining pipeline automation

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

Created as part of a data science project for vendor invoice intelligence and cost prediction.

## 📞 Support

For issues or questions, please open an issue on GitHub or contact the project maintainer.

---

**Last Updated**: June 2026  
**Version**: 1.0.0
