"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
import waCommon.WACommon_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class WAMediaTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class Thumbnail(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            @typing.final
            class DownloadableThumbnail(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                FILESHA256_FIELD_NUMBER: builtins.int
                FILEENCSHA256_FIELD_NUMBER: builtins.int
                DIRECTPATH_FIELD_NUMBER: builtins.int
                MEDIAKEY_FIELD_NUMBER: builtins.int
                MEDIAKEYTIMESTAMP_FIELD_NUMBER: builtins.int
                OBJECTID_FIELD_NUMBER: builtins.int
                THUMBNAILSCANSSIDECAR_FIELD_NUMBER: builtins.int
                THUMBNAILSCANLENGTHS_FIELD_NUMBER: builtins.int
                fileSHA256: builtins.bytes
                fileEncSHA256: builtins.bytes
                directPath: builtins.str
                mediaKey: builtins.bytes
                mediaKeyTimestamp: builtins.int
                objectID: builtins.str
                thumbnailScansSidecar: builtins.bytes
                @property
                def thumbnailScanLengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
                def __init__(
                    self,
                    *,
                    fileSHA256: builtins.bytes | None = ...,
                    fileEncSHA256: builtins.bytes | None = ...,
                    directPath: builtins.str | None = ...,
                    mediaKey: builtins.bytes | None = ...,
                    mediaKeyTimestamp: builtins.int | None = ...,
                    objectID: builtins.str | None = ...,
                    thumbnailScansSidecar: builtins.bytes | None = ...,
                    thumbnailScanLengths: collections.abc.Iterable[builtins.int] | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID", "thumbnailScansSidecar", b"thumbnailScansSidecar"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID", "thumbnailScanLengths", b"thumbnailScanLengths", "thumbnailScansSidecar", b"thumbnailScansSidecar"]) -> None: ...

            JPEGTHUMBNAIL_FIELD_NUMBER: builtins.int
            DOWNLOADABLETHUMBNAIL_FIELD_NUMBER: builtins.int
            THUMBNAILWIDTH_FIELD_NUMBER: builtins.int
            THUMBNAILHEIGHT_FIELD_NUMBER: builtins.int
            JPEGThumbnail: builtins.bytes
            thumbnailWidth: builtins.int
            thumbnailHeight: builtins.int
            @property
            def downloadableThumbnail(self) -> global___WAMediaTransport.Ancillary.Thumbnail.DownloadableThumbnail: ...
            def __init__(
                self,
                *,
                JPEGThumbnail: builtins.bytes | None = ...,
                downloadableThumbnail: global___WAMediaTransport.Ancillary.Thumbnail.DownloadableThumbnail | None = ...,
                thumbnailWidth: builtins.int | None = ...,
                thumbnailHeight: builtins.int | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["JPEGThumbnail", b"JPEGThumbnail", "downloadableThumbnail", b"downloadableThumbnail", "thumbnailHeight", b"thumbnailHeight", "thumbnailWidth", b"thumbnailWidth"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["JPEGThumbnail", b"JPEGThumbnail", "downloadableThumbnail", b"downloadableThumbnail", "thumbnailHeight", b"thumbnailHeight", "thumbnailWidth", b"thumbnailWidth"]) -> None: ...

        FILELENGTH_FIELD_NUMBER: builtins.int
        MIMETYPE_FIELD_NUMBER: builtins.int
        THUMBNAIL_FIELD_NUMBER: builtins.int
        OBJECTID_FIELD_NUMBER: builtins.int
        fileLength: builtins.int
        mimetype: builtins.str
        objectID: builtins.str
        @property
        def thumbnail(self) -> global___WAMediaTransport.Ancillary.Thumbnail: ...
        def __init__(
            self,
            *,
            fileLength: builtins.int | None = ...,
            mimetype: builtins.str | None = ...,
            thumbnail: global___WAMediaTransport.Ancillary.Thumbnail | None = ...,
            objectID: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["fileLength", b"fileLength", "mimetype", b"mimetype", "objectID", b"objectID", "thumbnail", b"thumbnail"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["fileLength", b"fileLength", "mimetype", b"mimetype", "objectID", b"objectID", "thumbnail", b"thumbnail"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILESHA256_FIELD_NUMBER: builtins.int
        MEDIAKEY_FIELD_NUMBER: builtins.int
        FILEENCSHA256_FIELD_NUMBER: builtins.int
        DIRECTPATH_FIELD_NUMBER: builtins.int
        MEDIAKEYTIMESTAMP_FIELD_NUMBER: builtins.int
        fileSHA256: builtins.bytes
        mediaKey: builtins.bytes
        fileEncSHA256: builtins.bytes
        directPath: builtins.str
        mediaKeyTimestamp: builtins.int
        def __init__(
            self,
            *,
            fileSHA256: builtins.bytes | None = ...,
            mediaKey: builtins.bytes | None = ...,
            fileEncSHA256: builtins.bytes | None = ...,
            directPath: builtins.str | None = ...,
            mediaKeyTimestamp: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___WAMediaTransport.Integral: ...
    @property
    def ancillary(self) -> global___WAMediaTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___WAMediaTransport.Integral | None = ...,
        ancillary: global___WAMediaTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___WAMediaTransport = WAMediaTransport

@typing.final
class ImageTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _HdType:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _HdTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ImageTransport.Ancillary._HdType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            NONE: ImageTransport.Ancillary._HdType.ValueType  # 0
            LQ_4K: ImageTransport.Ancillary._HdType.ValueType  # 1
            HQ_4K: ImageTransport.Ancillary._HdType.ValueType  # 2

        class HdType(_HdType, metaclass=_HdTypeEnumTypeWrapper): ...
        NONE: ImageTransport.Ancillary.HdType.ValueType  # 0
        LQ_4K: ImageTransport.Ancillary.HdType.ValueType  # 1
        HQ_4K: ImageTransport.Ancillary.HdType.ValueType  # 2

        HEIGHT_FIELD_NUMBER: builtins.int
        WIDTH_FIELD_NUMBER: builtins.int
        SCANSSIDECAR_FIELD_NUMBER: builtins.int
        SCANLENGTHS_FIELD_NUMBER: builtins.int
        MIDQUALITYFILESHA256_FIELD_NUMBER: builtins.int
        HDTYPE_FIELD_NUMBER: builtins.int
        MEMORIESCONCEPTSCORES_FIELD_NUMBER: builtins.int
        MEMORIESCONCEPTIDS_FIELD_NUMBER: builtins.int
        height: builtins.int
        width: builtins.int
        scansSidecar: builtins.bytes
        midQualityFileSHA256: builtins.bytes
        hdType: global___ImageTransport.Ancillary.HdType.ValueType
        @property
        def scanLengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        @property
        def memoriesConceptScores(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
        @property
        def memoriesConceptIDs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        def __init__(
            self,
            *,
            height: builtins.int | None = ...,
            width: builtins.int | None = ...,
            scansSidecar: builtins.bytes | None = ...,
            scanLengths: collections.abc.Iterable[builtins.int] | None = ...,
            midQualityFileSHA256: builtins.bytes | None = ...,
            hdType: global___ImageTransport.Ancillary.HdType.ValueType | None = ...,
            memoriesConceptScores: collections.abc.Iterable[builtins.float] | None = ...,
            memoriesConceptIDs: collections.abc.Iterable[builtins.int] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["hdType", b"hdType", "height", b"height", "midQualityFileSHA256", b"midQualityFileSHA256", "scansSidecar", b"scansSidecar", "width", b"width"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["hdType", b"hdType", "height", b"height", "memoriesConceptIDs", b"memoriesConceptIDs", "memoriesConceptScores", b"memoriesConceptScores", "midQualityFileSHA256", b"midQualityFileSHA256", "scanLengths", b"scanLengths", "scansSidecar", b"scansSidecar", "width", b"width"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSPORT_FIELD_NUMBER: builtins.int
        @property
        def transport(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            transport: global___WAMediaTransport | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["transport", b"transport"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["transport", b"transport"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___ImageTransport.Integral: ...
    @property
    def ancillary(self) -> global___ImageTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___ImageTransport.Integral | None = ...,
        ancillary: global___ImageTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___ImageTransport = ImageTransport

@typing.final
class VideoTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Attribution:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _AttributionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[VideoTransport.Ancillary._Attribution.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            NONE: VideoTransport.Ancillary._Attribution.ValueType  # 0
            GIPHY: VideoTransport.Ancillary._Attribution.ValueType  # 1
            TENOR: VideoTransport.Ancillary._Attribution.ValueType  # 2

        class Attribution(_Attribution, metaclass=_AttributionEnumTypeWrapper): ...
        NONE: VideoTransport.Ancillary.Attribution.ValueType  # 0
        GIPHY: VideoTransport.Ancillary.Attribution.ValueType  # 1
        TENOR: VideoTransport.Ancillary.Attribution.ValueType  # 2

        SECONDS_FIELD_NUMBER: builtins.int
        CAPTION_FIELD_NUMBER: builtins.int
        GIFPLAYBACK_FIELD_NUMBER: builtins.int
        HEIGHT_FIELD_NUMBER: builtins.int
        WIDTH_FIELD_NUMBER: builtins.int
        SIDECAR_FIELD_NUMBER: builtins.int
        GIFATTRIBUTION_FIELD_NUMBER: builtins.int
        seconds: builtins.int
        gifPlayback: builtins.bool
        height: builtins.int
        width: builtins.int
        sidecar: builtins.bytes
        gifAttribution: global___VideoTransport.Ancillary.Attribution.ValueType
        @property
        def caption(self) -> waCommon.WACommon_pb2.MessageText: ...
        def __init__(
            self,
            *,
            seconds: builtins.int | None = ...,
            caption: waCommon.WACommon_pb2.MessageText | None = ...,
            gifPlayback: builtins.bool | None = ...,
            height: builtins.int | None = ...,
            width: builtins.int | None = ...,
            sidecar: builtins.bytes | None = ...,
            gifAttribution: global___VideoTransport.Ancillary.Attribution.ValueType | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["caption", b"caption", "gifAttribution", b"gifAttribution", "gifPlayback", b"gifPlayback", "height", b"height", "seconds", b"seconds", "sidecar", b"sidecar", "width", b"width"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["caption", b"caption", "gifAttribution", b"gifAttribution", "gifPlayback", b"gifPlayback", "height", b"height", "seconds", b"seconds", "sidecar", b"sidecar", "width", b"width"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSPORT_FIELD_NUMBER: builtins.int
        @property
        def transport(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            transport: global___WAMediaTransport | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["transport", b"transport"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["transport", b"transport"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___VideoTransport.Integral: ...
    @property
    def ancillary(self) -> global___VideoTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___VideoTransport.Integral | None = ...,
        ancillary: global___VideoTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___VideoTransport = VideoTransport

@typing.final
class AudioTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class AvatarAudio(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            class _AnimationsType:
                ValueType = typing.NewType("ValueType", builtins.int)
                V: typing_extensions.TypeAlias = ValueType

            class _AnimationsTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType], builtins.type):
                DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                TALKING_A: AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType  # 0
                IDLE_A: AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType  # 1
                TALKING_B: AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType  # 2
                IDLE_B: AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType  # 3
                BACKGROUND: AudioTransport.Ancillary.AvatarAudio._AnimationsType.ValueType  # 4

            class AnimationsType(_AnimationsType, metaclass=_AnimationsTypeEnumTypeWrapper): ...
            TALKING_A: AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType  # 0
            IDLE_A: AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType  # 1
            TALKING_B: AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType  # 2
            IDLE_B: AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType  # 3
            BACKGROUND: AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType  # 4

            @typing.final
            class DownloadableAvatarAnimations(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor

                FILESHA256_FIELD_NUMBER: builtins.int
                FILEENCSHA256_FIELD_NUMBER: builtins.int
                DIRECTPATH_FIELD_NUMBER: builtins.int
                MEDIAKEY_FIELD_NUMBER: builtins.int
                MEDIAKEYTIMESTAMP_FIELD_NUMBER: builtins.int
                OBJECTID_FIELD_NUMBER: builtins.int
                ANIMATIONSTYPE_FIELD_NUMBER: builtins.int
                fileSHA256: builtins.bytes
                fileEncSHA256: builtins.bytes
                directPath: builtins.str
                mediaKey: builtins.bytes
                mediaKeyTimestamp: builtins.int
                objectID: builtins.str
                animationsType: global___AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType
                def __init__(
                    self,
                    *,
                    fileSHA256: builtins.bytes | None = ...,
                    fileEncSHA256: builtins.bytes | None = ...,
                    directPath: builtins.str | None = ...,
                    mediaKey: builtins.bytes | None = ...,
                    mediaKeyTimestamp: builtins.int | None = ...,
                    objectID: builtins.str | None = ...,
                    animationsType: global___AudioTransport.Ancillary.AvatarAudio.AnimationsType.ValueType | None = ...,
                ) -> None: ...
                def HasField(self, field_name: typing.Literal["animationsType", b"animationsType", "directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID"]) -> builtins.bool: ...
                def ClearField(self, field_name: typing.Literal["animationsType", b"animationsType", "directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID"]) -> None: ...

            POSEID_FIELD_NUMBER: builtins.int
            AVATARANIMATIONS_FIELD_NUMBER: builtins.int
            poseID: builtins.int
            @property
            def avatarAnimations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AudioTransport.Ancillary.AvatarAudio.DownloadableAvatarAnimations]: ...
            def __init__(
                self,
                *,
                poseID: builtins.int | None = ...,
                avatarAnimations: collections.abc.Iterable[global___AudioTransport.Ancillary.AvatarAudio.DownloadableAvatarAnimations] | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["poseID", b"poseID"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["avatarAnimations", b"avatarAnimations", "poseID", b"poseID"]) -> None: ...

        SECONDS_FIELD_NUMBER: builtins.int
        AVATARAUDIO_FIELD_NUMBER: builtins.int
        seconds: builtins.int
        @property
        def avatarAudio(self) -> global___AudioTransport.Ancillary.AvatarAudio: ...
        def __init__(
            self,
            *,
            seconds: builtins.int | None = ...,
            avatarAudio: global___AudioTransport.Ancillary.AvatarAudio | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["avatarAudio", b"avatarAudio", "seconds", b"seconds"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["avatarAudio", b"avatarAudio", "seconds", b"seconds"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _AudioFormat:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _AudioFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AudioTransport.Integral._AudioFormat.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            UNKNOWN: AudioTransport.Integral._AudioFormat.ValueType  # 0
            OPUS: AudioTransport.Integral._AudioFormat.ValueType  # 1

        class AudioFormat(_AudioFormat, metaclass=_AudioFormatEnumTypeWrapper): ...
        UNKNOWN: AudioTransport.Integral.AudioFormat.ValueType  # 0
        OPUS: AudioTransport.Integral.AudioFormat.ValueType  # 1

        TRANSPORT_FIELD_NUMBER: builtins.int
        AUDIOFORMAT_FIELD_NUMBER: builtins.int
        audioFormat: global___AudioTransport.Integral.AudioFormat.ValueType
        @property
        def transport(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            transport: global___WAMediaTransport | None = ...,
            audioFormat: global___AudioTransport.Integral.AudioFormat.ValueType | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["audioFormat", b"audioFormat", "transport", b"transport"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["audioFormat", b"audioFormat", "transport", b"transport"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___AudioTransport.Integral: ...
    @property
    def ancillary(self) -> global___AudioTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___AudioTransport.Integral | None = ...,
        ancillary: global___AudioTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___AudioTransport = AudioTransport

@typing.final
class DocumentTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PAGECOUNT_FIELD_NUMBER: builtins.int
        pageCount: builtins.int
        def __init__(
            self,
            *,
            pageCount: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["pageCount", b"pageCount"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["pageCount", b"pageCount"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSPORT_FIELD_NUMBER: builtins.int
        @property
        def transport(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            transport: global___WAMediaTransport | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["transport", b"transport"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["transport", b"transport"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___DocumentTransport.Integral: ...
    @property
    def ancillary(self) -> global___DocumentTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___DocumentTransport.Integral | None = ...,
        ancillary: global___DocumentTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___DocumentTransport = DocumentTransport

@typing.final
class StickerTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PAGECOUNT_FIELD_NUMBER: builtins.int
        HEIGHT_FIELD_NUMBER: builtins.int
        WIDTH_FIELD_NUMBER: builtins.int
        FIRSTFRAMELENGTH_FIELD_NUMBER: builtins.int
        FIRSTFRAMESIDECAR_FIELD_NUMBER: builtins.int
        MUSTACHETEXT_FIELD_NUMBER: builtins.int
        ISTHIRDPARTY_FIELD_NUMBER: builtins.int
        RECEIVERFETCHID_FIELD_NUMBER: builtins.int
        pageCount: builtins.int
        height: builtins.int
        width: builtins.int
        firstFrameLength: builtins.int
        firstFrameSidecar: builtins.bytes
        mustacheText: builtins.str
        isThirdParty: builtins.bool
        receiverFetchID: builtins.str
        def __init__(
            self,
            *,
            pageCount: builtins.int | None = ...,
            height: builtins.int | None = ...,
            width: builtins.int | None = ...,
            firstFrameLength: builtins.int | None = ...,
            firstFrameSidecar: builtins.bytes | None = ...,
            mustacheText: builtins.str | None = ...,
            isThirdParty: builtins.bool | None = ...,
            receiverFetchID: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["firstFrameLength", b"firstFrameLength", "firstFrameSidecar", b"firstFrameSidecar", "height", b"height", "isThirdParty", b"isThirdParty", "mustacheText", b"mustacheText", "pageCount", b"pageCount", "receiverFetchID", b"receiverFetchID", "width", b"width"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["firstFrameLength", b"firstFrameLength", "firstFrameSidecar", b"firstFrameSidecar", "height", b"height", "isThirdParty", b"isThirdParty", "mustacheText", b"mustacheText", "pageCount", b"pageCount", "receiverFetchID", b"receiverFetchID", "width", b"width"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRANSPORT_FIELD_NUMBER: builtins.int
        ISANIMATED_FIELD_NUMBER: builtins.int
        RECEIVERFETCHID_FIELD_NUMBER: builtins.int
        isAnimated: builtins.bool
        receiverFetchID: builtins.str
        @property
        def transport(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            transport: global___WAMediaTransport | None = ...,
            isAnimated: builtins.bool | None = ...,
            receiverFetchID: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["isAnimated", b"isAnimated", "receiverFetchID", b"receiverFetchID", "transport", b"transport"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["isAnimated", b"isAnimated", "receiverFetchID", b"receiverFetchID", "transport", b"transport"]) -> None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___StickerTransport.Integral: ...
    @property
    def ancillary(self) -> global___StickerTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___StickerTransport.Integral | None = ...,
        ancillary: global___StickerTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___StickerTransport = StickerTransport

@typing.final
class ContactTransport(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Ancillary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DISPLAYNAME_FIELD_NUMBER: builtins.int
        displayName: builtins.str
        def __init__(
            self,
            *,
            displayName: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["displayName", b"displayName"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["displayName", b"displayName"]) -> None: ...

    @typing.final
    class Integral(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VCARD_FIELD_NUMBER: builtins.int
        DOWNLOADABLEVCARD_FIELD_NUMBER: builtins.int
        vcard: builtins.str
        @property
        def downloadableVcard(self) -> global___WAMediaTransport: ...
        def __init__(
            self,
            *,
            vcard: builtins.str | None = ...,
            downloadableVcard: global___WAMediaTransport | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["contact", b"contact", "downloadableVcard", b"downloadableVcard", "vcard", b"vcard"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["contact", b"contact", "downloadableVcard", b"downloadableVcard", "vcard", b"vcard"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["contact", b"contact"]) -> typing.Literal["vcard", "downloadableVcard"] | None: ...

    INTEGRAL_FIELD_NUMBER: builtins.int
    ANCILLARY_FIELD_NUMBER: builtins.int
    @property
    def integral(self) -> global___ContactTransport.Integral: ...
    @property
    def ancillary(self) -> global___ContactTransport.Ancillary: ...
    def __init__(
        self,
        *,
        integral: global___ContactTransport.Integral | None = ...,
        ancillary: global___ContactTransport.Ancillary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ancillary", b"ancillary", "integral", b"integral"]) -> None: ...

global___ContactTransport = ContactTransport
