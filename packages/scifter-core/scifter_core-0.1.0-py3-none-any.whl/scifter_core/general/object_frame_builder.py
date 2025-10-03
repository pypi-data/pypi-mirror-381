"""Tools for converting iterables of Python objects into Polars DataFrames.

This module provides a structured and efficient way to extract attributes from
complex Python objects and represent them in a Polars DataFrame for fast,
vectorized processing, while retaining a reference to the original objects.
"""

from dataclasses import dataclass
from typing import Callable, Any, Iterable, List, Generator
from itertools import batched

import polars as pl

@dataclass
class FieldExtractor:
    """A data class to configure the extraction of a single field from an object.

    This class bundles the desired column name, its Polars data type, and the
    function used to extract the value from a source object.

    Attributes:
        name: The name of the resulting column in the DataFrame.
        dtype: The Polars DataType for the new column.
        extractor: A callable that takes a source object and returns the
            extracted value.
    """
    name: str
    dtype: pl.DataType
    extractor: Callable[[Any], Any]

class ObjectFrameBuilder:
    """Builds a Polars DataFrame from an iterable of Python objects.

    This class uses a predefined list of FieldExtractor configurations to create
    new columns based on attributes of the source objects. The final DataFrame
    contains a column with the original objects plus the new extracted columns.
    """
    extractors: List[FieldExtractor]
    object_col: str
    _struct_dtype: pl.Struct

    def __init__(self, extractors: List[FieldExtractor], object_col: str = "object"):
        """Initializes the builder with a list of extractors.

        Args:
            extractors: A list of FieldExtractor objects defining what data to
                extract from the source objects.
            object_col: The desired name for the column that will hold the
                original source objects.
        """
        self.extractors = extractors
        self.object_col = object_col

        self._struct_dtype = pl.Struct([
            pl.Field(e.name, e.dtype) for e in self.extractors
        ])

    def _create_record(self, obj: Any) -> dict[str, Any]:
        """Creates a dictionary record from a single source object.

        This internal method applies all configured extractors to one object.

        Args:
            obj: The source object.

        Returns:
            A dictionary where keys are field names and values are the
            extracted data.
        """
        return {e.name: e.extractor(obj) for e in self.extractors}

    def to_polars(self, objects: Iterable[Any], dtype: pl.DataType = pl.Object) -> pl.DataFrame:
        """Converts an iterable of objects into a Polars DataFrame.

        This is the main method of the builder. It takes the objects, applies
        the extraction logic to each one, and returns a structured DataFrame.

        Args:
            objects: An iterable of source objects to process.

        Returns:
            A Polars DataFrame containing the original objects and the
            extracted attribute columns.
        """
        return (
            pl.DataFrame({self.object_col: pl.Series(objects, dtype = dtype)})
            .with_columns(
                pl.col(self.object_col)
                .map_elements(
                    self._create_record,
                    return_dtype=self._struct_dtype,
                )
                .alias("attributes")
            )
            .unnest("attributes")
        )

def stream_to_polars(
    iterable: Iterable[Any], 
    batch_size: int, 
    extractors: List[FieldExtractor], 
    object_col: str = "object"
    ) -> Generator[pl.DataFrame, None, None]:
    """Processes a large iterable of objects in batches, yielding each as a DataFrame.

    This generator function is useful for streaming data and processing large
    collections that may not fit into memory at once.

    Args:
        iterable: The source iterable of objects to process.
        batch_size: The number of objects to process in each batch.
        extractors: A list of FieldExtractor objects defining the extraction logic.
        object_col: The name for the column that will hold the original objects.

    Yields:
        A Polars DataFrame for each batch of objects from the iterable.
    """
    processor = ObjectFrameBuilder(extractors, object_col)
    for batch in batched(iterable, batch_size):
        yield processor.to_polars(batch)