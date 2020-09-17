from Page.back_stage_login import BackStageLogin


class Page:

    @classmethod
    def get_tp_login(cls):
        return BackStageLogin()
