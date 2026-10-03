# ==========================================
# SPATIA - ROOM UNDERSTANDING
# ==========================================

print("=" * 55)
print("              SPATIA")
print("       ROOM UNDERSTANDING")
print("=" * 55)

# ------------------------------------------
# ROOM INVENTORY
# ------------------------------------------

room = {
    "room_type": "Bedroom",

    "furniture": [
        "Modern bed",
        "Older iron bed",
        "Low floor table",
        "Chair",
        "Cupboard"
    ],

    "electronics": [
        "Laptop"
    ],

    "features": [
        "Washroom door",
        "Electrical switches"
    ]
}


# ------------------------------------------
# ROOM DESCRIPTION
# ------------------------------------------

print("\nROOM TYPE")
print("---------")
print(room["room_type"])


print("\nFURNITURE")
print("---------")

for item in room["furniture"]:
    print(f"✓ {item}")


print("\nELECTRONICS")
print("-----------")

for item in room["electronics"]:
    print(f"✓ {item}")


print("\nROOM FEATURES")
print("-------------")

for item in room["features"]:
    print(f"✓ {item}")


# ------------------------------------------
# INITIAL ROOM OBSERVATIONS
# ------------------------------------------

print("\nROOM OBSERVATIONS")
print("-----------------")

observations = [

    "Two different beds are present in the room.",

    "The modern bed occupies the main visible area.",

    "A low floor table is used as a workspace.",

    "A laptop is placed on the floor table.",

    "A chair is positioned near the bed.",

    "A cupboard is visible along the side of the room.",

    "A washroom door is located beside the cupboard.",

    "Electrical switches are visible near the door."
]

for observation in observations:
    print(f"• {observation}")


print("\n" + "=" * 55)
print("       ROOM UNDERSTANDING COMPLETE")
print("=" * 55)