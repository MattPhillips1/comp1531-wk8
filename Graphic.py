from Rectangle import Rectangle, Circle
#  https://github.com/MattPhillips1/comp1531-wk8


class Graphic:

    def area_calculator(self, shape):
        return shape.area()

    def scale(self, shape, ratio):
        shape.scale(ratio)


