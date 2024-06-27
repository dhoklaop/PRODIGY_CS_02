from PIL import Image

def encrypt_decrypt(image_path, key, mode):
  img = Image.open(image_path)
  pixels = img.load()
  width, height = img.size

  # Function to perform encryption/decryption on a single pixel value
  def modify_pixel(pixel_value):
    new_value = (pixel_value + key) if mode == 'encrypt' else (pixel_value - key) % 256
    return new_value

  # Modify each pixel value based on mode and key
  for y in range(height):
    for x in range(width):
      red, green, blue = pixels[x, y]
      new_red = modify_pixel(red)
      new_green = modify_pixel(green)
      new_blue = modify_pixel(blue)
      pixels[x, y] = (new_red, new_green, new_blue)

  # Save the modified image with a new name
  new_path = f"{image_path.split('.')[0]}_{mode}.png"
  img.save(new_path)
  return new_path

def main():
  while True:
    image_path = input("Enter the image path: ")
    key = int(input("Enter a secret key (integer): "))
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    if mode not in ('encrypt', 'decrypt'):
      print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
      continue

    new_path = encrypt_decrypt(image_path, key, mode)
    print(f"{mode.title()}d image saved at: {new_path}")

    choice = input("Do you want to encrypt/decrypt another image? (y/n): ").lower()
    if choice != 'y':
      break

if __name__ == "__main__":
  main()
