import sys

import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QTabWidget, QVBoxLayout
from fbs_runtime.application_context.PyQt5 import ApplicationContext


def updateqr(qrtype):
    if enternamelinedit.text() and not entersurnamelinedit.text():
        name = f'N:{enternamelinedit.text()};'
    elif entersurnamelinedit.text() and not enternamelinedit.text():
        name = f'N:{entersurnamelinedit.text()};'
    elif enternamelinedit.text() and entersurnamelinedit.text():
        name = f'N:{enternamelinedit.text()},{entersurnamelinedit.text()};'
    else:
        name = ''
    if enterphonelinedit.text():
        phone = f'TEL:{enterphonelinedit.text()};'
    else:
        phone = ''
    if entercontactemaillinedit.text():
        email = f'EMAIL:{entercontactemaillinedit.text()};'
    else:
        email = ''
    if enterstreetlinedit.text() or entercitylinedit.text() or enterziplinedit.text() or entercountrylinedit.text():
        address = f'ADR:{enterstreetlinedit.text()},{enterziplinedit.text()},{entercitylinedit.text()},{entercountrylinedit.text()};'
    else:
        address = ''

    if str(qrtype) == 'Text':
        data = entertextlinedit.text()
    elif str(qrtype) == 'Contact':
        data = f'MECARD:{name}{address}{phone}{email};'
    elif str(qrtype) == 'Email':
        data = f'mailto:{enteremaillinedit.text()}'
    else:
        data = 'https://www.palemonas.kaunas.lm.lt/'

    image = ImageQt(qrcode.make(data))
    pixmap = QPixmap.fromImage(image)
    qrimage.setPixmap(pixmap)


if __name__ == '__main__':
    appctxt = ApplicationContext()

    # Init window
    window = QWidget()
    window.setMinimumSize(1280, 800)
    window.show()

    # Main layout
    mainlayout = QHBoxLayout()
    mainlayout.setContentsMargins(10, 10, 10, 10)
    window.setLayout(mainlayout)

    # Main tab
    maintab = QTabWidget()
    mainlayout.addWidget(maintab, 6)

    # Text QR tab
    entertextwidget = QWidget()
    entertext = QGridLayout()
    entertextwidget.setLayout(entertext)
    maintab.addTab(entertextwidget, 'Text / URL')

    entertextlabel = QLabel()
    entertextlabel.setText('Text / URL:')
    entertext.addWidget(entertextlabel, 1, 1)

    entertextlinedit = QLineEdit()
    entertextlinedit.textChanged.connect(lambda: updateqr('Text'))
    entertext.addWidget(entertextlinedit, 1, 2)

    # Email
    enteremailwidget = QWidget()
    enteremail = QGridLayout()
    enteremailwidget.setLayout(enteremail)
    maintab.addTab(enteremailwidget, 'Email')

    enteremaillabel = QLabel()
    enteremaillabel.setText('Email:')
    enteremail.addWidget(enteremaillabel, 1, 1)

    enteremaillinedit = QLineEdit()
    enteremaillinedit.textChanged.connect(lambda: updateqr('Email'))
    enteremail.addWidget(enteremaillinedit, 1, 2)

    # Conctact QR tab
    enterinfowidget = QWidget()
    enterinfo = QGridLayout()
    enterinfowidget.setLayout(enterinfo)
    maintab.addTab(enterinfowidget, 'Contact')

    # Your name
    enternamelabel = QLabel()
    enternamelabel.setText('Your Name:')
    enterinfo.addWidget(enternamelabel, 1, 1)

    enternamelinedit = QLineEdit()
    enternamelinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(enternamelinedit, 1, 2)

    entersurnamelinedit = QLineEdit()
    entersurnamelinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(entersurnamelinedit, 1, 3)

    # Phone
    enterphonelabel = QLabel()
    enterphonelabel.setText('Phone:')
    enterinfo.addWidget(enterphonelabel, 2, 1)

    enterphonelinedit = QLineEdit()
    enterphonelinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(enterphonelinedit, 2, 2, 1, 2)

    # Email
    entercontactemaillabel = QLabel()
    entercontactemaillabel.setText('Email:')
    enterinfo.addWidget(entercontactemaillabel, 3, 1)

    entercontactemaillinedit = QLineEdit()
    entercontactemaillinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(entercontactemaillinedit, 3, 2, 1, 2)

    # Address tab
    enterstreetlabel = QLabel()
    enterstreetlabel.setText('Street:')
    enterinfo.addWidget(enterstreetlabel, 4, 1)

    enterstreetlinedit = QLineEdit()
    enterstreetlinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(enterstreetlinedit, 4, 2, 1, 2)

    entercitylabel = QLabel()
    entercitylabel.setText('City / State:')
    enterinfo.addWidget(entercitylabel, 5, 1)

    entercitylinedit = QLineEdit()
    entercitylinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(entercitylinedit, 5, 2)

    enterziplinedit = QLineEdit()
    enterziplinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(enterziplinedit, 5, 3)

    entercountrylabel = QLabel()
    entercountrylabel.setText('Country:')
    enterinfo.addWidget(entercountrylabel, 6, 1)

    entercountrylinedit = QLineEdit()
    entercountrylinedit.textChanged.connect(lambda: updateqr('Contact'))
    enterinfo.addWidget(entercountrylinedit, 6, 2, 1, 2)

    # QR layout
    qrlayout = QVBoxLayout()
    mainlayout.addLayout(qrlayout)

    # QR image
    qrimage = QLabel()
    qrlayout.addWidget(qrimage)
    qrimage.setAlignment(Qt.AlignCenter)
    mainlayout.addWidget(qrimage, 4)

    updateqr('start')

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
