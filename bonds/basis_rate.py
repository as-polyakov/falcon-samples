from random import randint

class BondBasisRateCalculator:
    def get_basis_rate(self, isin, start_date, end_date):
        return (isin, start_date, end_date, randint(1, 100))
