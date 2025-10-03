"""A framework for extracting barcodes from objects using various strategies.

This module provides a flexible, strategy-pattern-based approach for parsing
barcode information from different types of source objects. The primary components
are the abstract `BarcodeExtractor` base class and its concrete implementations,
such as `TagExtractor` and `RegexExtractor`.
"""
from abc import ABC, abstractmethod
from typing import Protocol, Any, Iterable
import re

class BarcodeExtractor(ABC):
    """Abstract base class for barcode extraction strategies.

    This class defines the common interface for extracting and assembling a
    barcode string from a source object. Subclasses must implement the
    `get_parts` method to define their specific extraction logic.
    """
    separator: str

    def __init__(self, separator: str = "_"):
        """Initializes the extractor with a component separator.

        Args:
            separator: The string used to join the parts of the barcode.
        """
        self.separator = separator
    
    @abstractmethod
    def get_parts(self, barcoded: Any) -> tuple[str]:
        """Abstract method to extract barcode components from a source object.

        Args:
            barcoded: The source object containing barcode information.

        Returns:
            A tuple of strings representing the parts of the barcode.
        """
        ...
    
    def join(self, parts: Iterable[str]) -> str:
        """Joins barcode parts into a single string.

        Args:
            parts: An iterable of strings to be joined.

        Returns:
            The final barcode string.
        """
        return self.separator.join([str(part) for part in parts])

    def get_barcode(self, barcoded: Any) -> str:
        """Extracts and assembles the full barcode from a source object.

        This method orchestrates the extraction of parts and joins them into the
        final barcode string.

        Args:
            barcoded: The source object.

        Returns:
            The complete barcode string, or an empty string if no parts are found.
        """
        return self.join(self.get_parts(barcoded))

class Tagged(Protocol):
    """A Protocol for objects that have readable string tags.

    This is used for type hinting to ensure an object has the necessary
    `get_tag` and `has_tag` methods for the `TagExtractor`.
    """
    def get_tag(self, tag: str) -> str: ...
    def has_tag(self, tag: str) -> bool: ...

class TagExtractor(BarcodeExtractor):
    """Extracts a barcode by retrieving a sequence of tags from an object."""

    def __init__(self, tags: list[str], separator = "_"):
        """Initializes the extractor with an ordered list of tags.

        Args:
            tags: An ordered list of tag names to extract as barcode parts.
            separator: The string used to join the tag values.
        """
        super().__init__(separator = separator)
        self.tags = tags

    def get_parts(self, tagged: Tagged) -> tuple[str]:
        """Extracts barcode parts by reading tags from a source object.

        It retrieves tags in the order they were specified during initialization,
        skipping any tags that are not present on the object.

        Args:
            tagged: An object that conforms to the `Tagged` protocol.

        Returns:
            A tuple of the found tag values.
        """
        return (tagged.get_tag(tag) for tag in self.tags if tagged.has_tag(tag))

class RegexExtractor(BarcodeExtractor):
    """Extracts a barcode by applying a regex to an object's attribute.

    The captured groups from the regular expression match form the parts of
    the barcode.
    """
    attr: str
    pattern: re.Pattern

    def __init__(self, attr: str, pattern: str, separator = "_"):
        """Initializes the extractor with an attribute name and regex pattern.

        Args:
            attr: The name of the attribute on the source object to read from.
            pattern: The regular expression string to apply. Captured groups
                will become the barcode parts.
            separator: The string used to join the captured groups.
        """
        super().__init__(separator = separator)
        self.attr = attr
        self.pattern = re.compile(pattern)
    
    def get_parts(self, obj: Any) -> tuple[str]:
        """Extracts barcode parts from an object's attribute using a regex.

        Args:
            obj: The source object.

        Returns:
            A tuple of strings corresponding to the captured groups of the
            regex match, or an empty tuple if there is no match.
        """
        val = getattr(obj, self.attr)
        match = self.pattern.search(val)
        return match.groups() if match else tuple()
