import os
from rembg import remove

# Path to your input folder
input_folder = r"C:\Users\Admin\Documents\GitHub\AttendanceAI\student_list"
# Path to the output folder
output_folder = r"C:\Users\Admin\Documents\GitHub\AttendanceAI\processed_students"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize counter for the student filenames
counter = 1

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    
    # Process only image files (you can add more types if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        try:
            # Open the image
            with open(file_path, 'rb') as input_file:
                input_data = input_file.read()
            
            # Remove background
            output_data = remove(input_data)
            
            # Define the output filename as student1.png, student2.png, etc.
            output_filename = f"student{counter}.png"
            output_file_path = os.path.join(output_folder, output_filename)
            
            # Save the processed image
            with open(output_file_path, 'wb') as output_file:
                output_file.write(output_data)

            print(f"Processed {filename} successfully as {output_filename}.")
            
            # Increment the counter for the next student
            counter += 1
        
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("Background removal for all images completed.")
