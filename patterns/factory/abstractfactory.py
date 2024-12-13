# -*- coding: utf-8 -*-
# 抽象工厂

from abc import ABC, abstractmethod


class BYD:
    def __repr__(self):
        return "比亚迪"


class BMW:
    def __repr__(self):
        return "宝马"


class BMW_SUV:
    def __repr__(self):
        return "宝马SUV"


class BYD_SUV:
    def __repr__(self):
        return "比亚迪SUV"


class AbstractFactory(ABC):
    @abstractmethod
    def product_car(self):
        pass

    @abstractmethod
    def product_suv(self):
        pass


class BydFactory(AbstractFactory):
    def __str__(self):
        return "BYD工厂"

    def product_car(self):
        return BYD()

    def product_suv(self):
        return BYD_SUV()


class BmwFactory(AbstractFactory):
    def __str__(self):
        return "BMW工厂"

    def product_car(self):
        return BMW()

    def product_suv(self):
        return BMW_SUV()


if __name__ == "__main__":
    byd_factory = BydFactory()
    print(byd_factory.product_car())
    print(byd_factory.product_suv())

    bmw_factory = BmwFactory()
    print(bmw_factory.product_car())
    print(bmw_factory.product_suv())

