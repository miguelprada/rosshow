import time
import math
import librosshow.termgraphics as termgraphics
from librosshow.plotters import ScopePlotter, AnglePlotter

class TwistViewer(object):
    def __init__(self, canvas, title = ""):
        self.g = canvas
        self.last_update_shape_time = 0
        self.title = title
        self.right = 10
        self.vx = [ 0. ] * 128
        self.vx_p = 0
        self.vy = [ 0. ] * 128
        self.vy_p = 0
        self.vz = [ 0. ] * 128
        self.vz_p = 0
        self.vrx = [ 0. ] * 128
        self.vrx_p = 0
        self.vry = [ 0. ] * 128
        self.vry_p = 0
        self.vrz = [ 0. ] * 128
        self.vrz_p = 0

        hmargin = self.g.shape[0]/40.
        vmargin = self.g.shape[1]/20.
        hsize = (self.g.shape[0] - 4*hmargin ) / 2
        vsize = (self.g.shape[1] - 4*vmargin ) / 3

        self.vx_scope_plotter = ScopePlotter(self.g,
            left = hmargin,
            top = vmargin,
            right = hmargin + hsize,
            bottom = vmargin + vsize,
            ymin = None,
            ymax = None,
            title = "vel x",
        )

        self.vy_scope_plotter = ScopePlotter(self.g,
            left = hmargin,
            top = 2*vmargin + vsize,
            right = hmargin + hsize,
            bottom = 2*vmargin + 2*vsize,
            ymin = None,
            ymax = None,
            title = "vel y",
        )

        self.vz_scope_plotter = ScopePlotter(self.g,
            left = hmargin,
            top = 3*vmargin + 2*vsize,
            right = hmargin + hsize,
            bottom = 3*vmargin + 3*vsize,
            ymin = None,
            ymax = None,
            title = "vel z",
        )

        self.vrx_scope_plotter = ScopePlotter(self.g,
            left = 2*hmargin + hsize,
            top = vmargin,
            right = 2*hmargin + 2*hsize,
            bottom = vmargin + vsize,
            ymin = None,
            ymax = None,
            title = "vel rx",
        )

        self.vry_scope_plotter = ScopePlotter(self.g,
            left = 2*hmargin + hsize,
            top = 2*vmargin + vsize,
            right = 2*hmargin + 2*hsize,
            bottom = 2*vmargin + 2*vsize,
            ymin = None,
            ymax = None,
            title = "vel ry",
        )

        self.vrz_scope_plotter = ScopePlotter(self.g,
            left = 2*hmargin + hsize,
            top = 3*vmargin + 2*vsize,
            right = 2*hmargin + 2*hsize,
            bottom = 3*vmargin + 3*vsize,
            ymin = None,
            ymax = None,
            title = "vel rz",
        )

    def keypress(self, c):
        return

    def update(self, data):
        self.vx_scope_plotter.update(data.linear.x)
        self.vy_scope_plotter.update(data.linear.y)
        self.vz_scope_plotter.update(data.linear.z)
        self.vrx_scope_plotter.update(data.angular.x)
        self.vry_scope_plotter.update(data.angular.y)
        self.vrz_scope_plotter.update(data.angular.z)

    def draw(self):
        t = time.time()

        # capture changes in terminal shape at least every 0.5s
        if t - self.last_update_shape_time > 0.25:
            self.g.update_shape()
            self.last_update_shape_time = t

        self.g.clear()
        self.g.set_color(termgraphics.COLOR_WHITE)
        self.vx_scope_plotter.plot()
        self.vy_scope_plotter.plot()
        self.vz_scope_plotter.plot()
        self.vrx_scope_plotter.plot()
        self.vry_scope_plotter.plot()
        self.vrz_scope_plotter.plot()
        if self.title:
            self.g.set_color((0, 127, 255))
            self.g.text(self.title, (0, self.g.shape[1] - 4))
        self.g.draw()
