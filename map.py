map_data = [0,0,0,0,1,0,0,0,0]

def map_print():
    for i in range(0, len(map_data), 3):
        print(map_data[i:i+3])