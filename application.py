import os
import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

app = QApplication(sys.argv)

# ===== Dark Palette =====
palette = QPalette()
palette.setColor(QPalette.Window, QColor("#0d0f12"))
palette.setColor(QPalette.WindowText, QColor("#e8eaf2"))
palette.setColor(QPalette.Base, QColor("#0d0f12"))
palette.setColor(QPalette.AlternateBase, QColor("#141820"))
palette.setColor(QPalette.Text, QColor("#e8eaf2"))
palette.setColor(QPalette.Button, QColor("#6382ff"))
palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
app.setPalette(palette)

app.setStyleSheet("""
    QWidget {
        font-family: 'Segoe UI', Arial;
        font-size: 14px;
        color: #e8eaf2;
        background-color: #0d0f12;
    }
    QFrame#card {
        background-color: #141820;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.08);
    }
    QLabel#section_title {
        font-size: 20px;
        font-weight: bold;
        color: #eef0f7;
    }
    QLabel#section_sub {
        font-size: 12px;
        color: rgba(255,255,255,0.4);
    }
    QLabel.field_label {
        font-size: 12px;
        color: rgba(255,255,255,0.5);
        margin-bottom: 2px;
    }
    QLineEdit, QTextEdit {
        background-color: #0d0f12;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 8px 12px;
        color: #e8eaf2;
        font-size: 14px;
    }
    QLineEdit:focus, QTextEdit:focus {
        border: 1px solid rgba(99,130,255,0.6);
    }
    QPushButton#submit_btn {
        background-color: #6382ff;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 15px;
        font-weight: bold;
    }
    QPushButton#submit_btn:hover {
        background-color: #7590ff;
    }
    QPushButton#submit_btn:pressed {
        background-color: #4f6ee0;
    }
""")

# ===== Window =====
window = QWidget()
window.setWindowTitle("نظام الدعم")
window.setFixedWidth(480)
window.setMinimumHeight(560)

# ===== Card =====
card = QFrame(window)
card.setObjectName("card")
card_layout = QVBoxLayout(card)
card_layout.setContentsMargins(28, 28, 28, 28)
card_layout.setSpacing(12)

# Header
title = QLabel("سجّل مشكلتك")
title.setObjectName("section_title")
title.setAlignment(Qt.AlignRight)
sub = QLabel("غادي نتواصلو معك فـ 24 ساعة")
sub.setObjectName("section_sub")
sub.setAlignment(Qt.AlignRight)
card_layout.addWidget(title)
card_layout.addWidget(sub)

# ---- Helper ----
def make_field(label_text):
    lbl = QLabel(label_text)
    lbl.setAlignment(Qt.AlignRight)
    lbl.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 12px;")
    return lbl

# Fields
lbl_name = make_field("الاسم الكامل")
name_input = QLineEdit()
name_input.setPlaceholderText("اكتب اسمك هنا...")
name_input.setLayoutDirection(Qt.RightToLeft)

lbl_house = make_field("السكن")
house_input = QLineEdit()
house_input.setPlaceholderText("المدينة أو الحي...")
house_input.setLayoutDirection(Qt.RightToLeft)

lbl_problem = make_field("وصف المشكل")
problem_input = QTextEdit()
problem_input.setPlaceholderText("اشرح المشكل بالتفصيل...")
problem_input.setLayoutDirection(Qt.RightToLeft)
problem_input.setFixedHeight(90)

# Divider
divider = QFrame()
divider.setFrameShape(QFrame.HLine)
divider.setStyleSheet("color: rgba(255,255,255,0.06);")

# Email + Phone row
row_layout = QHBoxLayout()
row_layout.setSpacing(12)

left_col = QVBoxLayout()
lbl_phone = make_field("Téléphone")
phone_input = QLineEdit()
phone_input.setPlaceholderText("+212...")
left_col.addWidget(lbl_phone)
left_col.addWidget(phone_input)

right_col = QVBoxLayout()
lbl_email = make_field("Email")
email_input = QLineEdit()
email_input.setPlaceholderText("mail@...")
right_col.addWidget(lbl_email)
right_col.addWidget(email_input)

row_layout.addLayout(right_col)
row_layout.addLayout(left_col)

# Button
add_button = QPushButton("تسجيل الطلب ←")
add_button.setObjectName("submit_btn")
add_button.setFixedHeight(48)

# Add to card
for w in [lbl_name, name_input, lbl_house, house_input,
          lbl_problem, problem_input, divider]:
    card_layout.addWidget(w)

card_layout.addLayout(row_layout)
card_layout.addSpacing(8)
card_layout.addWidget(add_button)

# ===== Main Layout =====
main_layout = QVBoxLayout(window)
main_layout.setContentsMargins(20, 20, 20, 20)
main_layout.addWidget(card)

# ===== Action =====
def handle_click():
    name = name_input.text().strip()
    house = house_input.text().strip()
    problem = problem_input.toPlainText().strip()
    email = email_input.text().strip()
    phone = phone_input.text().strip()

    if not all([name, house, problem, email, phone]):
        msg = QMessageBox(window)
        msg.setWindowTitle("خطأ")
        msg.setText("عمر جميع الخانات!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        return

    

# ضيف هادا فوق الكود (مرة واحدة)
    if getattr(sys, 'frozen', False):
        BASE_DIR = os.path.dirname(sys.executable)  # مكان الـ .exe
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # مكان الـ .py

    CSV_PATH = os.path.join(BASE_DIR, "data.csv")

# ثم بدّل السطر ديال الكتابة
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([name, house, problem, email, phone])

    msg = QMessageBox(window)
    msg.setWindowTitle("تم ✅")
    msg.setText("تم تسجيل الطلب بنجاح!\nغادي نتواصلو معك فـ 24 ساعة.")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()

    for field in [name_input, house_input, email_input, phone_input]:
        field.clear()
    problem_input.clear()

add_button.clicked.connect(handle_click)

window.show()
sys.exit(app.exec_())