
def tower_of_h(source, dist, hel, n):
    if n == 0:
        return

    tower_of_h(source, hel, dist, n-1)
    print("Plates ", n, "from", source, "to", dist)
    tower_of_h(hel, dist, source, n-1)


tower_of_h("source", "destination", "helper", 4)