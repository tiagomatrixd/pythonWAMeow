# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Neonize.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import def_pb2 as def__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rNeonize.proto\x12\x07neonize\x1a\tdef.proto\"j\n\x03JID\x12\x0c\n\x04User\x18\x01 \x02(\t\x12\x10\n\x08RawAgent\x18\x02 \x02(\r\x12\x0e\n\x06\x44\x65vice\x18\x03 \x02(\r\x12\x12\n\nIntegrator\x18\x04 \x02(\r\x12\x0e\n\x06Server\x18\x05 \x02(\t\x12\x0f\n\x07IsEmpty\x18\x06 \x02(\x08\"\xb1\x02\n\x0bMessageInfo\x12-\n\rMessageSource\x18\x01 \x02(\x0b\x32\x16.neonize.MessageSource\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x10\n\x08ServerID\x18\x03 \x02(\x03\x12\x0c\n\x04Type\x18\x04 \x02(\t\x12\x10\n\x08Pushname\x18\x05 \x02(\t\x12\x11\n\tTimestamp\x18\x06 \x02(\x03\x12\x10\n\x08\x43\x61tegory\x18\x07 \x02(\t\x12\x11\n\tMulticast\x18\x08 \x02(\x08\x12\x11\n\tMediaType\x18\t \x02(\t\x12\x0c\n\x04\x45\x64it\x18\n \x02(\t\x12+\n\x0cVerifiedName\x18\x0b \x01(\x0b\x32\x15.neonize.VerifiedName\x12/\n\x0e\x44\x65viceSentMeta\x18\x0c \x01(\x0b\x32\x17.neonize.DeviceSentMeta\"\x92\x01\n\x0eUploadResponse\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x12\n\nDirectPath\x18\x02 \x02(\t\x12\x0e\n\x06Handle\x18\x03 \x02(\t\x12\x10\n\x08MediaKey\x18\x04 \x02(\x0c\x12\x15\n\rFileEncSHA256\x18\x05 \x02(\x0c\x12\x12\n\nFileSHA256\x18\x06 \x02(\x0c\x12\x12\n\nFileLength\x18\x07 \x02(\r\"\x96\x01\n\rMessageSource\x12\x1a\n\x04\x43hat\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x1c\n\x06Sender\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x10\n\x08IsFromMe\x18\x03 \x02(\x08\x12\x0f\n\x07IsGroup\x18\x04 \x02(\x08\x12(\n\x12\x42roadcastListOwner\x18\x05 \x02(\x0b\x32\x0c.neonize.JID\"7\n\x0e\x44\x65viceSentMeta\x12\x16\n\x0e\x44\x65stinationJID\x18\x01 \x02(\t\x12\r\n\x05Phash\x18\x02 \x02(\t\"\x82\x01\n\x0cVerifiedName\x12\x36\n\x0b\x43\x65rtificate\x18\x01 \x01(\x0b\x32!.defproto.VerifiedNameCertificate\x12:\n\x07\x44\x65tails\x18\x02 \x01(\x0b\x32).defproto.VerifiedNameCertificate.Details\"{\n\x14IsOnWhatsAppResponse\x12\r\n\x05Query\x18\x01 \x02(\t\x12\x19\n\x03JID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x0c\n\x04IsIn\x18\x03 \x02(\x08\x12+\n\x0cVerifiedName\x18\x04 \x01(\x0b\x32\x15.neonize.VerifiedName\"y\n\x08UserInfo\x12+\n\x0cVerifiedName\x18\x01 \x01(\x0b\x32\x15.neonize.VerifiedName\x12\x0e\n\x06Status\x18\x02 \x02(\t\x12\x11\n\tPictureID\x18\x03 \x02(\t\x12\x1d\n\x07\x44\x65vices\x18\x04 \x03(\x0b\x32\x0c.neonize.JID\"s\n\x06\x44\x65vice\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12\x10\n\x08Platform\x18\x02 \x02(\t\x12\x15\n\rBussinessName\x18\x03 \x02(\t\x12\x10\n\x08PushName\x18\x04 \x02(\t\x12\x13\n\x0bInitialized\x18\x05 \x02(\x08\"M\n\tGroupName\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x11\n\tNameSetAt\x18\x02 \x02(\x03\x12\x1f\n\tNameSetBy\x18\x03 \x02(\x0b\x32\x0c.neonize.JID\"x\n\nGroupTopic\x12\r\n\x05Topic\x18\x01 \x02(\t\x12\x0f\n\x07TopicID\x18\x02 \x02(\t\x12\x12\n\nTopicSetAt\x18\x03 \x02(\x03\x12 \n\nTopicSetBy\x18\x04 \x02(\x0b\x32\x0c.neonize.JID\x12\x14\n\x0cTopicDeleted\x18\x05 \x02(\x08\"\x1f\n\x0bGroupLocked\x12\x10\n\x08isLocked\x18\x01 \x02(\x08\">\n\rGroupAnnounce\x12\x12\n\nIsAnnounce\x18\x01 \x02(\x08\x12\x19\n\x11\x41nnounceVersionID\x18\x02 \x02(\t\"@\n\x0eGroupEphemeral\x12\x13\n\x0bIsEphemeral\x18\x01 \x02(\x08\x12\x19\n\x11\x44isappearingTimer\x18\x02 \x02(\r\"%\n\x0eGroupIncognito\x12\x13\n\x0bIsIncognito\x18\x01 \x02(\x08\"F\n\x0bGroupParent\x12\x10\n\x08IsParent\x18\x01 \x02(\x08\x12%\n\x1d\x44\x65\x66\x61ultMembershipApprovalMode\x18\x02 \x02(\t\":\n\x11GroupLinkedParent\x12%\n\x0fLinkedParentJID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\".\n\x11GroupIsDefaultSub\x12\x19\n\x11IsDefaultSubGroup\x18\x01 \x02(\x08\">\n\x1aGroupParticipantAddRequest\x12\x0c\n\x04\x43ode\x18\x01 \x02(\t\x12\x12\n\nExpiration\x18\x02 \x02(\x02\"\xcc\x01\n\x10GroupParticipant\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12\x19\n\x03LID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x0f\n\x07IsAdmin\x18\x03 \x02(\x08\x12\x14\n\x0cIsSuperAdmin\x18\x04 \x02(\x08\x12\x13\n\x0b\x44isplayName\x18\x05 \x02(\t\x12\r\n\x05\x45rror\x18\x06 \x02(\x05\x12\x37\n\nAddRequest\x18\x07 \x01(\x0b\x32#.neonize.GroupParticipantAddRequest\"\x83\x05\n\tGroupInfo\x12\x1e\n\x08OwnerJID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12%\n\tGroupName\x18\x03 \x02(\x0b\x32\x12.neonize.GroupName\x12\'\n\nGroupTopic\x18\x04 \x02(\x0b\x32\x13.neonize.GroupTopic\x12)\n\x0bGroupLocked\x18\x05 \x02(\x0b\x32\x14.neonize.GroupLocked\x12-\n\rGroupAnnounce\x18\x06 \x02(\x0b\x32\x16.neonize.GroupAnnounce\x12/\n\x0eGroupEphemeral\x18\x07 \x02(\x0b\x32\x17.neonize.GroupEphemeral\x12/\n\x0eGroupIncognito\x18\x08 \x02(\x0b\x32\x17.neonize.GroupIncognito\x12)\n\x0bGroupParent\x18\t \x02(\x0b\x32\x14.neonize.GroupParent\x12\x35\n\x11GroupLinkedParent\x18\n \x02(\x0b\x32\x1a.neonize.GroupLinkedParent\x12\x35\n\x11GroupIsDefaultSub\x18\x0b \x02(\x0b\x32\x1a.neonize.GroupIsDefaultSub\x12\x14\n\x0cGroupCreated\x18\x0c \x02(\x02\x12\x1c\n\x14ParticipantVersionID\x18\r \x02(\t\x12/\n\x0cParticipants\x18\x0e \x03(\x0b\x32\x19.neonize.GroupParticipant\"1\n\x12GroupMemberAddMode\x12\x1b\n\x17GroupMemberAddModeAdmin\x10\x01\"\xb8\x01\n\x13MessageDebugTimings\x12\r\n\x05Queue\x18\x01 \x02(\x03\x12\x0f\n\x07Marshal\x18\x02 \x02(\x03\x12\x17\n\x0fGetParticipants\x18\x03 \x02(\x03\x12\x12\n\nGetDevices\x18\x04 \x02(\x03\x12\x14\n\x0cGroupEncrypt\x18\x05 \x02(\x03\x12\x13\n\x0bPeerEncrypt\x18\x06 \x02(\x03\x12\x0c\n\x04Send\x18\x07 \x02(\x03\x12\x0c\n\x04Resp\x18\x08 \x02(\x03\x12\r\n\x05Retry\x18\t \x02(\x03\"s\n\x0cSendResponse\x12\x11\n\tTimestamp\x18\x01 \x02(\x03\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x10\n\x08ServerID\x18\x03 \x02(\x03\x12\x32\n\x0c\x44\x65\x62ugTimings\x18\x04 \x02(\x0b\x32\x1c.neonize.MessageDebugTimings\"W\n\x19SendMessageReturnFunction\x12\r\n\x05\x45rror\x18\x01 \x01(\t\x12+\n\x0cSendResponse\x18\x02 \x01(\x0b\x32\x15.neonize.SendResponse\"R\n\x1aGetGroupInfoReturnFunction\x12%\n\tGroupInfo\x18\x01 \x01(\x0b\x32\x12.neonize.GroupInfo\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"K\n\x1fJoinGroupWithLinkReturnFunction\x12\r\n\x05\x45rror\x18\x01 \x01(\t\x12\x19\n\x03Jid\x18\x02 \x01(\x0b\x32\x0c.neonize.JID\"E\n GetGroupInviteLinkReturnFunction\x12\x12\n\nInviteLink\x18\x01 \x01(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"7\n\x16\x44ownloadReturnFunction\x12\x0e\n\x06\x42inary\x18\x01 \x01(\x0c\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"V\n\x14UploadReturnFunction\x12/\n\x0eUploadResponse\x18\x01 \x01(\x0b\x32\x17.neonize.UploadResponse\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"?\n\x1bSetGroupPhotoReturnFunction\x12\x11\n\tPictureID\x18\x01 \x02(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"h\n\x1aIsOnWhatsAppReturnFunction\x12;\n\x14IsOnWhatsAppResponse\x18\x01 \x03(\x0b\x32\x1d.neonize.IsOnWhatsAppResponse\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"a\n\x1fGetUserInfoSingleReturnFunction\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12#\n\x08UserInfo\x18\x02 \x01(\x0b\x32\x11.neonize.UserInfo\"g\n\x19GetUserInfoReturnFunction\x12;\n\tUsersInfo\x18\x01 \x03(\x0b\x32(.neonize.GetUserInfoSingleReturnFunction\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"Q\n\x1b\x42uildPollVoteReturnFunction\x12#\n\x08PollVote\x18\x01 \x01(\x0b\x32\x11.defproto.Message\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"h\n\x1e\x43reateNewsLetterReturnFunction\x12\x37\n\x12NewsletterMetadata\x18\x01 \x01(\x0b\x32\x1b.neonize.NewsletterMetadata\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"R\n\x1aGetBlocklistReturnFunction\x12%\n\tBlocklist\x18\x01 \x01(\x0b\x32\x12.neonize.Blocklist\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"=\n\x1eGetContactQRLinkReturnFunction\x12\x0c\n\x04Link\x18\x01 \x02(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"^\n)GetGroupRequestParticipantsReturnFunction\x12\"\n\x0cParticipants\x18\x01 \x03(\x0b\x32\x0c.neonize.JID\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"Q\n\x1dGetJoinedGroupsReturnFunction\x12!\n\x05Group\x18\x01 \x03(\x0b\x32\x12.neonize.GroupInfo\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xb7\x01\n\x0eReqCreateGroup\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\"\n\x0cParticipants\x18\x02 \x03(\x0b\x32\x0c.neonize.JID\x12\x11\n\tCreateKey\x18\x03 \x02(\t\x12)\n\x0bGroupParent\x18\x04 \x01(\x0b\x32\x14.neonize.GroupParent\x12\x35\n\x11GroupLinkedParent\x18\x05 \x01(\x0b\x32\x1a.neonize.GroupLinkedParent\"&\n\x08JIDArray\x12\x1a\n\x04JIDS\x18\x01 \x03(\x0b\x32\x0c.neonize.JID\"\x1b\n\x0b\x41rrayString\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\";\n\x15NewsLetterMessageMeta\x12\x0e\n\x06\x45\x64itTS\x18\x01 \x02(\x03\x12\x12\n\nOriginalTS\x18\x02 \x02(\x03\"\xba\x02\n\x07Message\x12\"\n\x04Info\x18\x01 \x02(\x0b\x32\x14.neonize.MessageInfo\x12\"\n\x07Message\x18\x02 \x01(\x0b\x32\x11.defproto.Message\x12\x13\n\x0bIsEphemeral\x18\x03 \x02(\x08\x12\x12\n\nIsViewOnce\x18\x04 \x02(\x08\x12\x14\n\x0cIsViewOnceV2\x18\x05 \x02(\x08\x12\x0e\n\x06IsEdit\x18\x06 \x02(\x08\x12.\n\x0cSourceWebMsg\x18\x07 \x01(\x0b\x32\x18.defproto.WebMessageInfo\x12\x1c\n\x14UnavailableRequestID\x18\x08 \x02(\t\x12\x12\n\nRetryCount\x18\t \x02(\x03\x12\x36\n\x0eNewsLetterMeta\x18\n \x01(\x0b\x32\x1e.neonize.NewsLetterMessageMeta\"L\n\x16\x43reateNewsletterParams\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x13\n\x0b\x44\x65scription\x18\x02 \x02(\t\x12\x0f\n\x07Picture\x18\x03 \x02(\x0c\"\x97\x01\n\x16WrappedNewsletterState\x12=\n\x04Type\x18\x01 \x02(\x0e\x32/.neonize.WrappedNewsletterState.NewsletterState\">\n\x0fNewsletterState\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tSUSPENDED\x10\x02\x12\x10\n\x0cGEOSUSPENDED\x10\x03\">\n\x0eNewsletterText\x12\x0c\n\x04Text\x18\x01 \x02(\t\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x12\n\nUpdateTime\x18\x03 \x02(\x03\"O\n\x12ProfilePictureInfo\x12\x0b\n\x03URL\x18\x01 \x02(\t\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x0c\n\x04Type\x18\x03 \x02(\t\x12\x12\n\nDirectPath\x18\x04 \x02(\t\"\xb0\x01\n\x1aNewsletterReactionSettings\x12J\n\x05Value\x18\x01 \x02(\x0e\x32;.neonize.NewsletterReactionSettings.NewsletterReactionsMode\"F\n\x17NewsletterReactionsMode\x12\x07\n\x03\x41LL\x10\x01\x12\t\n\x05\x42\x41SIC\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\r\n\tBLOCKLIST\x10\x04\"O\n\x11NewsletterSetting\x12:\n\rReactionCodes\x18\x01 \x02(\x0b\x32#.neonize.NewsletterReactionSettings\"\xd3\x03\n\x18NewsletterThreadMetadata\x12\x14\n\x0c\x43reationTime\x18\x01 \x02(\x03\x12\x12\n\nInviteCode\x18\x02 \x02(\t\x12%\n\x04Name\x18\x03 \x02(\x0b\x32\x17.neonize.NewsletterText\x12,\n\x0b\x44\x65scription\x18\x04 \x02(\x0b\x32\x17.neonize.NewsletterText\x12\x17\n\x0fSubscriberCount\x18\x05 \x02(\x03\x12X\n\x11VerificationState\x18\x06 \x02(\x0e\x32=.neonize.NewsletterThreadMetadata.NewsletterVerificationState\x12,\n\x07Picture\x18\x07 \x01(\x0b\x32\x1b.neonize.ProfilePictureInfo\x12,\n\x07Preview\x18\x08 \x02(\x0b\x32\x1b.neonize.ProfilePictureInfo\x12,\n\x08Settings\x18\t \x02(\x0b\x32\x1a.neonize.NewsletterSetting\";\n\x1bNewsletterVerificationState\x12\x0c\n\x08VERIFIED\x10\x01\x12\x0e\n\nUNVERIFIED\x10\x02\"m\n\x18NewsletterViewerMetadata\x12*\n\x04Mute\x18\x01 \x02(\x0e\x32\x1c.neonize.NewsletterMuteState\x12%\n\x04Role\x18\x02 \x02(\x0e\x32\x17.neonize.NewsletterRole\"\xcc\x01\n\x12NewsletterMetadata\x12\x18\n\x02ID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12.\n\x05State\x18\x02 \x02(\x0b\x32\x1f.neonize.WrappedNewsletterState\x12\x35\n\nThreadMeta\x18\x03 \x02(\x0b\x32!.neonize.NewsletterThreadMetadata\x12\x35\n\nViewerMeta\x18\x04 \x01(\x0b\x32!.neonize.NewsletterViewerMetadata\"6\n\tBlocklist\x12\r\n\x05\x44Hash\x18\x01 \x02(\t\x12\x1a\n\x04JIDs\x18\x02 \x03(\x0b\x32\x0c.neonize.JID\"\'\n\x08Reaction\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\x03\"\x8f\x01\n\x11NewsletterMessage\x12\x17\n\x0fMessageServerID\x18\x01 \x02(\x03\x12\x12\n\nViewsCount\x18\x02 \x02(\x03\x12)\n\x0eReactionCounts\x18\x03 \x03(\x0b\x32\x11.neonize.Reaction\x12\"\n\x07Message\x18\x04 \x02(\x0b\x32\x11.defproto.Message\"p\n(GetNewsletterMessageUpdateReturnFunction\x12\x35\n\x11NewsletterMessage\x18\x01 \x03(\x0b\x32\x1a.neonize.NewsletterMessage\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xa5\x04\n\x0fPrivacySettings\x12\x39\n\x08GroupAdd\x18\x01 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x39\n\x08LastSeen\x18\x02 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x37\n\x06Status\x18\x03 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x38\n\x07Profile\x18\x04 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12=\n\x0cReadReceipts\x18\x05 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x38\n\x07\x43\x61llAdd\x18\x06 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x37\n\x06Online\x18\x07 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\"w\n\x0ePrivacySetting\x12\r\n\tUNDEFINED\x10\x01\x12\x07\n\x03\x41LL\x10\x02\x12\x0c\n\x08\x43ONTACTS\x10\x03\x12\x15\n\x11\x43ONTACT_BLACKLIST\x10\x04\x12\x13\n\x0fMATCH_LAST_SEEN\x10\x05\x12\t\n\x05KNOWN\x10\x06\x12\x08\n\x04NONE\x10\x07\"(\n\tNodeAttrs\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"V\n\x04Node\x12\x0b\n\x03Tag\x18\x01 \x02(\t\x12!\n\x05\x41ttrs\x18\x02 \x03(\x0b\x32\x12.neonize.NodeAttrs\x12\x1e\n\x07\x43ontent\x18\x03 \x03(\x0b\x32\r.neonize.Node\"X\n\tInfoQuery\x12\x11\n\tNamespace\x18\x01 \x02(\t\x12\x0c\n\x04Type\x18\x02 \x02(\t\x12\n\n\x02To\x18\x03 \x02(\t\x12\x1e\n\x07\x43ontent\x18\x04 \x03(\x0b\x32\r.neonize.Node\"S\n\x17GetProfilePictureParams\x12\x0f\n\x07Preview\x18\x01 \x01(\x08\x12\x12\n\nExistingID\x18\x02 \x01(\t\x12\x13\n\x0bIsCommunity\x18\x03 \x01(\x08\"^\n\x1fGetProfilePictureReturnFunction\x12,\n\x07Picture\x18\x01 \x01(\x0b\x32\x1b.neonize.ProfilePictureInfo\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xb7\x01\n\rStatusPrivacy\x12\x36\n\x04Type\x18\x01 \x02(\x0e\x32(.neonize.StatusPrivacy.StatusPrivacyType\x12\x1a\n\x04List\x18\x02 \x03(\x0b\x32\x0c.neonize.JID\x12\x11\n\tIsDefault\x18\x03 \x02(\x08\"?\n\x11StatusPrivacyType\x12\x0c\n\x08\x43ONTACTS\x10\x01\x12\r\n\tBLACKLIST\x10\x02\x12\r\n\tWHITELIST\x10\x03\"^\n\x1eGetStatusPrivacyReturnFunction\x12-\n\rStatusPrivacy\x18\x01 \x03(\x0b\x32\x16.neonize.StatusPrivacy\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\x8a\x01\n\x0fGroupLinkTarget\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12%\n\tGroupName\x18\x02 \x02(\x0b\x32\x12.neonize.GroupName\x12\x35\n\x11GroupIsDefaultSub\x18\x03 \x02(\x0b\x32\x1a.neonize.GroupIsDefaultSub\"^\n\x1aGetSubGroupsReturnFunction\x12\x31\n\x0fGroupLinkTarget\x18\x01 \x03(\x0b\x32\x18.neonize.GroupLinkTarget\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"h\n&GetSubscribedNewslettersReturnFunction\x12/\n\nNewsletter\x18\x01 \x03(\x0b\x32\x1b.neonize.NewsletterMetadata\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"H\n\x1cGetUserDevicesreturnFunction\x12\x19\n\x03JID\x18\x01 \x03(\x0b\x32\x0c.neonize.JID\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"O\n,NewsletterSubscribeLiveUpdatesReturnFunction\x12\x10\n\x08\x44uration\x18\x01 \x01(\x03\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xad\x01\n\nPairStatus\x12\x18\n\x02ID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x14\n\x0c\x42usinessName\x18\x02 \x02(\t\x12\x10\n\x08Platform\x18\x03 \x02(\t\x12+\n\x06Status\x18\x04 \x02(\x0e\x32\x1b.neonize.PairStatus.PStatus\x12\r\n\x05\x45rror\x18\x05 \x01(\t\"!\n\x07PStatus\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\";\n\x10KeepAliveTimeout\x12\x12\n\nErrorCount\x18\x01 \x02(\x03\x12\x13\n\x0bLastSuccess\x18\x02 \x02(\x03\"M\n\tLoggedOut\x12\x11\n\tOnConnect\x18\x01 \x02(\x08\x12-\n\x06Reason\x18\x02 \x02(\x0e\x32\x1d.neonize.ConnectFailureReason\"\xe7\x01\n\x0cTemporaryBan\x12\x31\n\x04\x43ode\x18\x01 \x02(\x0e\x32#.neonize.TemporaryBan.TempBanReason\x12\x0e\n\x06\x45xpire\x18\x02 \x02(\x03\"\x93\x01\n\rTempBanReason\x12\x1b\n\x17SEND_TO_TOO_MANY_PEOPLE\x10\x01\x12\x14\n\x10\x42LOCKED_BY_USERS\x10\x02\x12\x1b\n\x17\x43REATED_TOO_MANY_GROUPS\x10\x03\x12\x1e\n\x1aSENT_TOO_MANY_SAME_MESSAGE\x10\x04\x12\x12\n\x0e\x42ROADCAST_LIST\x10\x05\"l\n\x0e\x43onnectFailure\x12-\n\x06Reason\x18\x01 \x02(\x0e\x32\x1d.neonize.ConnectFailureReason\x12\x0f\n\x07Message\x18\x02 \x02(\t\x12\x1a\n\x03Raw\x18\x03 \x02(\x0b\x32\r.neonize.Node\"7\n\x0bStreamError\x12\x0c\n\x04\x43ode\x18\x01 \x02(\t\x12\x1a\n\x03Raw\x18\x04 \x02(\x0b\x32\r.neonize.Node\"2\n\x0bHistorySync\x12#\n\x04\x44\x61ta\x18\x01 \x02(\x0b\x32\x15.defproto.HistorySync\"\xe5\x01\n\x07Receipt\x12-\n\rMessageSource\x18\x01 \x02(\x0b\x32\x16.neonize.MessageSource\x12\x12\n\nMessageIDs\x18\x02 \x03(\t\x12\x11\n\tTimestamp\x18\x03 \x02(\x03\x12*\n\x04Type\x18\x04 \x02(\x0e\x32\x1c.neonize.Receipt.ReceiptType\"X\n\x0bReceiptType\x12\r\n\tDELIVERED\x10\x01\x12\n\n\x06SENDER\x10\x02\x12\t\n\x05RETRY\x10\x03\x12\x08\n\x04READ\x10\x04\x12\r\n\tREAD_SELF\x10\x05\x12\n\n\x06PLAYED\x10\x06\"\xfd\x01\n\x0c\x43hatPresence\x12-\n\rMessageSource\x18\x01 \x02(\x0b\x32\x16.neonize.MessageSource\x12\x31\n\x05State\x18\x02 \x02(\x0e\x32\".neonize.ChatPresence.ChatPresence\x12\x36\n\x05Media\x18\x03 \x02(\x0e\x32\'.neonize.ChatPresence.ChatPresenceMedia\")\n\x0c\x43hatPresence\x12\r\n\tCOMPOSING\x10\x01\x12\n\n\x06PAUSED\x10\x02\"(\n\x11\x43hatPresenceMedia\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\"M\n\x08Presence\x12\x1a\n\x04\x46rom\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x13\n\x0bUnavailable\x18\x02 \x02(\x08\x12\x10\n\x08LastSeen\x18\x03 \x02(\x03\"e\n\x0bJoinedGroup\x12\x0e\n\x06Reason\x18\x01 \x02(\t\x12\x0c\n\x04Type\x18\x02 \x02(\t\x12\x11\n\tCreateKey\x18\x03 \x02(\t\x12%\n\tGroupInfo\x18\x04 \x02(\x0b\x32\x12.neonize.GroupInfo\"e\n\x07Picture\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x1c\n\x06\x41uthor\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x11\n\tTimestamp\x18\x03 \x02(\x03\x12\x0e\n\x06Remove\x18\x04 \x02(\x08\"P\n\x0eIdentityChange\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x11\n\tTimestamp\x18\x02 \x02(\x03\x12\x10\n\x08Implicit\x18\x03 \x02(\x08\"u\n\x12OfflineSyncPreview\x12\r\n\x05Total\x18\x01 \x02(\x03\x12\x16\n\x0e\x41ppDataChanges\x18\x02 \x02(\x03\x12\x0f\n\x07Message\x18\x03 \x02(\x03\x12\x15\n\rNotifications\x18\x04 \x02(\x03\x12\x10\n\x08Receipts\x18\x05 \x02(\x03\"%\n\x14OfflineSyncCompleted\x12\r\n\x05\x43ount\x18\x01 \x02(\x03\"\xb2\x01\n\x0e\x42locklistEvent\x12/\n\x06\x41\x63tion\x18\x01 \x02(\x0e\x32\x1f.neonize.BlocklistEvent.Actions\x12\r\n\x05\x44HASH\x18\x02 \x02(\t\x12\x11\n\tPrevDHash\x18\x03 \x02(\t\x12)\n\x07\x43hanges\x18\x04 \x03(\x0b\x32\x18.neonize.BlocklistChange\"\"\n\x07\x41\x63tions\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\n\n\x06MODIFY\x10\x02\"N\n\x0f\x42locklistChange\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\" \n\x06\x41\x63tion\x12\t\n\x05\x42LOCK\x10\x01\x12\x0b\n\x07UNBLOCK\x10\x02\"I\n\x0eNewsletterJoin\x12\x37\n\x12NewsletterMetadata\x18\x01 \x02(\x0b\x32\x1b.neonize.NewsletterMetadata\"R\n\x0fNewsletterLeave\x12\x18\n\x02ID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12%\n\x04Role\x18\x02 \x02(\x0e\x32\x17.neonize.NewsletterRole\"\\\n\x14NewsletterMuteChange\x12\x18\n\x02ID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12*\n\x04Mute\x18\x02 \x02(\x0e\x32\x1c.neonize.NewsletterMuteState\"m\n\x14NewsletterLiveUpdate\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x0c\n\x04TIME\x18\x02 \x02(\x03\x12,\n\x08Messages\x18\x03 \x03(\x0b\x32\x1a.neonize.NewsletterMessage\"\x13\n\x02QR\x12\r\n\x05\x43odes\x18\x01 \x03(\t*A\n\x0eNewsletterRole\x12\x0e\n\nSUBSCRIBER\x10\x01\x12\t\n\x05GUEST\x10\x02\x12\t\n\x05\x41\x44MIN\x10\x03\x12\t\n\x05OWNER\x10\x04*&\n\x13NewsletterMuteState\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02*\xdd\x01\n\x14\x43onnectFailureReason\x12\x0b\n\x07GENERIC\x10\x01\x12\x0e\n\nLOGGED_OUT\x10\x02\x12\x0f\n\x0bTEMP_BANNED\x10\x03\x12\x14\n\x10MAIN_DEVICE_GONE\x10\x04\x12\x12\n\x0eUNKNOWN_LOGOUT\x10\x05\x12\x13\n\x0f\x43LIENT_OUTDATED\x10\x06\x12\x12\n\x0e\x42\x41\x44_USER_AGENT\x10\x07\x12\x19\n\x15INTERNAL_SERVER_ERROR\x10\x08\x12\x10\n\x0c\x45XPERIMENTAL\x10\t\x12\x17\n\x13SERVICE_UNAVAILABLE\x10\nB\x0bZ\t./neonize')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Neonize_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\t./neonize'
  _globals['_NEWSLETTERROLE']._serialized_start=11046
  _globals['_NEWSLETTERROLE']._serialized_end=11111
  _globals['_NEWSLETTERMUTESTATE']._serialized_start=11113
  _globals['_NEWSLETTERMUTESTATE']._serialized_end=11151
  _globals['_CONNECTFAILUREREASON']._serialized_start=11154
  _globals['_CONNECTFAILUREREASON']._serialized_end=11375
  _globals['_JID']._serialized_start=37
  _globals['_JID']._serialized_end=143
  _globals['_MESSAGEINFO']._serialized_start=146
  _globals['_MESSAGEINFO']._serialized_end=451
  _globals['_UPLOADRESPONSE']._serialized_start=454
  _globals['_UPLOADRESPONSE']._serialized_end=600
  _globals['_MESSAGESOURCE']._serialized_start=603
  _globals['_MESSAGESOURCE']._serialized_end=753
  _globals['_DEVICESENTMETA']._serialized_start=755
  _globals['_DEVICESENTMETA']._serialized_end=810
  _globals['_VERIFIEDNAME']._serialized_start=813
  _globals['_VERIFIEDNAME']._serialized_end=943
  _globals['_ISONWHATSAPPRESPONSE']._serialized_start=945
  _globals['_ISONWHATSAPPRESPONSE']._serialized_end=1068
  _globals['_USERINFO']._serialized_start=1070
  _globals['_USERINFO']._serialized_end=1191
  _globals['_DEVICE']._serialized_start=1193
  _globals['_DEVICE']._serialized_end=1308
  _globals['_GROUPNAME']._serialized_start=1310
  _globals['_GROUPNAME']._serialized_end=1387
  _globals['_GROUPTOPIC']._serialized_start=1389
  _globals['_GROUPTOPIC']._serialized_end=1509
  _globals['_GROUPLOCKED']._serialized_start=1511
  _globals['_GROUPLOCKED']._serialized_end=1542
  _globals['_GROUPANNOUNCE']._serialized_start=1544
  _globals['_GROUPANNOUNCE']._serialized_end=1606
  _globals['_GROUPEPHEMERAL']._serialized_start=1608
  _globals['_GROUPEPHEMERAL']._serialized_end=1672
  _globals['_GROUPINCOGNITO']._serialized_start=1674
  _globals['_GROUPINCOGNITO']._serialized_end=1711
  _globals['_GROUPPARENT']._serialized_start=1713
  _globals['_GROUPPARENT']._serialized_end=1783
  _globals['_GROUPLINKEDPARENT']._serialized_start=1785
  _globals['_GROUPLINKEDPARENT']._serialized_end=1843
  _globals['_GROUPISDEFAULTSUB']._serialized_start=1845
  _globals['_GROUPISDEFAULTSUB']._serialized_end=1891
  _globals['_GROUPPARTICIPANTADDREQUEST']._serialized_start=1893
  _globals['_GROUPPARTICIPANTADDREQUEST']._serialized_end=1955
  _globals['_GROUPPARTICIPANT']._serialized_start=1958
  _globals['_GROUPPARTICIPANT']._serialized_end=2162
  _globals['_GROUPINFO']._serialized_start=2165
  _globals['_GROUPINFO']._serialized_end=2808
  _globals['_GROUPINFO_GROUPMEMBERADDMODE']._serialized_start=2759
  _globals['_GROUPINFO_GROUPMEMBERADDMODE']._serialized_end=2808
  _globals['_MESSAGEDEBUGTIMINGS']._serialized_start=2811
  _globals['_MESSAGEDEBUGTIMINGS']._serialized_end=2995
  _globals['_SENDRESPONSE']._serialized_start=2997
  _globals['_SENDRESPONSE']._serialized_end=3112
  _globals['_SENDMESSAGERETURNFUNCTION']._serialized_start=3114
  _globals['_SENDMESSAGERETURNFUNCTION']._serialized_end=3201
  _globals['_GETGROUPINFORETURNFUNCTION']._serialized_start=3203
  _globals['_GETGROUPINFORETURNFUNCTION']._serialized_end=3285
  _globals['_JOINGROUPWITHLINKRETURNFUNCTION']._serialized_start=3287
  _globals['_JOINGROUPWITHLINKRETURNFUNCTION']._serialized_end=3362
  _globals['_GETGROUPINVITELINKRETURNFUNCTION']._serialized_start=3364
  _globals['_GETGROUPINVITELINKRETURNFUNCTION']._serialized_end=3433
  _globals['_DOWNLOADRETURNFUNCTION']._serialized_start=3435
  _globals['_DOWNLOADRETURNFUNCTION']._serialized_end=3490
  _globals['_UPLOADRETURNFUNCTION']._serialized_start=3492
  _globals['_UPLOADRETURNFUNCTION']._serialized_end=3578
  _globals['_SETGROUPPHOTORETURNFUNCTION']._serialized_start=3580
  _globals['_SETGROUPPHOTORETURNFUNCTION']._serialized_end=3643
  _globals['_ISONWHATSAPPRETURNFUNCTION']._serialized_start=3645
  _globals['_ISONWHATSAPPRETURNFUNCTION']._serialized_end=3749
  _globals['_GETUSERINFOSINGLERETURNFUNCTION']._serialized_start=3751
  _globals['_GETUSERINFOSINGLERETURNFUNCTION']._serialized_end=3848
  _globals['_GETUSERINFORETURNFUNCTION']._serialized_start=3850
  _globals['_GETUSERINFORETURNFUNCTION']._serialized_end=3953
  _globals['_BUILDPOLLVOTERETURNFUNCTION']._serialized_start=3955
  _globals['_BUILDPOLLVOTERETURNFUNCTION']._serialized_end=4036
  _globals['_CREATENEWSLETTERRETURNFUNCTION']._serialized_start=4038
  _globals['_CREATENEWSLETTERRETURNFUNCTION']._serialized_end=4142
  _globals['_GETBLOCKLISTRETURNFUNCTION']._serialized_start=4144
  _globals['_GETBLOCKLISTRETURNFUNCTION']._serialized_end=4226
  _globals['_GETCONTACTQRLINKRETURNFUNCTION']._serialized_start=4228
  _globals['_GETCONTACTQRLINKRETURNFUNCTION']._serialized_end=4289
  _globals['_GETGROUPREQUESTPARTICIPANTSRETURNFUNCTION']._serialized_start=4291
  _globals['_GETGROUPREQUESTPARTICIPANTSRETURNFUNCTION']._serialized_end=4385
  _globals['_GETJOINEDGROUPSRETURNFUNCTION']._serialized_start=4387
  _globals['_GETJOINEDGROUPSRETURNFUNCTION']._serialized_end=4468
  _globals['_REQCREATEGROUP']._serialized_start=4471
  _globals['_REQCREATEGROUP']._serialized_end=4654
  _globals['_JIDARRAY']._serialized_start=4656
  _globals['_JIDARRAY']._serialized_end=4694
  _globals['_ARRAYSTRING']._serialized_start=4696
  _globals['_ARRAYSTRING']._serialized_end=4723
  _globals['_NEWSLETTERMESSAGEMETA']._serialized_start=4725
  _globals['_NEWSLETTERMESSAGEMETA']._serialized_end=4784
  _globals['_MESSAGE']._serialized_start=4787
  _globals['_MESSAGE']._serialized_end=5101
  _globals['_CREATENEWSLETTERPARAMS']._serialized_start=5103
  _globals['_CREATENEWSLETTERPARAMS']._serialized_end=5179
  _globals['_WRAPPEDNEWSLETTERSTATE']._serialized_start=5182
  _globals['_WRAPPEDNEWSLETTERSTATE']._serialized_end=5333
  _globals['_WRAPPEDNEWSLETTERSTATE_NEWSLETTERSTATE']._serialized_start=5271
  _globals['_WRAPPEDNEWSLETTERSTATE_NEWSLETTERSTATE']._serialized_end=5333
  _globals['_NEWSLETTERTEXT']._serialized_start=5335
  _globals['_NEWSLETTERTEXT']._serialized_end=5397
  _globals['_PROFILEPICTUREINFO']._serialized_start=5399
  _globals['_PROFILEPICTUREINFO']._serialized_end=5478
  _globals['_NEWSLETTERREACTIONSETTINGS']._serialized_start=5481
  _globals['_NEWSLETTERREACTIONSETTINGS']._serialized_end=5657
  _globals['_NEWSLETTERREACTIONSETTINGS_NEWSLETTERREACTIONSMODE']._serialized_start=5587
  _globals['_NEWSLETTERREACTIONSETTINGS_NEWSLETTERREACTIONSMODE']._serialized_end=5657
  _globals['_NEWSLETTERSETTING']._serialized_start=5659
  _globals['_NEWSLETTERSETTING']._serialized_end=5738
  _globals['_NEWSLETTERTHREADMETADATA']._serialized_start=5741
  _globals['_NEWSLETTERTHREADMETADATA']._serialized_end=6208
  _globals['_NEWSLETTERTHREADMETADATA_NEWSLETTERVERIFICATIONSTATE']._serialized_start=6149
  _globals['_NEWSLETTERTHREADMETADATA_NEWSLETTERVERIFICATIONSTATE']._serialized_end=6208
  _globals['_NEWSLETTERVIEWERMETADATA']._serialized_start=6210
  _globals['_NEWSLETTERVIEWERMETADATA']._serialized_end=6319
  _globals['_NEWSLETTERMETADATA']._serialized_start=6322
  _globals['_NEWSLETTERMETADATA']._serialized_end=6526
  _globals['_BLOCKLIST']._serialized_start=6528
  _globals['_BLOCKLIST']._serialized_end=6582
  _globals['_REACTION']._serialized_start=6584
  _globals['_REACTION']._serialized_end=6623
  _globals['_NEWSLETTERMESSAGE']._serialized_start=6626
  _globals['_NEWSLETTERMESSAGE']._serialized_end=6769
  _globals['_GETNEWSLETTERMESSAGEUPDATERETURNFUNCTION']._serialized_start=6771
  _globals['_GETNEWSLETTERMESSAGEUPDATERETURNFUNCTION']._serialized_end=6883
  _globals['_PRIVACYSETTINGS']._serialized_start=6886
  _globals['_PRIVACYSETTINGS']._serialized_end=7435
  _globals['_PRIVACYSETTINGS_PRIVACYSETTING']._serialized_start=7316
  _globals['_PRIVACYSETTINGS_PRIVACYSETTING']._serialized_end=7435
  _globals['_NODEATTRS']._serialized_start=7437
  _globals['_NODEATTRS']._serialized_end=7477
  _globals['_NODE']._serialized_start=7479
  _globals['_NODE']._serialized_end=7565
  _globals['_INFOQUERY']._serialized_start=7567
  _globals['_INFOQUERY']._serialized_end=7655
  _globals['_GETPROFILEPICTUREPARAMS']._serialized_start=7657
  _globals['_GETPROFILEPICTUREPARAMS']._serialized_end=7740
  _globals['_GETPROFILEPICTURERETURNFUNCTION']._serialized_start=7742
  _globals['_GETPROFILEPICTURERETURNFUNCTION']._serialized_end=7836
  _globals['_STATUSPRIVACY']._serialized_start=7839
  _globals['_STATUSPRIVACY']._serialized_end=8022
  _globals['_STATUSPRIVACY_STATUSPRIVACYTYPE']._serialized_start=7959
  _globals['_STATUSPRIVACY_STATUSPRIVACYTYPE']._serialized_end=8022
  _globals['_GETSTATUSPRIVACYRETURNFUNCTION']._serialized_start=8024
  _globals['_GETSTATUSPRIVACYRETURNFUNCTION']._serialized_end=8118
  _globals['_GROUPLINKTARGET']._serialized_start=8121
  _globals['_GROUPLINKTARGET']._serialized_end=8259
  _globals['_GETSUBGROUPSRETURNFUNCTION']._serialized_start=8261
  _globals['_GETSUBGROUPSRETURNFUNCTION']._serialized_end=8355
  _globals['_GETSUBSCRIBEDNEWSLETTERSRETURNFUNCTION']._serialized_start=8357
  _globals['_GETSUBSCRIBEDNEWSLETTERSRETURNFUNCTION']._serialized_end=8461
  _globals['_GETUSERDEVICESRETURNFUNCTION']._serialized_start=8463
  _globals['_GETUSERDEVICESRETURNFUNCTION']._serialized_end=8535
  _globals['_NEWSLETTERSUBSCRIBELIVEUPDATESRETURNFUNCTION']._serialized_start=8537
  _globals['_NEWSLETTERSUBSCRIBELIVEUPDATESRETURNFUNCTION']._serialized_end=8616
  _globals['_PAIRSTATUS']._serialized_start=8619
  _globals['_PAIRSTATUS']._serialized_end=8792
  _globals['_PAIRSTATUS_PSTATUS']._serialized_start=8759
  _globals['_PAIRSTATUS_PSTATUS']._serialized_end=8792
  _globals['_KEEPALIVETIMEOUT']._serialized_start=8794
  _globals['_KEEPALIVETIMEOUT']._serialized_end=8853
  _globals['_LOGGEDOUT']._serialized_start=8855
  _globals['_LOGGEDOUT']._serialized_end=8932
  _globals['_TEMPORARYBAN']._serialized_start=8935
  _globals['_TEMPORARYBAN']._serialized_end=9166
  _globals['_TEMPORARYBAN_TEMPBANREASON']._serialized_start=9019
  _globals['_TEMPORARYBAN_TEMPBANREASON']._serialized_end=9166
  _globals['_CONNECTFAILURE']._serialized_start=9168
  _globals['_CONNECTFAILURE']._serialized_end=9276
  _globals['_STREAMERROR']._serialized_start=9278
  _globals['_STREAMERROR']._serialized_end=9333
  _globals['_HISTORYSYNC']._serialized_start=9335
  _globals['_HISTORYSYNC']._serialized_end=9385
  _globals['_RECEIPT']._serialized_start=9388
  _globals['_RECEIPT']._serialized_end=9617
  _globals['_RECEIPT_RECEIPTTYPE']._serialized_start=9529
  _globals['_RECEIPT_RECEIPTTYPE']._serialized_end=9617
  _globals['_CHATPRESENCE']._serialized_start=9620
  _globals['_CHATPRESENCE']._serialized_end=9873
  _globals['_CHATPRESENCE_CHATPRESENCE']._serialized_start=9790
  _globals['_CHATPRESENCE_CHATPRESENCE']._serialized_end=9831
  _globals['_CHATPRESENCE_CHATPRESENCEMEDIA']._serialized_start=9833
  _globals['_CHATPRESENCE_CHATPRESENCEMEDIA']._serialized_end=9873
  _globals['_PRESENCE']._serialized_start=9875
  _globals['_PRESENCE']._serialized_end=9952
  _globals['_JOINEDGROUP']._serialized_start=9954
  _globals['_JOINEDGROUP']._serialized_end=10055
  _globals['_PICTURE']._serialized_start=10057
  _globals['_PICTURE']._serialized_end=10158
  _globals['_IDENTITYCHANGE']._serialized_start=10160
  _globals['_IDENTITYCHANGE']._serialized_end=10240
  _globals['_OFFLINESYNCPREVIEW']._serialized_start=10242
  _globals['_OFFLINESYNCPREVIEW']._serialized_end=10359
  _globals['_OFFLINESYNCCOMPLETED']._serialized_start=10361
  _globals['_OFFLINESYNCCOMPLETED']._serialized_end=10398
  _globals['_BLOCKLISTEVENT']._serialized_start=10401
  _globals['_BLOCKLISTEVENT']._serialized_end=10579
  _globals['_BLOCKLISTEVENT_ACTIONS']._serialized_start=10545
  _globals['_BLOCKLISTEVENT_ACTIONS']._serialized_end=10579
  _globals['_BLOCKLISTCHANGE']._serialized_start=10581
  _globals['_BLOCKLISTCHANGE']._serialized_end=10659
  _globals['_BLOCKLISTCHANGE_ACTION']._serialized_start=10627
  _globals['_BLOCKLISTCHANGE_ACTION']._serialized_end=10659
  _globals['_NEWSLETTERJOIN']._serialized_start=10661
  _globals['_NEWSLETTERJOIN']._serialized_end=10734
  _globals['_NEWSLETTERLEAVE']._serialized_start=10736
  _globals['_NEWSLETTERLEAVE']._serialized_end=10818
  _globals['_NEWSLETTERMUTECHANGE']._serialized_start=10820
  _globals['_NEWSLETTERMUTECHANGE']._serialized_end=10912
  _globals['_NEWSLETTERLIVEUPDATE']._serialized_start=10914
  _globals['_NEWSLETTERLIVEUPDATE']._serialized_end=11023
  _globals['_QR']._serialized_start=11025
  _globals['_QR']._serialized_end=11044
# @@protoc_insertion_point(module_scope)
