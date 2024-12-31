from PIL import Image

def encrypt_image(image_path, output_path, key):
    """Encrypt an image by adding a key value to each pixel."""
    try:
        img = Image.open(image_path)
        pixels = img.load()
        
        for i in range(img.width):
            for j in range(img.height):
                if len(pixels[i, j]) == 3:  # RGB image
                    r, g, b = pixels[i, j]
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
                elif len(pixels[i, j]) == 4:  # RGBA image
                    r, g, b, a = pixels[i, j]
                    pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)
        
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, output_path, key):
    """Decrypt an image by subtracting a key value from each pixel."""
    try:
        img = Image.open(image_path)
        pixels = img.load()
        
        for i in range(img.width):
            for j in range(img.height):
                if len(pixels[i, j]) == 3:  # RGB image
                    r, g, b = pixels[i, j]
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
                elif len(pixels[i, j]) == 4:  # RGBA image
                    r, g, b, a = pixels[i, j]
                    pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256, a)
        
        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Image Encryption/Decryption Tool")
    try:
        choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
        image_path = input("Enter the image file path: ").strip().strip('"')
        output_path = input("Enter the output file path: ").strip().strip('"')
        key = int(input("Enter the key (integer): ").strip())
        
        if choice == "encrypt":
            encrypt_image(image_path, output_path, key)
        elif choice == "decrypt":
            decrypt_image(image_path, output_path, key)
        else:
            print("Invalid choice!")
    except ValueError:
        print("Key must be an integer!")
    except Exception as e:
        print(f"Unexpected error: {e}")