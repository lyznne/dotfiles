# COLORS FOR THE BAR
# Theme name: Arczen

# bg  - #020d18 - rich black
# logo - #BE3F24 -logo
# worksace - #0B1D28 - solarized black

from typing import List

# def init_colors() -> List[List[str]]:
#     return [
#         ["rgba(2, 13, 25, 0.8)", "rgba(2, 13, 25, 0.8)"],      # color 0 - Background
#         ["#A0B2C2", "#A0B2C2"],                                # color 1 -  Foreground(accent-light).
#         [
#             "rgba(217,89,62,0.9)",
#             "rgba(217,89,62,0.9)",
#         ],                                                     # color 2 - Workspace_active_focus + volume
#         ["rgba(10,66,127,0.32)", "rgba(10,66,127,0.32)"],      # color 3 - Workspace_active
#         ["#D9593E", "#D9593E"],                                # color 4 - Base_Foreground
#         ["rgba(160,178,194, 0.8)", "rgba(160,178,194, 0.8)"],  # color 5 - term
#         ["rgba(160,178,194,0.8)", "rgba(160,178,194,0.8)"],    # color 6 - notes
#         ["rgba(194,116,177,0.76)", "rgba(194,116,177,0.76)"],  # color 7 - wifi + net
#         ["rgba(36,109,153,0.88)", "rgba(36,109,153,0.88)"],    # color 8 - cpu + battery
#         ["rgba(98,168,244,0.7)", "rgba(98,168,244,0.7)"],      # color 9 - Time
#     ]


def init_colors() -> List[List[str]]:
    return [
        ["#020D19CC", "#020D19CC"],  # color 0 - Background
        ["#A0B2C2FF", "#A0B2C2FF"],  # color 1 - Foreground(accent-light)
        ["#D9593EE6", "#D9593EE6"],  # color 2 - Workspace_active_focus + volume
        ["#0A427F52", "#0A427F52"],  # color 3 - Workspace_active
        ["#D9593EFF", "#D9593EFF"],  # color 4 - Base_Foreground
        ["#A0B2C2CC", "#A0B2C2CC"],  # color 5 - term
        ["#A0B2C2CC", "#A0B2C2CC"],  # color 6 - notes
        ["#C274B1C2", "#C274B1C2"],  # color 7 - wifi + net
        ["#246D99E0", "#246D99E0"],  # color 8 - cpu + battery
        ["#62A8F4B3", "#62A8F4B3"],  # color 9 - Time
    ]
