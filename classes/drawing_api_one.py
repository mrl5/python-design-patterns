# -*- coding: utf-8 -*-


class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))
