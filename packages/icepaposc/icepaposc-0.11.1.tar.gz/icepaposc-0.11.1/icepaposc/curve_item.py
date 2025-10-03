#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# This file is part of IcepapOCS link:
#        https://github.com/ALBA-Synchrotron/IcepapOCS
#
# Copyright 2017:
#       MAX IV Laboratory, Lund, Sweden
#       CELLS / ALBA Synchrotron, Bellaterra, Spain
#
# Distributed under the terms of the GNU General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
#
# You should have received a copy of the GNU General Public License
# along with IcepapOCS. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

from PyQt5 import QtCore, QtGui
from collections import namedtuple
from threading import RLock
from pyqtgraph import PlotCurveItem, PlotDataItem


class CurveItem:
    """Represents a curve to be plotted in a diagram."""

    def __init__(self, subscription_id, driver_addr, sig_name, y_axis,
                 linecolor, linestyle, linemarker):
        """
        Initializes an instance of class CurveItem.

        driver_addr - IcePAP driver address.
        sig_name    - Signal name.
        y_axis      - Y axis to plot against.
        """
        self.subscription_id = subscription_id
        self.driver_addr = driver_addr
        self.signal_name = sig_name
        self.y_axis = y_axis
        self.array_time = []
        self.array_val = []
        self.array_val_corr = []
        self.val_min = 0
        self.val_max = 0
        self.val_cross = 0
        self.val_local_min = 0
        self.val_local_max = 0
        self.last_idx_min = 0
        self.last_idx_max = 0
        self.color = linecolor
        self.pen = {'color': linecolor,
                    'width': 1,
                    'style': linestyle}
        self.symbol = linemarker
        self.curve = None
        self.lock = RLock()
        self.signature = ''
        self.update_signature()
        if sig_name.upper().startswith("POS"): 
            self.signal_type = 1
        elif sig_name.upper().startswith("DIF"):
            self.signal_type = 3
        elif sig_name.upper().startswith("ENC"):
            self.signal_type = 2
        elif sig_name.upper().startswith("VEL"):
            self.signal_type = 3
        else:
            self.signal_type = 0
        self.corr_factors = [1,0,1,0]

    def update_signature(self):
        """Sets the new value of the signature string."""
        self.signature = '{}:{}:{}'.format(self.driver_addr,
                                           self.signal_name,
                                           self.y_axis)

    def create_curve(self):
        """Creates a new plot item."""
        with self.lock:
            if self.symbol != '':
                self.curve = PlotDataItem(x=self.array_time,
                                          y=self.array_val_corr,
                                          pen=self.pen,
                                          symbol=self.symbol,
                                          symbolBrush=QtGui.QBrush(self.color),
                                          symbolPen=self.color)
            else:
                self.curve = PlotDataItem(x=self.array_time,
                                          y=self.array_val_corr,
                                          pen=self.pen)

        return self.curve

    def update_curve(self, time_min, time_max, corr_factors=[]):
        """Updates the curve with recent collected data."""
        with self.lock:
            if corr_factors != None and corr_factors != [] :
                self.corr_factors = corr_factors
                self.update_array_val_corr()
            self.last_idx_min = self.get_time_index(time_min)
            self.last_idx_max = self.get_time_index(time_max)
            self.curve.setData(x=self.array_time[self.last_idx_min:self.last_idx_max],
                               y=self.array_val_corr[self.last_idx_min:self.last_idx_max])
                               
    def update_array_val_corr(self):
        if self.signal_type == 1:
            self.array_val_corr = [self.corr_factors[0]*x + self.corr_factors[1] for x in self.array_val]
        elif self.signal_type == 2:
            self.array_val_corr = [self.corr_factors[2]*x + self.corr_factors[3] for x in self.array_val]
        elif self.signal_type == 3:
            self.array_val_corr = [self.corr_factors[0]*x for x in self.array_val]
        self.val_min = min(self.array_val_corr)
        self.val_max = max(self.array_val_corr)
    
    def calculate_val_corr(self, val):
        if self.signal_type == 1:
            return val * self.corr_factors[0] + self.corr_factors[1]
        elif self.signal_type == 2:
            return val * self.corr_factors[2] + self.corr_factors[3]
        elif self.signal_type == 3:
            return val * self.corr_factors[0]
        else:
            return val
    
    def calculate_local_min(self, t1, t2):
        idx_min = self.get_time_index(t1)
        idx_max = self.get_time_index(t2)
        return min(self.array_val_corr[idx_min:idx_max])
                               
    def calculate_local_max(self, t1, t2):
        idx_min = self.get_time_index(t1)
        idx_max = self.get_time_index(t2)
        return max(self.array_val_corr[idx_min:idx_max])

    def in_range(self, t):
        """
        Check to see if time is within range of collected data.

        t - Time value.
        Return: True if time is within range of collected data.
                Otherwise False.
        """
        with self.lock:
            if self.array_time and \
                    self.array_time[0] < t < self.array_time[-1]:
                return True
        return False

    def start_time(self):
        """
        Get time for first data sample.

        Return: Time of the first collected data sample. -1 if none.
        """
        with self.lock:
            if self.array_time:
                return self.array_time[0]
        return -1

    def collect(self, new_data):
        """Store new collected data."""
        with self.lock:
            if not self.array_val:
                self.val_min = self.val_max = new_data[0][1]
            for t, v in new_data:
                self.array_time.append(t)
                self.array_val.append(v)
                vcorr = self.calculate_val_corr(v)
                self.array_val_corr.append(vcorr)
                if vcorr > self.val_max:
                    self.val_max = v
                elif vcorr < self.val_min:
                    self.val_min = v

    def get_y(self, time_val):
        """
        Retrieve the signal value corresponding to the provided time value.

        t_val - Time value.
        Return: Signal value corresponding to an adjacent sample in time.
        """
        with self.lock:
            idx = self.get_time_index(time_val)
            return self.array_val_corr[idx]

    def clear(self):
        self.array_time[:] = []
        self.array_val[:] = []
        self.array_val_corr[:] = []

    def get_time_index(self, time_val):
        """
        Retrieve the sample index corresponding to the provided time value.

        t_val - Time value.
        Return: Index of a sample adjacent to the provided time value.
        """
        with self.lock:
            if not self.array_time:
                return -1
            if len(self.array_time) == 1:
                return 0
            time_min = self.array_time[0]
            time_max = self.array_time[-1]
            if time_val < time_min:
                return 0
            elif time_val > time_max:
                return len(self.array_time)
            delta_t = time_max - time_min
            t = time_val - time_min
            idx = int((t / delta_t) * len(self.array_time))
            if idx >= len(self.array_time):
                idx = len(self.array_time) - 1
            if idx < 0:
                idx = 0
            while self.array_time[idx] > time_val:
                idx -= 1
            while self.array_time[idx] < time_val:
                idx += 1
            return idx
