from utils.TrialConstants import CLASS_CONSTANT


class Trial:

    def __init__(self, account=None, mark1=None, mark2=None):
        self.account = account
        self.mark1 = mark1
        self.mark2 = mark2

    def is_passed(self):
        return self.mark1 + self.mark2 > CLASS_CONSTANT

    @staticmethod
    def copy():
        return Trial()

    def set_account(self, account):
        self.account = account

    def set_mark1(self, mark1):
        self.mark1 = mark1

    def set_mark2(self, mark2):
        self.mark2 = mark2

    def get_account(self):
        return self.account

    def get_mark1(self):
        return self.mark1

    def get_mark2(self):
        return self.mark2

    def __eq__(self, other):
        if isinstance(other, Trial):
            return \
                self.account == other.account \
                and self.mark1 == other.mark1 \
                and self.mark2 == other.mark2
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.account, self.mark1, self.mark2))

    def __str__(self):
        return "{}; trial is passed - {}" \
            .format(self.fields_to_string(), self.is_passed())

    def fields_to_string(self):
        return "{}; His marks : {}; {}" \
            .format(self.account, self.mark1, self.mark2)
