#!/usr/bin/env python3
# -----------------------------------------------------------------------------.
# Copyright (c) 2021-2023 DISDRODB developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------.
"""Reader for SHMI OTT Parsivel2."""
import pandas as pd

from disdrodb.l0.l0_reader import is_documented_by, reader_generic_docstring
from disdrodb.l0.l0a_processing import read_raw_text_file


def parse_old_format(df):
    """Reformat old format."""
    # Remove rows with invalid number of separators
    df = df[df["TO_PARSE"].str.count(";") == 1106]

    # Split the columns
    df = df["TO_PARSE"].str.split(";", n=18, expand=True)

    # Assign column names
    names = [
        "time",
        "rainfall_rate_32bit",
        "rainfall_accumulated_32bit",
        "weather_code_synop_4680",  # wawa
        "reflectivity_32bit",
        "mor_visibility",
        "sample_interval",
        "laser_amplitude",
        "number_particles",
        "sensor_temperature",
        "sensor_serial_number",
        "firmware_iop",
        "sensor_heating_current",
        "sensor_battery_voltage",
        "sensor_status",
        "station_id",
        "rainfall_amount_absolute_32bit",
        "error_code",
        "TO_SPLIT",
    ]

    df.columns = names

    # Derive raw arrays
    df_split = df["TO_SPLIT"].str.split(";", expand=True)
    df["raw_drop_concentration"] = df_split.iloc[:, :32].agg(",".join, axis=1)
    df["raw_drop_average_velocity"] = df_split.iloc[:, 32:64].agg(",".join, axis=1)
    df["raw_drop_number"] = df_split.iloc[:, 64:1088].agg(",".join, axis=1)

    # Ensure the time column is datetime dtype
    df["time"] = df["time"].str[0:12] + "00"
    df["time"] = pd.to_datetime(df["time"], format="%Y%m%d%H%M%S", errors="coerce")

    # Drop columns not agreeing with DISDRODB L0 standards
    columns_to_drop = [
        "sensor_serial_number",
        "firmware_iop",
        "station_id",
        "TO_SPLIT",
    ]
    df = df.drop(columns=columns_to_drop)

    # Return the dataframe adhering to DISDRODB L0 standards
    return df


def parse_new_format(df):
    """Reformat new format."""
    # Remove rows with invalid number of separators
    df = df[df["TO_PARSE"].str.count(";") == 1106]

    # Split the columns
    df = df["TO_PARSE"].str.split(";", n=18, expand=True)

    # Assign column names
    names = [
        "time",
        "rainfall_rate_32bit",
        "rainfall_accumulated_32bit",
        "weather_code_synop_4680",  # wawa
        "reflectivity_32bit",
        "mor_visibility",
        "sample_interval",
        "laser_amplitude",
        "number_particles",
        "sensor_temperature",
        "sensor_serial_number",
        "firmware_iop",
        "sensor_heating_current",
        "sensor_battery_voltage",
        "sensor_status",
        "station_id",
        "rainfall_amount_absolute_32bit",
        "error_code",
        "TO_SPLIT",
    ]

    df.columns = names

    # Derive raw arrays
    df_split = df["TO_SPLIT"].str.split(";", expand=True)
    df["raw_drop_concentration"] = df_split.iloc[:, :32].agg(",".join, axis=1)
    df["raw_drop_average_velocity"] = df_split.iloc[:, 32:64].agg(",".join, axis=1)
    df["raw_drop_number"] = df_split.iloc[:, 64:1088].agg(",".join, axis=1)

    # Add the time column
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S", errors="coerce")

    # Drop columns not agreeing with DISDRODB L0 standards
    columns_to_drop = [
        "sensor_serial_number",
        "firmware_iop",
        "station_id",
        "TO_SPLIT",
    ]
    df = df.drop(columns=columns_to_drop)

    # Return the dataframe adhering to DISDRODB L0 standards
    return df


@is_documented_by(reader_generic_docstring)
def reader(
    filepath,
    logger=None,
):
    """Reader."""
    ##------------------------------------------------------------------------.
    #### Define column names
    column_names = ["TO_PARSE"]

    ##------------------------------------------------------------------------.
    #### Define reader options
    reader_kwargs = {}
    # Skip first row as columns names
    reader_kwargs["header"] = None
    # Skip file with encoding errors
    reader_kwargs["encoding_errors"] = "ignore"
    # - Define delimiter
    reader_kwargs["delimiter"] = "\\n"
    # - Avoid first column to become df index !!!
    reader_kwargs["index_col"] = False
    # - Define behaviour when encountering bad lines
    reader_kwargs["on_bad_lines"] = "skip"

    # - Define reader engine
    #   - C engine is faster
    #   - Python engine is more feature-complete
    reader_kwargs["engine"] = "python"
    # - Define on-the-fly decompression of on-disk data
    #   - Available: gzip, bz2, zip
    reader_kwargs["compression"] = "infer"
    # - Strings to recognize as NA/NaN and replace with standard NA flags
    #   - Already included: '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN',
    #                       '-NaN', '-nan', '1.#IND', '1.#QNAN', '<NA>', 'N/A',
    #                       'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null'
    reader_kwargs["na_values"] = ["na", "", "error", "NA", "-.-"]

    ##------------------------------------------------------------------------.
    #### Read the data
    df = read_raw_text_file(
        filepath=filepath,
        column_names=column_names,
        reader_kwargs=reader_kwargs,
        logger=logger,
    )

    ##------------------------------------------------------------------------.
    #### Adapt the dataframe to adhere to DISDRODB L0 standards
    if df["TO_PARSE"].iloc[0].startswith("datetime_utc"):
        # Remove header if present (2025 onward)
        df = df.iloc[1:]
        # Parse new format
        return parse_new_format(df)
    return parse_old_format(df)
