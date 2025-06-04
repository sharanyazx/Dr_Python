
def analyze_ml_code(code):
    issues = []
    if 'fit(' in code and 'train_test_split' not in code:
        issues.append("⚠️ Consider using train_test_split to evaluate model performance.")
    if 'accuracy_score' in code and 'classification_report' not in code:
        issues.append("ℹ️ Add classification_report for better evaluation insights.")
    if 'StandardScaler' not in code and 'fit(' in code:
        issues.append("🧪 StandardScaler missing — consider feature scaling.")
    return '\n'.join(issues) if issues else "✅ No obvious ML code issues detected."
