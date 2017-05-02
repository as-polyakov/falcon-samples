import falcon, json
import bonds.basis_rate as bs

class BondsResource:
    def __init__(self):
        self.generator = bs.BondBasisRateCalculator()

    def on_get(self, req, resp, isin):
        resp.satus = falcon.HTTP_200
        resp.body = json.dumps(self.generator.get_basis_rate(isin, req.get_param('start_date'), req.get_param('end_date')))

api = application = falcon.API()
api.add_route('/bonds/basis-rate/{isin}', BondsResource())
