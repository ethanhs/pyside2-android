
'''Tests for QKeyEvent'''

import unittest

from PySide2.QtCore import Qt, QObject, QEvent
from PySide2.QtGui import QKeyEvent
from PySide2.QtWidgets import QLineEdit
from PySide2.QtTest import QTest

from helper import UsesQApplication


class KeyEventFilter(QObject):

    def __init__(self, widget, eventType, key):
        QObject.__init__(self)

        self.widget = widget
        self.eventType = eventType
        self.key = key

        self.processed = False

    def eventFilter(self, obj, event):
        if self.widget == obj and event.type() == self.eventType and \
               isinstance(event, QKeyEvent) and event.key() == self.key:
            self.processed = True
            return True

        return False

class EventFilterTest(UsesQApplication):

    def testKeyEvent(self):
        widget = QLineEdit()
        key = Qt.Key_A
        eventFilter = KeyEventFilter(widget, QEvent.KeyPress, key)
        widget.installEventFilter(eventFilter)

        QTest.keyClick(widget, key)

        self.assert_(eventFilter.processed)



if __name__ == '__main__':
    unittest.main()
