import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QToolBar, QTabWidget, QPushButton
)
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage


# App Start
app = QApplication(sys.argv)


# Set Profile
profile = QWebEngineProfile("Default Profile")

profile.setPersistentStoragePath(
    "/home/Your Path Here/browser_profile"
)
profile.setCachePath(
    "/home/Your Path Here/browser_cache"
)

profile.setPersistentCookiesPolicy(
    QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
)


class BrowserTab(QWebEngineView):
    def __init__(self, profile):
        super().__init__()

        # 🔗 WICHTIG: eigenes Profil nutzen
        self.page = QWebEnginePage(profile, self)
        self.setPage(self.page)


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TB Browser")
        self.setGeometry(100, 100, 1200, 800)

        # 📑 Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)
        self.setCentralWidget(self.tabs)

        # Toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back
        back_btn = QPushButton("←")
        back_btn.clicked.connect(self.go_back)
        navbar.addWidget(back_btn)

        # Forward
        forward_btn = QPushButton("→")
        forward_btn.clicked.connect(self.go_forward)
        navbar.addWidget(forward_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Reload
        reload_btn = QPushButton("⟳")
        reload_btn.clicked.connect(self.reload_page)
        navbar.addWidget(reload_btn)

        # New Tab
        new_tab_btn = QPushButton("+ Tab")
        new_tab_btn.clicked.connect(
            lambda: self.add_new_tab("https://duckduckgo.com")
        )
        navbar.addWidget(new_tab_btn)

        # First Tab at Start
        self.add_new_tab("https://duckduckgo.com")

    # Create Tab
    def add_new_tab(self, url):
        browser = BrowserTab(profile)

        browser.setUrl(QUrl(url))

        i = self.tabs.addTab(browser, "New Tab")
        browser.titleChanged.connect(
        lambda title, browser=browser: self.update_tab_title(browser, title)
)

        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(self.update_url_from_browser)

    # Close Tab
    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    # Navigation
    def navigate_to_url(self):
        url = self.url_bar.text()

        if not url.startswith("http"):
            url = "https://" + url

        self.tabs.currentWidget().setUrl(QUrl(url))
    
    

    # Reload
    def reload_page(self):
        self.tabs.currentWidget().reload()

    # URL Bar sync
    def update_url_bar(self, i):
        browser = self.tabs.widget(i)
        if browser:
            self.url_bar.setText(browser.url().toString())

    # URL update from page
    def update_url_from_browser(self, q):
        self.url_bar.setText(q.toString())
    
    # Titel Update
    def update_tab_title(self, browser, title):
        index = self.tabs.indexOf(browser)

        if index != -1:
            self.tabs.setTabText(index, title)

    # Back
    def go_back(self):
        self.tabs.currentWidget().back()
 
    # Forward
    def go_forward(self):
        self.tabs.currentWidget().forward()


# Start Window
window = Browser()
window.show()

sys.exit(app.exec())
