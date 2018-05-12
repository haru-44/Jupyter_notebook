from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics.pairwise import euclidean_distances

class CoordinateTransformerBase(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return self
    def _getDistance3(self, X):
        return euclidean_distances(X, [[0, 0, 0]])

#3次元直交座標から球座標に変換する
class CartesianToSphericalTransformer(CoordinateTransformerBase):
    def __init__(self):
        pass
    def transform(self, X):
        # 'phi'は、x-y平面に対する角度
        # x = r sin(theta)cos(phi)
        # y = r sin(theta)cos(phi)
        # z = r cos(theta)
        # を満たす。
        r = super()._getDistance3(X).reshape(-1,)
        if type(X) is pd.DataFrame :
            x = X['x']
            y = X['y']
            z = X['z']
        else:
            x = [row[0] for row in X]
            y = [row[1] for row in X]
            z = [row[2] for row in X]
        return pd.DataFrame({'r' : r, 
                            'theta' : np.arccos(z / r),
                            'phi' : np.arctan2(y, x)})
