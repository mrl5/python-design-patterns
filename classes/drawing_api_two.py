# -*- coding: utf-8 -*-


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))
