
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'While' else -1
        self.value = value * value_sign
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self):
        pass


# El3skry
class Pawn(Piece):
    def __inti__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


# el7osan
class Knight(Piece):
    def __inti__(self, color):
        super().__init__('knight', color, 3.0)


# elfyl
class Bishop(Piece):
    def __inti__(self, color):
        super().__init__('bishop', color, 3.001)


# el tabya
class Rook(Piece):
    def __inti__(self, color):
        super().__init__('rook', color, 5.0)


# elwzer
class Queen(Piece):
    def __inti__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __inti__(self, color):
        super().__init__('king', color, 10000)
