import surgical_instrument_tracker as sit

def main():
    tracker = sit.SurgicalInstrumentTracker()

    # Insert the example data
    instrument_distances = [100, 50, 150, 30, 70, 180]
    for distance in instrument_distances:
        tracker.insert(distance)

    print("Surgical Instrument Tracking System")
    print("===================================")
    print("Instrument distances in the system (in mm):")
    print(" ".join(map(str, tracker.get_all_distances())))
    print()

    min_distance = 70
    max_distance = 150

    result = tracker.display_instrument_movements(min_distance, max_distance)
    print(result)

if __name__ == "__main__":
    main()
    