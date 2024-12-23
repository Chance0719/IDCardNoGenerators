import sys,json
import calendar

from PyQt6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_IDCardGenerator(object):

    ADMDVS_MAP = {}
    ODD_NUM = [1, 3, 5, 7, 9]
    EVEN_NUM = [2, 4, 6, 8, 0]
    # 加权因子
    WEIGHTS = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验码表
    CHECK_CODE = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    def setupUi(self, IDCardGenerator):
        if not IDCardGenerator.objectName():
            IDCardGenerator.setObjectName(u"IDCardGenerator")
        IDCardGenerator.resize(550, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IDCardGenerator.sizePolicy().hasHeightForWidth())
        IDCardGenerator.setSizePolicy(sizePolicy)
        IDCardGenerator.setMinimumSize(QSize(550, 380))
        IDCardGenerator.setMaximumSize(QSize(550, 380))
        IDCardGenerator.setBaseSize(QSize(550, 380))
        self.verticalLayout = QVBoxLayout(IDCardGenerator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(IDCardGenerator)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.groupBox.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setMargin(0)

        self.horizontalLayout.addWidget(self.label_2)

        self.provinceSel = QComboBox(self.groupBox)
        self.provinceSel.setObjectName(u"provinceSel")

        self.horizontalLayout.addWidget(self.provinceSel)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.citySel = QComboBox(self.groupBox)
        self.citySel.setObjectName(u"citySel")

        self.horizontalLayout.addWidget(self.citySel)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.districtSel = QComboBox(self.groupBox)
        self.districtSel.setObjectName(u"districtSel")

        self.horizontalLayout.addWidget(self.districtSel)

        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 3)

        self.verticalLayout_6.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(IDCardGenerator)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.yearSel = QComboBox(self.groupBox_2)
        self.yearSel.setObjectName(u"yearSel")

        self.horizontalLayout_2.addWidget(self.yearSel)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.monthSel = QComboBox(self.groupBox_2)
        self.monthSel.setObjectName(u"monthSel")

        self.horizontalLayout_2.addWidget(self.monthSel)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.daySel = QComboBox(self.groupBox_2)
        self.daySel.setObjectName(u"daySel")

        self.horizontalLayout_2.addWidget(self.daySel)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 1)

        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(IDCardGenerator)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.man = QRadioButton(self.groupBox_3)
        self.man.setObjectName(u"man")
        self.man.setChecked(True)

        self.horizontalLayout_4.addWidget(self.man)

        self.woman = QRadioButton(self.groupBox_3)
        self.woman.setObjectName(u"woman")

        self.horizontalLayout_4.addWidget(self.woman)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_4 = QGroupBox(IDCardGenerator)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.certNos = QTextEdit(self.groupBox_4)
        self.certNos.setObjectName(u"certNos")
        self.certNos.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.certNos)


        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.getCertNoButton = QPushButton(IDCardGenerator)
        self.getCertNoButton.setObjectName(u"getCertNoButton")

        self.verticalLayout_4.addWidget(self.getCertNoButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.groupBox_5 = QGroupBox(IDCardGenerator)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.certNo = QLineEdit(self.groupBox_5)
        self.certNo.setObjectName(u"certNo")

        self.horizontalLayout_6.addWidget(self.certNo)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.tipsEdit = QTextEdit(self.groupBox_5)
        self.tipsEdit.setObjectName(u"tipsEdit")
        self.tipsEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.tipsEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkCertNoButton = QPushButton(self.groupBox_5)
        self.checkCertNoButton.setObjectName(u"checkCertNoButton")

        self.horizontalLayout_7.addWidget(self.checkCertNoButton)

        self.aboutButton = QPushButton(self.groupBox_5)
        self.aboutButton.setObjectName(u"aboutButton")

        self.horizontalLayout_7.addWidget(self.aboutButton)

        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)
        self.verticalLayout_5.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(IDCardGenerator)
        self.addData()
        QMetaObject.connectSlotsByName(IDCardGenerator)
    # setupUi

    def retranslateUi(self, IDCardGenerator):
        IDCardGenerator.setWindowTitle(QCoreApplication.translate("IDCardGenerator", u"\u8eab\u4efd\u8bc1\u53f7\u7801\u751f\u6210\u5668", None))
        self.groupBox.setTitle(QCoreApplication.translate("IDCardGenerator", u"\u5730\u533a", None))
        self.label_2.setText(QCoreApplication.translate("IDCardGenerator", u"\u7701", None))
        self.label.setText(QCoreApplication.translate("IDCardGenerator", u"\u5e02", None))
        self.label_3.setText(QCoreApplication.translate("IDCardGenerator", u"\u533a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("IDCardGenerator", u"\u51fa\u751f\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("IDCardGenerator", u"\u5e74", None))
        self.label_5.setText(QCoreApplication.translate("IDCardGenerator", u"\u6708", None))
        self.label_6.setText(QCoreApplication.translate("IDCardGenerator", u"\u65e5", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("IDCardGenerator", u"\u6027\u522b", None))
        self.man.setText(QCoreApplication.translate("IDCardGenerator", u"\u7537", None))
        self.woman.setText(QCoreApplication.translate("IDCardGenerator", u"\u5973", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("IDCardGenerator", u"\u8eab\u4efd\u8bc1\u53f7\u7801", None))
        self.getCertNoButton.setText(QCoreApplication.translate("IDCardGenerator", u"\u83b7\u53d6\u8bc1\u4ef6\u53f7\u7801", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("IDCardGenerator", u"\u89e3\u6790\u8eab\u4efd\u8bc1\u53f7\u7801", None))
        self.label_7.setText(QCoreApplication.translate("IDCardGenerator", u"\u8bc1\u4ef6\u53f7\u7801", None))
        self.checkCertNoButton.setText(QCoreApplication.translate("IDCardGenerator", u"\u89e3\u6790", None))
        self.aboutButton.setText(QCoreApplication.translate("IDCardGenerator", u"\u5173\u4e8e", None))
    # retranslateUi

    # 设置信号与槽
    def setSignalSlot(self):
        self.provinceSel.activated.connect(self.updateCity)
        self.provinceSel.activated.connect(self.updateDistrict)
        self.citySel.activated.connect(self.updateDistrict)
        self.monthSel.activated.connect(self.updateDay)
        self.yearSel.activated.connect(self.updateDay)
        self.getCertNoButton.clicked.connect(self.getCertNo)

    def updateDay(self,index):
        year = self.yearSel.currentText()
        month = self.monthSel.currentText()
        maxDay = calendar.monthrange(int(year), int(month))[1]
        self.daySel.clear()
        for i in range(1,maxDay + 1):
            self.daySel.addItem(str(i).rjust(2,'0'))

    def updateCity(self, index):
        provinceCode = self.provinceSel.currentData()
        for item in self.ADMDVS_MAP:
            if item["value"] == provinceCode:
                self.citySel.clear()
                for city in item["children"]:
                    self.citySel.addItem(city['name'], city['value'])
                break

    def updateDistrict(self,index):
        cityCode = self.citySel.currentData()
        provinceCode = self.provinceSel.currentData()
        print(cityCode)
        print(provinceCode)
        for item in self.ADMDVS_MAP:
            if item["value"] == provinceCode:
                for city in item["children"]:
                    if city["value"] == cityCode:
                        self.districtSel.clear()
                        for district in city["children"]:
                            self.districtSel.addItem(district['name'], district['value'])
                        break
                break

    def initQComboBox(self):
        for item in self.ADMDVS_MAP:
            self.provinceSel.addItem(item['name'], item['value'])
        self.updateCity(1)
        self.updateDistrict(1)

        for i in range(1949,3000):
            self.yearSel.addItem(str(i))

        for i in range(1,13):
            self.monthSel.addItem(str(i).rjust(2,'0'))

        for i in range(1,32):
            self.daySel.addItem(str(i).rjust(2,'0'))

        self.provinceSel.setMaxVisibleItems(20)
        # self.yearSel.setEditable(True)
        # validator = QIntValidator(1949, 3000)
        # self.yearSel.setValidator(validator)

    def getCertNo(self):
        admdvs = self.districtSel.currentData()
        year = self.yearSel.currentText()
        month = self.monthSel.currentText()
        day = self.daySel.currentText()
        isMan = self.man.isChecked() # 男单数
        pre = admdvs + year + month + day
        for i in range(100):
            temp = pre + str(i).rjust(2,'0')
            if isMan:
                for j in self.ODD_NUM:
                    temp2 = temp + str(j)
                    checkCode = self.calculate_check_digit(temp2)
                    print(temp2 + checkCode)
            else:
                for j in self.EVEN_NUM:
                    temp2 = temp + str(j)
                    checkCode = self.calculate_check_digit(temp2)
                    print(temp2 + checkCode)

    def calculate_check_digit(self,id_number):
        # 加权因子
        weights = self.WEIGHTS
        # 校验码表
        check_codes = self.CHECK_CODE
        total = sum(int(id_number[i]) * weights[i] for i in range(17))
        mod_result = total % 11
        return check_codes[mod_result]

    def readJsonFromFile(self):
        try:
            with open('admdvs.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.ADMDVS_MAP = data
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def addData(self):
        self.readJsonFromFile()
        self.initQComboBox()
        self.setSignalSlot()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    IDCardGenerator = QWidget()
    ui = Ui_IDCardGenerator()
    ui.setupUi(IDCardGenerator)
    IDCardGenerator.show()

    sys.exit(app.exec())