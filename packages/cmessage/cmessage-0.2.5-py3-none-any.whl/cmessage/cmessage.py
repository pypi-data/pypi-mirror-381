import ctypes

# ------------------------
# BUTTON FLAGS
# ------------------------
MB_OK = 0x0
MB_OKCANCEL = 0x1
MB_ABORTRETRYIGNORE = 0x2
MB_YESNOCANCEL = 0x3
MB_YESNO = 0x4
MB_RETRYCANCEL = 0x5
MB_CANCELTRYCONTINUE = 0x6

# ------------------------
# RETURN VALUES
# ------------------------
IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDRETRY = 4
IDIGNORE = 5
IDYES = 6
IDNO = 7
IDTRYAGAIN = 10
IDCONTINUE = 11

# ------------------------
# ICONS
# ------------------------




class CMessage:
    ICON_NONE = 0x0
    ICON_ERROR = 0x10
    ICON_QUESTION = 0x20
    ICON_WARNING = 0x30
    ICON_INFO = 0x40
    def __init__(self):
        self.user32 = ctypes.windll.user32

    # ------------------------
    # Simple OK
    # ------------------------
    class Message:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedok=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_OK | icon_flag
            )
            if result == IDOK and pressedok:
                pressedok()
            return result

    # ------------------------
    # Yes / No
    # ------------------------
    class MessageYesNo:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedyes=None, pressedno=None, icon_flag=None):
            if icon_flag is None:
                icon_flag = CMessage.ICON_NONE  # domyślna wartość zamiast None
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_YESNO | icon_flag
            )

            if result == IDYES and pressedyes:
                pressedyes()
            elif result == IDNO and pressedno:
                pressedno()
            return result

    # ------------------------
    # OK / Cancel
    # ------------------------
    class MessageOkCancel:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedok=None, pressedcancel=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_OKCANCEL | icon_flag
            )
            if result == IDOK and pressedok:
                pressedok()
            elif result == IDCANCEL and pressedcancel:
                pressedcancel()
            return result

    # ------------------------
    # Retry / Cancel
    # ------------------------
    class MessageRetryCancel:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedretry=None, pressedcancel=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_RETRYCANCEL | icon_flag
            )
            if result == IDRETRY and pressedretry:
                pressedretry()
            elif result == IDCANCEL and pressedcancel:
                pressedcancel()
            return result

    # ------------------------
    # Abort / Retry / Ignore
    # ------------------------
    class MessageAbortRetryIgnore:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedabort=None, pressedretry=None, pressedignore=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_ABORTRETRYIGNORE | icon_flag
            )
            if result == IDABORT and pressedabort:
                pressedabort()
            elif result == IDRETRY and pressedretry:
                pressedretry()
            elif result == IDIGNORE and pressedignore:
                pressedignore()
            return result

    # ------------------------
    # Yes / No / Cancel
    # ------------------------
    class MessageYesNoCancel:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedyes=None, pressedno=None, pressedcancel=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_YESNOCANCEL | icon_flag
            )
            if result == IDYES and pressedyes:
                pressedyes()
            elif result == IDNO and pressedno:
                pressedno()
            elif result == IDCANCEL and pressedcancel:
                pressedcancel()
            return result

    # ------------------------
    # Cancel / Try Again / Continue
    # ------------------------
    class MessageCancelTryContinue:
        def __init__(self, parent=None):
            self.parent = parent if parent else 0

        def Show(self, title, text, pressedcancel=None, pressedtryagain=None, pressedcontinue=None, icon_flag=None):
            result = ctypes.windll.user32.MessageBoxW(
                self.parent, text, title, MB_CANCELTRYCONTINUE | icon_flag
            )
            if result == IDCANCEL and pressedcancel:
                pressedcancel()
            elif result == IDTRYAGAIN and pressedtryagain:
                pressedtryagain()
            elif result == IDCONTINUE and pressedcontinue:
                pressedcontinue()
            return result
