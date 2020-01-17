from varsome_api.client import VarSomeAPIClient, VarSomeAPIException
from varsome_api.models.variant import AnnotatedVariant

class Varsome():

    api_key = 'ABgxPSr6UD*mseWP22!ZC?01Or#1O&&hYUrCorQf'

    api = VarSomeAPIClient(api_key)

    def send_req(self, rs_No):
        result = Varsome.api.lookup(rs_No, params={'add-source-databases': 'all' },  ref_genome='hg19')
        annotated_variant = AnnotatedVariant(**result)
        return annotated_variant

    def clinvar_verdict_f(self, variant):
        try:
            return variant.ncbi_clinvar2[0].clinical_significance
        except IndexError:
            return("CLINVAR VERISI YOK")

    def DANN_score_f(self, variant):
        try:
            return variant.dann_snvs[0].dann_score
        except IndexError:
            return("DANN VERISI YOK")

    def GERP_score_f(self, variant):
        try:
            return variant.gerp[0].gerp_nr
        except IndexError:
            return("GERP VERISI YOK")

    def gnomAD_Freq_f(self, variant):
        try:
            return variant.gnomad_genomes_af
        except IndexError:
            return("gnomAD VERISI YOK")

    def ACMG_verdict_f(self, variant):
        try:
            return variant.acmg_annotation
        except IndexError:
            return("ACMG VERISI YOK")

    def mutationtaster_pred_f(self, variant):
        try:
            return variant.dbnsfp[0].mutationtaster_pred
        except IndexError:
            return("MUTATIONTASTER VERISI YOK")

    def SIFT_pred_f(self, variant):
        try:
            return variant.dbnsfp[0].sift_prediction
        except IndexError:
            return("SIFT VERISI YOK")

    def SIFT_score_f(self, variant):
        try:
            return variant.dbnsfp[0].sift_converted_rankscore
        except IndexError:
            return("SIFT VERISI YOK")

    def PROVEAN_pred_f(self, variant):
        try:
            return variant.dbnsfp[0].provean_pred
        except IndexError:
            return("PROVEAN VERISI YOK")

    def PROVEAN_score_f(self, variant):
        try:
            return variant.dbnsfp[0].provean_converted_rankscore
        except IndexError:
            return("PROVEAN VERISI YOK")

'''
    def MutationTaster_verdict_f(self, variant):
        try:
            return variant.ncbi_clinvar2[0].clinical_significance
        except IndexError:
            print("===== CLINVAR VERISI YOK ====")

    def SIFT_score_f(self, variant):
        try:
            return variant.ncbi_clinvar2[0].clinical_significance
        except IndexError:
            print("===== CLINVAR VERISI YOK ====")

    def PROVEAN_score_f(self, variant):
        try:
            return variant.ncbi_clinvar2[0].clinical_significance
        except IndexError:
            print("===== CLINVAR VERISI YOK ====")
'''

