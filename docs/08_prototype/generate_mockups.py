import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

OUTPUT_DIR = r"C:\Users\zhetp\intelligent-gis-astana\docs\08_prototype"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DARK_BG = "#0D1117"
PANEL_BG = "#161B22"
PANEL_BORDER = "#30363D"
TEXT_WHITE = "#F0F6FC"
TEXT_MUTED = "#8B949E"
CYAN = "#58A6FF"
GREEN = "#3FB950"
ORANGE = "#D29922"
RED = "#F85149"
ACCENT_BLUE = "#1F6FEB"
PURPLE = "#A371F7"

def draw_header(ax, title_suffix=""):
    ax.add_patch(Rectangle((0, 930), 1600, 70, facecolor=PANEL_BG, edgecolor=PANEL_BORDER, linewidth=1, zorder=10))
    ax.text(30, 965, "GBI-UHI PLATFORM", color=CYAN, fontsize=14, fontweight='bold', va='center', zorder=11)
    ax.text(210, 965, "|  ASTANA URBAN CLIMATE INTELLIGENCE", color=TEXT_WHITE, fontsize=12, fontweight='medium', va='center', zorder=11)
    if title_suffix:
        ax.text(610, 965, f"-  {title_suffix}", color=GREEN, fontsize=12, fontweight='bold', va='center', zorder=11)
    
    # District pill
    rect = FancyBboxPatch((1040, 945), 230, 40, boxstyle="round,pad=3", facecolor="#21262D", edgecolor=PANEL_BORDER, zorder=11)
    ax.add_patch(rect)
    ax.text(1155, 965, "Astana (All Districts)", color=TEXT_WHITE, fontsize=10, ha='center', va='center', zorder=12)
    
    # User Profile pill
    rect2 = FancyBboxPatch((1290, 945), 280, 40, boxstyle="round,pad=3", facecolor="#21262D", edgecolor=PANEL_BORDER, zorder=11)
    ax.add_patch(rect2)
    ax.add_patch(Circle((1315, 965), 14, facecolor=ACCENT_BLUE, zorder=12))
    ax.text(1315, 965, "ZB", color=TEXT_WHITE, fontsize=9, fontweight='bold', ha='center', va='center', zorder=13)
    ax.text(1340, 965, "Zhetpis Baigulov (GIS Lead)", color=TEXT_WHITE, fontsize=10, fontweight='bold', va='center', zorder=12)

def draw_bottom_bar(ax, metrics):
    ax.add_patch(Rectangle((0, 0), 1600, 50, facecolor=PANEL_BG, edgecolor=PANEL_BORDER, linewidth=1, zorder=10))
    x = 40
    for label, val, color in metrics:
        ax.text(x, 25, label + ":", color=TEXT_MUTED, fontsize=10, va='center', zorder=11)
        ax.text(x + len(label)*6.5 + 10, 25, val, color=color, fontsize=11, fontweight='bold', va='center', zorder=11)
        x += 280

def draw_map_background(ax):
    # Dark GIS Map canvas
    ax.add_patch(Rectangle((0, 50), 1600, 880, facecolor="#090D13", zorder=1))
    
    # Grid lines simulating coordinates
    for x in range(350, 1600, 160):
        ax.plot([x, x], [50, 930], color="#161B22", linewidth=0.8, linestyle="--", zorder=2)
    for y in range(50, 930, 120):
        ax.plot([350, 1600], [y, y], color="#161B22", linewidth=0.8, linestyle="--", zorder=2)
        
    # Yesil River (curved blue spline)
    river_x = np.array([360, 480, 620, 780, 950, 1100, 1280, 1420, 1580])
    river_y = np.array([320, 410, 460, 520, 480, 450, 560, 640, 720])
    ax.plot(river_x, river_y, color="#1D5373", linewidth=26, alpha=0.85, zorder=3)
    ax.plot(river_x, river_y, color="#388BFD", linewidth=12, alpha=0.95, zorder=4)
    ax.text(850, 505, "Yesil (Ishim) River Corridor", color="#79C0FF", fontsize=9, fontstyle='italic', rotation=5, zorder=5)

    # Road network (grey veins)
    roads = [
        ([360, 1580], [380, 380]),
        ([360, 1580], [680, 680]),
        ([600, 600], [50, 930]),
        ([920, 920], [50, 930]),
        ([1250, 1250], [50, 930]),
        ([450, 1400], [200, 850]),
        ([450, 1400], [850, 200]),
    ]
    for rx, ry in roads:
        ax.plot(rx, ry, color="#21262D", linewidth=3, zorder=3)
        ax.plot(rx, ry, color="#30363D", linewidth=1, zorder=4)

    # Green Parks polygons
    parks = [
        ([850, 930, 930, 850], [330, 330, 410, 410], "Botanical Garden"),
        ([1120, 1200, 1220, 1140], [480, 490, 570, 550], "Triathlon Park"),
        ([670, 740, 750, 680], [420, 430, 490, 470], "City Central Park"),
        ([980, 1050, 1060, 990], [520, 530, 610, 590], "Presidential Park"),
    ]
    for px, py, name in parks:
        poly = Polygon(list(zip(px, py)), facecolor="#238636", edgecolor="#3FB950", linewidth=1.5, alpha=0.75, zorder=5)
        ax.add_patch(poly)
        ax.text(np.mean(px), np.mean(py), f"[PARK] {name}", color="#E6EDF3", fontsize=8, fontweight='bold', ha='center', va='center', zorder=6)

    # Heat Island hotspots (radial thermal clusters)
    hotspots = [
        (650, 270, 37.8, "Nura South Hotspot"),
        (1350, 380, 38.4, "Industrial Logistics Hub"),
        (820, 780, 36.9, "Saryarka Dense Sector"),
        (1150, 750, 36.5, "Almaty District East"),
    ]
    for hx, hy, temp, label in hotspots:
        for r, alpha in [(130, 0.12), (90, 0.22), (50, 0.40), (25, 0.65)]:
            ax.add_patch(Circle((hx, hy), r, facecolor="#F85149", edgecolor=None, alpha=alpha, zorder=4))
        ax.text(hx, hy, f"[HOTSPOT] {temp}°C\n{label}", color="#FFFFFF", fontsize=8, fontweight='bold', ha='center', va='center', zorder=7)

    # Scale and coordinate legend
    ax.add_patch(FancyBboxPatch((370, 70), 190, 45, boxstyle="round,pad=3", facecolor="#161B22", edgecolor=PANEL_BORDER, alpha=0.9, zorder=8))
    ax.plot([385, 465], [83, 83], color=TEXT_WHITE, linewidth=2, zorder=9)
    ax.text(425, 93, "2 km", color=TEXT_WHITE, fontsize=8, ha='center', zorder=9)
    ax.text(510, 83, "51.1694° N, 71.4491° E", color=TEXT_MUTED, fontsize=8, va='center', zorder=9)

def draw_sidebar_layers(ax, active_layer="LST"):
    # Left Sidebar background
    ax.add_patch(Rectangle((0, 50), 340, 880, facecolor=PANEL_BG, edgecolor=PANEL_BORDER, linewidth=1, zorder=10))
    
    # Section: Layer Controls
    ax.text(25, 890, "GEOSPATIAL LAYERS", color=TEXT_MUTED, fontsize=11, fontweight='bold', zorder=11)
    
    layers = [
        ("[X] Land Surface Temp (LST 2026)", True, RED),
        ("[X] Vegetation Index (NDVI)", True, GREEN),
        ("[ ] Water Corridors (NDWI)", False, CYAN),
        ("[X] Cadastral Land Parcels", True, ORANGE),
        ("[ ] 3D Building Heights & Density", False, TEXT_MUTED),
        ("[ ] Ecological Network Graph", False, PURPLE),
    ]
    
    y = 850
    for text, checked, color in layers:
        bg_col = "#21262D" if checked else "#161B22"
        ax.add_patch(FancyBboxPatch((20, y-15), 300, 34, boxstyle="round,pad=3", facecolor=bg_col, edgecolor=PANEL_BORDER, zorder=11))
        ax.text(35, y+2, text, color=TEXT_WHITE if checked else TEXT_MUTED, fontsize=10, fontweight='bold' if checked else 'normal', va='center', zorder=12)
        if checked:
            ax.add_patch(Circle((305, y+2), 5, facecolor=color, zorder=12))
        y -= 45
        
    # Legend Section
    ax.text(25, 560, "THERMAL SCALE (°C)", color=TEXT_MUTED, fontsize=11, fontweight='bold', zorder=11)
    # Gradient bar
    grad_colors = ["#388BFD", "#58A6FF", "#3FB950", "#D29922", "#F85149", "#DA3633"]
    gx = 25
    for c in grad_colors:
        ax.add_patch(Rectangle((gx, 520), 48, 16, facecolor=c, edgecolor=None, zorder=11))
        gx += 48
    ax.text(25, 500, "22°C (Cool)", color="#58A6FF", fontsize=9, zorder=11)
    ax.text(160, 500, "30°C", color=ORANGE, fontsize=9, ha='center', zorder=11)
    ax.text(310, 500, "38°C (Extreme)", color=RED, fontsize=9, ha='right', zorder=11)
    
    # District Quick Focus
    ax.text(25, 440, "DISTRICT FOCUS", color=TEXT_MUTED, fontsize=11, fontweight='bold', zorder=11)
    districts = [
        ("Nura District", "37.8°C", RED, "Hotspot"),
        ("Yesil District", "31.4°C", GREEN, "Moderate"),
        ("Almaty District", "32.1°C", ORANGE, "Elevated"),
        ("Saryarka District", "33.5°C", ORANGE, "Dense"),
        ("Baikonur District", "33.0°C", ORANGE, "Industrial"),
    ]
    dy = 405
    for dname, dtemp, dcol, badge in districts:
        ax.add_patch(FancyBboxPatch((20, dy-12), 300, 30, boxstyle="round,pad=2", facecolor="#1B222C", edgecolor=PANEL_BORDER, zorder=11))
        ax.text(32, dy+3, dname, color=TEXT_WHITE, fontsize=9, fontweight='medium', va='center', zorder=12)
        ax.text(205, dy+3, dtemp, color=dcol, fontsize=9, fontweight='bold', va='center', zorder=12)
        ax.text(295, dy+3, badge, color=TEXT_MUTED, fontsize=8, ha='right', va='center', zorder=12)
        dy -= 38

    # System Status box
    ax.add_patch(FancyBboxPatch((20, 80), 300, 110, boxstyle="round,pad=4", facecolor="#11161D", edgecolor=PANEL_BORDER, zorder=11))
    ax.text(32, 165, "SYSTEM HEALTH", color=CYAN, fontsize=9, fontweight='bold', zorder=12)
    ax.text(32, 142, "- Data Feed: Sentinel-2 & Landsat 8/9", color=TEXT_MUTED, fontsize=8, zorder=12)
    ax.text(32, 122, "- ML Predictor: LightGBM v1.2 (Active)", color=GREEN, fontsize=8, zorder=12)
    ax.text(32, 102, "- PostGIS Store: Connected (EPSG:32642)", color=TEXT_WHITE, fontsize=8, zorder=12)


# ==============================================================================
# SCREEN 1: City-Wide Thermal Heatmap (LST) Dashboard
# ==============================================================================
def generate_screen_1():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
    ax.set_xlim(0, 1600)
    ax.set_ylim(0, 1000)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    draw_map_background(ax)
    draw_sidebar_layers(ax, active_layer="LST")
    draw_header(ax, title_suffix="CITY-WIDE THERMAL MONITORING (LST)")
    
    metrics = [
        ("Astana Mean LST", "31.8°C", ORANGE),
        ("Peak Hotspot", "38.4°C (Industrial Hub)", RED),
        ("Green Canopy Cover", "14.2% (Target: 25%)", GREEN),
        ("Spatial Resolution", "30m Pixel Grid", CYAN),
        ("API Latency", "42 ms (FastAPI)", GREEN),
    ]
    draw_bottom_bar(ax, metrics)
    
    out_path = os.path.join(OUTPUT_DIR, "mockup_01_city_thermal_heatmap.png")
    fig.savefig(out_path, bbox_inches='tight', pad_inches=0, facecolor=DARK_BG)
    plt.close(fig)
    print("Screen 1 generated successfully:", out_path)


# ==============================================================================
# SCREEN 2: Interactive "What-If" Land Cover Modification Scenario
# ==============================================================================
def generate_screen_2():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
    ax.set_xlim(0, 1600)
    ax.set_ylim(0, 1000)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    draw_map_background(ax)
    draw_sidebar_layers(ax)
    draw_header(ax, title_suffix="INTERACTIVE 'WHAT-IF' SIMULATION")
    
    # Highlighted Selected Parcel on map (AST-NUR-402 in Nura hotspot)
    hx, hy = 650, 270
    poly_pts = [(hx-60, hy-40), (hx+70, hy-30), (hx+80, hy+60), (hx-50, hy+50)]
    sel_poly = Polygon(poly_pts, facecolor="#58A6FF", edgecolor="#FFFFFF", linewidth=3, linestyle="--", alpha=0.4, zorder=8)
    ax.add_patch(sel_poly)
    
    # Pulse callout line to modal
    ax.plot([hx+80, 1060], [hy+60, 480], color=CYAN, linewidth=2, linestyle=":", zorder=9)
    ax.add_patch(Circle((hx+80, hy+60), 6, facecolor=CYAN, edgecolor="#FFFFFF", zorder=10))

    # Floating Scenario Builder Modal on the right
    mx, my, mw, mh = 1060, 160, 500, 690
    ax.add_patch(FancyBboxPatch((mx, my), mw, mh, boxstyle="round,pad=8", facecolor="#161B22", edgecolor=CYAN, linewidth=2, alpha=0.98, zorder=15))
    
    # Modal Header
    ax.text(mx+25, my+mh-35, "SCENARIO BUILDER: 'WHAT-IF' SIMULATION", color=TEXT_WHITE, fontsize=12, fontweight='bold', zorder=16)
    ax.text(mx+25, my+mh-58, "Parcel ID: #AST-NUR-402 (Nura District)", color=CYAN, fontsize=10, fontweight='bold', zorder=16)
    ax.plot([mx+20, mx+mw-20], [my+mh-72, my+mh-72], color=PANEL_BORDER, linewidth=1, zorder=16)
    
    # Parcel Current Stats
    ax.add_patch(FancyBboxPatch((mx+25, my+mh-145), mw-50, 60, boxstyle="round,pad=4", facecolor="#0D1117", edgecolor=PANEL_BORDER, zorder=16))
    ax.text(mx+40, my+mh-105, "Parcel Size: 4.2 Hectares", color=TEXT_WHITE, fontsize=10, fontweight='bold', zorder=17)
    ax.text(mx+40, my+mh-125, "Current Land Cover: 90% Impervious Asphalt / Bare Soil", color=TEXT_MUTED, fontsize=9, zorder=17)
    ax.text(mx+320, my+mh-105, "Baseline LST: 36.4°C", color=RED, fontsize=11, fontweight='bold', zorder=17)

    # Intervention Sliders
    ax.text(mx+25, my+mh-175, "INTERVENTION PARAMETERS", color=TEXT_MUTED, fontsize=10, fontweight='bold', zorder=16)
    
    # Slider 1: Greenery
    ax.text(mx+25, my+mh-205, "Tree Canopy & Lawn Ratio: 60% (+2.52 ha)", color=TEXT_WHITE, fontsize=10, fontweight='medium', zorder=16)
    ax.add_patch(Rectangle((mx+25, my+mh-225), mw-50, 8, facecolor="#30363D", zorder=16))
    ax.add_patch(Rectangle((mx+25, my+mh-225), (mw-50)*0.6, 8, facecolor=GREEN, zorder=16))
    ax.add_patch(Circle((mx+25 + (mw-50)*0.6, my+mh-221), 9, facecolor="#FFFFFF", edgecolor=GREEN, linewidth=2, zorder=17))

    # Slider 2: Water Body
    ax.text(mx+25, my+mh-255, "Cooling Water Retention Pond: 20% (+0.84 ha)", color=TEXT_WHITE, fontsize=10, fontweight='medium', zorder=16)
    ax.add_patch(Rectangle((mx+25, my+mh-275), mw-50, 8, facecolor="#30363D", zorder=16))
    ax.add_patch(Rectangle((mx+25, my+mh-275), (mw-50)*0.2, 8, facecolor=CYAN, zorder=16))
    ax.add_patch(Circle((mx+25 + (mw-50)*0.2, my+mh-271), 9, facecolor="#FFFFFF", edgecolor=CYAN, linewidth=2, zorder=17))

    # Slider 3: Permeable Pavement
    ax.text(mx+25, my+mh-305, "Permeable Eco-Paving: 20% (+0.84 ha)", color=TEXT_WHITE, fontsize=10, fontweight='medium', zorder=16)
    ax.add_patch(Rectangle((mx+25, my+mh-325), mw-50, 8, facecolor="#30363D", zorder=16))
    ax.add_patch(Rectangle((mx+25, my+mh-325), (mw-50)*0.2, 8, facecolor=ORANGE, zorder=16))
    ax.add_patch(Circle((mx+25 + (mw-50)*0.2, my+mh-321), 9, facecolor="#FFFFFF", edgecolor=ORANGE, linewidth=2, zorder=17))

    # Action Button
    ax.add_patch(FancyBboxPatch((mx+25, my+mh-385), mw-50, 42, boxstyle="round,pad=4", facecolor=ACCENT_BLUE, edgecolor=CYAN, zorder=16))
    ax.text(mx+mw/2, my+mh-364, ">> Run AI Microclimate Simulation", color="#FFFFFF", fontsize=11, fontweight='bold', ha='center', va='center', zorder=17)

    # Simulation Forecast Card (Results)
    ax.add_patch(FancyBboxPatch((mx+25, my+65), mw-50, 220, boxstyle="round,pad=4", facecolor="#0D1117", edgecolor=GREEN, linewidth=1.5, zorder=16))
    ax.text(mx+40, my+260, "SIMULATION RESULTS (LightGBM Surrogate)", color=GREEN, fontsize=10, fontweight='bold', zorder=17)
    
    results = [
        ("Projected Surface Temp:", "34.1°C", TEXT_WHITE),
        ("Net Temperature Reduction:", "-2.3°C (Significant Cooling)", GREEN),
        ("Cooling Buffer Radius:", "320 meters around parcel", CYAN),
        ("Graph Connectivity Gain:", "+15.4% (New Eco-Corridor)", PURPLE),
        ("Estimated Benefited Population:", "~12,800 Citizens", TEXT_WHITE),
        ("Model Confidence (R2):", "0.82 (High Statistical Reliability)", GREEN),
    ]
    ry = my + 230
    for label, val, col in results:
        ax.text(mx+40, ry, label, color=TEXT_MUTED, fontsize=9, zorder=17)
        ax.text(mx+mw-45, ry, val, color=col, fontsize=9, fontweight='bold', ha='right', zorder=17)
        ry -= 25

    # Bottom bar
    metrics = [
        ("Active Simulation", "Scenario #NUR-SIM-04", CYAN),
        ("Net Cooling Impact", "-2.3°C", GREEN),
        ("Connectivity Delta", "+15.4%", PURPLE),
        ("Execution Time", "1.42s (FastAPI REST)", GREEN),
    ]
    draw_bottom_bar(ax, metrics)
    
    out_path = os.path.join(OUTPUT_DIR, "mockup_02_what_if_scenario.png")
    fig.savefig(out_path, bbox_inches='tight', pad_inches=0, facecolor=DARK_BG)
    plt.close(fig)
    print("Screen 2 generated successfully:", out_path)


# ==============================================================================
# SCREEN 3: Algorithmic Multi-Objective Optimization (NSGA-II)
# ==============================================================================
def generate_screen_3():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
    ax.set_xlim(0, 1600)
    ax.set_ylim(0, 1000)
    ax.axis('off')
    fig.patch.set_facecolor(DARK_BG)
    
    draw_map_background(ax)
    draw_sidebar_layers(ax)
    draw_header(ax, title_suffix="MULTI-OBJECTIVE GBI OPTIMIZATION (NSGA-II)")

    # Top-3 Recommended Optimal Parcels marked on Map
    top_parcels = [
        (880, 270, "RANK #1: Parcel AST-YES-104\nArea: 2.1 ha | dT: -2.4°C | Score: 94.2"),
        (1080, 420, "RANK #2: Parcel AST-YES-219\nArea: 1.8 ha | dT: -1.9°C | Score: 88.5"),
        (760, 600, "RANK #3: Parcel AST-YES-088\nArea: 1.1 ha | dT: -1.5°C | Score: 81.0"),
    ]
    
    for ox, oy, odesc in top_parcels:
        # Green pulsing polygon
        ax.add_patch(Polygon([(ox-40, oy-30), (ox+40, oy-30), (ox+50, oy+40), (ox-30, oy+40)],
                             facecolor="#238636", edgecolor="#3FB950", linewidth=3, alpha=0.6, zorder=8))
        # Marker pin
        ax.add_patch(Circle((ox, oy), 14, facecolor="#3FB950", edgecolor="#FFFFFF", linewidth=2, zorder=9))
        ax.text(ox, oy, "*", color="#FFFFFF", fontsize=16, fontweight='bold', ha='center', va='center', zorder=10)
        # Tooltip badge
        ax.add_patch(FancyBboxPatch((ox-110, oy+50), 220, 50, boxstyle="round,pad=3", facecolor="#161B22", edgecolor=GREEN, linewidth=1.5, zorder=10))
        ax.text(ox, oy+75, odesc, color=TEXT_WHITE, fontsize=8, fontweight='bold', ha='center', va='center', zorder=11)

    # Optimization Control Drawer on the Right
    mx, my, mw, mh = 1120, 140, 450, 720
    ax.add_patch(FancyBboxPatch((mx, my), mw, mh, boxstyle="round,pad=8", facecolor="#161B22", edgecolor=PURPLE, linewidth=2, alpha=0.98, zorder=15))
    
    # Drawer Title
    ax.text(mx+20, my+mh-35, "NSGA-II OPTIMIZATION ENGINE", color=TEXT_WHITE, fontsize=12, fontweight='bold', zorder=16)
    ax.text(mx+20, my+mh-58, "Target Region: Yesil & Nura Districts", color=PURPLE, fontsize=10, fontweight='bold', zorder=16)
    ax.plot([mx+20, mx+mw-20], [my+mh-72, my+mh-72], color=PANEL_BORDER, linewidth=1, zorder=16)

    # Parameters Input Box
    ax.text(mx+20, my+mh-95, "OPTIMIZATION CONSTRAINTS", color=TEXT_MUTED, fontsize=9, fontweight='bold', zorder=16)
    
    cbox = FancyBboxPatch((mx+20, my+mh-220), mw-40, 115, boxstyle="round,pad=4", facecolor="#0D1117", edgecolor=PANEL_BORDER, zorder=16)
    ax.add_patch(cbox)
    
    ax.text(mx+35, my+mh-120, "- Intervention Budget:", color=TEXT_MUTED, fontsize=9, zorder=17)
    ax.text(mx+mw-35, my+mh-120, "50,000 m2 (5.0 ha)", color=CYAN, fontsize=9, fontweight='bold', ha='right', zorder=17)
    
    ax.text(mx+35, my+mh-145, "- Objective 1: Maximize Cooling (dLST)", color=TEXT_MUTED, fontsize=9, zorder=17)
    ax.text(mx+mw-35, my+mh-145, "Weight: 0.50", color=GREEN, fontsize=9, fontweight='bold', ha='right', zorder=17)
    
    ax.text(mx+35, my+mh-170, "- Objective 2: Maximize Network Connectivity", color=TEXT_MUTED, fontsize=9, zorder=17)
    ax.text(mx+mw-35, my+mh-170, "Weight: 0.35", color=PURPLE, fontsize=9, fontweight='bold', ha='right', zorder=17)

    ax.text(mx+35, my+mh-195, "- Objective 3: Minimize Land Conversion Cost", color=TEXT_MUTED, fontsize=9, zorder=17)
    ax.text(mx+mw-35, my+mh-195, "Weight: 0.15", color=ORANGE, fontsize=9, fontweight='bold', ha='right', zorder=17)

    # Run Button
    ax.add_patch(FancyBboxPatch((mx+20, my+mh-275), mw-40, 40, boxstyle="round,pad=4", facecolor=PURPLE, edgecolor="#FFFFFF", zorder=16))
    ax.text(mx+mw/2, my+mh-255, ">> Find Pareto-Optimal GBI Allocations", color="#FFFFFF", fontsize=10, fontweight='bold', ha='center', va='center', zorder=17)

    # Pareto Frontier Solutions
    ax.text(mx+20, my+mh-305, "PARETO-OPTIMAL ALLOCATIONS FOUND", color=GREEN, fontsize=10, fontweight='bold', zorder=16)
    
    cards = [
        ("RANK 1: Parcel #AST-YES-104 (Optimal)", "Cooling: -2.4°C | Conn: +18.2% | Budget: 21,000 m2", GREEN),
        ("RANK 2: Parcel #AST-YES-219 (Balanced)", "Cooling: -1.9°C | Conn: +12.4% | Budget: 18,000 m2", CYAN),
        ("RANK 3: Parcel #AST-YES-088 (Corridor)", "Cooling: -1.5°C | Conn: +9.1%  | Budget: 11,000 m2", ORANGE),
    ]
    cy = my + mh - 370
    for ctitle, cdesc, ccolor in cards:
        ax.add_patch(FancyBboxPatch((mx+20, cy-5), mw-40, 52, boxstyle="round,pad=4", facecolor="#0D1117", edgecolor=ccolor, linewidth=1.2, zorder=16))
        ax.text(mx+32, cy+32, ctitle, color=ccolor, fontsize=9, fontweight='bold', zorder=17)
        ax.text(mx+32, cy+12, cdesc, color=TEXT_MUTED, fontsize=8, zorder=17)
        cy -= 65

    # Aggregate Impact Summary Card
    ax.add_patch(FancyBboxPatch((mx+20, my+30), mw-40, 95, boxstyle="round,pad=4", facecolor="#1B222C", edgecolor=PANEL_BORDER, zorder=16))
    ax.text(mx+35, my+105, "CUMULATIVE PROGRAM IMPACT", color=CYAN, fontsize=9, fontweight='bold', zorder=17)
    ax.text(mx+35, my+82, "- Total Budget Utilized: 50,000 / 50,000 m2 (100%)", color=TEXT_WHITE, fontsize=8, zorder=17)
    ax.text(mx+35, my+62, "- Average District Heat Mitigation: -2.1°C", color=GREEN, fontsize=8, fontweight='bold', zorder=17)
    ax.text(mx+35, my+42, "- Ecological Network Cohesion: +24.8% Gain", color=PURPLE, fontsize=8, fontweight='bold', zorder=17)

    # Bottom metrics bar
    metrics = [
        ("Algorithm Engine", "NSGA-II (DEAP / PyGAD)", PURPLE),
        ("Pareto Candidates", "18 Evaluated / 3 Selected", GREEN),
        ("Budget Allocated", "50,000 m2 (100%)", CYAN),
        ("Mean Cooling Delta", "-2.1°C District-Wide", GREEN),
    ]
    draw_bottom_bar(ax, metrics)
    
    out_path = os.path.join(OUTPUT_DIR, "mockup_03_nsga2_optimization.png")
    fig.savefig(out_path, bbox_inches='tight', pad_inches=0, facecolor=DARK_BG)
    plt.close(fig)
    print("Screen 3 generated successfully:", out_path)

if __name__ == "__main__":
    generate_screen_1()
    generate_screen_2()
    generate_screen_3()
    print("All 3 mockups successfully rendered without missing glyphs!")
