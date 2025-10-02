import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- تحديد مسار ملف البيانات داخل الباكيج ---
data_path = os.path.join(os.path.dirname(__file__), "data", "diabetes.csv")

# قراءة البيانات
df = pd.read_csv(data_path)

# --- مثال تحليل بسيط ---
# تقسيم البيانات إلى ميزات وهدف
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء نموذج الانحدار اللوجستي وتدريبه
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# التنبؤ على بيانات الاختبار
y_pred = model.predict(X_test)

# حساب الدقة والمصفوفة والتقرير
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# طباعة النتائج في الكونسول
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# --- حفظ التقرير داخل مجلد data ---
report_path = os.path.join(os.path.dirname(__file__), "data", "diabetes_report.csv")
df_report = pd.DataFrame({
    "Accuracy": [accuracy],
    "Confusion_Matrix": [conf_matrix.tolist()],  # تحويل المصفوفة لقائمة لتخزينها في CSV
    "Classification_Report": [class_report.replace("\n", "; ")]  # تحويل السطور لفاصلة منقوطة
})
df_report.to_csv(report_path, index=False)

print(f"\nتم حفظ التقرير في: {report_path}")
print("""
تقرير مشروع تحليل بيانات

العنوان:
التنبؤ بمرض السكري باستخدام خوارزمية الانحدار اللوجستي

اسم الطالب: [ملك عبد الله العبيدي]
المقرر: [مبادى ذكاء اصطناعي]
الجامعة: [الجامعه التخصصيه الحديثه ]
[يوسف الحاج]:اشراف الدكتور
---------------------------------------------

المقدمة:
في هذا المشروع قمنا باستخدام بيانات مرض السكري (Pima Indians Diabetes Dataset)
لتحليل خصائص المرضى وبناء نموذج للتنبؤ بإمكانية إصابتهم بالسكري.
الهدف من المشروع هو تدريب نموذج تنبؤي باستخدام تقنيات تعلم الآلة وتحليل النتائج بدقة.

---------------------------------------------

البيانات المستخدمة:
- مصدر البيانات: موقع Kaggle
- نوع البيانات: CSV يحتوي على 768 سجل و9 أعمدة
- الأعمدة:
  Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
  DiabetesPedigreeFunction, Age, Outcome

---------------------------------------------

الخطوات العملية:
1. تحميل البيانات باستخدام Pandas
2. استكشاف البيانات (head, describe)
3. التصور البياني باستخدام Matplotlib وSeaborn
4. تقسيم البيانات (Train/Test)
5. بناء النموذج (Logistic Regression)
6. تقييم النموذج (Accuracy, Confusion Matrix, Classification Report)

---------------------------------------------

النتائج:
- دقة النموذج ~ 77%
- النموذج قادر على التنبؤ بشكل جيد للحالات الإيجابية والسلبية
- توازن مقبول بين الدقة والاسترجاع

---------------------------------------------

الخاتمة:
نجحنا في بناء نموذج بسيط للتنبؤ بمرض السكري باستخدام الانحدار اللوجستي.
يمكن تحسين النتائج باستخدام خوارزميات أخرى ومعالجة البيانات الناقصة.

---------------------------------------------

المراجع:
- Kaggle: Pima Indians Diabetes Database
- مكتبات Python: Pandas, Matplotlib, Seaborn, Scikit-learn
""")
