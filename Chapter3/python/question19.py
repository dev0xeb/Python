for sidea in range(20):
    for sideb in range(sidea, 20):
        for sidec in range(sideb, 20):
            if sidea*sidea + sideb*sideb == sidec*sidec:
                print(f"{sidea}, {sideb}, {sidec}")
