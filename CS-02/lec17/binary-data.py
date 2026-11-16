import pickle as p

def save_data(data, filename):
    try:
       with open(filename, "wb") as f:
           p.dump(data,f)
           print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

# name = "Amresh"
# save_data(name,"Happy.cbse")

def read_data(filename):
    try:
       with open(filename, "rb") as f:
           d = p.load(f)
           print(d)
           print(f"Data fetched successfully from this {filename}")
    except Exception as e:
        print(f"Error while fetching data: {e}")


read_data("Happy.cbse")
