import sys, os

sys.path.insert(0, os.getcwd())
from datetime import datetime
from PIL import Image
import time
import random
import base64
from io import BytesIO
from neonize.client import NewClient
from neonize.proto.def_pb2 import (
    Message,
    ImageMessage,
    ContextInfo,
    ExtendedTextMessage,
    StickerMessage,
    Chat,
    VideoMessage,
)
from neonize.proto.Neonize_pb2 import Message as MessageResponse, MessageInfo, JID, PairStatus
from neonize.utils import Jid2String, MediaType
from neonize.utils import ChatPresence, ChatPresenceMedia
from neonize.utils import LogLevel, ReceiptType
import magic
import time
import segno

def onQr(client: NewClient, data_qr: bytes):
    segno.make_qr(data_qr).terminal()

client = NewClient("krypton.so", qrCallback=onQr)

@client.event(MessageResponse)
def onMessage(client: NewClient, message: MessageResponse):
    text = message.Message.conversation or message.Message.extendedTextMessage.text
    chat = message.Info.MessageSource.Chat
    match text:
        case "ping":
            client.send_message(chat, "pong")
        case "sticker":
            client.send_sticker(chat, "/home/krypton-byte/Downloads/5b231c4cdac4c254142ff.png")
        case "debug":
            client.send_message(chat, message.__str__())
        case "viewonce":
            upload = client.upload(open("/home/krypton-byte/Downloads/5b231c4cdac4c254142ff.png", "rb").read())
            client.send_message(
                chat,
                Message(
                    imageMessage=ImageMessage(
                        url=upload.url,
                        caption="CAPTION",
                        directPath=upload.DirectPath,
                        fileEncSha256=upload.FileEncSHA256,
                        fileLength=upload.FileLength,
                        fileSha256=upload.FileSHA256,
                        jpegThumbnail=open("/home/krypton-byte/Downloads/5b231c4cdac4c254142ff.png","rb").read(),
                        mediaKey=upload.MediaKey,
                        mimetype=magic.from_file("/home/krypton-byte/Downloads/5b231c4cdac4c254142ff.png", mime=True),
                        thumbnailDirectPath=upload.DirectPath,
                        thumbnailEncSha256=upload.FileEncSHA256,
                        thumbnailSha256=upload.FileSHA256,
                        viewOnce=True
                    )
                )
            )
        case "profile_pict":
            client.send_message(chat, client.get_profile_picture(chat).__str__())
        case "status_privacy":
            client.send_message(chat, client.get_status_privacy().__str__())
        case "read":
            client.send_message(chat, client.mark_read([message.Info.ID], message.Info.MessageSource.Chat, message.Info.MessageSource.Sender, ReceiptType.READ).__str__())
        case "read_channel":
            metadata = client.get_newsletter_info_with_invite("https://whatsapp.com/channel/0029Va4K0PZ5a245NkngBA2M")
            err=client.follow_newsletter(metadata.ID)
            client.send_message(chat, 'error: '+err)
            resp=client.newsletter_mark_viewed(metadata.ID, [0])
            client.send_message(chat, resp.__str__() +'\n'+ metadata.__str__())
        case "keluar":
            client.logout()
        case "send_react_channel":
            metadata = client.get_newsletter_info_with_invite("https://whatsapp.com/channel/0029Va4K0PZ5a245NkngBA2M")
            data_msg = client.get_newsletter_messages(metadata.ID, 2, 0)
            client.send_message(chat, data_msg.__str__())
            for data in data_msg:
                client.newsletter_send_reaction(metadata.ID, data.MessageServerID, "🗿", data.Message.ID)
        case "subscribe_channel_updates":
            metadata = client.get_newsletter_info_with_invite("https://whatsapp.com/channel/0029Va4K0PZ5a245NkngBA2M")
            result = client.newsletter_subscribe_live_updates(metadata.ID)
            client.send_message(chat, result.__str__())
@client.event(PairStatus)
def PairStatusMessage(client: NewClient, message: PairStatus):
    print(client, message)

client.connect(log_level=LogLevel.INFO)
