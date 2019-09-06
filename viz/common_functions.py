#!/usr/bin/env python
# Copyright 2017 Blue Marble Analytics LLC. All rights reserved.

"""

"""

import os.path
import sqlite3

from bokeh import events
from bokeh.models import CustomJS
from bokeh.plotting import output_file, show

from gridpath.common_functions import determine_scenario_directory, \
    create_directory_if_not_exists


def connect_to_database(parsed_arguments):
    """
    Connect to the database

    :param parsed_arguments:
    :return:
    """
    if parsed_arguments.database is None:
        db_path = os.path.join(os.getcwd(), "..", "db", "io.db")
    else:
        db_path = parsed_arguments.database

    if not os.path.isfile(db_path):
        raise OSError(
            "The database file {} was not found. Did you mean to "
            "specify a different database file?".format(
                os.path.abspath(db_path)
            )
        )

    conn = sqlite3.connect(db_path)

    return conn


def show_hide_legend(plot):
    """
    Show/hide the legend on double tap.

    :param plot:
    """
    def show_hide_legend_py(legend=plot.legend[0]):
        legend.visible = not legend.visible

    plot.js_on_event(
        events.DoubleTap,
        CustomJS.from_py_func(show_hide_legend_py)
    )


def adjust_legend_size(plot, max_font_size=12, max_legend_width_share=0.4):
    """
    Get the number of legend items and the longest character length of the
    legend items and adjust the legend size accordingly so that everything
    fits within a predetermined size.
    :param plot: Bokeh plot object
    :param max_font_size:
    :param max_legend_width_share:
    :return:
    """

    n_items = len(plot.legend[0].items)
    n_chars = max(len(item.label['value']) for item in plot.legend[0].items)

    pixels_per_font_size_v = 3  # trial and error
    pixels_per_font_size_h = 0.5  # trial and error

    max_font_size_v = plot.plot_height / pixels_per_font_size_v / n_items
    max_font_size_h = plot.plot_width * max_legend_width_share \
                      / pixels_per_font_size_h / n_chars
    max_font_size = int(round(min(
        max_font_size_v,
        max_font_size_h,
        max_font_size)
    ))

    # Resize labels and glyphs to fit legend
    plot.legend.glyph_height = max_font_size
    plot.legend.label_height = max_font_size
    plot.legend.label_text_line_height = max_font_size
    plot.legend.label_text_font_size = str(max_font_size) + "pt"
    plot.legend.spacing = int(round(0.2 * max_font_size))


def show_plot(scenario_directory, scenario, plot, plot_name):
    """
    Show plot in HTML browser file if requested

    :param scenario_directory:
    :param scenario:
    :param plot:
    :param plot_name:
    :return:
    """

    scenario_directory = determine_scenario_directory(
        scenario_location=scenario_directory, scenario_name=scenario)
    figures_directory = os.path.join(scenario_directory, "results", "figures")
    create_directory_if_not_exists(figures_directory)

    filename = plot_name + ".html"
    output_file(os.path.join(figures_directory, filename))
    show(plot)


def get_scenario_and_scenario_id(parsed_arguments, c):
    """
    Get the scenario and the scenario_id from the parsed arguments.

    Usually only one is given, so we determine the missing one from the one
    that is provided.

    :param parsed_arguments:
    :param c:
    :return:
    """

    if parsed_arguments.scenario_id is None:
        scenario = parsed_arguments.scenario
        # Get the scenario ID
        scenario_id = c.execute(
            """SELECT scenario_id
            FROM scenarios
            WHERE scenario_name = '{}';""".format(scenario)
        ).fetchone()[0]
    else:
        scenario_id = parsed_arguments.scenario_id
        # Get the scenario name
        scenario = c.execute(
            """SELECT scenario_name
            FROM scenarios
            WHERE scenario_id = {};""".format(scenario_id)
        ).fetchone()[0]

    return scenario, scenario_id
