class ConfigurationService(object):
    _recipe_size: int = 5

    @property
    def recipe_size(self) -> int:
        '''The number of ingredients in recipes'''
        return self._recipe_size
