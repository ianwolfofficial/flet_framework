"""plotting a barchart with the help of flet framework"""

import pandas as pd
import flet as ft


# defining the main window page
def main(page: ft.Page):
    # configuring title bar
    page.appbar = ft.AppBar(
        title=ft.Text("BARCHART USING FLET"),
        leading_width=40,
        center_title=True,
        color="black",
        bgcolor="#FF0000",
    )
    page.bgcolor = "#151B54"
    dik = {
        "name": ["ian", "john", "kira", "luke"],
        "profession": ["programmer", "wrestler", "actress", "gamer"],
        "age": [23, 40, 29, 31],
    }
    # processing data with pandas
    dik = pd.DataFrame(dik)

    # plot the barchart graph
    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=dik["age"][0],
                        width=40,
                        color=ft.colors.GREEN,
                        tooltip=dik["name"][0],
                        border_radius=0,
                    )
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=dik["age"][1],
                        width=40,
                        color=ft.colors.RED,
                        tooltip=dik["name"][1],
                        border_radius=0,
                    )
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=dik["age"][2],
                        width=40,
                        color=ft.colors.CYAN,
                        tooltip=dik["name"][2],
                        border_radius=0,
                    )
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=dik["age"][3],
                        width=40,
                        color=ft.colors.YELLOW,
                        tooltip=dik["name"][3],
                        border_radius=0,
                    )
                ],
            ),
        ],
        # setting border color thorughout
        border=ft.border.all(1, ft.colors.BLUE),
        # setting up left/ y axis with title and labels
        left_axis=ft.ChartAxis(
            labels_size=40,
            title=ft.Text("AGE", color="orange", size=30),
            title_size=40,
        ),
        # setting up bottom/x axis with title and labels
        bottom_axis=ft.ChartAxis(
            title=ft.Text("NAMES", color="red", size=30),
            title_size=40,
            # adjusting labels individually
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Container(
                        ft.Text("ian", color="#FFEF00", size=15), padding=10
                    ),
                ),
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Container(
                        ft.Text("john", color="#01F9C6", size=15), padding=10
                    ),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text("kira", color="#EB5406", size=15), padding=10
                    ),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Container(
                        ft.Text("luke", color="#00FF00", size=15), padding=10
                    ),
                ),
            ],
            labels_size=40,
        ),
        # configuring th grid lines
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.RED, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLUE),
        max_y=50,
        interactive=True,
        expand=True,
    )
    # adding the barchart to the page
    page.add(chart)


ft.app(target=main)
