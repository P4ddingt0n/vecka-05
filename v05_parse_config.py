# Filen du sparat fran routern. Lagg den bredvid skriptet.
filnamn = "R-Nordvik-01_startup-config.txt"

routes = []

# with ser till att filen stangs igen nar vi ar klara.

with open(filnamn) as f:
    for rad in f:
        # strip tar bort mellanslag och radbrytning i bada andar.
        rad = rad.strip()
        if rad.startswith("ip route "):
            routes.append(rad)

    print(f"Hittade {len(routes)} statiska rutter:")
    for rad in routes:
        print(f" {rad}")