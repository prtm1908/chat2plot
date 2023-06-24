from textwrap import dedent

import pandas as pd


def description(
    df: pd.DataFrame, description_strategy: str = "head", num_rows: int = 5
) -> str:
    """Returns a description of the given data for LLM"""

    if description_strategy == "head":
        return description_by_head(df, num_rows)
    elif description_strategy == "dtypes":
        return description_by_dtypes(df)
    else:
        raise ValueError(f"Unknown description_strategy: {description_strategy}")


def description_by_head(df: pd.DataFrame, num_rows: int = 5) -> str:
    head_part = str(df.sample(num_rows, random_state=0).to_markdown())

    return dedent(
        f"""
        This is the result of `print(df.head())`:

        {head_part}
        """
    )


def description_by_dtypes(df: pd.DataFrame) -> str:
    return dedent(
        f"""
        This is the result of `print(df.dtypes)`:

        {str(df.dtypes.to_markdown())}
        """
    )
