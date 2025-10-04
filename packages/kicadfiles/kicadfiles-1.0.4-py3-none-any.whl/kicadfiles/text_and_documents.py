"""Text and document related elements for KiCad S-expressions."""

from dataclasses import dataclass, field
from typing import Any, List, Optional

from .base_element import (
    KiCadFloat,
    KiCadInt,
    KiCadObject,
    KiCadStr,
    OptionalFlag,
    ParseStrictness,
)
from .base_types import (
    AtXY,
    End,
    Font,
    Justify,
    Pos,
    Size,
    Start,
    Uuid,
)


@dataclass
class Comment(KiCadObject):
    """Comment definition token.

    The 'comment' token defines document comments in the format::

        (comment N "COMMENT")

    Where N is a number from 1 to 9.

    Args:
        number: Comment number (1-9)
        text: Comment text
    """

    __token_name__ = "comment"

    number: int = field(default=1, metadata={"description": "Comment number (1-9)"})
    text: str = field(default="", metadata={"description": "Comment text"})


@dataclass
class Data(KiCadObject):
    """Data definition token.

    The 'data' token defines hexadecimal byte data in the format::

        (data XX1 ... XXN)

    Where XXN represents hexadecimal bytes separated by spaces, with a maximum of 32 bytes per data token.

    Args:
        hex_bytes: Hexadecimal byte values (up to 32 bytes)
    """

    __token_name__ = "data"

    hex_bytes: List[str] = field(
        default_factory=list,
        metadata={"description": "Hexadecimal byte values (up to 32 bytes)"},
    )


@dataclass
class Paper(KiCadObject):
    """Paper settings definition token.

    The 'paper' token defines paper size and orientation in the format::

        (paper PAPER_SIZE | WIDTH HEIGHT [portrait])

    Where PAPER_SIZE can be: A0, A1, A2, A3, A4, A5, A, B, C, D, E.

    Args:
        size: Standard paper size (optional)
        width: Custom paper width (optional)
        height: Custom paper height (optional)
        portrait: Whether paper is in portrait mode (optional)
    """

    __token_name__ = "paper"

    size: Optional[str] = field(
        default=None, metadata={"description": "Standard paper size", "required": False}
    )
    width: Optional[float] = field(
        default=None, metadata={"description": "Custom paper width", "required": False}
    )
    height: Optional[float] = field(
        default=None, metadata={"description": "Custom paper height", "required": False}
    )
    portrait: OptionalFlag = field(
        default_factory=lambda: OptionalFlag("portrait"),
        metadata={
            "description": "Whether paper is in portrait mode",
            "required": False,
        },
    )


@dataclass
class TitleBlock(KiCadObject):
    """Title block definition token.

    The 'title_block' token defines the document title block in the format::

        (title_block
            (title "TITLE")
            (date "DATE")
            (rev "REVISION")
            (company "COMPANY_NAME")
            (comment N "COMMENT")
        )

    Args:
        title: Document title (optional)
        date: Document date (optional)
        rev: Document revision (optional)
        company: Company name (optional)
        comments: List of comments (optional)
    """

    __token_name__ = "title_block"

    title: KiCadStr = field(
        default_factory=lambda: KiCadStr("title", "", required=False),
        metadata={"description": "Document title", "required": False},
    )
    date: KiCadStr = field(
        default_factory=lambda: KiCadStr("date", "", required=False),
        metadata={"description": "Document date", "required": False},
    )
    rev: KiCadStr = field(
        default_factory=lambda: KiCadStr("rev", "", required=False),
        metadata={"description": "Document revision", "required": False},
    )
    company: KiCadStr = field(
        default_factory=lambda: KiCadStr("company", "", required=False),
        metadata={"description": "Company name", "required": False},
    )
    comments: Optional[List[Comment]] = field(
        default_factory=list,
        metadata={"description": "List of comments", "required": False},
    )


@dataclass
class Tbtext(KiCadObject):
    """Title block text definition token.

    The 'tbtext' token defines text elements in the title block in the format::

        (tbtext
            "TEXT"
            (name "NAME")
            (pos X Y [CORNER])
            (font [(size WIDTH HEIGHT)] [bold] [italic])
            [(repeat COUNT)]
            [(incrx DISTANCE)]
            [(incry DISTANCE)]
            [(comment "COMMENT")]
        )

    Args:
        text: Text content
        name: Text element name
        pos: Position coordinates
        font: Font settings (optional)
        repeat: Repeat count for incremental text (optional)
        incrx: Repeat distance on X axis (optional)
        incry: Repeat distance on Y axis (optional)
        comment: Comment for the text object (optional)
    """

    __token_name__ = "tbtext"

    text: str = field(default="", metadata={"description": "Text content"})
    name: KiCadStr = field(
        default_factory=lambda: KiCadStr("name", ""),
        metadata={"description": "Text element name"},
    )
    pos: Pos = field(
        default_factory=lambda: Pos(), metadata={"description": "Position coordinates"}
    )
    font: Optional[Font] = field(
        default=None, metadata={"description": "Font settings", "required": False}
    )
    repeat: KiCadInt = field(
        default_factory=lambda: KiCadInt("repeat", 0, required=False),
        metadata={
            "description": "Repeat count for incremental text",
            "required": False,
        },
    )
    incrx: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incrx", 0.0, required=False),
        metadata={"description": "Repeat distance on X axis", "required": False},
    )
    incry: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incry", 0.0, required=False),
        metadata={"description": "Repeat distance on Y axis", "required": False},
    )
    comment: Optional[str] = field(
        default=None,
        metadata={"description": "Comment for the text object", "required": False},
    )


@dataclass
class Textsize(KiCadObject):
    """Text size definition token.

    The 'textsize' token defines text size in the format::

        (textsize WIDTH HEIGHT)

    Args:
        size: Text size (width and height)
    """

    __token_name__ = "textsize"

    size: Size = field(
        default_factory=lambda: Size(),
        metadata={"description": "Text size (width and height)"},
    )


@dataclass
class Members(KiCadObject):
    """Group members definition token.

    The 'members' token defines the members of a group in the format::

        (members UUID1 UUID2 ... UUIDN)

    Args:
        uuids: List of member UUIDs
    """

    __token_name__ = "members"

    uuids: List[str] = field(
        default_factory=list, metadata={"description": "List of member UUIDs"}
    )


@dataclass
class Group(KiCadObject):
    """Group definition token.

    The 'group' token defines a group of objects in the format::

        (group
            "NAME"
            (uuid UUID)
            (members UUID1 ... UUIDN)
        )

    Args:
        name: Group name
        uuid: Group unique identifier (optional)
        members: List of member UUIDs (optional)
    """

    __token_name__ = "group"

    name: str = field(default="", metadata={"description": "Group name"})
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={"description": "Group unique identifier", "required": False},
    )
    members: Optional[Members] = field(
        default=None,
        metadata={"description": "List of member UUIDs", "required": False},
    )


@dataclass
class WksTextsize(KiCadObject):
    """Worksheet text size definition token.

    Args:
        width: Text width
        height: Text height
    """

    __token_name__ = "textsize"

    width: float = field(
        default=1.0,
        metadata={"description": "Text width"},
    )
    height: float = field(
        default=1.0,
        metadata={"description": "Text height"},
    )


@dataclass
class WksSetup(KiCadObject):
    """Worksheet setup definition token.

    Args:
        textsize: Text size (optional)
        linewidth: Line width (optional)
        textlinewidth: Text line width (optional)
        left_margin: Left margin (optional)
        right_margin: Right margin (optional)
        top_margin: Top margin (optional)
        bottom_margin: Bottom margin (optional)
    """

    __token_name__ = "setup"

    textsize: Optional[WksTextsize] = field(
        default=None,
        metadata={"description": "Text size", "required": False},
    )
    linewidth: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("linewidth", 0.0, required=False),
        metadata={"description": "Line width", "required": False},
    )
    textlinewidth: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("textlinewidth", 0.0, required=False),
        metadata={"description": "Text line width", "required": False},
    )
    left_margin: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("left_margin", 0.0, required=False),
        metadata={"description": "Left margin", "required": False},
    )
    right_margin: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("right_margin", 0.0, required=False),
        metadata={"description": "Right margin", "required": False},
    )
    top_margin: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("top_margin", 0.0, required=False),
        metadata={"description": "Top margin", "required": False},
    )
    bottom_margin: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("bottom_margin", 0.0, required=False),
        metadata={"description": "Bottom margin", "required": False},
    )


@dataclass
class WksRect(KiCadObject):
    """Worksheet rectangle definition token.

    Args:
        name: Rectangle name (optional)
        start: Start position
        end: End position
        comment: Comment (optional)
        repeat: Repeat count (optional)
        incrx: X increment (optional)
        incry: Y increment (optional)
        linewidth: Line width (optional)
    """

    __token_name__ = "rect"

    name: Optional[str] = field(
        default=None, metadata={"description": "Rectangle name", "required": False}
    )
    start: Start = field(
        default_factory=lambda: Start(), metadata={"description": "Start position"}
    )
    end: End = field(
        default_factory=lambda: End(), metadata={"description": "End position"}
    )
    comment: KiCadStr = field(
        default_factory=lambda: KiCadStr("comment", "", required=False),
        metadata={"description": "Comment", "required": False},
    )
    repeat: KiCadInt = field(
        default_factory=lambda: KiCadInt("repeat", 0, required=False),
        metadata={"description": "Repeat count", "required": False},
    )
    incrx: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incrx", 0.0, required=False),
        metadata={"description": "X increment", "required": False},
    )
    incry: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incry", 0.0, required=False),
        metadata={"description": "Y increment", "required": False},
    )
    linewidth: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("linewidth", 0.0, required=False),
        metadata={"description": "Line width", "required": False},
    )


@dataclass
class WksLine(KiCadObject):
    """Worksheet line definition token.

    Args:
        name: Line name (optional)
        start: Start position
        end: End position
        repeat: Repeat count (optional)
        incrx: X increment (optional)
        incry: Y increment (optional)
    """

    __token_name__ = "line"

    name: Optional[str] = field(
        default=None, metadata={"description": "Line name", "required": False}
    )
    start: Start = field(
        default_factory=lambda: Start(), metadata={"description": "Start position"}
    )
    end: End = field(
        default_factory=lambda: End(), metadata={"description": "End position"}
    )
    repeat: KiCadInt = field(
        default_factory=lambda: KiCadInt("repeat", 0, required=False),
        metadata={"description": "Repeat count", "required": False},
    )
    incrx: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incrx", 0.0, required=False),
        metadata={"description": "X increment", "required": False},
    )
    incry: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incry", 0.0, required=False),
        metadata={"description": "Y increment", "required": False},
    )


@dataclass
class WksTbText(KiCadObject):
    """Worksheet text block definition token.

    Args:
        text: Text content
        name: Text name (optional)
        pos: Text position
        font: Font settings (optional)
        justify: Text justification (optional)
        repeat: Repeat count (optional)
        incrx: X increment (optional)
        incry: Y increment (optional)
        comment: Comment (optional)
    """

    __token_name__ = "tbtext"

    text: str = field(default="", metadata={"description": "Text content"})
    name: KiCadStr = field(
        default_factory=lambda: KiCadStr("name", "", required=False),
        metadata={"description": "Text name", "required": False},
    )
    pos: Pos = field(
        default_factory=lambda: Pos(), metadata={"description": "Text position"}
    )
    font: Optional[Font] = field(
        default=None, metadata={"description": "Font settings", "required": False}
    )
    justify: Optional[Justify] = field(
        default=None, metadata={"description": "Text justification", "required": False}
    )
    repeat: KiCadInt = field(
        default_factory=lambda: KiCadInt("repeat", 0, required=False),
        metadata={"description": "Repeat count", "required": False},
    )
    incrx: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incrx", 0.0, required=False),
        metadata={"description": "X increment", "required": False},
    )
    incry: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incry", 0.0, required=False),
        metadata={"description": "Y increment", "required": False},
    )
    comment: KiCadStr = field(
        default_factory=lambda: KiCadStr("comment", "", required=False),
        metadata={"description": "Comment", "required": False},
    )


@dataclass
class KicadWks(KiCadObject):
    """KiCad worksheet definition token.

    The 'kicad_wks' token defines worksheet format information in the format::

        (kicad_wks
            (version VERSION)
            (generator GENERATOR)
            ;; contents of the schematic file...
        )

    Args:
        version: Format version (optional)
        generator: Generator name (optional)
        generator_version: Generator version (optional)
        page: Page settings (optional)
        title_block: Title block (optional)
        setup: Worksheet setup (optional)
        rect: List of rectangles (optional)
        line: List of lines (optional)
        tbtext: List of text blocks (optional)
        elements: List of worksheet elements (optional)
    """

    __token_name__ = "kicad_wks"
    __legacy_token_names__ = ["page_layout"]

    version: KiCadInt = field(
        default_factory=lambda: KiCadInt("version", 0, required=False),
        metadata={"description": "Format version", "required": False},
    )
    generator: KiCadStr = field(
        default_factory=lambda: KiCadStr("generator", "", required=False),
        metadata={"description": "Generator name", "required": False},
    )
    generator_version: KiCadStr = field(
        default_factory=lambda: KiCadStr("generator_version", "", required=False),
        metadata={"description": "Generator version", "required": False},
    )
    page: KiCadStr = field(
        default_factory=lambda: KiCadStr("page", "", required=False),
        metadata={"description": "Page settings", "required": False},
    )
    title_block: Optional[TitleBlock] = field(
        default=None, metadata={"description": "Title block", "required": False}
    )
    setup: Optional[WksSetup] = field(
        default=None, metadata={"description": "Worksheet setup", "required": False}
    )
    rect: Optional[List[WksRect]] = field(
        default_factory=list,
        metadata={"description": "List of rectangles", "required": False},
    )
    line: Optional[List[WksLine]] = field(
        default_factory=list,
        metadata={"description": "List of lines", "required": False},
    )
    tbtext: Optional[List[WksTbText]] = field(
        default_factory=list,
        metadata={"description": "List of text blocks", "required": False},
    )
    elements: Optional[List[Any]] = field(
        default_factory=list,
        metadata={"description": "List of worksheet elements", "required": False},
    )

    @classmethod
    def from_file(
        cls,
        file_path: str,
        strictness: ParseStrictness = ParseStrictness.STRICT,
        encoding: str = "utf-8",
    ) -> "KicadWks":
        """Parse from S-expression file - convenience method for worksheet operations."""
        if not file_path.endswith(".kicad_wks"):
            raise ValueError("Unsupported file extension. Expected: .kicad_wks")
        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()
        return cls.from_str(content, strictness)

    def save_to_file(self, file_path: str, encoding: str = "utf-8") -> None:
        """Save to .kicad_wks file format.

        Args:
            file_path: Path to write the .kicad_wks file
            encoding: File encoding (default: utf-8)
        """
        if not file_path.endswith(".kicad_wks"):
            raise ValueError("Unsupported file extension. Expected: .kicad_wks")
        content = self.to_sexpr_str()
        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)


# Image related elements
@dataclass
class Bitmap(KiCadObject):
    """Bitmap image definition token.

    The 'bitmap' token defines a bitmap image in the format::

        (bitmap
            (name "NAME")
            (pos X Y)
            (scale SCALAR)
            [(repeat COUNT)]
            [(incrx DISTANCE)]
            [(incry DISTANCE)]
            [(comment "COMMENT")]
            (pngdata IMAGE_DATA)
        )

    Args:
        name: Image name
        pos: Position coordinates
        scale: Scale factor
        repeat: Repeat count (optional)
        incrx: X increment distance (optional)
        incry: Y increment distance (optional)
        comment: Image comment (optional)
        pngdata: PNG image data
    """

    __token_name__ = "bitmap"

    name: KiCadStr = field(
        default_factory=lambda: KiCadStr("name", ""),
        metadata={"description": "Image name"},
    )
    pos: Pos = field(
        default_factory=lambda: Pos(), metadata={"description": "Position coordinates"}
    )
    scale: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("factor", 0.0),
        metadata={"description": "Scale factor"},
    )
    repeat: KiCadInt = field(
        default_factory=lambda: KiCadInt("repeat", 0, required=False),
        metadata={"description": "Repeat count", "required": False},
    )
    incrx: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incrx", 0.0, required=False),
        metadata={"description": "X increment distance", "required": False},
    )
    incry: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("incry", 0.0, required=False),
        metadata={"description": "Y increment distance", "required": False},
    )
    comment: Optional[str] = field(
        default=None, metadata={"description": "Image comment", "required": False}
    )
    pngdata: "Pngdata" = field(
        default_factory=lambda: Pngdata(), metadata={"description": "PNG image data"}
    )


@dataclass
class Image(KiCadObject):
    """Image definition token.

    The 'image' token defines an image object in PCB files in the format::

        (image (at X Y) (scale FACTOR) (uuid UUID) (data ...))

    Args:
        at: Position
        scale: Scale factor (optional)
        uuid: Unique identifier (optional)
        data: Image data (optional)
        locked: Whether image is locked (optional)
    """

    __token_name__ = "image"

    at: AtXY = field(
        default_factory=lambda: AtXY(), metadata={"description": "Position"}
    )
    scale: KiCadFloat = field(
        default_factory=lambda: KiCadFloat("scale", 1.0, required=False),
        metadata={"description": "Scale factor", "required": False},
    )
    uuid: Optional[Uuid] = field(
        default=None, metadata={"description": "Unique identifier", "required": False}
    )
    data: Optional[Data] = field(
        default=None, metadata={"description": "Image data", "required": False}
    )
    locked: OptionalFlag = field(
        default_factory=lambda: OptionalFlag("locked"),
        metadata={"description": "Whether image is locked", "required": False},
    )


@dataclass
class Pngdata(KiCadObject):
    """PNG data definition token.

    The 'pngdata' token defines PNG image data in the format::

        (pngdata
            (data XX1 ... XXN)
            (data XX1 ... XXN)
            ...
        )

    Where each data line contains up to 32 hexadecimal bytes.

    Args:
        data_lines: List of data token objects containing hexadecimal bytes
    """

    __token_name__ = "pngdata"

    data_lines: List[Data] = field(
        default_factory=list,
        metadata={
            "description": "List of data token objects containing hexadecimal bytes"
        },
    )
