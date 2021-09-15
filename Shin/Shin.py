# -*- coding: utf-8 -*-
# Shin Megami Tensei III Nocturne HD Save Editor
import sys, os
import binascii
import struct
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import functools
from shinvalues import *

class ShinApp(QMainWindow):

    def __init__(self):
        super().__init__()
        global root
        root = QFileInfo(__file__).absolutePath()
        self.title = "Shin Megami Tensei III Nocturne HD Save Editor"
        self.setWindowIcon(QIcon(root + '/img/icon.png'))
        width = 675
        height = 300
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.width = width
        self.height = height
        self.setFixedSize(width, height)
        self.initUI()

    def initUI(self):
        global root
        root = QFileInfo(__file__).absolutePath()
        self.setWindowTitle(self.title)

        #########################################
        #               MENUBAR                 #
        #########################################

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu('&Help')

        fileMenu_open = QAction(QIcon(root + '/img/open_file.png'), '&Open', self)
        fileMenu_open.setShortcut('Ctrl+O')
        fileMenu_open.setStatusTip('Open File')
        fileMenu_open.triggered.connect(self.openfile)

        fileMenu_save = QAction(QIcon(root + '/img/save_file.png'), '&Save', self)
        fileMenu_save.setShortcut('Ctrl+S')
        fileMenu_save.setStatusTip('Save File')
        fileMenu_save.triggered.connect(self.savefile)

        fileMenu_exit = QAction(QIcon(root + '/img/exit.png'), '&Exit', self)
        fileMenu_exit.setShortcut('Ctrl+Q')
        fileMenu_exit.setStatusTip('Exit')
        fileMenu_exit.triggered.connect(qApp.quit)

        helpMenu_usage = QAction(QIcon(root + '/img/help.png'), '&How to use', self)
        helpMenu_usage.setShortcut('Ctrl+H')
        helpMenu_usage.setStatusTip('How to use')
        helpMenu_usage.triggered.connect(self.show_howto)

        helpMenu_about = QAction(QIcon(root + '/img/about.png'), '&About', self)
        helpMenu_about.setStatusTip('About')
        helpMenu_about.triggered.connect(self.show_about)

        fileMenu.addAction(fileMenu_open)
        fileMenu.addAction(fileMenu_save)
        fileMenu.addAction(fileMenu_exit)
        helpMenu.addAction(helpMenu_usage)
        helpMenu.addAction(helpMenu_about)

        #########################################
        #               TOOLBAR                 #
        #########################################

        toolbar = self.addToolBar("File")
        toolbar.setMovable(False)

        toolbar_openfile = QAction(QIcon(root + "/img/open_file.png"), "Open File", self)
        toolbar_openfile.triggered.connect(self.openfile)

        toolbar_savefile = QAction(QIcon(root + "/img/save_file.png"), "Save File", self)
        toolbar_savefile.triggered.connect(self.savefile)

        toolbar.addAction(toolbar_openfile)
        toolbar.addAction(toolbar_savefile)

        #########################################
        #               TABS                    #
        #########################################

        centralWidget = QWidget(self)
        centralWidgetLayout = QVBoxLayout(centralWidget)
        centralWidget.setLayout(centralWidgetLayout)

        tabContainer = QTabWidget(centralWidget)

        tab1 = QWidget(tabContainer)
        tab2 = QWidget(tabContainer)
        tab3 = QWidget(tabContainer)
        tab4 = QWidget(tabContainer)
        tab5 = QWidget(tabContainer)
        tab6 = QWidget(tabContainer)
        tab7 = QWidget(tabContainer)
        tab8 = QWidget(tabContainer)
        tab9 = QWidget(tabContainer)
        tab10 = QWidget(tabContainer)
        tab11 = QWidget(tabContainer)
        tab12 = QWidget(tabContainer)
        tab13 = QWidget(tabContainer)
        tab14 = QWidget(tabContainer)
        tab15 = QWidget(tabContainer)
        tab16 = QWidget(tabContainer)
        tab17 = QWidget(tabContainer)
        tab18 = QWidget(tabContainer)
        tab19 = QWidget(tabContainer)
        tab20 = QWidget(tabContainer)

        tab1layout = QVBoxLayout(tab1)

        tabContainer.setLayout(tab1layout)

        tabContainer.addTab(tab1, "Save 1")
        tabContainer.addTab(tab2, "Save 2")
        tabContainer.addTab(tab3, "Save 3")
        tabContainer.addTab(tab4, "Save 4")
        tabContainer.addTab(tab5, "Save 5")
        tabContainer.addTab(tab6, "Save 6")
        tabContainer.addTab(tab7, "Save 7")
        tabContainer.addTab(tab8, "Save 8")
        tabContainer.addTab(tab9, "Save 9")
        tabContainer.addTab(tab10, "Save 10")
        tabContainer.addTab(tab11, "Save 11")
        tabContainer.addTab(tab12, "Save 12")
        tabContainer.addTab(tab13, "Save 13")
        tabContainer.addTab(tab14, "Save 14")
        tabContainer.addTab(tab15, "Save 15")
        tabContainer.addTab(tab16, "Save 16")
        tabContainer.addTab(tab17, "Save 17")
        tabContainer.addTab(tab18, "Save 18")
        tabContainer.addTab(tab19, "Save 19")
        tabContainer.addTab(tab20, "Save 20")

        tabContainer.setCurrentIndex(0)
        centralWidgetLayout.addWidget(tabContainer)
        self.setCentralWidget(centralWidget)

        #########################################
        #               Save 1                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab1)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_1"))

        btn_herostat = QPushButton('Hero_Stats1', tab1)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_1"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab1)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_1"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab1)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_1"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab1)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_1"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab1)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_1"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab1)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_1"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab1)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_1"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab1)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_1"))

        btn_items = QPushButton('Items', tab1)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_1"))

        btn_magatama = QPushButton('Magatama', tab1)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_1"))

        #########################################
        #               Save 2                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab2)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_2"))

        btn_herostat = QPushButton('Hero_Stats1', tab2)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_2"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab2)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_2"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab2)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_2"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab2)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_2"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab2)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_2"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab2)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_2"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab2)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_2"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab2)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_2"))

        btn_items = QPushButton('Items', tab2)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_2"))

        btn_magatama = QPushButton('Magatama', tab2)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_2"))

        #########################################
        #               Save 3                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab3)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_3"))

        btn_herostat = QPushButton('Hero_Stats1', tab3)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_3"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab3)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_3"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab3)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_3"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab3)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_3"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab3)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_3"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab3)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_3"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab3)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_3"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab3)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_3"))

        btn_items = QPushButton('Items', tab3)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_3"))

        btn_magatama = QPushButton('Magatama', tab3)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_3"))

        #########################################
        #               Save 4                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab4)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_4"))

        btn_herostat = QPushButton('Hero_Stats1', tab4)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_4"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab4)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_4"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab4)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_4"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab4)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_4"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab4)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_4"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab4)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_4"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab4)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_4"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab4)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_4"))

        btn_items = QPushButton('Items', tab4)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_4"))

        btn_magatama = QPushButton('Magatama', tab4)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_4"))

        #########################################
        #               Save 5                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab5)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_5"))

        btn_herostat = QPushButton('Hero_Stats1', tab5)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_5"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab5)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_5"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab5)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_5"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab5)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_5"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab5)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_5"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab5)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_5"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab5)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_5"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab5)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_5"))

        btn_items = QPushButton('Items', tab5)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_5"))

        btn_magatama = QPushButton('Magatama', tab5)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_5"))

        #########################################
        #               Save 6                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab6)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_6"))

        btn_herostat = QPushButton('Hero_Stats1', tab6)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_6"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab6)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_6"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab6)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_6"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab6)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_6"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab6)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_6"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab6)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_6"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab6)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_6"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab6)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_6"))

        btn_items = QPushButton('Items', tab6)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_6"))

        btn_magatama = QPushButton('Magatama', tab6)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_6"))

        #########################################
        #               Save 7                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab7)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_7"))

        btn_herostat = QPushButton('Hero_Stats1', tab7)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_7"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab7)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_7"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab7)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_7"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab7)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_7"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab7)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_7"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab7)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_7"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab7)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_7"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab7)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_7"))

        btn_items = QPushButton('Items', tab7)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_7"))

        btn_magatama = QPushButton('Magatama', tab7)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_7"))

        #########################################
        #               Save 8                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab8)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_8"))

        btn_herostat = QPushButton('Hero_Stats1', tab8)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_8"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab8)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_8"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab8)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_8"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab8)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_8"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab8)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_8"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab8)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_8"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab8)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_8"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab8)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_8"))

        btn_items = QPushButton('Items', tab8)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_8"))

        btn_magatama = QPushButton('Magatama', tab8)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_8"))

        #########################################
        #               Save 9                  #
        #########################################

        btn_money = QPushButton('Hero_$', tab9)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_9"))

        btn_herostat = QPushButton('Hero_Stats1', tab9)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_9"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab9)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_9"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab9)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_9"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab9)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_9"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab9)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_9"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab9)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_9"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab9)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_9"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab9)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_9"))

        btn_items = QPushButton('Items', tab9)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_9"))

        btn_magatama = QPushButton('Magatama', tab9)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_9"))

        #########################################
        #               Save 10                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab10)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_10"))

        btn_herostat = QPushButton('Hero_Stats1', tab10)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_10"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab10)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_10"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab10)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_10"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab10)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_10"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab10)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_10"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab10)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_10"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab10)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_10"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab10)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_10"))

        btn_items = QPushButton('Items', tab10)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_10"))

        btn_magatama = QPushButton('Magatama', tab10)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_10"))

        #########################################
        #               Save 11                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab11)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_11"))

        btn_herostat = QPushButton('Hero_Stats1', tab11)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_11"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab11)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_11"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab11)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_11"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab11)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_11"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab11)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_11"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab11)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_11"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab11)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_11"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab11)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_11"))

        btn_items = QPushButton('Items', tab11)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_11"))

        btn_magatama = QPushButton('Magatama', tab11)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_11"))

        #########################################
        #               Save 12                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab12)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_12"))

        btn_herostat = QPushButton('Hero_Stats1', tab12)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_12"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab12)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_12"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab12)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_12"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab12)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_12"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab12)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_12"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab12)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_12"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab12)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_12"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab12)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_12"))

        btn_items = QPushButton('Items', tab12)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_12"))

        btn_magatama = QPushButton('Magatama', tab12)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_12"))

        #########################################
        #               Save 13                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab13)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_13"))

        btn_herostat = QPushButton('Hero_Stats1', tab13)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_13"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab13)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_13"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab13)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_13"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab13)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_13"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab13)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_13"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab13)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_13"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab13)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_13"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab13)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_13"))

        btn_items = QPushButton('Items', tab13)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_13"))

        btn_magatama = QPushButton('Magatama', tab13)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_13"))

        #########################################
        #               Save 14                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab14)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_14"))

        btn_herostat = QPushButton('Hero_Stats1', tab14)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_14"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab14)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_14"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab14)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_14"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab14)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_14"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab14)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_14"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab14)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_14"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab14)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_14"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab14)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_14"))

        btn_items = QPushButton('Items', tab14)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_14"))

        btn_magatama = QPushButton('Magatama', tab14)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_14"))

        #########################################
        #               Save 15                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab15)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_15"))

        btn_herostat = QPushButton('Hero_Stats1', tab15)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_15"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab15)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_15"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab15)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_15"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab15)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_15"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab15)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_15"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab15)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_15"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab15)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_15"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab15)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_15"))

        btn_items = QPushButton('Items', tab15)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_15"))

        btn_magatama = QPushButton('Magatama', tab15)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_15"))

        #########################################
        #               Save 16                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab16)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_16"))

        btn_herostat = QPushButton('Hero_Stats1', tab16)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_16"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab16)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_16"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab16)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_16"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab16)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_16"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab16)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_16"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab16)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_16"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab16)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_16"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab16)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_16"))

        btn_items = QPushButton('Items', tab16)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_16"))

        btn_magatama = QPushButton('Magatama', tab16)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_16"))

        #########################################
        #               Save 17                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab17)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_17"))

        btn_herostat = QPushButton('Hero_Stats1', tab17)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_17"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab17)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_17"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab17)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_17"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab17)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_17"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab17)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_17"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab17)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_17"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab17)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_17"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab17)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_17"))

        btn_items = QPushButton('Items', tab17)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_17"))

        btn_magatama = QPushButton('Magatama', tab17)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_17"))

        #########################################
        #               Save 18                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab18)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_18"))

        btn_herostat = QPushButton('Hero_Stats1', tab18)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_18"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab18)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_18"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab18)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_18"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab18)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_18"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab18)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_18"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab18)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_18"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab18)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_18"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab18)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_18"))

        btn_items = QPushButton('Items', tab18)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_18"))

        btn_magatama = QPushButton('Magatama', tab18)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_18"))

        #########################################
        #               Save 19                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab19)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_19"))

        btn_herostat = QPushButton('Hero_Stats1', tab19)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_19"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab19)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_19"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab19)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_19"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab19)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_19"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab19)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_19"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab19)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_19"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab19)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_19"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab19)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_19"))

        btn_items = QPushButton('Items', tab19)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_19"))

        btn_magatama = QPushButton('Magatama', tab19)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_19"))

        #########################################
        #               Save 20                 #
        #########################################

        btn_money = QPushButton('Hero_$', tab20)
        btn_money.setToolTip(f"Hero's Money")
        btn_money.move(35, 30)
        btn_money.clicked.connect(lambda: self.show_statwindow("HeroMoney_20"))

        btn_herostat = QPushButton('Hero_Stats1', tab20)
        btn_herostat.setToolTip('HP, Max HP, MP, Max MP')
        btn_herostat.move(135, 30)
        btn_herostat.clicked.connect(lambda: self.show_statwindow("HeroMainStat_20"))

        btn_herosubstat = QPushButton('Hero_Stats2', tab20)
        btn_herosubstat.setToolTip('Str, Mag, Vit, Agi, Luc')
        btn_herosubstat.move(235, 30)
        btn_herosubstat.clicked.connect(lambda: self.show_statwindow("HeroSubStat_20"))

        btn_demonstat = QPushButton('Demon_ID_Stats', tab20)
        btn_demonstat.setToolTip('Demon ID, HP, Max HP, MP, Max MP and Level')
        btn_demonstat.move(335, 30)
        btn_demonstat.clicked.connect(lambda: self.show_statwindow("DemonMainStat_20"))

        btn_demonsubstat = QPushButton('Demon_Stats2', tab20)
        btn_demonsubstat.setToolTip('Demon Str, Mag, Vit, Agi, Luc')
        btn_demonsubstat.move(460, 30)
        btn_demonsubstat.clicked.connect(lambda: self.show_statwindow("DemonSubStat_20"))

        btn_herodemonlevel = QPushButton('Hero_Demon_Level', tab20)
        btn_herodemonlevel.setToolTip('Hero & Demon Level')
        btn_herodemonlevel.move(35, 90)
        btn_herodemonlevel.clicked.connect(lambda: self.show_statwindow("HeroDemonLevel_20"))

        btn_herodemonexp = QPushButton('Hero_Demon_EXP', tab20)
        btn_herodemonexp.setToolTip('Hero & Demon EXP')
        btn_herodemonexp.move(200, 90)
        btn_herodemonexp.clicked.connect(lambda: self.show_statwindow("HeroDemonExp_20"))

        btn_herodemonskill = QPushButton('Hero_Demon_Skill', tab20)
        btn_herodemonskill.setToolTip('Hero & Demon Skills 1 to 8')
        btn_herodemonskill.move(350, 90)
        btn_herodemonskill.clicked.connect(lambda: self.show_statwindow("HeroDemonSkills_20"))

        btn_herodemonskillamt = QPushButton('Skill Amount', tab20)
        btn_herodemonskillamt.setToolTip('Hero & Demon Skills Amount')
        btn_herodemonskillamt.move(490, 90)
        btn_herodemonskillamt.clicked.connect(lambda: self.show_statwindow("HeroDemonSkillsAmt_20"))

        btn_items = QPushButton('Items', tab20)
        btn_items.setToolTip('Items')
        btn_items.move(35, 150)
        btn_items.clicked.connect(lambda: self.show_statwindow("Items_20"))

        btn_magatama = QPushButton('Magatama', tab20)
        btn_magatama.setToolTip('Magatama')
        btn_magatama.move(135, 150)
        btn_magatama.clicked.connect(lambda: self.show_statwindow("Magatamas_20"))

        self.show()

    # Open File
    @pyqtSlot()
    def openfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', 'savedata')
        if filename[0] == '':
            return
        #if (os.path.getsize(filename[0]) == 6291456):  # Filesize check
        if (os.path.getsize(filename[0]) >= 1048576):  # Filesize check
            f = open(filename[0], "rb").read()
            global h
            h = (binascii.hexlify(f))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not a valid savefile!")
            msg.setWindowTitle("Not valid")
            msg.setWindowIcon(QIcon(root + '/img/icon.ico'))
            msg.exec_()

    # Save File
    def savefile(self):
        if self.checkforsave():
            savedir = QFileDialog.getSaveFileName(self, 'Save File', 'SaveData')
            if savedir[0] == '':
                return
            file = open(savedir[0], "wb")
            file.write(binascii.unhexlify(h))
            file.close()

    # Check if a savefile is open
    def checkforsave(self):
        if "h" in globals():
            return True
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Open a <b>Save File</b> first!")
            msg.setWindowTitle("No Save File")
            msg.setWindowIcon(QIcon(root + '/img/icon.ico'))
            msg.exec_()
            return False

    # How to
    def show_howto(self):
        global root
        howto = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        howto.setWindowTitle("How To Use")
        howto.setWindowIcon(QIcon(root + '/img/help.png'))
        width = 400
        height = 200
        howto.resize(width, height)
        howto.setFixedSize(width, height)
        howto.setWindowModality(Qt.ApplicationModal)

        l1 = QLabel()
        l2 = QLabel()

        l1.setText("<center><b>HOW TO USE</b><br><br></center>")
        l2.setText(
            "<ul><li>1. Dump your save with your preferred save manager</li><li>2. Open your save (savedata)</li><li>3. Edit stuff to your liking</li><li>4. Save it (Ctrl + S)</li><li>5. Overwrite your save with the one you just edited</li><li>6. That's it!</li></ul>")

        l1.setAlignment(Qt.AlignLeft)
        l2.setAlignment(Qt.AlignLeft)

        vbox = QVBoxLayout()
        vbox.addWidget(l1)
        vbox.addWidget(l2)
        vbox.addStretch()
        howto.setLayout(vbox)
        howto.exec_()

    # About
    def show_about(self):
        global root
        about = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        about.setWindowTitle("About")
        about.setWindowIcon(QIcon(root + '/img/about.png'))
        width = 450
        height = 350
        about.resize(width, height)
        about.setFixedSize(width, height)
        about.setWindowModality(Qt.ApplicationModal)

        l1 = QLabel()
        l1.setText(
            "<b>THIS SOFTWARE MUST NOT BE SOLD,NEITHER ALONE NOR AS PART OF A BUNDLE. IF YOU PAID FOR THIS SOFTWARE OR RECEIVED IT AS PART OF A BUNDLE FOLLOWING PAYMENT,<br>YOU HAVE BEEN SCAMMED AND SHOULD DEMAND YOUR MONEY BACK IMMEDIATELY.</b>")
        l1.setAlignment(Qt.AlignCenter)
        l1.setWordWrap(True)
        l2 = QLabel()
        l2.setText("Created by: <a href=\"https://github.com/Amuyea-gbatemp\"><b>Amuyea-gbatemp</b></a>")
        l2.setOpenExternalLinks(True)
        l2.setAlignment(Qt.AlignLeft)
        l3 = QLabel()
        l3.setText("Advices/Helpful: Pj1980/Skiller & PS4 Save Wizard JP/EN<br>Reference on Python Save Editor: <a href=\"https://github.com/CapitanRetraso/Ultimate-Smasher\"><b>Capitán Retraso</b></a>")
        l3.setOpenExternalLinks(True)
        l3.setAlignment(Qt.AlignLeft)
        l4 = QLabel()
        l4.setText("<a href=\"https://github.com/Amuyea-gbatemp/Persona-5-Strikers-Scramble-Save-Editor/issues\"><b>Report a problem</b></a>")
        l4.setOpenExternalLinks(True)
        l4.setAlignment(Qt.AlignRight)
        l5 = QLabel()
        l5.setText(
            "<b>DISCLAIMER</b><br> This tool can damage your savegame or cause a ban if not used correctly.<br><b>By using it you are responsible for any data lost or ban.</b><br>Be careful when editing your savegame and always keep a clean backup.")
        l5.setAlignment(Qt.AlignCenter)
        l5.setWordWrap(True)

        vbox = QVBoxLayout()
        vbox.addWidget(l1)
        vbox.addStretch()
        vbox.addWidget(l5)
        vbox.addStretch()
        vbox.addWidget(l2)
        vbox.addWidget(l3)
        vbox.addWidget(l4)
        about.setLayout(vbox)

        about.exec_()

    # Name & Value
    def show_statwindow(self, category):
        if self.checkforsave():
            statwindow = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            statwindow.setWindowTitle("Stats - " + category)
            statwindow.setWindowIcon(QIcon(root + '/img/icon.ico'))
            width = 550
            height = 400
            statwindow.resize(width, height)
            statwindow.setFixedSize(width, height)
            self.layout = QVBoxLayout()

            #########################################
            #             Save 1 Offsets            #
            #########################################

            if (category == "HeroMoney_1"):
                statNames = moneyList
                statOffsets = save_1_moneyOffsets

            elif(category == "HeroMainStat_1"):
                statNames = herostat1List
                statOffsets = save_1_hslListOffsets

            elif(category == "HeroSubStat_1"):
                statNames = herostat2List
                statOffsets = save_1_hs2ListOffsets

            elif(category == "DemonMainStat_1"):
                statNames = demonidstatList
                statOffsets = save_1_disListOffsets

            elif (category == "DemonSubStat_1"):
                statNames = demonstatList
                statOffsets = save_1_dstatsListOffsets

            elif (category == "HeroDemonLevel_1"):
                statNames = herodemonlevelList
                statOffsets = save_1_hdlevelListOffsets

            elif (category == "HeroDemonExp_1"):
                statNames = herodemonexpList
                statOffsets = save_1_hdexpListOffsets

            elif (category == "HeroDemonSkills_1"):
                statNames = herodemonskillList
                statOffsets = save_1_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_1"):
                statNames = herodemonamountList
                statOffsets = save_1_skillamountOffsets

            elif (category == "Items_1"):
                statNames = itemList
                statOffsets = save_1_itemsListOffsets

            elif (category == "Magatamas_1"):
                statNames = magatamaList
                statOffsets = save_1_magatamaListOffsets

            #########################################
            #             Save 2 Offsets            #
            #########################################

            if (category == "HeroMoney_2"):
                statNames = moneyList
                statOffsets = save_2_moneyOffsets

            elif(category == "HeroMainStat_2"):
                statNames = herostat1List
                statOffsets = save_2_hslListOffsets

            elif(category == "HeroSubStat_2"):
                statNames = herostat2List
                statOffsets = save_2_hs2ListOffsets

            elif(category == "DemonMainStat_2"):
                statNames = demonidstatList
                statOffsets = save_2_disListOffsets

            elif (category == "DemonSubStat_2"):
                statNames = demonstatList
                statOffsets = save_2_dstatsListOffsets

            elif (category == "HeroDemonLevel_2"):
                statNames = herodemonlevelList
                statOffsets = save_2_hdlevelListOffsets

            elif (category == "HeroDemonExp_2"):
                statNames = herodemonexpList
                statOffsets = save_2_hdexpListOffsets

            elif (category == "HeroDemonSkills_2"):
                statNames = herodemonskillList
                statOffsets = save_2_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_2"):
                statNames = herodemonamountList
                statOffsets = save_2_skillamountOffsets

            elif (category == "Items_2"):
                statNames = itemList
                statOffsets = save_2_itemsListOffsets

            elif (category == "Magatamas_2"):
                statNames = magatamaList
                statOffsets = save_2_magatamaListOffsets

            #########################################
            #             Save 3 Offsets            #
            #########################################

            if (category == "HeroMoney_3"):
                statNames = moneyList
                statOffsets = save_3_moneyOffsets

            elif(category == "HeroMainStat_3"):
                statNames = herostat1List
                statOffsets = save_3_hslListOffsets

            elif(category == "HeroSubStat_3"):
                statNames = herostat2List
                statOffsets = save_3_hs2ListOffsets

            elif(category == "DemonMainStat_3"):
                statNames = demonidstatList
                statOffsets = save_3_disListOffsets

            elif (category == "DemonSubStat_3"):
                statNames = demonstatList
                statOffsets = save_3_dstatsListOffsets

            elif (category == "HeroDemonLevel_3"):
                statNames = herodemonlevelList
                statOffsets = save_3_hdlevelListOffsets

            elif (category == "HeroDemonExp_3"):
                statNames = herodemonexpList
                statOffsets = save_3_hdexpListOffsets

            elif (category == "HeroDemonSkills_3"):
                statNames = herodemonskillList
                statOffsets = save_3_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_3"):
                statNames = herodemonamountList
                statOffsets = save_3_skillamountOffsets

            elif (category == "Items_3"):
                statNames = itemList
                statOffsets = save_3_itemsListOffsets

            elif (category == "Magatamas_3"):
                statNames = magatamaList
                statOffsets = save_3_magatamaListOffsets

            #########################################
            #             Save 4 Offsets            #
            #########################################

            if (category == "HeroMoney_4"):
                statNames = moneyList
                statOffsets = save_4_moneyOffsets

            elif(category == "HeroMainStat_4"):
                statNames = herostat1List
                statOffsets = save_4_hslListOffsets

            elif(category == "HeroSubStat_4"):
                statNames = herostat2List
                statOffsets = save_4_hs2ListOffsets

            elif(category == "DemonMainStat_4"):
                statNames = demonidstatList
                statOffsets = save_4_disListOffsets

            elif (category == "DemonSubStat_4"):
                statNames = demonstatList
                statOffsets = save_4_dstatsListOffsets

            elif (category == "HeroDemonLevel_4"):
                statNames = herodemonlevelList
                statOffsets = save_4_hdlevelListOffsets

            elif (category == "HeroDemonExp_4"):
                statNames = herodemonexpList
                statOffsets = save_4_hdexpListOffsets

            elif (category == "HeroDemonSkills_4"):
                statNames = herodemonskillList
                statOffsets = save_4_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_4"):
                statNames = herodemonamountList
                statOffsets = save_4_skillamountOffsets

            elif (category == "Items_4"):
                statNames = itemList
                statOffsets = save_4_itemsListOffsets

            elif (category == "Magatamas_4"):
                statNames = magatamaList
                statOffsets = save_4_magatamaListOffsets

            #########################################
            #             Save 5 Offsets            #
            #########################################

            if (category == "HeroMoney_5"):
                statNames = moneyList
                statOffsets = save_5_moneyOffsets

            elif(category == "HeroMainStat_5"):
                statNames = herostat1List
                statOffsets = save_5_hslListOffsets

            elif(category == "HeroSubStat_5"):
                statNames = herostat2List
                statOffsets = save_5_hs2ListOffsets

            elif(category == "DemonMainStat_5"):
                statNames = demonidstatList
                statOffsets = save_5_disListOffsets

            elif (category == "DemonSubStat_5"):
                statNames = demonstatList
                statOffsets = save_5_dstatsListOffsets

            elif (category == "HeroDemonLevel_5"):
                statNames = herodemonlevelList
                statOffsets = save_5_hdlevelListOffsets

            elif (category == "HeroDemonExp_5"):
                statNames = herodemonexpList
                statOffsets = save_5_hdexpListOffsets

            elif (category == "HeroDemonSkills_5"):
                statNames = herodemonskillList
                statOffsets = save_5_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_5"):
                statNames = herodemonamountList
                statOffsets = save_5_skillamountOffsets

            elif (category == "Items_5"):
                statNames = itemList
                statOffsets = save_5_itemsListOffsets

            elif (category == "Magatamas_5"):
                statNames = magatamaList
                statOffsets = save_5_magatamaListOffsets

            #########################################
            #             Save 6 Offsets            #
            #########################################

            if (category == "HeroMoney_6"):
                statNames = moneyList
                statOffsets = save_6_moneyOffsets

            elif(category == "HeroMainStat_6"):
                statNames = herostat1List
                statOffsets = save_6_hslListOffsets

            elif(category == "HeroSubStat_6"):
                statNames = herostat2List
                statOffsets = save_6_hs2ListOffsets

            elif(category == "DemonMainStat_6"):
                statNames = demonidstatList
                statOffsets = save_6_disListOffsets

            elif (category == "DemonSubStat_6"):
                statNames = demonstatList
                statOffsets = save_6_dstatsListOffsets

            elif (category == "HeroDemonLevel_6"):
                statNames = herodemonlevelList
                statOffsets = save_6_hdlevelListOffsets

            elif (category == "HeroDemonExp_6"):
                statNames = herodemonexpList
                statOffsets = save_6_hdexpListOffsets

            elif (category == "HeroDemonSkills_6"):
                statNames = herodemonskillList
                statOffsets = save_6_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_6"):
                statNames = herodemonamountList
                statOffsets = save_6_skillamountOffsets

            elif (category == "Items_6"):
                statNames = itemList
                statOffsets = save_6_itemsListOffsets

            elif (category == "Magatamas_6"):
                statNames = magatamaList
                statOffsets = save_6_magatamaListOffsets

            #########################################
            #             Save 7 Offsets            #
            #########################################

            if (category == "HeroMoney_7"):
                statNames = moneyList
                statOffsets = save_7_moneyOffsets

            elif(category == "HeroMainStat_7"):
                statNames = herostat1List
                statOffsets = save_7_hslListOffsets

            elif(category == "HeroSubStat_7"):
                statNames = herostat2List
                statOffsets = save_7_hs2ListOffsets

            elif(category == "DemonMainStat_7"):
                statNames = demonidstatList
                statOffsets = save_7_disListOffsets

            elif (category == "DemonSubStat_7"):
                statNames = demonstatList
                statOffsets = save_7_dstatsListOffsets

            elif (category == "HeroDemonLevel_7"):
                statNames = herodemonlevelList
                statOffsets = save_7_hdlevelListOffsets

            elif (category == "HeroDemonExp_7"):
                statNames = herodemonexpList
                statOffsets = save_7_hdexpListOffsets

            elif (category == "HeroDemonSkills_7"):
                statNames = herodemonskillList
                statOffsets = save_7_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_7"):
                statNames = herodemonamountList
                statOffsets = save_7_skillamountOffsets

            elif (category == "Items_7"):
                statNames = itemList
                statOffsets = save_7_itemsListOffsets

            elif (category == "Magatamas_7"):
                statNames = magatamaList
                statOffsets = save_7_magatamaListOffsets

            #########################################
            #             Save 8 Offsets            #
            #########################################

            if (category == "HeroMoney_8"):
                statNames = moneyList
                statOffsets = save_8_moneyOffsets

            elif(category == "HeroMainStat_8"):
                statNames = herostat1List
                statOffsets = save_8_hslListOffsets

            elif(category == "HeroSubStat_8"):
                statNames = herostat2List
                statOffsets = save_8_hs2ListOffsets

            elif(category == "DemonMainStat_8"):
                statNames = demonidstatList
                statOffsets = save_8_disListOffsets

            elif (category == "DemonSubStat_8"):
                statNames = demonstatList
                statOffsets = save_8_dstatsListOffsets

            elif (category == "HeroDemonLevel_8"):
                statNames = herodemonlevelList
                statOffsets = save_8_hdlevelListOffsets

            elif (category == "HeroDemonExp_8"):
                statNames = herodemonexpList
                statOffsets = save_8_hdexpListOffsets

            elif (category == "HeroDemonSkills_8"):
                statNames = herodemonskillList
                statOffsets = save_8_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_8"):
                statNames = herodemonamountList
                statOffsets = save_8_skillamountOffsets

            elif (category == "Items_8"):
                statNames = itemList
                statOffsets = save_8_itemsListOffsets

            elif (category == "Magatamas_8"):
                statNames = magatamaList
                statOffsets = save_8_magatamaListOffsets

            #########################################
            #             Save 9 Offsets            #
            #########################################

            if (category == "HeroMoney_9"):
                statNames = moneyList
                statOffsets = save_9_moneyOffsets

            elif(category == "HeroMainStat_9"):
                statNames = herostat1List
                statOffsets = save_9_hslListOffsets

            elif(category == "HeroSubStat_9"):
                statNames = herostat2List
                statOffsets = save_9_hs2ListOffsets

            elif(category == "DemonMainStat_9"):
                statNames = demonidstatList
                statOffsets = save_9_disListOffsets

            elif (category == "DemonSubStat_9"):
                statNames = demonstatList
                statOffsets = save_9_dstatsListOffsets

            elif (category == "HeroDemonLevel_9"):
                statNames = herodemonlevelList
                statOffsets = save_9_hdlevelListOffsets

            elif (category == "HeroDemonExp_9"):
                statNames = herodemonexpList
                statOffsets = save_9_hdexpListOffsets

            elif (category == "HeroDemonSkills_9"):
                statNames = herodemonskillList
                statOffsets = save_9_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_9"):
                statNames = herodemonamountList
                statOffsets = save_9_skillamountOffsets

            elif (category == "Items_9"):
                statNames = itemList
                statOffsets = save_9_itemsListOffsets

            elif (category == "Magatamas_9"):
                statNames = magatamaList
                statOffsets = save_9_magatamaListOffsets

            #########################################
            #             Save 10 Offsets           #
            #########################################

            if (category == "HeroMoney_10"):
                statNames = moneyList
                statOffsets = save_10_moneyOffsets

            elif(category == "HeroMainStat_10"):
                statNames = herostat1List
                statOffsets = save_10_hslListOffsets

            elif(category == "HeroSubStat_10"):
                statNames = herostat2List
                statOffsets = save_10_hs2ListOffsets

            elif(category == "DemonMainStat_10"):
                statNames = demonidstatList
                statOffsets = save_10_disListOffsets

            elif (category == "DemonSubStat_10"):
                statNames = demonstatList
                statOffsets = save_10_dstatsListOffsets

            elif (category == "HeroDemonLevel_10"):
                statNames = herodemonlevelList
                statOffsets = save_10_hdlevelListOffsets

            elif (category == "HeroDemonExp_10"):
                statNames = herodemonexpList
                statOffsets = save_10_hdexpListOffsets

            elif (category == "HeroDemonSkills_10"):
                statNames = herodemonskillList
                statOffsets = save_10_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_10"):
                statNames = herodemonamountList
                statOffsets = save_10_skillamountOffsets

            elif (category == "Items_10"):
                statNames = itemList
                statOffsets = save_10_itemsListOffsets

            elif (category == "Magatamas_10"):
                statNames = magatamaList
                statOffsets = save_10_magatamaListOffsets

            #########################################
            #             Save 11 Offsets           #
            #########################################

            if (category == "HeroMoney_11"):
                statNames = moneyList
                statOffsets = save_11_moneyOffsets

            elif(category == "HeroMainStat_11"):
                statNames = herostat1List
                statOffsets = save_11_hslListOffsets

            elif(category == "HeroSubStat_11"):
                statNames = herostat2List
                statOffsets = save_11_hs2ListOffsets

            elif(category == "DemonMainStat_11"):
                statNames = demonidstatList
                statOffsets = save_11_disListOffsets

            elif (category == "DemonSubStat_11"):
                statNames = demonstatList
                statOffsets = save_11_dstatsListOffsets

            elif (category == "HeroDemonLevel_11"):
                statNames = herodemonlevelList
                statOffsets = save_11_hdlevelListOffsets

            elif (category == "HeroDemonExp_11"):
                statNames = herodemonexpList
                statOffsets = save_11_hdexpListOffsets

            elif (category == "HeroDemonSkills_11"):
                statNames = herodemonskillList
                statOffsets = save_11_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_11"):
                statNames = herodemonamountList
                statOffsets = save_11_skillamountOffsets

            elif (category == "Items_11"):
                statNames = itemList
                statOffsets = save_11_itemsListOffsets

            elif (category == "Magatamas_11"):
                statNames = magatamaList
                statOffsets = save_11_magatamaListOffsets

            #########################################
            #             Save 12 Offsets           #
            #########################################

            if (category == "HeroMoney_12"):
                statNames = moneyList
                statOffsets = save_12_moneyOffsets

            elif(category == "HeroMainStat_12"):
                statNames = herostat1List
                statOffsets = save_12_hslListOffsets

            elif(category == "HeroSubStat_12"):
                statNames = herostat2List
                statOffsets = save_12_hs2ListOffsets

            elif(category == "DemonMainStat_12"):
                statNames = demonidstatList
                statOffsets = save_12_disListOffsets

            elif (category == "DemonSubStat_12"):
                statNames = demonstatList
                statOffsets = save_12_dstatsListOffsets

            elif (category == "HeroDemonLevel_12"):
                statNames = herodemonlevelList
                statOffsets = save_12_hdlevelListOffsets

            elif (category == "HeroDemonExp_12"):
                statNames = herodemonexpList
                statOffsets = save_12_hdexpListOffsets

            elif (category == "HeroDemonSkills_12"):
                statNames = herodemonskillList
                statOffsets = save_12_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_12"):
                statNames = herodemonamountList
                statOffsets = save_12_skillamountOffsets

            elif (category == "Items_12"):
                statNames = itemList
                statOffsets = save_12_itemsListOffsets

            elif (category == "Magatamas_12"):
                statNames = magatamaList
                statOffsets = save_12_magatamaListOffsets

            #########################################
            #             Save 13 Offsets           #
            #########################################

            if (category == "HeroMoney_13"):
                statNames = moneyList
                statOffsets = save_13_moneyOffsets

            elif(category == "HeroMainStat_13"):
                statNames = herostat1List
                statOffsets = save_13_hslListOffsets

            elif(category == "HeroSubStat_13"):
                statNames = herostat2List
                statOffsets = save_13_hs2ListOffsets

            elif(category == "DemonMainStat_13"):
                statNames = demonidstatList
                statOffsets = save_13_disListOffsets

            elif (category == "DemonSubStat_13"):
                statNames = demonstatList
                statOffsets = save_13_dstatsListOffsets

            elif (category == "HeroDemonLevel_13"):
                statNames = herodemonlevelList
                statOffsets = save_13_hdlevelListOffsets

            elif (category == "HeroDemonExp_13"):
                statNames = herodemonexpList
                statOffsets = save_13_hdexpListOffsets

            elif (category == "HeroDemonSkills_13"):
                statNames = herodemonskillList
                statOffsets = save_13_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_13"):
                statNames = herodemonamountList
                statOffsets = save_13_skillamountOffsets

            elif (category == "Items_13"):
                statNames = itemList
                statOffsets = save_13_itemsListOffsets

            elif (category == "Magatamas_13"):
                statNames = magatamaList
                statOffsets = save_13_magatamaListOffsets

            #########################################
            #             Save 14 Offsets           #
            #########################################

            if (category == "HeroMoney_14"):
                statNames = moneyList
                statOffsets = save_14_moneyOffsets

            elif(category == "HeroMainStat_14"):
                statNames = herostat1List
                statOffsets = save_14_hslListOffsets

            elif(category == "HeroSubStat_14"):
                statNames = herostat2List
                statOffsets = save_14_hs2ListOffsets

            elif(category == "DemonMainStat_14"):
                statNames = demonidstatList
                statOffsets = save_14_disListOffsets

            elif (category == "DemonSubStat_14"):
                statNames = demonstatList
                statOffsets = save_14_dstatsListOffsets

            elif (category == "HeroDemonLevel_14"):
                statNames = herodemonlevelList
                statOffsets = save_14_hdlevelListOffsets

            elif (category == "HeroDemonExp_14"):
                statNames = herodemonexpList
                statOffsets = save_14_hdexpListOffsets

            elif (category == "HeroDemonSkills_14"):
                statNames = herodemonskillList
                statOffsets = save_14_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_14"):
                statNames = herodemonamountList
                statOffsets = save_14_skillamountOffsets

            elif (category == "Items_14"):
                statNames = itemList
                statOffsets = save_14_itemsListOffsets

            elif (category == "Magatamas_14"):
                statNames = magatamaList
                statOffsets = save_14_magatamaListOffsets

            #########################################
            #             Save 15 Offsets           #
            #########################################

            if (category == "HeroMoney_15"):
                statNames = moneyList
                statOffsets = save_15_moneyOffsets

            elif(category == "HeroMainStat_15"):
                statNames = herostat1List
                statOffsets = save_15_hslListOffsets

            elif(category == "HeroSubStat_15"):
                statNames = herostat2List
                statOffsets = save_15_hs2ListOffsets

            elif(category == "DemonMainStat_15"):
                statNames = demonidstatList
                statOffsets = save_15_disListOffsets

            elif (category == "DemonSubStat_15"):
                statNames = demonstatList
                statOffsets = save_15_dstatsListOffsets

            elif (category == "HeroDemonLevel_15"):
                statNames = herodemonlevelList
                statOffsets = save_15_hdlevelListOffsets

            elif (category == "HeroDemonExp_15"):
                statNames = herodemonexpList
                statOffsets = save_15_hdexpListOffsets

            elif (category == "HeroDemonSkills_15"):
                statNames = herodemonskillList
                statOffsets = save_15_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_15"):
                statNames = herodemonamountList
                statOffsets = save_15_skillamountOffsets

            elif (category == "Items_15"):
                statNames = itemList
                statOffsets = save_15_itemsListOffsets

            elif (category == "Magatamas_15"):
                statNames = magatamaList
                statOffsets = save_15_magatamaListOffsets

            #########################################
            #             Save 16 Offsets           #
            #########################################

            if (category == "HeroMoney_16"):
                statNames = moneyList
                statOffsets = save_16_moneyOffsets

            elif(category == "HeroMainStat_16"):
                statNames = herostat1List
                statOffsets = save_16_hslListOffsets

            elif(category == "HeroSubStat_16"):
                statNames = herostat2List
                statOffsets = save_16_hs2ListOffsets

            elif(category == "DemonMainStat_16"):
                statNames = demonidstatList
                statOffsets = save_16_disListOffsets

            elif (category == "DemonSubStat_16"):
                statNames = demonstatList
                statOffsets = save_16_dstatsListOffsets

            elif (category == "HeroDemonLevel_16"):
                statNames = herodemonlevelList
                statOffsets = save_16_hdlevelListOffsets

            elif (category == "HeroDemonExp_16"):
                statNames = herodemonexpList
                statOffsets = save_16_hdexpListOffsets

            elif (category == "HeroDemonSkills_16"):
                statNames = herodemonskillList
                statOffsets = save_16_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_16"):
                statNames = herodemonamountList
                statOffsets = save_16_skillamountOffsets

            elif (category == "Items_16"):
                statNames = itemList
                statOffsets = save_16_itemsListOffsets

            elif (category == "Magatamas_16"):
                statNames = magatamaList
                statOffsets = save_16_magatamaListOffsets

            #########################################
            #             Save 17 Offsets           #
            #########################################

            if (category == "HeroMoney_17"):
                statNames = moneyList
                statOffsets = save_17_moneyOffsets

            elif(category == "HeroMainStat_17"):
                statNames = herostat1List
                statOffsets = save_17_hslListOffsets

            elif(category == "HeroSubStat_17"):
                statNames = herostat2List
                statOffsets = save_17_hs2ListOffsets

            elif(category == "DemonMainStat_17"):
                statNames = demonidstatList
                statOffsets = save_17_disListOffsets

            elif (category == "DemonSubStat_17"):
                statNames = demonstatList
                statOffsets = save_17_dstatsListOffsets

            elif (category == "HeroDemonLevel_17"):
                statNames = herodemonlevelList
                statOffsets = save_17_hdlevelListOffsets

            elif (category == "HeroDemonExp_17"):
                statNames = herodemonexpList
                statOffsets = save_17_hdexpListOffsets

            elif (category == "HeroDemonSkills_17"):
                statNames = herodemonskillList
                statOffsets = save_17_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_17"):
                statNames = herodemonamountList
                statOffsets = save_17_skillamountOffsets

            elif (category == "Items_17"):
                statNames = itemList
                statOffsets = save_17_itemsListOffsets

            elif (category == "Magatamas_17"):
                statNames = magatamaList
                statOffsets = save_17_magatamaListOffsets

            #########################################
            #             Save 18 Offsets           #
            #########################################

            if (category == "HeroMoney_18"):
                statNames = moneyList
                statOffsets = save_18_moneyOffsets

            elif(category == "HeroMainStat_18"):
                statNames = herostat1List
                statOffsets = save_18_hslListOffsets

            elif(category == "HeroSubStat_18"):
                statNames = herostat2List
                statOffsets = save_18_hs2ListOffsets

            elif(category == "DemonMainStat_18"):
                statNames = demonidstatList
                statOffsets = save_18_disListOffsets

            elif (category == "DemonSubStat_18"):
                statNames = demonstatList
                statOffsets = save_18_dstatsListOffsets

            elif (category == "HeroDemonLevel_18"):
                statNames = herodemonlevelList
                statOffsets = save_18_hdlevelListOffsets

            elif (category == "HeroDemonExp_18"):
                statNames = herodemonexpList
                statOffsets = save_18_hdexpListOffsets

            elif (category == "HeroDemonSkills_18"):
                statNames = herodemonskillList
                statOffsets = save_18_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_18"):
                statNames = herodemonamountList
                statOffsets = save_18_skillamountOffsets

            elif (category == "Items_18"):
                statNames = itemList
                statOffsets = save_18_itemsListOffsets

            elif (category == "Magatamas_18"):
                statNames = magatamaList
                statOffsets = save_18_magatamaListOffsets

            #########################################
            #             Save 19 Offsets           #
            #########################################

            if (category == "HeroMoney_19"):
                statNames = moneyList
                statOffsets = save_19_moneyOffsets

            elif (category == "HeroMainStat_19"):
                statNames = herostat1List
                statOffsets = save_19_hslListOffsets

            elif (category == "HeroSubStat_19"):
                statNames = herostat2List
                statOffsets = save_19_hs2ListOffsets

            elif (category == "DemonMainStat_19"):
                statNames = demonidstatList
                statOffsets = save_19_disListOffsets

            elif (category == "DemonSubStat_19"):
                statNames = demonstatList
                statOffsets = save_19_dstatsListOffsets

            elif (category == "HeroDemonLevel_19"):
                statNames = herodemonlevelList
                statOffsets = save_19_hdlevelListOffsets

            elif (category == "HeroDemonExp_19"):
                statNames = herodemonexpList
                statOffsets = save_19_hdexpListOffsets

            elif (category == "HeroDemonSkills_19"):
                statNames = herodemonskillList
                statOffsets = save_19_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_19"):
                statNames = herodemonamountList
                statOffsets = save_19_skillamountOffsets

            elif (category == "Items_19"):
                statNames = itemList
                statOffsets = save_19_itemsListOffsets

            elif (category == "Magatamas_19"):
                statNames = magatamaList
                statOffsets = save_19_magatamaListOffsets

            #########################################
            #             Save 20 Offsets           #
            #########################################

            if (category == "HeroMoney_20"):
                statNames = moneyList
                statOffsets = save_20_moneyOffsets

            elif(category == "HeroMainStat_20"):
                statNames = herostat1List
                statOffsets = save_20_hslListOffsets

            elif(category == "HeroSubStat_20"):
                statNames = herostat2List
                statOffsets = save_20_hs2ListOffsets

            elif(category == "DemonMainStat_20"):
                statNames = demonidstatList
                statOffsets = save_20_disListOffsets

            elif (category == "DemonSubStat_20"):
                statNames = demonstatList
                statOffsets = save_20_dstatsListOffsets

            elif (category == "HeroDemonLevel_20"):
                statNames = herodemonlevelList
                statOffsets = save_20_hdlevelListOffsets

            elif (category == "HeroDemonExp_20"):
                statNames = herodemonexpList
                statOffsets = save_20_hdexpListOffsets

            elif (category == "HeroDemonSkills_20"):
                statNames = herodemonskillList
                statOffsets = save_20_dskillListOffsets

            elif (category == "HeroDemonSkillsAmt_20"):
                statNames = herodemonamountList
                statOffsets = save_20_skillamountOffsets

            elif (category == "Items_20"):
                statNames = itemList
                statOffsets = save_20_itemsListOffsets

            elif (category == "Magatamas_20"):
                statNames = magatamaList
                statOffsets = save_20_magatamaListOffsets

            #######
            self.tableWidget = QTableWidget()
            self.tableWidget.setColumnCount(2)
            if (category == "HeroMoney_1" or category == "HeroMoney_2" or category == "HeroMoney_3" or category == "HeroMoney_4" or category == "HeroMoney_5" or category == "HeroMoney_6" or category == "HeroMoney_7" or category == "HeroMoney_8" or category == "HeroMoney_9" or category == "HeroMoney_10" or category == "HeroMoney_11" or category == "HeroMoney_12" or category == "HeroMoney_13" or category == "HeroMoney_14" or category == "HeroMoney_15" or category == "HeroMoney_16" or category == "HeroMoney_17" or category == "HeroMoney_18" or category == "HeroMoney_19" or category == "HeroMoney_20" or category == "HeroDemonExp_1" or category == "HeroDemonExp_2" or category == "HeroDemonExp_3" or category == "HeroDemonExp_4" or category == "HeroDemonExp_5" or category == "HeroDemonExp_6" or category == "HeroDemonExp_7" or category == "HeroDemonExp_8" or category == "HeroDemonExp_9" or category == "HeroDemonExp_10" or category == "HeroDemonExp_11" or category == "HeroDemonExp_12" or category == "HeroDemonExp_13" or category == "HeroDemonExp_14" or category == "HeroDemonExp_15" or category == "HeroDemonExp_16" or category == "HeroDemonExp_17" or category == "HeroDemonExp_18" or category == "HeroDemonExp_19" or category == "HeroDemonExp_20"):
                self.tableWidget.setRowCount(len(statNames))
                for x in range(len(statOffsets)):
                    self.tableWidget.setItem(x, 0, QTableWidgetItem(statNames[x]))
                    self.tableWidget.setItem(x, 1, QTableWidgetItem(
                        str(self.readFromPosition(statOffsets[x], statOffsets[x] + 4, "<L"))))

            elif (category == "HeroDemonSkills_1" or category == "HeroDemonSkills_2" or category == "HeroDemonSkills_3" or category == "HeroDemonSkills_4" or category == "HeroDemonSkills_5" or category == "HeroDemonSkills_6" or category == "HeroDemonSkills_7" or category == "HeroDemonSkills_8" or category == "HeroDemonSkills_9" or category == "HeroDemonSkills_10" or category == "HeroDemonSkills_11" or category == "HeroDemonSkills_12" or category == "HeroDemonSkills_13" or category == "HeroDemonSkills_14" or category == "HeroDemonSkills_15" or category == "HeroDemonSkills_16" or category == "HeroDemonSkills_17" or category == "HeroDemonSkills_18" or category == "HeroDemonSkills_19" or category == "HeroDemonSkills_20"):
                self.tableWidget.setRowCount(len(statNames))
                for x in range(len(statOffsets)):
                    self.tableWidget.setItem(x, 0, QTableWidgetItem(statNames[x]))
                    self.tableWidget.setItem(x, 1, QTableWidgetItem(
                        str(self.readFromPosition2bytes(statOffsets[x], statOffsets[x] + 2, ">L"))))

            elif(category == "Items_1" or category == "Items_2" or category == "Items_3" or category == "Items_4" or category == "Items_5" or category == "Items_6" or category == "Items_7" or category == "Items_8" or category == "Items_9" or category == "Items_10" or category == "Items_11" or category == "Items_12" or category == "Items_13" or category == "Items_14" or category == "Items_15" or category == "Items_16" or category == "Items_17" or category == "Items_18" or category == "Items_19" or category == "Items_20" or category == "Magatamas_1" or category == "Magatamas_2" or category == "Magatamas_3" or category == "Magatamas_4" or category == "Magatamas_5" or category == "Magatamas_6" or category == "Magatamas_7" or category == "Magatamas_8" or category == "Magatamas_9" or category == "Magatamas_10" or category == "Magatamas_11" or category == "Magatamas_12" or category == "Magatamas_13" or category == "Magatamas_14" or category == "Magatamas_15" or category == "Magatamas_16" or category == "Magatamas_17" or category == "Magatamas_18" or category == "Magatamas_19" or category == "Magatamas_20" or category == "HeroSubStat_1" or category == "HeroSubStat_2" or category == "HeroSubStat_3" or category == "HeroSubStat_4" or category == "HeroSubStat_5" or category == "HeroSubStat_6" or category == "HeroSubStat_7" or category == "HeroSubStat_8" or category == "HeroSubStat_9" or category == "HeroSubStat_10" or category == "HeroSubStat_11" or category == "HeroSubStat_12" or category == "HeroSubStat_13" or category == "HeroSubStat_14" or category == "HeroSubStat_15" or category == "HeroSubStat_16" or category == "HeroSubStat_17" or category == "HeroSubStat_18" or category == "HeroSubStat_19" or category == "HeroSubStat_20" or category == "DemonSubStat_1" or category == "DemonSubStat_2" or category == "DemonSubStat_3" or category == "DemonSubStat_4" or category == "DemonSubStat_5" or category == "DemonSubStat_6" or category == "DemonSubStat_7" or category == "DemonSubStat_8" or category == "DemonSubStat_9" or category == "DemonSubStat_10" or category == "DemonSubStat_11" or category == "DemonSubStat_12" or category == "DemonSubStat_13" or category == "DemonSubStat_14" or category == "DemonSubStat_15" or category == "DemonSubStat_16" or category == "DemonSubStat_17" or category == "DemonSubStat_18" or category == "DemonSubStat_19" or category == "DemonSubStat_20"):
                self.tableWidget.setRowCount(len(statNames))
                for x in range(len(statOffsets)):
                    self.tableWidget.setItem(x, 0, QTableWidgetItem(statNames[x]))
                    self.tableWidget.setItem(x, 1, QTableWidgetItem(
                        str(self.readFromPositionbyte(statOffsets[x], statOffsets[x] + 1, "<L"))))


            elif (category == "HeroDemonSkillsAmt_1" or category == "HeroDemonSkillsAmt_2" or category == "HeroDemonSkillsAmt_3" or category == "HeroDemonSkillsAmt_4" or category == "HeroDemonSkillsAmt_5" or category == "HeroDemonSkillsAmt_6" or category == "HeroDemonSkillsAmt_7" or category == "HeroDemonSkillsAmt_8" or category == "HeroDemonSkillsAmt_9" or category == "HeroDemonSkillsAmt_10" or category == "HeroDemonSkillsAmt_11" or category == "HeroDemonSkillsAmt_12" or category == "HeroDemonSkillsAmt_13" or category == "HeroDemonSkillsAmt_14" or category == "HeroDemonSkillsAmt_15" or category == "HeroDemonSkillsAmt_16" or category == "HeroDemonSkillsAmt_17" or category == "HeroDemonSkillsAmt_18" or category == "HeroDemonSkillsAmt_19" or category == "HeroDemonSkillsAmt_20"):
                self.tableWidget.setRowCount(len(statNames))
                for x in range(len(statOffsets)):
                    self.tableWidget.setItem(x, 0, QTableWidgetItem(statNames[x]))
                    self.tableWidget.setItem(x, 1, QTableWidgetItem(
                        str(self.readFromPositionbyte(statOffsets[x], statOffsets[x] + 1, "<L"))))

            else:
                self.tableWidget.setRowCount(len(statNames))
                for x in range(len(statOffsets)):
                    self.tableWidget.setItem(x, 0, QTableWidgetItem(statNames[x]))
                    self.tableWidget.setItem(x, 1, QTableWidgetItem(
                        str(self.readFromPosition2bytes(statOffsets[x], statOffsets[x] + 2, ">L"))))

            # Money Write (EXP)
            def writeStats():
                for x in range(len(statOffsets)):
                    value = int(self.tableWidget.item(x, 1).text())
                    if (value <= 9999999):
                        self.writeToPosition(value, statOffsets[x], statOffsets[x] + 4, "<L")
                        print(value)

                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("One or more values are too high!")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                        return

                    if (x == len(statOffsets) - 1):
                        statwindow.done(0)

            def write2bytesStats2bytes():
                for x in range(len(statOffsets)):
                    value = int(self.tableWidget.item(x, 1).text())
                    if (value <= 999999):
                        self.writeToPosition(value, statOffsets[x], statOffsets[x] + 1, "<L")
                        print(value)

                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("One or more values are too high!")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                        return

                    if (x == len(statOffsets) - 1):
                        statwindow.done(0)

            def give_items_number():
                # Items
                if (category == "HeroMainStat_1" or category == "HeroMainStat_2" or category == "HeroMainStat_3" or category == "HeroMainStat_4" or category == "HeroMainStat_5" or category == "HeroMainStat_6" or category == "HeroMainStat_7" or category == "HeroMainStat_8" or category == "HeroMainStat_9" or category == "HeroMainStat_10" or category == "HeroMainStat_11" or category == "HeroMainStat_12" or category == "HeroMainStat_13" or category == "HeroMainStat_14" or category == "HeroMainStat_15" or category == "HeroMainStat_16" or category == "HeroMainStat_17" or category == "HeroMainStat_18" or category == "HeroMainStat_19" or category == "HeroMainStat_20"  ):
                    amount, okPressed = QInputDialog.getInt(self, "Items", "Amount:", 0, 0, 0x3E7, 10)
                    if okPressed:
                        for x in range(len(statOffsets)):
                            value = self.tableWidget.item(x, 1).setText(str(amount))

                elif(category == "HeroSubStat_1" or category == "HeroSubStat_2" or category == "HeroSubStat_3" or category == "HeroSubStat_4" or category == "HeroSubStat_5" or category == "HeroSubStat_6" or category == "HeroSubStat_7" or category == "HeroSubStat_8" or category == "HeroSubStat_9" or category == "HeroSubStat_10" or category == "HeroSubStat_11" or category == "HeroSubStat_12" or category == "HeroSubStat_13" or category == "HeroSubStat_14" or category == "HeroSubStat_15" or category == "HeroSubStat_16" or category == "HeroSubStat_17" or category == "HeroSubStat_18" or category == "HeroSubStat_19" or category == "HeroSubStat_20" or category == "DemonSubStat_1" or category == "DemonSubStat_2" or category == "DemonSubStat_3" or category == "DemonSubStat_4" or category == "DemonSubStat_5" or category == "DemonSubStat_6" or category == "DemonSubStat_7" or category == "DemonSubStat_8" or category == "DemonSubStat_9" or category == "DemonSubStat_10" or category == "DemonSubStat_11" or category == "DemonSubStat_12" or category == "DemonSubStat_13" or category == "DemonSubStat_14" or category == "DemonSubStat_15" or category == "DemonSubStat_16" or category == "DemonSubStat_17" or category == "DemonSubStat_18" or category == "DemonSubStat_19" or category == "DemonSubStat_20"):
                    amount, okPressed = QInputDialog.getInt(self, "Items", "Amount:", 0, 0, 0x28, 10)
                    if okPressed:
                        for x in range(len(statOffsets)):
                            value = self.tableWidget.item(x, 1).setText(str(amount))

                elif (category == "HeroDemonSkillsAmt_1" or category == "HeroDemonSkillsAmt_2" or category == "HeroDemonSkillsAmt_3" or category == "HeroDemonSkillsAmt_4" or category == "HeroDemonSkillsAmt_5" or category == "HeroDemonSkillsAmt_6" or category == "HeroDemonSkillsAmt_7" or category == "HeroDemonSkillsAmt_8" or category == "HeroDemonSkillsAmt_9" or category == "HeroDemonSkillsAmt_10" or category == "HeroDemonSkillsAmt_11" or category == "HeroDemonSkillsAmt_12" or category == "HeroDemonSkillsAmt_13" or category == "HeroDemonSkillsAmt_14" or category == "HeroDemonSkillsAmt_15" or category == "HeroDemonSkillsAmt_16" or category == "HeroDemonSkillsAmt_17" or category == "HeroDemonSkillsAmt_18" or category == "HeroDemonSkillsAmt_19" or category == "HeroDemonSkillsAmt_20"):
                    amount, okPressed = QInputDialog.getInt(self, "Items", "Amount:", 0, 0, 0x8, 10)
                    if okPressed:
                        for x in range(len(statOffsets)):
                            value = self.tableWidget.item(x, 1).setText(str(amount))

                elif(category == "Items_1" or category == "Items_2" or category == "Items_3" or category == "Items_4" or category == "Items_5" or category == "Items_6" or category == "Items_7" or category == "Items_8" or category == "Items_9" or category == "Items_10" or category == "Items_11" or category == "Items_12" or category == "Items_13" or category == "Items_14" or category == "Items_15" or category == "Items_16" or category == "Items_17" or category == "Items_18" or category == "Items_19" or category == "Items_20" or category == "HeroDemonLevel_1" or category == "HeroDemonLevel_2" or category == "HeroDemonLevel_3" or category == "HeroDemonLevel_4" or category == "HeroDemonLevel_5" or category == "HeroDemonLevel_6" or category == "HeroDemonLevel_7" or category == "HeroDemonLevel_8" or category == "HeroDemonLevel_9" or category == "HeroDemonLevel_10" or category == "HeroDemonLevel_11" or category == "HeroDemonLevel_12" or category == "HeroDemonLevel_13" or category == "HeroDemonLevel_14" or category == "HeroDemonLevel_15" or category == "HeroDemonLevel_16" or category == "HeroDemonLevel_17" or category == "HeroDemonLevel_18" or category == "HeroDemonLevel_19" or category == "HeroDemonLevel_20"):
                    amount, okPressed = QInputDialog.getInt(self, "Items", "Amount:", 0, 0, 0x63, 10)
                    if okPressed:
                        for x in range(len(statOffsets)):
                            value = self.tableWidget.item(x, 1).setText(str(amount))

            button_save = QPushButton("Save Changes")
            button_give = QPushButton("Give items")
            if (category == "HeroMoney_1" or category == "HeroMoney_2" or category == "HeroMoney_3" or category == "HeroMoney_4" or category == "HeroMoney_5" or category == "HeroMoney_6" or category == "HeroMoney_7" or category == "HeroMoney_8" or category == "HeroMoney_9" or category == "HeroMoney_10" or category == "HeroMoney_11" or category == "HeroMoney_12" or category == "HeroMoney_13" or category == "HeroMoney_14" or category == "HeroMoney_15" or category == "HeroMoney_16" or category == "HeroMoney_17" or category == "HeroMoney_18" or category == "HeroMoney_19" or category == "HeroMoney_20" or category == "HeroDemonExp_1" or category == "HeroDemonExp_2" or category == "HeroDemonExp_3" or category == "HeroDemonExp_4" or category == "HeroDemonExp_5" or category == "HeroDemonExp_6" or category == "HeroDemonExp_7" or category == "HeroDemonExp_8" or category == "HeroDemonExp_9" or category == "HeroDemonExp_10" or category == "HeroDemonExp_11" or category == "HeroDemonExp_12" or category == "HeroDemonExp_13" or category == "HeroDemonExp_14" or category == "HeroDemonExp_15" or category == "HeroDemonExp_16" or category == "HeroDemonExp_17" or category == "HeroDemonExp_18" or category == "HeroDemonExp_19" or category == "HeroDemonExp_20"):
                button_save.clicked.connect(writeStats)

            elif (category == "DemonMainStat_1" or category == "DemonMainStat_2" or category == "DemonMainStat_3" or category == "DemonMainStat_4" or category == "DemonMainStat_5" or category == "DemonMainStat_6" or category == "DemonMainStat_7" or category == "DemonMainStat_8" or category == "DemonMainStat_9" or category == "DemonMainStat_10" or category == "DemonMainStat_11" or category == "DemonMainStat_12" or category == "DemonMainStat_13" or category == "DemonMainStat_14" or category == "DemonMainStat_15" or category == "DemonMainStat_16" or category == "DemonMainStat_17" or category == "DemonMainStat_18" or category == "DemonMainStat_19" or category == "DemonMainStat_20" or category == "HeroMainStat_1" or category == "HeroMainStat_2" or category == "HeroMainStat_3" or category == "HeroMainStat_4" or category == "HeroMainStat_5" or category == "HeroMainStat_6" or category == "HeroMainStat_7" or category == "HeroMainStat_8" or category == "HeroMainStat_9" or category == "HeroMainStat_10" or category == "HeroMainStat_11" or category == "HeroMainStat_12" or category == "HeroMainStat_13" or category == "HeroMainStat_14" or category == "HeroMainStat_15" or category == "HeroMainStat_16" or category == "HeroMainStat_17" or category == "HeroMainStat_18" or category == "HeroMainStat_19" or category == "HeroMainStat_20" or category == "Magatamas_1" or category == "Magatamas_2" or category == "Magatamas_3" or category == "Magatamas_4" or category == "Magatamas_5" or category == "Magatamas_6" or category == "Magatamas_7" or category == "Magatamas_8" or category == "Magatamas_9" or category == "Magatamas_10" or category == "Magatamas_11" or category == "Magatamas_12" or category == "Magatamas_13" or category == "Magatamas_14" or category == "Magatamas_15" or category == "Magatamas_16" or category == "Magatamas_17" or category == "Magatamas_18" or category == "Magatamas_19" or category == "Magatamas_20" or category == "Items_1" or category == "Items_2" or category == "Items_3" or category == "Items_4" or category == "Items_5" or category == "Items_6" or category == "Items_7" or category == "Items_8" or category == "Items_9" or category == "Items_10" or category == "Items_11" or category == "Items_12" or category == "Items_13" or category == "Items_14" or category == "Items_15" or category == "Items_16" or category == "Items_17" or category == "Items_18" or category == "Items_19" or category == "Items_20" or category == "HeroSubStat_1" or category == "HeroSubStat_2" or category == "HeroSubStat_3" or category == "HeroSubStat_4" or category == "HeroSubStat_5" or category == "HeroSubStat_6" or category == "HeroSubStat_7" or category == "HeroSubStat_8" or category == "HeroSubStat_9" or category == "HeroSubStat_10" or category == "HeroSubStat_11" or category == "HeroSubStat_12" or category == "HeroSubStat_13" or category == "HeroSubStat_14" or category == "HeroSubStat_15" or category == "HeroSubStat_16" or category == "HeroSubStat_17" or category == "HeroSubStat_18" or category == "HeroSubStat_19" or category == "HeroSubStat_20" or category == "DemonSubStat_1" or category == "DemonSubStat_2" or category == "DemonSubStat_3" or category == "DemonSubStat_4" or category == "DemonSubStat_5" or category == "DemonSubStat_6" or category == "DemonSubStat_7" or category == "DemonSubStat_8" or category == "DemonSubStat_9" or category == "DemonSubStat_10" or category == "DemonSubStat_11" or category == "DemonSubStat_12" or category == "DemonSubStat_13" or category == "DemonSubStat_14" or category == "DemonSubStat_15" or category == "DemonSubStat_16" or category == "DemonSubStat_17" or category == "DemonSubStat_18" or category == "DemonSubStat_19" or category == "DemonSubStat_20" or category == "Items_1" or category == "Items_2" or category == "Items_3" or category == "Items_4" or category == "Items_5" or category == "Items_6" or category == "Items_7" or category == "Items_8" or category == "Items_9" or category == "Items_10" or category == "Items_11" or category == "Items_12" or category == "Items_13" or category == "Items_14" or category == "Items_15" or category == "Items_16" or category == "Items_17" or category == "Items_18" or category == "Items_19" or category == "Items_20" or category == "HeroDemonLevel_1" or category == "HeroDemonLevel_2" or category == "HeroDemonLevel_3" or category == "HeroDemonLevel_4" or category == "HeroDemonLevel_5" or category == "HeroDemonLevel_6" or category == "HeroDemonLevel_7" or category == "HeroDemonLevel_8" or category == "HeroDemonLevel_9" or category == "HeroDemonLevel_10" or category == "HeroDemonLevel_11" or category == "HeroDemonLevel_12" or category == "HeroDemonLevel_13" or category == "HeroDemonLevel_14" or category == "HeroDemonLevel_15" or category == "HeroDemonLevel_16" or category == "HeroDemonLevel_17" or category == "HeroDemonLevel_18" or category == "HeroDemonLevel_19" or category == "HeroDemonLevel_20"):
                button_save.clicked.connect(writeStats)

            elif (category == "HeroDemonSkills_1" or category == "HeroDemonSkills_2" or category == "HeroDemonSkills_3" or category == "HeroDemonSkills_4" or category == "HeroDemonSkills_5" or category == "HeroDemonSkills_6" or category == "HeroDemonSkills_7" or category == "HeroDemonSkills_8" or category == "HeroDemonSkills_9" or category == "HeroDemonSkills_10" or category == "HeroDemonSkills_11" or category == "HeroDemonSkills_12" or category == "HeroDemonSkills_13" or category == "HeroDemonSkills_14" or category == "HeroDemonSkills_15" or category == "HeroDemonSkills_16" or category == "HeroDemonSkills_17" or category == "HeroDemonSkills_18" or category == "HeroDemonSkills_19" or category == "HeroDemonSkills_20"):
                button_save.clicked.connect(writeStats)

            elif (category == "HeroDemonSkillsAmt_1" or category == "HeroDemonSkillsAmt_2" or category == "HeroDemonSkillsAmt_3" or category == "HeroDemonSkillsAmt_4" or category == "HeroDemonSkillsAmt_5" or category == "HeroDemonSkillsAmt_6" or category == "HeroDemonSkillsAmt_7" or category == "HeroDemonSkillsAmt_8" or category == "HeroDemonSkillsAmt_9" or category == "HeroDemonSkillsAmt_10" or category == "HeroDemonSkillsAmt_11" or category == "HeroDemonSkillsAmt_12" or category == "HeroDemonSkillsAmt_13" or category == "HeroDemonSkillsAmt_14" or category == "HeroDemonSkillsAmt_15" or category == "HeroDemonSkillsAmt_16" or category == "HeroDemonSkillsAmt_17" or category == "HeroDemonSkillsAmt_18" or category == "HeroDemonSkillsAmt_19" or category == "HeroDemonSkillsAmt_20"):
                button_save.clicked.connect(writeStats)

            else:
                button_save.clicked.connect(write2bytesStats2bytes)

            #button_save.clicked.connect(writeStats)

            button_give.clicked.connect(give_items_number)

            button_cancel = QPushButton("Cancel")
            button_cancel.clicked.connect(statwindow.done)
            hbox = QHBoxLayout()
            hbox.addWidget(button_save)
            hbox.addWidget(button_cancel)
            if (category != "HeroMoney_1" and category != "HeroMoney_2" and category != "HeroMoney_3" and category != "HeroMoney_4" and category != "HeroMoney_5" and category != "HeroMoney_6" and category != "HeroMoney_7" and category != "HeroMoney_8" and category != "HeroMoney_9" and category != "HeroMoney_10" and category != "HeroMoney_11" and category != "HeroMoney_12" and category != "HeroMoney_13" and category != "HeroMoney_14" and category != "HeroMoney_15" and category != "HeroMoney_16" and category != "HeroMoney_17" and category != "HeroMoney_18" and category != "HeroMoney_19" and category != "HeroMoney_20" and category != "Magatamas_1" and category != "Magatamas_2" and category != "Magatamas_3" and category != "Magatamas_4" and category != "Magatamas_5" and category != "Magatamas_6" and category != "Magatamas_7" and category != "Magatamas_8" and category != "Magatamas_9" and category != "Magatamas_10" and category != "Magatamas_11" and category != "Magatamas_12" and category != "Magatamas_13" and category != "Magatamas_14" and category != "Magatamas_15" and category != "Magatamas_16" and category != "Magatamas_17" and category != "Magatamas_18" and category != "Magatamas_19" and category != "Magatamas_20" and category != "HeroDemonSkills_1" and category != "HeroDemonSkills_2" and category != "HeroDemonSkills_3" and category != "HeroDemonSkills_4" and category != "HeroDemonSkills_5" and category != "HeroDemonSkills_6" and category != "HeroDemonSkills_7" and category != "HeroDemonSkills_8" and category != "HeroDemonSkills_9" and category != "HeroDemonSkills_10" and category != "HeroDemonSkills_11" and category != "HeroDemonSkills_12" and category != "HeroDemonSkills_13" and category != "HeroDemonSkills_14" and category != "HeroDemonSkills_15" and category != "HeroDemonSkills_16" and category != "HeroDemonSkills_17" and category != "HeroDemonSkills_18" and category != "HeroDemonSkills_19" and category != "HeroDemonSkills_20"):
                hbox.addWidget(button_give)

            self.layout.addLayout(hbox)

            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Value'])
            self.tableWidget.verticalHeader().hide()
            self.tableWidget.setColumnWidth(0, 350)
            self.tableWidget.setColumnWidth(1, 150)
            self.layout.addWidget(self.tableWidget)
            statwindow.setLayout(self.layout)
            statwindow.setWindowModality(Qt.ApplicationModal)
            statwindow.exec_()

    # Read Offset Money, EXP don't touch
    def readFromPosition(self, startOffset, endOffset, type):
        valueToRead = (binascii.unhexlify(h[startOffset * 2:endOffset * 2]))
        valueToRead1 = struct.unpack(type, valueToRead)
        valueToRead2 = functools.reduce(lambda rst, d: rst * 10 + d, (valueToRead1))
        return valueToRead2

    # SUBs don't touch
    def readFromPosition2bytes(self, startOffset, endOffset, type):
        valueToRead = (binascii.unhexlify(h[startOffset * 2:endOffset * 2]))
        reverseval = bytes([c for t in zip(valueToRead[1::2], valueToRead[::2]) for c in t])
        valueToRead1 = binascii.hexlify(reverseval)
        valueToRead2 = int(valueToRead1, 16)
        return valueToRead2

    # Skills don't touch
    def readFromPositionskill(self, startOffset, endOffset, type):
        valueToRead = (binascii.unhexlify(h[startOffset * 2:endOffset * 2]))
        print(valueToRead)
        valueToRead1 = binascii.hexlify(valueToRead)
        valueToRead2 = int(valueToRead1, 16)
        return valueToRead2

    # Items don't touch
    def readFromPositionbyte(self, startOffset, endOffset, type):
        valueToRead = (binascii.unhexlify(h[startOffset * 2:endOffset * 2]))
        valueToRead1 = binascii.hexlify(valueToRead)
        valueToRead2 = int(valueToRead1, 16)
        return valueToRead2

    # Write to Save Values
    def writeToPosition(self, value, startOffset, endOffset, type):
        global h
        valueToWrite = binascii.hexlify(struct.pack(type, value))
        h = h[:startOffset * 2] + valueToWrite + h[endOffset * 2:]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    if (sys.platform.startswith('linux')):
        font = app.font()
        font.setPointSize(9)
        app.setFont(font)
    ex = ShinApp()
    sys.exit(app.exec_())