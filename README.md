# 🔎 Log Classification with Hybrid Classification Framework

## 📌 Overview
This project implements a **hybrid log classification system** designed to improve the accuracy and efficiency of log analysis.  
Instead of relying on a single method, the framework combines:

1. **Regex-based classification** → for predictable patterns  
2. **Sentence Transformer + Logistic Regression** → for semantic classification of moderately complex logs  
3. **LLM-based classification** → for poorly labeled / complex cases  

By strategically routing logs based on their complexity, the system ensures both **accuracy and performance**.

---

## ✨ Key Features
- ✅ Hybrid multi-tier classification pipeline  
- ✅ Regex rules for fast, rule-based log detection  
- ✅ Transformer embeddings (`SentenceTransformer`) for semantic understanding  
- ✅ Logistic Regression classifier for mid-complexity logs  
- ✅ LLM-based classifier for edge cases with poor/noisy labels  
- ✅ Accuracy improved by ~25% compared to a single-method baseline  
- ✅ Processing efficiency improved by ~40% on large datasets  

---

## 🏗️ Architecture

            ┌─────────────────┐
            │   Input Logs     │
            └───────┬─────────┘
                    │
    ┌───────────────┼────────────────┐
    │                               │
┌──────▼───────┐ ┌────────▼────────┐
│ Regex Rule │ │ Transformer + │
│ Classifier │ │ Logistic Reg. │
└──────┬───────┘ └────────┬────────┘
│ │
└───────────────┬───────────────┘
│
┌──────▼───────┐
│ LLM-based │
│ Classifier │
└──────┬───────┘
│
┌───────▼────────┐
│ Final Predicted │
│ Class │
└────────────────┘

---

## ⚙️ Tech Stack
- **Python 3.9+**
- **Regex** → Pattern-based classification  
- **Sentence Transformers** → `all-MiniLM-L6-v2` for embeddings  
- **Scikit-learn** → Logistic Regression  
- **LLM APIs** (e.g., GPT-based) for fallback classification  
- **Pandas / NumPy** for data preprocessing  
- **Matplotlib/Seaborn** for evaluation & visualization  

---

## 📊 Results
- Improved classification **accuracy by ~25%** vs single baseline methods  
- Reduced **processing latency by 40%** for large datasets  
- Demonstrated **robust handling of noisy & complex logs**  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/log-classification-hybrid.git
cd log-classification-hybrid
Install Dependencies

pip install -r requirements.txt


📂 Repository Structure

├── training/                  # Model Training
├── models/                    # Saved Models
├── resources/                 # Contains test CSV files,output files,images
              
├── processor_regex.py
│── processor_bert.py
├── processor_llm.py
│   
├── classify             
├── requirements.txt
└── README.md

📖 Future Work
🔹 Expand to multi-lingual log datasets

🔹 Integrate anomaly detection for unseen log types

🔹 Optimize LLM inference with caching or smaller distilled models


