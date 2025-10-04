import os
from dataclasses import dataclass
from functools import cached_property

from utils import WWW, File, Log, TSVFile

from gig.core.GIGConstants import GIGConstants

log = Log("EntType")


@dataclass
class EntType:
    name: str

    @staticmethod
    def from_id(id: str):
        if id == "LK":
            return EntType.COUNTRY

        prefix = id.partition("-")[0]
        n = len(id)

        return EntType.ID_TYPE_CONFIG.get(prefix, {}).get(n, EntType.UNKNOWN)

    @staticmethod
    def list():
        return [
            EntType.COUNTRY,
            EntType.PROVINCE,
            EntType.DISTRICT,
            EntType.DSD,
            EntType.GND,
            EntType.ED,
            EntType.PD,
            EntType.LG,
            EntType.MOH,
        ]

    @property
    def url_remote_data_path(self):
        return f"{GIGConstants.URL_BASE}/ents/{self.name}.tsv"

    @property
    def temp_data_path(self):
        temp_gig_dir_ents = os.path.join(GIGConstants.TEMP_GIG_DIR, "ents")
        os.makedirs(temp_gig_dir_ents, exist_ok=True)
        return os.path.join(temp_gig_dir_ents, f"{self.name}.tsv")

    @cached_property
    def remote_data_list(self) -> list:
        if not os.path.exists(self.temp_data_path):
            content = WWW(self.url_remote_data_path).read()
            File(self.temp_data_path).write(content)
            log.debug(
                f"Downloaded {self.url_remote_data_path}"
                + f" to {self.temp_data_path}"
            )
        d_list = TSVFile(self.temp_data_path).read()
        n = len(d_list)
        log.debug(f"Loaded {n} records from {self.temp_data_path}")
        return d_list


EntType.COUNTRY = EntType("country")
EntType.PROVINCE = EntType("province")
EntType.DISTRICT = EntType("district")
EntType.DSD = EntType("dsd")
EntType.GND = EntType("gnd")
EntType.ED = EntType("ed")
EntType.PD = EntType("pd")
EntType.LG = EntType("lg")
EntType.MOH = EntType("moh")
EntType.UNKNOWN = EntType("unknown")

EntType.ID_TYPE_CONFIG = {
    "LK": {
        2: EntType.COUNTRY,
        4: EntType.PROVINCE,
        5: EntType.DISTRICT,
        7: EntType.DSD,
        10: EntType.GND,
    },
    "EC": {
        5: EntType.ED,
        6: EntType.PD,
    },
    "LG": {
        8: EntType.LG,
    },
    "MOH": {
        9: EntType.MOH,
    },
}
