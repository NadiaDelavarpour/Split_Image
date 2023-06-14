from PIL import Image
import math
import os
Image.MAX_IMAGE_PIXELS = None

def split_image(image_path, rows, cols, name, output_directory):
    # Open the image
    image = Image.open(image_path)
    name1, ext1 = os.path.splitext(image_path)

    #print(output_directory)

    # Get the width and height of the image
    width, height = image.size

    # Calculate the width and height of each tile
    tile_width = width // cols
    tile_height = height // rows



    # Split the image into tiles
    n = 0
    for r in range(rows):
        for c in range(cols):
            # Calculate the coordinates for each tile
            left = c * tile_width
            upper = r * tile_height
            right = (c + 1) * tile_width
            lower = (r + 1) * tile_height

            # Crop the tile from the image
            tile = image.crop((left, upper, right, lower))            

            # Save the tile to the output directory
            tile_name = name + "_" + str(n) + ext1
            print(tile_name)
            tile_path = os.path.join(output_directory, tile_name)
            print(tile_path)
            tile.save(tile_path)
            print(f"Saved {tile_path}")
            n += 1


directory = "H:/Ortho_Data/UAV2021/Soybean"
for filename in os.listdir(directory):
    # Check if the file has .txt extension
    if filename.endswith('.jpg'):
        
        name, ext = os.path.splitext(filename)
        image_path = os.path.join(directory, filename)
        output_directory = os.path.join(directory, name)
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        
        print(filename)
        print()
        # Ask user for flight altitude
        Filght_altitude = float(input("Enter flight altitude (ft): "))
        #flight_altitude = 100
        alt = flight_altitude * 0.3048
        print("Flight Altitude:", alt, "m")
        print()
        # Ask user for GSD
        Image_Width = 5472
        Image_Height = 3648
        Sensor_Width = 13.2
        Sensor_Height = 8
        Focal_Length = 8.8
        
        print("Use this website to calculate the GSD considering your sensor and flight altitude (m): https://www.propelleraero.com/gsd-calculator/ ")
        GSD = ((alt * 1000 * Sensor_Height) / (Focal_Length * Image_Height))
        print("GSD:", GSD, "cm/px")
        print()

        #im_height = float(input("Enter im_height (px): "))
        #im_width = float(input("Enter im_width (px): "))
       
        image = Image.open(image_path)
        im_width, im_height = image.size

        # Ask user for plot height
        #plot_height = float(input("Enter plot height (m): "))
        plot_height = 3

        # Ask user for plot width
        #plot_width = float(input("Enter plot width (m): "))
        plot_width = 1.5

        
        # Print the entered information
        print("Plot Height:", plot_height, "m")
        print("Plot Width:", plot_width, "m")

        print()
        Plot_Height_Pixel = (plot_height * 100)//GSD
        print("Plot_Height_Pixel:", Plot_Height_Pixel)
        Plot_Width_Pixel = (plot_width * 100)//GSD
        print("Plot_Width_Pixel:", Plot_Width_Pixel)

        print()
        if Plot_Height_Pixel > 640 and Plot_Width_Pixel > 640:
            print("Both variables are greater than 640.")
        else:
            while Plot_Height_Pixel <= 640 or Plot_Width_Pixel <= 640:
            # Check if Plot_Height_Pixel is less than or equal to 640 and multiply it by 2
                if Plot_Height_Pixel <= 640:
                    Plot_Height_Pixel *= 2

            # Check if Plot_Width_Pixel is less than or equal to 640 and multiply it by 2
                if Plot_Width_Pixel <= 640:
                    Plot_Width_Pixel *= 2

        print("Modified Plot_Height_Pixel:", Plot_Height_Pixel)
        print("Modified Plot_Width_Pixel:", Plot_Width_Pixel)


        print()
        tile1 = math.ceil(im_width // Plot_Width_Pixel)
        print("tile1:", tile1)
        tile2 = math.ceil(im_height // Plot_Height_Pixel)
        print("tile2:", tile2)
    

        #the bigger tile for rows, the smaller for cols
        rows = tile2
        cols = tile1
        split_image(image_path, rows, cols, name, output_directory)
