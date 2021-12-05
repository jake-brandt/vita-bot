class RecipeEntry(object):
    _fdc_id: int
    _pct_100_grams: float

    def __init__(self, fdc_id, pct_100_grams):
        self._fdc_id = fdc_id
        self._pct_100_grams = pct_100_grams

    @property
    def fdc_id(self) -> int:
        '''FDC ID of this ingredient'''
        return self._fdc_id

    @property
    def percent_100_grams(self) -> float:
        '''Amount of this ingredient, in percent of 100 grams'''
        return self._pct_100_grams

    @property
    def mass_g(self) -> float:
        '''Mass of this ingredient, in grams'''
        return self._pct_100_grams * 100
