garden = {}

def plant_crop():
    crop = input("Enter the crop name to plant:").lower()
    if crop in garden:
        print(f"{crop.title()} is already planted!")
    else:
        garden[crop] = 0 # Growth Value
        print(f"{crop.title()} has been planted.")

def water_crops():
    if not garden:
        print("No crops to water. Plant something first!")
    else:
        for crop in garden:
            if garden[crop] < 3:
                garden[crop] += 1
                print(f"Watered {crop.title()}! Growth: ({garden[crop]}/3)")
            else:
                print(f"{crop.title()} is fully grown!")

def harvest_crop():
    ready_crops = [crop for crop, growth in garden.items() if growth == 3]

    if not ready_crops:
        print("No crops are ready for harvest!")
    
    else:
        for crop in ready_crops:
            print(f"Harvesting {crop.title()}!")
            del garden[crop]

def check_garden():
    if not garden:
        print("Your garden is empty. Plant something!")
    else: 
        for crop, growth in garden.items():
            status = "Growing" if growth < 3 else "Ready to Harvest"
            print(f"{crop.title()}: {status} ({growth}/3)")
        

def main():
    while True:
        print("-" * 30)
        print("1. Plant a crop")
        print("2. Water crops")
        print("3.Harvest crops")
        print("4.Check garden status")
        print("5.Exit")

        choice = input("Choose an option (1-5):")
        print("-" * 30)

        if choice == "1":
            plant_crop()
        elif choice == "2":
            water_crops()
        elif choice == "3":
            harvest_crop()
        elif choice == "4":
            check_garden()
        elif choice == "5":
            print("Goodbye! Happy gardening!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    