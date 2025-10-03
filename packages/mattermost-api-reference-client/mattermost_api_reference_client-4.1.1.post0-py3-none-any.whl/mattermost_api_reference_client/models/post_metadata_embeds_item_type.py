from enum import Enum


class PostMetadataEmbedsItemType(str, Enum):
    IMAGE = "image"
    LINK = "link"
    MESSAGE_ATTACHMENT = "message_attachment"
    OPENGRAPH = "opengraph"
    PERMALINK = "permalink"

    def __str__(self) -> str:
        return str(self.value)
