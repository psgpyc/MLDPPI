
# Classification Metrics

## 1. 

**Definition**: Precision measures the proportion of correctly predicted positive instances out of all instances predicted as positive.

**Formula**:  
\[ \text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}} \]

**Interpretation**: High precision indicates that the model rarely labels a negative instance as positive (low false positive rate).

---

## 2. Recall (Sensitivity or True Positive Rate)
**Definition**: Recall measures the proportion of correctly predicted positive instances out of all actual positive instances.

**Formula**:  
\[ \text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}} \]

**Interpretation**: High recall indicates that the model correctly identifies most of the positive instances (low false negative rate).

---

## 3. F1-Score
**Definition**: F1-score is the harmonic mean of precision and recall. It provides a single metric that balances both precision and recall.

**Formula**:  
\[ \text{F1-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \]

**Interpretation**:  
- Useful when the dataset is imbalanced.  
- A high F1-score means the model has a good balance between precision and recall.
