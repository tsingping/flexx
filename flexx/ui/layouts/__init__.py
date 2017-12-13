""" Namespace for all layout widgets.
"""

# flake8: noqa

from .._widget import Widget

from ._layout import Layout
from ._hv import HVLayout, HBox, VBox, HFix, VFix, HSplit, VSplit
# from ._dock import DockPanel
from ._tabs import TabLayout
from ._stack import StackLayout
from ._form import FormLayout
from ._pinboard import PinboardLayout
