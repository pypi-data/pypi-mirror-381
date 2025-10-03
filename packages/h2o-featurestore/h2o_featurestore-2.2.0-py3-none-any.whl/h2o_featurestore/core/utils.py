import base64
import datetime
import hashlib
import json
import os
import tempfile
import textwrap
import warnings
from typing import Optional

import requests
from dateutil import tz


class Utils:
    @staticmethod
    def pretty_print_proto(m):
        return m.__repr__()

    @staticmethod
    def proto_to_dict(m):
        return m.to_dict()

    @staticmethod
    def output_indent_spacing(m, space):
        return textwrap.indent(m, space)

    @staticmethod
    def timestamp_to_string(timestamp: datetime.datetime) -> Optional[str]:
        if timestamp:
            return Utils.convert_timestamp_to_str_with_zone(timestamp)
        return None

    @staticmethod
    def is_running_on_databricks() -> bool:
        try:
            from pyspark.sql import SparkSession  # type: ignore

            spark = SparkSession.getActiveSession()
            spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion")
            return True
        except Exception:
            return False

    @staticmethod
    def read_env(variable_name, source):
        value = os.environ.get(variable_name)
        if value is None:
            raise Exception(
                "Environment variable "
                + variable_name
                + " is missing, it is required to read from "
                + source
                + " data source."
            )
        else:
            return value

    @staticmethod
    def download_files(output_dir, download_links):
        if output_dir is None:
            output_dir = tempfile.mkdtemp()
        for idx, path in list(enumerate(download_links)):
            dest = os.path.join(output_dir, "part_" + str(idx) + ".parquet")
            Utils.download_file(dest, path)
        return output_dir

    @staticmethod
    def download_file(dest, origin):
        with requests.get(origin, stream=True) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return dest

    @staticmethod
    def fetch_preview_as_json_array(preview_url: str):
        with requests.get(preview_url) as r:
            r.raise_for_status()
            if r.text:
                preview_array = r.text.strip().split("\n")
                return [json.loads(item) for item in preview_array]
            else:
                return []

    @staticmethod
    def generate_md5_checksum(file) -> str:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return base64.b64encode(hash_md5.digest()).decode("utf-8")

    @staticmethod
    def convert_timestamp_to_str_with_zone(timestamp: datetime.datetime) -> str:
        from_zone = tz.gettz("UTC")
        client_zone = tz.tzlocal()
        return timestamp.replace(tzinfo=from_zone).astimezone(client_zone).strftime("%Y-%m-%dT%H:%M:%S %z")

    @staticmethod
    def ensure_timezone_aware(timestamp: datetime.datetime) -> datetime.datetime:
        if timestamp.tzinfo is None:
            # Assume UTC if no timezone is provided
            return timestamp.replace(tzinfo=tz.UTC)
        return timestamp

    @staticmethod
    def warn_deprecated(message):
        warnings.warn(message, DeprecationWarning, stacklevel=2)

    @staticmethod
    def filepath_directory_exists(filepath):
        if os.path.exists(filepath):
            # filepath is either existing file or directory
            return True
        else:
            # check directory part of the filepath
            directory = os.path.dirname(filepath)
            return os.path.exists(directory)
