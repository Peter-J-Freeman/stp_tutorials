import requests


class VepApi:
    def __init__(self, genome_build="grch38", species="human", content_type="application/json"):
        self.url = None
        self.genome_build = genome_build
        self.endpoint = None
        self.species = species
        self.content_type = content_type

    def __vep_url_grch38(self):
        self.url = f"https://rest.ensembl.org/vep/{self.species}/{self.endpoint}/"

    def __vep_url_grch37(self):
        self.url = f"https://grch37.rest.ensembl.org/vep/{self.species}/{self.endpoint}/"

    def vep_coding_variant(self, variant=None, params={}):
        self.endpoint = "hgvs"
        params["content-type"] = self.content_type
        if self.genome_build == "grch37":
            self.__vep_url_grch37()
        elif self.genome_build == "grch38":
            self.__vep_url_grch38()
        url = self.url + f"{variant}/"
        headers = {
            "Accept": self.content_type
        }
        response = requests.get(url, params=params, headers=headers)
        return response


if __name__ == "__main__":
    vep_api_38 = VepApi()
    vep_api_37 = VepApi(genome_build="grch37")
    rsp_38 = vep_api_38.vep_coding_variant(variant="NM_000088.4:c.589G>T", params={"dbNSFP": "REVEL_score"})
    rsp_37 = vep_api_37.vep_coding_variant(variant="NM_000088.4:c.589G>T", params={"dbNSFP": "REVEL_score"})
    print(rsp_38.url)
    print(rsp_37.url)


g






