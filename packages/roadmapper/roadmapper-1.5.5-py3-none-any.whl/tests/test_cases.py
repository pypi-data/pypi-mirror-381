import os
from datetime import datetime
from src.roadmapper.roadmap import Roadmap
from src.roadmapper.timelinemode import TimelineMode


# ** Roadmap Tests


def colour_theme_demo(
    width: int = 1200,
    timelinemode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2024-12-01",
    number_of_items: int = 12,
    show_generic_dates: bool = False,
    file_name: str = "colour_theme_demo.png",
    colour_theme: str = "DEFAULT",
) -> None:
    output_file = file_name
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(
        width, 1000, auto_height=True, colour_theme=colour_theme, show_marker=False
    )
    roadmap.set_title("STRATEGY ROADMAP 2024")
    roadmap.set_subtitle("Mars Software Inc.")
    roadmap.set_timeline(
        timelinemode,
        start=start_date,
        number_of_items=number_of_items,
        show_generic_dates=show_generic_dates,
        year_fill_colour="#404040",
        item_fill_colour="#404040",
        year_font_colour="white",
        item_font_colour="white",
    )

    group = roadmap.add_group("Planning", fill_colour="#FFC000", font_colour="black")
    task = group.add_task(
        "Vision", "2024-01-01", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task = group.add_task(
        "Goals", "2024-02-15", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task.add_parallel_task(
        "Strategic Intent",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "Sales Budget",
        "2024-06-01",
        "2024-07-15",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "Release Plans",
        "2024-07-16",
        "2024-09-30",
        fill_colour="#FFC000",
        font_colour="black",
    )

    group = roadmap.add_group("Strategy", fill_colour="#ED7D31", font_colour="black")
    task = group.add_task(
        "Market Analysis",
        "2024-02-01",
        "2024-03-30",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "Competitor Review", "2024-03-30", fill_colour="#843C0C", font_colour="black"
    )
    task.add_parallel_task(
        "SWOT", "2024-04-01", "2024-04-30", fill_colour="#ED7D31", font_colour="black"
    )
    task = group.add_task(
        "Business Model",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "Price List (Draft)", "2024-06-01", fill_colour="#843C0C", font_colour="black"
    )
    parallel_task = task.add_parallel_task(
        "Price Reseach XXXXXXXXXXX",
        "2024-06-01",
        "2024-08-05",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "Price List (Final)", "2024-07-28", fill_colour="#843C0C", font_colour="black"
    )
    group.add_task(
        "Objectives",
        "2024-06-20",
        "2024-09-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group.add_task(
        "Sales Trends Analysis",
        "2024-08-15",
        "2024-10-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group = roadmap.add_group(
        "Service Development", fill_colour="#70AD47", font_colour="black"
    )
    task = group.add_task(
        "Product Roadmap",
        "2024-02-15",
        "2024-03-31",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task = task.add_parallel_task(
        "Development",
        "2024-04-01",
        "2024-08-30",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "Alpha May 20", "2024-05-20", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "Private Beta Jun 30", "2024-06-30", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "Public Beta Jun 30", "2024-08-10", fill_colour="#385723", font_colour="black"
    )

    parallel_task = task.add_parallel_task(
        "Release Candidate",
        "2024-09-01",
        "2024-10-15",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task = task.add_parallel_task(
        "Release To Public",
        "2024-10-16",
        "2024-12-31",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task.add_milestone(
        "Go Live Dec 20", "2024-12-20", fill_colour="#385723", font_colour="black"
    )

    group = roadmap.add_group(
        "Business Intelligence",
        fill_colour="#4472C4",
        font_colour="black",
    )
    task = group.add_task(
        "BI Development",
        "2024-04-15",
        "2024-12-31",
        fill_colour="#4472C4",
        font_colour="black",
    )

    task.add_milestone(
        "Service Dashboard", "2024-05-15", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "Real-Time Analytics", "2024-08-01", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "Sales Dashboard", "2024-12-15", fill_colour="#162641", font_colour="black"
    )

    roadmap.set_footer(
        "Generated by Roadmapper on " + datetime.now().strftime("%Y-%m-%d")
    )
    roadmap.draw()

    roadmap.save(output_file)

    assert os.path.exists(output_file)


def unicode_demo(
    width: int = 1200,
    timelinemode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2022-12-01",
    number_of_items: int = 12,
    show_generic_dates: bool = False,
    file_name: str = "unicode_demo.png",
    colour_theme: str = "DEFAULT",
) -> None:
    output_file = file_name
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(
        width, 1000, auto_height=True, colour_theme=colour_theme, show_marker=False
    )
    roadmap.set_title("2024 年戰略路線圖")
    roadmap.set_subtitle("火星科技公司")
    roadmap.set_timeline(
        timelinemode,
        start=start_date,
        number_of_items=number_of_items,
        show_generic_dates=show_generic_dates,
        year_fill_colour="#404040",
        item_fill_colour="#404040",
        year_font_colour="white",
        item_font_colour="white",
    )

    group = roadmap.add_group("規劃", fill_colour="#FFC000", font_colour="black")
    task = group.add_task(
        "願景", "2024-01-01", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task = group.add_task(
        "目標", "2024-02-15", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task.add_parallel_task(
        "戰略意圖",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "銷售預算",
        "2024-06-01",
        "2024-07-15",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "發布計劃",
        "2024-07-16",
        "2024-09-30",
        fill_colour="#FFC000",
        font_colour="black",
    )

    group = roadmap.add_group("戰略", fill_colour="#ED7D31", font_colour="black")
    task = group.add_task(
        "市場分析",
        "2024-02-01",
        "2024-03-30",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "競爭對手審查", "2024-03-30", fill_colour="#843C0C", font_colour="black"
    )
    task.add_parallel_task(
        "SWOT", "2024-04-01", "2024-04-30", fill_colour="#ED7D31", font_colour="black"
    )
    task = group.add_task(
        "商業模式",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "價目表（草稿）", "2024-06-01", fill_colour="#843C0C", font_colour="black"
    )
    parallel_task = task.add_parallel_task(
        "價格研究",
        "2024-06-01",
        "2024-08-05",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "價目表（最終）", "2024-07-28", fill_colour="#843C0C", font_colour="black"
    )
    group.add_task(
        "目標",
        "2024-06-20",
        "2024-09-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group.add_task(
        "銷售趨勢分析",
        "2024-08-15",
        "2024-10-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group = roadmap.add_group("服務發展", fill_colour="#70AD47", font_colour="black")
    task = group.add_task(
        "產品路線圖",
        "2024-02-15",
        "2024-03-31",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task = task.add_parallel_task(
        "軟件開發",
        "2024-04-01",
        "2024-08-30",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "阿尔法 5月20", "2024-05-20", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "私人測試 6月30", "2024-06-30", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "公開測試 8月30", "2024-08-10", fill_colour="#385723", font_colour="black"
    )

    parallel_task = task.add_parallel_task(
        "候选版本",
        "2024-09-01",
        "2024-10-15",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task = task.add_parallel_task(
        "公開發布",
        "2024-10-16",
        "2024-12-31",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task.add_milestone(
        "上綫 12月20", "2024-12-20", fill_colour="#385723", font_colour="black"
    )

    group = roadmap.add_group(
        "商業智能",
        fill_colour="#4472C4",
        font_colour="black",
    )
    task = group.add_task(
        "商業智能開發",
        "2024-04-15",
        "2024-12-31",
        fill_colour="#4472C4",
        font_colour="black",
    )

    task.add_milestone(
        "服務儀表板", "2024-05-15", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "實時分析", "2024-08-01", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "Sales Dashboard", "2024-12-15", fill_colour="#162641", font_colour="black"
    )

    roadmap.set_footer("由 Roadmapper 生成於 " + datetime.now().strftime("%Y-%m-%d"))
    roadmap.draw()

    roadmap.save(output_file)
    assert os.path.exists(output_file)


def sample_roadmap(
    width: int = 1200,
    timelinemode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2022-12-01",
    number_of_items: int = 12,
    show_generic_dates: bool = False,
    file_name: str = "sample_roadmap.png",
    colour_theme: str = "DEFAULT",
) -> None:
    output_file = file_name
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(
        width, 1000, auto_height=True, colour_theme=colour_theme, show_marker=False
    )
    roadmap.set_title("STRATEGY ROADMAP 2024")
    roadmap.set_subtitle("Matariki Technologies Inc.")
    roadmap.set_timeline(
        timelinemode,
        start=start_date,
        number_of_items=number_of_items,
        show_generic_dates=show_generic_dates,
        year_fill_colour="#404040",
        year_font_colour="white",
        item_fill_colour="#404040",
        item_font_colour="white",
    )

    group = roadmap.add_group("Planning", fill_colour="#FFC000", font_colour="black")
    task = group.add_task(
        "Vision", "2024-01-01", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task = group.add_task(
        "Goals", "2024-02-15", "2024-03-31", fill_colour="#FFC000", font_colour="black"
    )
    task.add_parallel_task(
        "Strategic Intent",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "Sales Budget",
        "2024-06-01",
        "2024-07-15",
        fill_colour="#FFC000",
        font_colour="black",
    )
    task.add_parallel_task(
        "Release Plans",
        "2024-07-16",
        "2024-09-30",
        fill_colour="#FFC000",
        font_colour="black",
    )

    group = roadmap.add_group("Strategy", fill_colour="#ED7D31", font_colour="black")
    task = group.add_task(
        "Market Analysis",
        "2024-02-01",
        "2024-03-30",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "Competitor Review", "2024-03-30", fill_colour="#843C0C", font_colour="black"
    )
    task.add_parallel_task(
        "SWOT", "2024-04-01", "2024-04-30", fill_colour="#ED7D31", font_colour="black"
    )
    task = group.add_task(
        "Business Model",
        "2024-04-01",
        "2024-05-31",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    task.add_milestone(
        "Price List (Draft)", "2024-06-01", fill_colour="#843C0C", font_colour="black"
    )
    parallel_task = task.add_parallel_task(
        "Price Reseach",
        "2024-06-01",
        "2024-08-05",
        fill_colour="#ED7D31",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "Price List (Final)", "2024-07-28", fill_colour="#843C0C", font_colour="black"
    )
    group.add_task(
        "Objectives",
        "2024-06-20",
        "2024-09-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group.add_task(
        "Sales Trends Analysis",
        "2024-08-15",
        "2024-10-10",
        fill_colour="#ED7D31",
        font_colour="black",
    )

    group = roadmap.add_group(
        "Service Development", fill_colour="#70AD47", font_colour="black"
    )
    task = group.add_task(
        "Product Roadmap",
        "2024-02-15",
        "2024-03-31",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task = task.add_parallel_task(
        "Development",
        "2024-04-01",
        "2024-08-30",
        fill_colour="#70AD47",
        font_colour="black",
    )
    parallel_task.add_milestone(
        "Alpha May 20", "2024-05-20", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "Private Beta Jul 02", "2024-07-02", fill_colour="#385723", font_colour="black"
    )
    parallel_task.add_milestone(
        "Public Beta Aug 15", "2024-08-15", fill_colour="#385723", font_colour="black"
    )

    parallel_task = task.add_parallel_task(
        "Release Candidate",
        "2024-09-01",
        "2024-10-15",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task = task.add_parallel_task(
        "Release To Public",
        "2024-10-16",
        "2024-12-31",
        fill_colour="#70AD47",
        font_colour="black",
    )

    parallel_task.add_milestone(
        "Go Live Dec 20", "2024-12-20", fill_colour="#385723", font_colour="black"
    )

    group = roadmap.add_group(
        "Business Intelligence",
        fill_colour="#4472C4",
        font_colour="black",
    )
    task = group.add_task(
        "BI Development",
        "2024-04-15",
        "2024-12-31",
        fill_colour="#4472C4",
        font_colour="black",
    )

    task.add_milestone(
        "Service Dashboard", "2024-05-15", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "Real-Time Analytics", "2024-08-01", fill_colour="#162641", font_colour="black"
    )

    task.add_milestone(
        "Sales Dashboard", "2024-12-15", fill_colour="#162641", font_colour="black"
    )

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()

    roadmap.save(output_file)

    assert os.path.exists(output_file)


def colour_theme_roadmap(
    width: int = 1200,
    timelinemode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2023-12-01",
    number_of_items: int = 12,
    show_generic_dates: bool = False,
    file_name: str = "colour_theme_roadmap.png",
    colour_theme: str = "DEFAULT",
) -> None:
    output_file = file_name
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(
        width, 1000, auto_height=True, colour_theme=colour_theme, show_marker=True
    )
    roadmap.set_title("SAMPLE ROADMAP 2023/2024")
    roadmap.set_subtitle("GodZone Corporation")
    roadmap.set_timeline(
        timelinemode,
        start=start_date,
        number_of_items=number_of_items,
        show_generic_dates=show_generic_dates,
    )

    group = roadmap.add_group("Core Product Work Stream", text_alignment="left")
    task = group.add_task("Base Functionality", "2023-11-01", "2024-10-31")
    task.add_milestone("v.1.0", "2024-02-15")
    task.add_milestone("v.1.1", "2024-08-01")
    parellel_task = task.add_parallel_task("Enhancements", "2024-11-15", "2024-03-31")
    parellel_task.add_milestone("v.2.0", "2024-03-30")

    task = group.add_task("Showcase #1", "2024-03-01", "2024-05-07")
    task.add_parallel_task("Showcase #2", "2024-06-01", "2024-08-07")

    group = roadmap.add_group("Mobility Work Stream", text_alignment="left")
    group.add_task("Mobile App Development", "2024-02-01", "2024-12-07")

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()

    roadmap.save(output_file)

    assert os.path.exists(output_file)


def custom_colour_roadmap(
    width: int = 1200,
    height: int = 1000,
    timelinemode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2023-11-01",
    number_of_items: int = 24,
    show_marker: bool = False,
    show_generic_dates: bool = False,
    file_name: str = "custom_colour_roadmap.png",
    colour_theme: str = "DEFAULT",
) -> None:
    output_file = file_name
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(
        width,
        height,
        auto_height=True,
        colour_theme=colour_theme,
        show_marker=show_marker,
    )
    roadmap.set_title("My Demo Roadmap!!!")
    roadmap.set_timeline(
        timelinemode,
        start=start_date,
        number_of_items=number_of_items,
        show_generic_dates=show_generic_dates,
    )

    group = roadmap.add_group("Core Product Work Stream")
    task = group.add_task("Base Functionality", "2023-11-01", "2024-10-31")
    task.add_milestone("v.1.0", "2024-02-15")
    task.add_milestone("v.1.1", "2024-08-01")
    parellel_task = task.add_parallel_task("Enhancements", "2024-11-15", "2024-03-31")
    parellel_task.add_milestone("v.2.0", "2024-03-30")

    task = group.add_task("Showcase #1", "2024-03-01", "2024-05-07")
    task.add_parallel_task("Showcase #2", "2024-06-01", "2024-08-07")

    group = roadmap.add_group("Mobility Work Stream")
    group.add_task("Mobile App Development", "2024-02-01", "2024-12-07")

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()
    roadmap.save(output_file)

    assert os.path.exists(output_file)


def banner_roadmap():
    color_theme_roadmap("../../images/color-theme01.png", "DEFAULT")
    color_theme_roadmap("../../images/color-theme02.png", "GREYWOOF")
    color_theme_roadmap("../../images/color-theme03.png", "ORANGEPEEL")
    color_theme_roadmap("../../images/color-theme04.png", "BLUEMOUNTAIN")
    color_theme_roadmap("../../images/color-theme05.png", "GREENTURTLE")


def multilingual_roadmap():
    en_NZ_roadmap("../../images/en_NZ-roadmap.png", "../json/rainbow.json", "en_US")
    zh_TW_with_locale_roadmap(
        "../../images/zh_TW-roadmap.png",
        "../json/rainbow-unicode.json",
        "../json/zh_TW_timeline_settings.json",
    )
    zh_TW_roadmap(
        "../../images/zh_TW-timeline-roadmap.png",
        "../json/rainbow-unicode.json",
    )
    ja_JP_roadmap(
        "../../images/ja_JP-roadmap.png",
        "../json/rainbow-unicode.json",
        "../json/ja_JP_timeline_settings.json",
    )
    ko_KR_roadmap(
        "../../images/ko-KR-roadmap.png",
        "../json/rainbow-unicode.json",
        "../json/ko_KR_timeline_settings.json",
    )


### Wiki Images
def home_roadmap():
    if not os.path.exists("images"):
        os.mkdir("images")

    output_file = "../../images/my_roadmap.png"
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    my_roadmap = Roadmap(width=500, height=400)
    my_roadmap.set_title("My Roadmap")
    my_roadmap.set_timeline(
        mode=TimelineMode.MONTHLY, start="2022-11-14", number_of_items=6
    )

    group = my_roadmap.add_group("Development")
    group.add_task("Activity 1", "2022-12-01", "2024-02-10")
    group.add_task("Activity 2", "2024-01-11", "2024-03-20")
    group.add_task("Activity 3", "2024-01-21", "2024-06-30")

    my_roadmap.set_footer("Generated by Roadmapper")
    my_roadmap.draw()
    my_roadmap.save(output_file)
    assert os.path.exists(output_file)


def readme_roadmap():
    if not os.path.exists("images"):
        os.mkdir("images")

    output_file = "../../images/demo01.png"
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(1200, 400, colour_theme="BLUEMOUNTAIN")
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_subtitle("Matariki Technologies Ltd")
    roadmap.set_timeline(TimelineMode.MONTHLY, start="2025-01-01", number_of_items=18)
    roadmap.add_logo(
        "../../images/logo/matariki-tech-logo.png",
        position="top-right",
        width=50,
        height=50,
    )

    group = roadmap.add_group("Core Product Work Stream")

    task = group.add_task("Base Functionality", "2025-01-01", "2025-10-31")
    task.add_milestone("v.1.0", "2025-02-15")
    task.add_milestone("v.1.1", "2025-08-01")

    parellel_task = task.add_parallel_task("Enhancements", "2025-11-15", "2026-03-31")
    parellel_task.add_milestone("v.2.0", "2026-03-30")

    task = group.add_task("Showcase #1", "2025-03-01", "2025-05-07")
    task.add_parallel_task("Showcase #2", "2025-06-01", "2025-08-07")

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()
    roadmap.save(output_file)
    assert os.path.exists(output_file)


def color_theme_roadmap(filename: str, colour_theme: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(600, 500, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-07-01", number_of_items=4)
    roadmap.set_footer("Generated by Roadmapper")

    group = roadmap.add_group("Workstream 1")
    task = group.add_task("Task 1-A", "2024-07-01", "2024-10-30")
    task.add_parallel_task("Task 2-B", "2024-11-15", "2024-02-28")
    group.add_task("Task 3-C", "2024-10-01", "2024-12-31")

    group = roadmap.add_group("Workstream 2")
    group.add_task("Task 2-A", "2024-10-01", "2024-12-30")
    group.add_task("Task 2-B", "2024-11-01", "2024-01-30")
    group.add_task("Task 2-C", "2024-12-01", "2024-02-28")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


def en_NZ_roadmap(filename: str, colour_theme: str, locale_name: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(800, 700, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("Strategy Roadmap 2024")
    roadmap.set_subtitle("Matariki Technologies Ltd")
    roadmap.set_timeline(
        TimelineMode.QUARTERLY,
        start="2024-01-01",
        number_of_items=4,
        timeline_locale=locale_name,
    )
    roadmap.set_footer("Generated by Roadmapper")

    group = roadmap.add_group("People Stream")
    task = group.add_task("Develop Inclusion Strategy", "2024-01-01", "2024-04-30")
    task.add_parallel_task(
        "Promote diversity, equity, and inclusion", "2024-05-01", "2024-12-30"
    )
    group.add_task("Implement a sustainability programme", "2024-03-01", "2024-11-30")

    group = roadmap.add_group("Process Stream")
    group.add_task(
        "Implement Business Improvement Programme", "2024-02-01", "2024-11-30"
    )
    task = group.add_task("Automate processes", "2024-07-01", "2024-12-30")
    task.add_milestone("30% Automated ", "2024-8-01")
    task.add_milestone("60% Automated ", "2024-12-01")

    group = roadmap.add_group("Tool Stream")
    group.add_task("Implement strategy", "2024-01-01", "2024-04-30")
    group.add_task("Tools Selection", "2024-02-01", "2024-08-30")
    task = group.add_task("Centralized Tool Administration", "2024-04-01", "2024-11-30")
    task.add_milestone("Admin Centralised", "2024-12-01")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


def zh_TW_with_locale_roadmap(filename: str, colour_theme: str, locale_name: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(800, 700, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("戰略路線圖 2024")
    roadmap.set_subtitle("瑪塔里奇太陽科技有限公司")
    roadmap.set_timeline(
        TimelineMode.QUARTERLY,
        start="2024-01-01",
        number_of_items=4,
        timeline_locale=locale_name,
    )
    roadmap.set_footer("由 Roadmapper 生成")

    group = roadmap.add_group("人員流程")
    task = group.add_task("制定包容戰略", "2024-01-01", "2024-04-30")
    task.add_parallel_task("促進多樣性、公平性和包容性", "2024-05-01", "2024-12-30")
    group.add_task("實施可持續發展計劃", "2024-03-01", "2024-11-30")

    group = roadmap.add_group("工作流程")
    group.add_task("實施業務改進計劃", "2024-02-01", "2024-11-30")
    task = group.add_task("自動化流程", "2024-07-01", "2024-12-30")
    task.add_milestone("30%自動化 ", "2024-8-01")
    task.add_milestone("60%自動化 ", "2024-12-01")

    group = roadmap.add_group("工具流程")
    group.add_task("實施工具選擇策略", "2024-01-01", "2024-04-30")
    group.add_task("工具選擇", "2024-02-01", "2024-08-30")
    task = group.add_task("集中工具管理", "2024-04-01", "2024-11-30")
    task.add_milestone("系統集中完成", "2024-12-01")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


def zh_TW_roadmap(filename: str, colour_theme: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(800, 700, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("戰略路線圖 2024")
    roadmap.set_subtitle("瑪塔里奇太陽科技有限公司")
    roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
    roadmap.set_footer("由 Roadmapper 生成")

    group = roadmap.add_group("人員流程")
    task = group.add_task("制定包容戰略", "2024-01-01", "2024-04-30")
    task.add_parallel_task("促進多樣性、公平性和包容性", "2024-05-01", "2024-12-30")
    group.add_task("實施可持續發展計劃", "2024-03-01", "2024-11-30")

    group = roadmap.add_group("工作流程")
    group.add_task("實施業務改進計劃", "2024-02-01", "2024-11-30")
    task = group.add_task("自動化流程", "2024-07-01", "2024-12-30")
    task.add_milestone("30%自動化 ", "2024-8-01")
    task.add_milestone("60%自動化 ", "2024-12-01")

    group = roadmap.add_group("工具流程")
    group.add_task("實施工具選擇策略", "2024-01-01", "2024-04-30")
    group.add_task("工具選擇", "2024-02-01", "2024-08-30")
    task = group.add_task("集中工具管理", "2024-04-01", "2024-11-30")
    task.add_milestone("系統集中完成", "2024-12-01")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


def ja_JP_roadmap(filename: str, colour_theme: str, locale_name: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(800, 700, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("戦略的ロードマップ 2024")
    roadmap.set_subtitle("マタリッチサンテクノロジー株式会社")
    roadmap.set_timeline(
        TimelineMode.QUARTERLY,
        start="2024-01-01",
        number_of_items=4,
        timeline_locale=locale_name,
    )
    roadmap.set_footer("ロードマッパーによって生成")

    group = roadmap.add_group("人事プロセス")
    task = group.add_task("インクルージョン戦略を策定する", "2024-01-01", "2024-04-30")
    task.add_parallel_task("多様性、公平性、包括性の促進", "2024-05-01", "2024-12-30")
    group.add_task("持続可能な開発計画の実施", "2024-03-01", "2024-11-30")

    group = roadmap.add_group("作業過程")
    group.add_task("業務改善計画の実施", "2024-02-01", "2024-11-30")
    task = group.add_task("自動化されたプロセス", "2024-07-01", "2024-12-30")
    task.add_milestone("30%自動化", "2024-8-01")
    task.add_milestone("60%自動化", "2024-12-01")

    group = roadmap.add_group("ツールフロー")
    group.add_task("ツール選択戦略を実装する", "2024-01-01", "2024-04-30")
    group.add_task("ツールの選択", "2024-02-01", "2024-08-30")
    task = group.add_task("集中ツール管理", "2024-04-01", "2024-11-30")
    task.add_milestone("システムは集中型", "2024-12-01")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


def ko_KR_roadmap(filename: str, colour_theme: str, locale_name: str):
    output_file = filename
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(800, 700, colour_theme=colour_theme, show_marker=True)
    roadmap.set_title("전략 로드맵 2024")
    roadmap.set_subtitle("마타리키 테크놀로지스")
    roadmap.set_timeline(
        TimelineMode.QUARTERLY,
        start="2024-01-01",
        number_of_items=4,
        timeline_locale=locale_name,
    )
    roadmap.set_footer("로드매퍼에서 생성")

    group = roadmap.add_group("인사 프로세스")
    task = group.add_task("포함 전략을 수립", "2024-01-01", "2024-04-30")
    task.add_parallel_task("다양성, 공정성, 포괄성 촉진", "2024-05-01", "2024-12-30")
    group.add_task("지속 가능한 개발 계획 실시", "2024-03-01", "2024-11-30")

    group = roadmap.add_group("작업 과정")
    group.add_task("업무 개선 계획 실시", "2024-02-01", "2024-11-30")
    task = group.add_task("자동화된 프로세스", "2024-07-01", "2024-12-30")
    task.add_milestone("30% 자동화", "2024-8-01")
    task.add_milestone("60% 자동화", "2024-12-01")

    group = roadmap.add_group("공구 흐름")
    group.add_task("도구 선택 전략 구현", "2024-01-01", "2024-04-30")
    group.add_task("도구 선택", "2024-02-01", "2024-08-30")
    task = group.add_task("중앙 집중식 도구 관리", "2024-04-01", "2024-11-30")
    task.add_milestone("시스템은 중앙 집중식", "2024-12-01")

    roadmap.draw()
    roadmap.save(filename)
    assert os.path.exists(output_file)


### Test case functions ###


def test_sample_case1():
    if not os.path.exists("../../images/test"):
        os.mkdir("../../images/test")
    colour_theme_demo(
        width=2500,
        file_name="../../images/test/test-ORANGEPEEL-weekly.png",
        colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.WEEKLY,
        number_of_items=52,
        start_date="2024-01-01",
    )


def test_sample_case2():
    if not os.path.exists("../../images/test"):
        os.mkdir("../../images/test")
    colour_theme_demo(
        file_name="../../images/test/test-ORANGEPEEL-monthly.png",
        colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )


def test_sample_case3():
    if not os.path.exists("../../images/test"):
        os.mkdir("../../images/test")
    colour_theme_demo(
        file_name="../../images/test/test-ORANGEPEEL-quarter.png",
        colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.QUARTERLY,
        number_of_items=4,
        start_date="2024-01-01",
    )


def test_sample_unicase1():
    if not os.path.exists("../../images/test"):
        os.mkdir("../../images/test")
    unicode_demo(
        file_name="../../images/test/test-unicode-monthly.png",
        # colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )
    assert True


def test_draw_anatomy():
    if not os.path.exists("images"):
        os.mkdir("images")

    output_file = "../../images/roadmapper-anatomy-base.png"
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(1200, 380, colour_theme="BLUEMOUNTAIN", show_marker=True)
    roadmap.set_title("Product Roadmap")
    roadmap.set_subtitle("Matariki Tech Ltd")
    roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=9)
    roadmap.set_footer("Generated by Roadmapper")

    group = roadmap.add_group("Workstream 1")
    task = group.add_task("Task 1-A", "2024-01-01", "2024-05-15")
    task.add_parallel_task("Task 2-B", "2024-05-16", "2024-08-30")
    task = group.add_task("Task 3-C", "2024-04-01", "2024-06-30")
    task.add_milestone("Milestone 1", "2024-06-30")

    roadmap.draw()

    roadmap.save(output_file)
    assert os.path.exists(output_file)


def test_draw_banner_theme():
    if not os.path.exists("images"):
        os.mkdir("images")

    output_file = "../../images/theme-demo01.png"
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(600, 380, colour_theme="BLUEMOUNTAIN", show_marker=True)
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
    roadmap.set_footer("Generated by Roadmapper")

    group = roadmap.add_group("Workstream 1")
    task = group.add_task("Task 1-A", "2024-01-01", "2024-04-30")
    task.add_parallel_task("Task 2-B", "2024-05-15", "2024-08-30")
    group.add_task("Task 3-C", "2024-04-01", "2024-06-30")

    group = roadmap.add_group("Workstream 2")
    group.add_task("Task 2-A", "2024-04-01", "2024-06-30")
    group.add_task("Task 2-B", "2024-05-01", "2024-07-30")
    group.add_task("Task 2-C", "2024-06-01", "2024-08-30")

    roadmap.draw()
    roadmap.save(output_file)
    assert os.path.exists(output_file)


def test_draw_banner():
    if not os.path.exists("images"):
        os.mkdir("images")

    output_file = "../../images/demo01.png"
    # if file exist, then delete it first
    if os.path.exists(output_file):
        os.remove(output_file)

    roadmap = Roadmap(600, 500, show_marker=False, auto_height=True)
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_timeline(
        TimelineMode.QUARTERLY,
        start="2024-01-01",
        number_of_items=3,
        year_fill_colour="#7CC1AC",
        year_font_colour="black",
        item_fill_colour="#7CC1AC",
        item_font_colour="black",
    )
    roadmap.set_footer("Generated by Roadmapper")
    group = roadmap.add_group(
        "Workstream 1", font_colour="black", fill_colour="#C38D9D", font_size=12
    )
    task = group.add_task(
        "Task 1-A",
        "2024-01-01",
        "2024-04-30",
        font_colour="black",
        fill_colour="#D7B3BD",
    )
    task.add_parallel_task(
        "Task 2-B",
        "2024-05-15",
        "2024-08-30",
        font_colour="black",
        fill_colour="#D7B3BD",
    )
    group.add_task(
        "Task 3-C",
        "2024-04-01",
        "2024-06-30",
        font_colour="black",
        fill_colour="#D7B3BD",
    )

    group = roadmap.add_group(
        "Workstream 2", font_colour="black", fill_colour="#E8A87C", font_size=12
    )
    group.add_task(
        "Task 2-A",
        "2024-04-01",
        "2024-06-30",
        font_colour="black",
        fill_colour="#EFC5A7",
    )
    group.add_task(
        "Task 2-B",
        "2024-05-01",
        "2024-07-30",
        font_colour="black",
        fill_colour="#EFC5A7",
    )
    group.add_task(
        "Task 2-C",
        "2024-06-01",
        "2024-08-30",
        font_colour="black",
        fill_colour="#EFC5A7",
    )

    roadmap.draw()
    roadmap.save(output_file)
    assert os.path.exists(output_file)


def test_gallery_images():
    ### Sample Roadmap ###
    sample_roadmap(
        width=1400,
        file_name="../../images/gallery/gallery-sample-01.png",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    ### Colour Theme Roadmap ###

    colour_theme_roadmap(
        file_name="../../images/gallery/gallery-DEFAULT-monthly.png",
        # colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    colour_theme_roadmap(
        file_name="../../images/gallery/gallery-ORANGEPEEL-monthly.png",
        colour_theme="ORANGEPEEL",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    colour_theme_roadmap(
        file_name="../../images/gallery/gallery-BLUEMOUNTAIN-monthly.png",
        colour_theme="BLUEMOUNTAIN",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    colour_theme_roadmap(
        file_name="../../images/gallery/gallery-GREENTURTLE-monthly.png",
        colour_theme="GREENTURTLE",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    colour_theme_roadmap(
        file_name="../../images/gallery/gallery-GREYWOOF-monthly.png",
        colour_theme="GREYWOOF",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
    )

    ### Marker Roadmap ###
    custom_colour_roadmap(
        width=1200,
        file_name="../../images/gallery/gallery-marker-monthly.png",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2023-11-01",
        show_marker=True,
        show_generic_dates=False,
    )

    ### WEEKLY Timeline Roadmap ###
    colour_theme_roadmap(
        width=2400,
        file_name="../../images/gallery/gallery-DEFAULT-weekly.png",
        colour_theme="DEFAULT",
        timelinemode=TimelineMode.WEEKLY,
        number_of_items=52,
        start_date="2024-01-01",
        show_generic_dates=False,
    )

    ### QUARTERLY Timeline Roadmap ###
    colour_theme_roadmap(
        width=1400,
        file_name="../../images/gallery/gallery-DEFAULT-quarterly.png",
        colour_theme="DEFAULT",
        timelinemode=TimelineMode.QUARTERLY,
        number_of_items=6,
        start_date="2024-01-01",
        show_generic_dates=False,
    )

    ### HALF-YEARLY Timeline Roadmap ###
    colour_theme_roadmap(
        width=1400,
        file_name="../../images/gallery/gallery-DEFAULT-halfyearly.png",
        colour_theme="DEFAULT",
        timelinemode=TimelineMode.HALF_YEARLY,
        number_of_items=4,
        start_date="2024-01-01",
        show_generic_dates=False,
    )

    ### YEARLY Timeline Roadmap ###
    colour_theme_roadmap(
        width=1400,
        file_name="../../images/gallery/gallery-DEFAULT-yearly.png",
        colour_theme="DEFAULT",
        timelinemode=TimelineMode.YEARLY,
        number_of_items=2,
        start_date="2023-01-01",
        show_generic_dates=False,
    )

    ### Generic Dates Roadmap ###
    colour_theme_roadmap(
        width=1400,
        file_name="../../images/gallery/gallery-DEFAULT-generic-monthly.png",
        colour_theme="DEFAULT",
        timelinemode=TimelineMode.MONTHLY,
        number_of_items=12,
        start_date="2024-01-01",
        show_generic_dates=True,
    )


def test_draw_wiki_roadmap():
    readme_roadmap()
    home_roadmap()
    banner_roadmap()
    multilingual_roadmap()


def test_with_context_manager():
    with Roadmap(
        1200, 500, show_marker=False, auto_height=True, colour_theme="ORANGEPEEL"
    ) as my_roadmap:
        my_roadmap.set_title("Context Manager Test Roadmap")
        my_roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01")
        with my_roadmap.add_group("Workstream 1") as group1:
            with group1.add_task(
                "Task 1-A",
                "2024-01-01",
                "2024-04-30",
            ) as task1:
                with task1.add_parallel_task(
                    "Task 2-B",
                    "2024-05-15",
                    "2024-08-30",
                ) as parallel_task1:
                    parallel_task1.add_milestone("Milestone 2", "2024-07-10")
                task1.add_milestone(
                    "Milestone 1",
                    "2024-04-01",
                )
        my_roadmap.draw()
        my_roadmap.save("../../images/with_context_manager.png")


def test_black_blackground():
    with Roadmap(
        1200, 500, show_marker=False, auto_height=True, colour_theme="ORANGEPEEL"
    ) as my_roadmap:
        my_roadmap.set_background_colour("black")
        my_roadmap.set_title("Black Background Test Roadmap")
        my_roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01")
        with my_roadmap.add_group("Workstream 1") as group1:
            with group1.add_task(
                "Task 1-A",
                "2024-01-01",
                "2024-04-30",
            ) as task1:
                with task1.add_parallel_task(
                    "Task 2-B",
                    "2024-05-15",
                    "2024-08-30",
                ) as parallel_task1:
                    parallel_task1.add_milestone("Milestone 2", "2024-08-10")
                task1.add_milestone(
                    "Milestone 1",
                    "2024-04-01",
                )
        my_roadmap.draw()
        my_roadmap.save("../../images/black_roadmap.png")


def test_transparent_blackground():
    with Roadmap(
        1200, 500, show_marker=False, auto_height=True, colour_theme="ORANGEPEEL"
    ) as my_roadmap:
        my_roadmap.set_background_colour("transparent")
        my_roadmap.set_title("Transparent Background Test Roadmap")
        my_roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01")
        with my_roadmap.add_group("Workstream 1") as group1:
            with group1.add_task(
                "Task 1-A",
                "2024-01-01",
                "2024-04-30",
            ) as task1:
                with task1.add_parallel_task(
                    "Task 2-B",
                    "2024-05-15",
                    "2024-08-30",
                ) as parallel_task1:
                    parallel_task1.add_milestone("Milestone 2", "2024-08-10")
                task1.add_milestone(
                    "Milestone 1",
                    "2024-04-01",
                )
        my_roadmap.draw()
        my_roadmap.save("../../images/transparent_roadmap.png")


def test_timeline_case01():
    roadmap = Roadmap(1800, 400, colour_theme="BLUEMOUNTAIN", show_marker=True)
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_subtitle("Matariki Technologies Ltd")

    roadmap.set_timeline(
        TimelineMode.MONTHLY,
        start="2024-12-01",
        number_of_items=12,
        show_first_day_of_week=True,
    )

    group = roadmap.add_group("Core Product Work Stream")

    group.add_task("Base Functionality", "2024-12-01", "2025-01-05")
    group.add_task("Enhancements12", "2025-01-06", "2025-03-31")

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()

    roadmap.save("../../images/defects/test_timeline_case01.png")
