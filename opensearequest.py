import requests
from PIL import Image, ImageDraw, ImageFont

def get_number_of_owners(asset_contract_address, token_id, api_key):
    url = f"https://api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}/owners"
    headers = {"Accept": "application/json", "X-API-KEY": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        total_mints = 0  # Initialize a variable to store the total mints count

        for owner_info in data['owners']:
            quantity = int(owner_info['quantity'])  # Extract the quantity and convert it to an integer
            total_mint += quantity  # Increment the total mints count by the quantity

            # Now, total_mints will contain the total number of mints
        print(total_mints)

        print(f"mints for token ID {token_id}: {total_mints}")
        print(f"Number of mints for token ID {token_id}: {(total_mints)}")
        return total_mints
    else:
        print(f"Error fetching data: {response.status_code}")
        return 0

def add_counters_to_image(image_path, owner_counts, y_position, font_path='arial.ttf', font_size=40):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Font not found, using default font.")
        font = ImageFont.load_default()

    image_width = image.width
    num_characters = len(owner_counts)
    counter_width = image_width / num_characters
    counter_x_positions = [(counter_width * i + counter_width / 2) for i in range(num_characters)]
    counter_positions_above = [(x, y_position) for x in counter_x_positions]

    for value, position in zip(owner_counts, counter_positions_above):
        draw.text(position, value, font=font, fill='white', anchor="mm")

    output_path = image_path.replace('.webp', '_with_counters_above.webp')
    image.save(output_path)
    return output_path

api_key = '04f1d6917de349caa2d1236eed4df99b'
contract_address = "0xae2bc979178e97e0688384aab00055e67bea91ed"
token_ids = [1, 2, 3, 4, 5]

owner_counts = [str(get_number_of_owners(contract_address, token_id, api_key)) for token_id in token_ids]

image_path = 'sansound.webp'
y_position_above = 150

output_image_path = add_counters_to_image(image_path, owner_counts, y_position_above)
print(f"Counters with owner counts added above characters. Saved new image to {output_image_path}")
