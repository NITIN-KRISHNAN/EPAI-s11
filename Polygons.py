from Polygon import Polygon


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]
        print("after init")

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

    def __iter__(self):
        print("Calling polygons instance __iter__")
        return self.PolygonIterator(self)

    class PolygonIterator:
        def __init__(self, polygons_obj):
            # cities is an instance of Cities
            print("Calling PolygonIterator __init__")
            self._polygons_obj = polygons_obj
            self._index = 0

        def __iter__(self):
            print("Calling PolygonIterator instance __iter__")
            return self

        def __next__(self):
            print("Calling PolygonIterator __next__")
            if self._index >= len(self._polygons_obj):
                raise StopIteration
            else:
                item = self._polygons_obj._polygons[self._index]
                self._index += 1
                return item