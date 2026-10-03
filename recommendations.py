# ==========================================
# SPATIA - DESIGN RECOMMENDATION ENGINE
# ==========================================

print("=" * 55)
print("              SPATIA")
print("       DESIGN RECOMMENDATIONS")
print("=" * 55)


# ------------------------------------------
# ROOM INFORMATION
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
# GENERATE RECOMMENDATIONS
# ------------------------------------------

recommendations = []


# Workspace recommendation
if "Low floor table" in room["furniture"]:

    recommendations.append({
        "category": "WORKSPACE",
        "title": "Improve your workspace",
        "description":
            "Your laptop is currently placed on a low floor table. "
            "A compact desk placed against a wall could create a "
            "more comfortable and organized workspace."
    })


# Bed recommendation
if (
    "Modern bed" in room["furniture"]
    and "Older iron bed" in room["furniture"]
):

    recommendations.append({
        "category": "BED ARRANGEMENT",
        "title": "Create a clear walking path",
        "description":
            "Two beds are present in the room. Keep enough space "
            "between the beds and the main walking path so that "
            "movement around the room remains comfortable."
    })


# Storage recommendation
if "Cupboard" in room["furniture"]:

    recommendations.append({
        "category": "STORAGE",
        "title": "Keep the cupboard area accessible",
        "description":
            "Keep enough clearance in front of the cupboard so "
            "the doors can open comfortably and the storage area "
            "remains easy to access."
    })


# Door recommendation
if "Washroom door" in room["features"]:

    recommendations.append({
        "category": "ACCESS",
        "title": "Keep the washroom entrance clear",
        "description":
            "Avoid placing large furniture directly in front of "
            "the washroom entrance. Maintain a clear path between "
            "the bedroom and washroom."
    })


# Organization recommendation
if "Laptop" in room["electronics"]:

    recommendations.append({
        "category": "ORGANIZATION",
        "title": "Create a dedicated study zone",
        "description":
            "Keep the laptop, charging cable and study items "
            "together in one defined workspace to reduce clutter."
    })


# ------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------

print("\nYOUR ROOM\n")

print(f"Room type: {room['room_type']}")

print("\n" + "=" * 55)
print("          SPATIA DESIGN SUGGESTIONS")
print("=" * 55)


for number, recommendation in enumerate(
    recommendations,
    start=1
):

    print(
        f"\n{number}. "
        f"{recommendation['category']}"
    )

    print(
        f"   {recommendation['title']}"
    )

    print(
        f"   {recommendation['description']}"
    )


print("\n" + "=" * 55)
print("       RECOMMENDATION ANALYSIS COMPLETE")
print("=" * 55)