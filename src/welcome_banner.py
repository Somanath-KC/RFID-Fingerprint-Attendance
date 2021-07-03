import time
import sys
from src.lcd import lcd


def print_banner():
    lcd.write_string("Attendance System")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Loading...")
    print("""\n
**********************************************************************************************
*                                                                                            *
*    ____  _____ ___ ____       _  _____ _____ _____ _   _ ____    _    _   _  ____ _____    *
*   |  _ \|  ___|_ _|  _ \     / \|_   _|_   _| ____| \ | |  _ \  / \  | \ | |/ ___| ____|   *
*   | |_) | |_   | || | | |   / _ \ | |   | | |  _| |  \| | | | |/ _ \ |  \| | |   |  _|     *
*   |  _ <|  _|  | || |_| |  / ___ \| |   | | | |___| |\  | |_| / ___ \| |\  | |___| |___    *
*   |_| \_\_|   |___|____/  /_/   \_\_|   |_| |_____|_| \_|____/_/   \_\_| \_|\____|_____|   *
*                                                                                            *
*         | B.Tech Project 2021 | Dept of Electronics & Communication Engg. | GVPCE  |       *
*                                                                                            *
*                                                                                            *
* Team Members                                                      Mentor                   *
*  > 17JG1A0486 - P Sowmya                                          > Mr. P V K Chaitanya    *
*  > 17JG1A0485 - P Sowdhamini                                                               *
*  > 17JG1A0475	- N Hari Priya                                                               *
*  > 18JG5A0404	- D Uma Maheshwari                                                           *
*                                                                                            *
*                                                                                            *
* Year: IV                            Section: B                                Branch: ECE  *
**********************************************************************************************\n""")


def loading():
    print(" "*44+"Loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + " "*42 + animation[i % len(animation)])
        sys.stdout.flush()
    
    print("\n")
    lcd.clear()
