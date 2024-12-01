from PySide6.QtWidgets import QFileDialog

def load_widget(current_widget: object, widget_to_load: object):
    """
    Loads a widget by setting it as the current widget of the
    QStackedWidget of the main_window windget.

    :param current_widget: The currently shown widget
    :type current_widget: object
    :param widget_to_load: The new widget to show
    :type widget_to_load: object
    """

    current_widget.stacked_widget = current_widget.parent()
    current_widget.stacked_widget.addWidget(widget_to_load)
    current_widget.stacked_widget.setCurrentWidget(widget_to_load)

def save_widget_to_file(parent_widget: object, widget_to_save: object):
    """
    Saves a widget as an image at the location and with the name that the
    user chose using the save file prompt.

    :param parent_widget: The widget the save file prompt originates from
    :type parent_widget: object
    :param widget_to_save: The widget to save as an image
    :type widtget_to_save: object
    """

    filename, _ = QFileDialog.getSaveFileName(parent_widget, ("Save File"), "./", ("Images (*.png *.jpg)"))
    
    img = widget_to_save.grab(widget_to_save.rect())
    img.save(filename)