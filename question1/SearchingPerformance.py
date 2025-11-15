import time
from HashTable import HashTable
from BabyProduct import BabyProduct


def load_data():
    """Same data records used for comparing the performance"""
    return [
        BabyProduct("P001", "Baby Diapers", "Hygiene", 35.90, 100),
        BabyProduct("P002", "Baby Milk Bottle", "Feeding", 19.50, 50),
        BabyProduct("P003", "Baby Lotion", "Skincare", 12.80, 80),
        BabyProduct("P004", "Baby Wet Wipes", "Hygiene", 8.90, 120),

        BabyProduct("P005", "Baby Shampoo", "Skincare", 14.50, 60),
        BabyProduct("P006", "Baby Soap Bar", "Skincare", 6.20, 90),
        BabyProduct("P007", "Pacifier", "Feeding", 4.50, 150),
        BabyProduct("P008", "Baby Food Jar - Apple", "Feeding", 3.90, 200),
        BabyProduct("P009", "Baby Food Jar - Banana", "Feeding", 3.90, 180),
        BabyProduct("P010", "Baby Powder", "Skincare", 7.80, 85),

        BabyProduct("P011", "Baby Blanket", "Bedding", 22.50, 40),
        BabyProduct("P012", "Baby Pillow", "Bedding", 15.90, 55),
        BabyProduct("P013", "Baby Mattress", "Bedding", 49.90, 20),
        BabyProduct("P014", "Baby Thermometer", "Healthcare", 18.50, 35),
        BabyProduct("P015", "Baby Nail Clipper", "Healthcare", 5.90, 90),
        BabyProduct("P016", "Baby Toothbrush", "Hygiene", 3.50, 110),
        BabyProduct("P017", "Teething Ring", "Feeding", 6.50, 95),
        BabyProduct("P018", "Baby Onesie - Blue", "Clothing", 12.90, 70),
        BabyProduct("P019", "Baby Onesie - Pink", "Clothing", 12.90, 75),
        BabyProduct("P020", "Baby Socks (5-pack)", "Clothing", 9.90, 130),

        BabyProduct("P021", "Baby Stroller", "Equipment", 199.90, 10),
        BabyProduct("P022", "Baby Car Seat", "Equipment", 249.90, 8),
        BabyProduct("P023", "Baby Carrier", "Equipment", 89.90, 14),
        BabyProduct("P024", "Breast Pump Manual", "Feeding", 39.90, 25),
        BabyProduct("P025", "Breast Milk Storage Bags", "Feeding", 16.90, 80),
        BabyProduct("P026", "Baby High Chair", "Equipment", 139.90, 12),
        BabyProduct("P027", "Baby Walker", "Equipment", 79.90, 20),
        BabyProduct("P028", "Baby Play Mat", "Toys", 29.90, 50),
        BabyProduct("P029", "Baby Rattle", "Toys", 5.90, 140),
        BabyProduct("P030", "Soft Plush Toy", "Toys", 12.50, 90),

        BabyProduct("P031", "Baby Hat", "Clothing", 7.90, 60),
        BabyProduct("P032", "Baby Mittens", "Clothing", 4.90, 100),
        BabyProduct("P033", "Baby Swaddle Wrap", "Bedding", 18.90, 45),
        BabyProduct("P034", "Baby Bib", "Feeding", 3.20, 160),
        BabyProduct("P035", "Baby Cup", "Feeding", 4.70, 140),
        BabyProduct("P036", "Baby Spoon Set", "Feeding", 6.80, 130),
        BabyProduct("P037", "Baby Fork Set", "Feeding", 6.80, 120),
        BabyProduct("P038", "Bottle Sterilizer", "Feeding", 89.90, 18),
        BabyProduct("P039", "Bottle Warmer", "Feeding", 49.90, 22),
        BabyProduct("P040", "Baby Formula Stage 1", "Feeding", 29.90, 50),

        BabyProduct("P041", "Baby Formula Stage 2", "Feeding", 32.90, 45),
        BabyProduct("P042", "Crib Mobile", "Toys", 34.90, 30),
        BabyProduct("P043", "Baby Monitor", "Equipment", 159.90, 15),
        BabyProduct("P044", "Baby Bath Tub", "Hygiene", 34.90, 25),
        BabyProduct("P045", "Bath Seat Support", "Hygiene", 19.90, 30),
        BabyProduct("P046", "Baby Hair Brush", "Hygiene", 5.50, 75),
        BabyProduct("P047", "Nasal Aspirator", "Healthcare", 12.50, 40),
        BabyProduct("P048", "Baby Medicine Dropper", "Healthcare", 4.50, 100),
        BabyProduct("P049", "Baby Safety Gate", "Equipment", 89.90, 12),
        BabyProduct("P050", "Cabinet Safety Locks", "Equipment", 14.90, 80),

        BabyProduct("P051", "Baby Socks - White", "Clothing", 3.90, 150),
        BabyProduct("P052", "Baby Towel", "Hygiene", 11.90, 70),
        BabyProduct("P053", "Baby Bathrobe", "Hygiene", 22.90, 40),
        BabyProduct("P054", "Baby Car Mirror", "Equipment", 17.90, 35),
        BabyProduct("P055", "Rear Facing Car Seat", "Equipment", 299.90, 6),
        BabyProduct("P056", "Baby UV Lotion", "Skincare", 14.90, 60),
        BabyProduct("P057", "Baby Moisturizer Cream", "Skincare", 13.50, 55),
        BabyProduct("P058", "Baby Rash Cream", "Skincare", 10.90, 70),
        BabyProduct("P059", "Baby Ear Buds", "Hygiene", 3.90, 200),
        BabyProduct("P060", "Baby Nail File Set", "Hygiene", 8.50, 90),

        BabyProduct("P061", "Baby Potty", "Hygiene", 25.90, 30),
        BabyProduct("P062", "Diaper Bag", "Equipment", 49.90, 20),
        BabyProduct("P063", "Baby Hoodie", "Clothing", 24.90, 45),
        BabyProduct("P064", "Baby Jacket", "Clothing", 29.90, 35),
        BabyProduct("P065", "Baby Pants", "Clothing", 12.90, 55),
        BabyProduct("P066", "Baby Shorts", "Clothing", 10.90, 60),
        BabyProduct("P067", "Baby Feeding Chair", "Feeding", 159.90, 10),
        BabyProduct("P068", "Baby Fleece Blanket", "Bedding", 19.90, 50),
        BabyProduct("P069", "Baby Mosquito Net", "Bedding", 14.90, 45),
        BabyProduct("P070", "Baby Teething Gel", "Healthcare", 8.90, 65),

        BabyProduct("P071", "Baby Teething Biscuits", "Feeding", 5.90, 120),
        BabyProduct("P072", "Baby Crib Sheet", "Bedding", 15.90, 35),
        BabyProduct("P073", "Baby Mattress Protector", "Bedding", 19.90, 30),
        BabyProduct("P074", "Baby Winter Socks", "Clothing", 5.90, 110),
        BabyProduct("P075", "Baby Onesie - Yellow", "Clothing", 13.90, 70),
        BabyProduct("P076", "Baby Jacket - Winter", "Clothing", 39.90, 25),
        BabyProduct("P077", "Baby Powder Puff", "Skincare", 4.50, 90),
        BabyProduct("P078", "Baby Changing Pad", "Hygiene", 24.90, 40),
        BabyProduct("P079", "Baby Wet Bag", "Hygiene", 9.90, 50),
        BabyProduct("P080", "Baby Wipes Refill Pack", "Hygiene", 12.90, 120),

        BabyProduct("P081", "Baby Bottle Brush", "Feeding", 6.90, 85),
        BabyProduct("P082", "Baby Snack Box", "Feeding", 7.90, 100),
        BabyProduct("P083", "Baby Crib Bumper", "Bedding", 29.90, 20),
        BabyProduct("P084", "Baby Play Gym", "Toys", 49.90, 18),
        BabyProduct("P085", "Baby Bath Sponge", "Hygiene", 3.90, 130),
        BabyProduct("P086", "Baby Cotton Buds", "Hygiene", 4.90, 200),
        BabyProduct("P087", "Baby Mittens - Pink", "Clothing", 5.20, 90),
        BabyProduct("P088", "Baby Mittens - Blue", "Clothing", 5.20, 95),
        BabyProduct("P089", "Baby Crib Organizer", "Bedding", 19.90, 30),
        BabyProduct("P090", "Baby Pacifier Clip", "Feeding", 4.90, 110),

        BabyProduct("P091", "Baby Learning Blocks", "Toys", 24.90, 40),
        BabyProduct("P092", "Baby Soft Book", "Toys", 14.90, 55),
        BabyProduct("P093", "Baby Development Cards", "Toys", 19.90, 50),
        BabyProduct("P094", "Baby Shoes", "Clothing", 19.90, 45),
        BabyProduct("P095", "Baby Slippers", "Clothing", 12.50, 60),
        BabyProduct("P096", "Baby Sippy Cup", "Feeding", 8.90, 90),
        BabyProduct("P097", "Baby Training Cup", "Feeding", 9.50, 80),
        BabyProduct("P098", "Baby Bottle Cap", "Feeding", 2.90, 180),
        BabyProduct("P099", "Baby Skin Serum", "Skincare", 16.90, 40),
        BabyProduct("P100", "Baby Vitamin Drops", "Healthcare", 22.90, 30),

        BabyProduct("P101", "Baby UV Hat", "Clothing", 14.50, 50),
        BabyProduct("P102", "Baby Carrier Wrap", "Equipment", 59.90, 22),
        BabyProduct("P103", "Baby Plush Blanket", "Bedding", 25.90, 35),
        BabyProduct("P104", "Baby Lotion Organic", "Skincare", 18.90, 45)
    ]

def array_search(array, target_id):
    """Perform linear search in array"""
    for item in array:
        if item.product_id == target_id:
            return item
    return None

"""Performance Comparison"""

def compare_performance():
    print("*" * 100)
    print("Searching Performance of Hash Table and Array".center(100))
    print("*" * 100)

    # Load identical data
    sample_data = load_data()

    # Create array and store the records
    array_storage = list(sample_data)

    # Create hash table and insert items
    hash_storage = HashTable(10)
    for product in sample_data:
        hash_storage.insert(product.product_id, product)

    # Pick a record to search (Last record to show max difference)
    search_key = "P104"

    """Hash Table Search"""
    # Record the starting time
    start_hash = time.time()

    result_hash = hash_storage.search(search_key)

    # Record the ending time
    end_hash = time.time()

    # Evaluate the execution time
    hash_time = end_hash - start_hash

    """Array Linear Search"""
    # Record the starting time
    start_arr = time.time()

    result_arr = array_search(array_storage, search_key)

    # Record the ending time
    end_arr = time.time()

    # Evaluate the execution time
    array_time = end_arr - start_arr

    print(f"Hash Table Search Time: {hash_time:.10f} seconds")
    print(f"Array Linear Search Time: {array_time:.10f} seconds")

    print(f"\nHash Table Result: {result_hash}")
    print(f"Array Search Result: {result_arr}")

    print()
    print("*" * 100)
    print("Analysis Summary".center(100))
    print("*" * 100)

    # If hash table is faster, then print the correct output message
    if hash_time < array_time:
        print("Hash Table Search is Faster")
    else:
        print("Array Linear Search is Faster")

if __name__ == "__main__":
    compare_performance()