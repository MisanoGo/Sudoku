from random import choice, randint
from typing import Generator ,List ,Tuple ,Dict
from itertools import product

from utils import NoneFilter, checkListDepublicate as cld,noneable

class SudokuDecart:
    range9 = range(1,10)
    cleanSudoku = {(x,y):None for x,y in product(range9,range9)}

    def __init__(self, decart= None) -> None:
        self.decart: Dict[Tuple[int,int]:int]= noneable(decart,self.cleanSudoku)

    def set(self, x: int, y: int, num: int):
        xy = (x,y)
        decart_copy = self.decart.copy()
        self.decart[xy] = num

        if self.checkCoordDepublicate(x,y):
            self.decart = decart_copy
            # TODO : raise Exception of depublicate value

    def randSet(self, x: int = None, y: int = None, n: int = None):
        n   = noneable(n, randint(1,9))
        x,y = choice(list(self.blankFields.items()))[0]

        self.set(x,y,n)

    @property
    def blankFields(self):
        return dict(filter(lambda i : i[1] is None, list(self.decart.items())))

    def get(self, x: int, y: int) -> int:
        xy = (x,y)
        return self.decart[xy]

    def getList(self, *coord: Tuple[int,int]) -> List[int]:
        return [self.get(*xy) for xy in coord]

    def getCAR(self, x: int, y: int) -> List[List[int]]:
        return [self.row(y),self.column(x),self.area(x,y)]

    def unset(self, x: int, y: int) -> int:
        xy = (x,y)
        n = self.get(x,y)

        self.decart[xy] = None
        return n

    def clean(self):
        self.decart = self.cleanSudoku

    def row(self, y: int) -> List[int]:
        if y in self.range9:
            return [self.decart[(x,y)] for x in self.range9]

    def column(self, x: int) -> List[int]:
        if x in self.range9:
            return [self.decart[(x,y)] for y in self.range9]

    def area(self, x: int, y: int) -> List[int]:
        """ return list of numbers in area of 3*3"""
        # get the area index in decart coordination
        ax = int(x//3.5)+1
        ay = int(y//3.5)+1
        return self.nArea(ax,ay)

    def nArea(self, ax: int, ay: int) -> List[int]:
        # get the start and stop coordination of area
        sx,sy = (ax*3)-2,(ay*3)-2
        dx,dy = ax*3,ay*3
        # get all of items coords in area and get theres numbers
        return self.getList(*product(range(sx,dx+1),range(sy,dy+1)))

    @property
    def rowList(self) -> List[List[int]]:
        return [self.row(y) for y in self.range9]

    @property
    def columnList(self) -> List[List[int]]:
        return [self.column(x) for x in self.range9]

    @property
    def areaList(self) -> List[List[int]]:
        range3 = range(1,4)
        return [self.nArea(ax,ay) for ax,ay in product(range3,range3)]

    @property
    def check(self) -> bool:
        ivl = NoneFilter(self.decart.values()) # item value list

        if len(self.blankFields) == 0 : # check to dont exists blank fields
            if sum(ivl) == (9*(9+1)//2)*9: # check sum of all numbers is 405
                return self.checkDepublicate # go to check all of numbers depublicates
        return False

    @property
    def checkDepublicate(self) -> bool:
        nl = list(self.rowList()) + list(self.columnList()) + list(self.areaList())
        return cld(*nl)

    def checkCoordDepublicate(self, x: int, y: int) -> bool:
        return cld(*self.getCAR(x,y))
