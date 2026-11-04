from enum import Enum


class EventType(str, Enum):
    ALL = "All"
    AUTHEXPIRED = "AuthExpired"
    CHATUPDATE = "ChatUpdate"
    CONNECTED = "Connected"
    CONTACTUPDATE = "ContactUpdate"
    DISCONNECTED = "Disconnected"
    FILEREADY = "FileReady"
    HISTORYSYNC = "HistorySync"
    LOGGEDOUT = "LoggedOut"
    MESSAGE = "Message"
    MESSAGEDELETE = "MessageDelete"
    MESSAGEEDIT = "MessageEdit"
    PRESENCEUPDATE = "PresenceUpdate"
    QRAUTHORIZED = "QRAuthorized"
    QREXPIRED = "QRExpired"
    QRGENERATED = "QRGenerated"
    QRSCANNED = "QRScanned"
    REACTIONCHANGE = "ReactionChange"
    READRECEIPT = "ReadReceipt"
    RECONNECTEXHAUSTED = "ReconnectExhausted"
    RECONNECTING = "Reconnecting"
    SYNC = "Sync"
    TYPING = "Typing"

    def __str__(self) -> str:
        return str(self.value)
