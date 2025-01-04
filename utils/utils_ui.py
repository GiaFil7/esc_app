from PySide6.QtWidgets import QFileDialog, QLabel, QTableWidget
from PySide6.QtCore import Qt

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

def save_widget_to_file(parent_widget: object, widget_to_save: object, scale_factor: float | int):
    """
    Saves a widget as an image at the location and with the name that the
    user chose using the save file prompt.

    :param parent_widget: The widget the save file prompt originates from
    :type parent_widget: object
    :param widget_to_save: The widget to save as an image
    :type widtget_to_save: object
    :param scale_factor: A factor to scale the created image by
    :type scale_factor: float | int
    """

    filename, _ = QFileDialog.getSaveFileName(parent_widget, ("Save File"), "./", ("Images (*.png *.jpg)"))
    img = widget_to_save.grab(widget_to_save.rect()).toImage()
    img = img.scaled(img.size() * scale_factor, aspectMode = Qt.KeepAspectRatio, mode = Qt.SmoothTransformation)
    img.save(filename, quality = 100)

def align_logos(layout: object):
    """
    Adds extra margin left and right of logos of menu items to align them.

    :param layout: The layout that contains the menu items
    :type layout: object
    """

    # Get the maximum width
    first_item = layout.itemAt(0).widget()
    first_logo = first_item.findChild(QLabel, "logo_label")
    max_width = first_logo.maximumSize().width()

    # Add extra margin if needed
    for i in range(layout.count()):
        item = layout.itemAt(i).widget()

        logo = item.findChild(QLabel, "logo_label")
        logo.adjustSize()

        extra_margin = max_width - logo.width()

        if extra_margin > 0:
            right_margin = extra_margin // 2
            left_margin = right_margin + (extra_margin  % 2)

            logo.setContentsMargins(left_margin, 0, right_margin, 0)

def resize_table(table: QTableWidget):
        """
        Resizes the table dimensions to the contents of the table.

        :param table: The table to resize
        :type table: QTableWidget
        """

        # Resize rows and columns
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        added_vertical_scrollbar_width = False
        added_horizontal_scrollbar_height = False

        # Compute and set the total width
        total_width = 0
        if table.verticalHeader().isVisible():
            total_width += table.verticalHeader().sizeHint().width()

        for col in range(table.columnCount()):
            total_width += table.columnWidth(col)
        
        total_width += table.frameWidth() * 2

        if table.verticalScrollBar().isVisible():
            total_width += table.verticalScrollBar().sizeHint().width()
            added_vertical_scrollbar_width = True

        table.setFixedWidth(total_width)

        # Compute and set the total height
        height_total = table.horizontalHeader().sizeHint().height()
        height_total += table.frameWidth() * 2

        if table.horizontalScrollBar().isVisible():
            height_total += table.horizontalScrollBar().sizeHint().height()
            added_horizontal_scrollbar_height = True

        height_visible = height_total

        viewport = table.viewport().geometry()
        header_height = table.horizontalHeader().height()
        viewport.adjust(0, -header_height, 0, 0)

        for row in range(table.rowCount()):
            height_total += table.rowHeight(row)

            rect = table.visualRect(table.model().index(row, 0))
            
            if viewport.intersects(rect):
                height_visible += table.rowHeight(row)

        # Adjust the height only if all rows are visible
        if height_total == height_visible:
            table.setFixedHeight(height_total)

        # Remove unnecessary width and height
        if not table.verticalScrollBar().isVisible() and added_vertical_scrollbar_width:
            table.setFixedWidth(total_width - table.verticalScrollBar().sizeHint().width())

        if not table.horizontalScrollBar().isVisible() and added_horizontal_scrollbar_height:
            table.setFixedHeight(height_total - table.horizontalScrollBar().sizeHint().height())